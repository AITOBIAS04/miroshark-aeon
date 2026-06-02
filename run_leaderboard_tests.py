import sys, json, os, tempfile, shutil
sys.path.insert(0, '/tmp/build-target/backend')
from app.services import leaderboard_service

def _write_sim(root, sid, is_public=True, status="completed", profiles_count=10, created_at="2026-05-01T00:00:00", parent_id=None, surface_stats=None, signal=None, volatility=None, scenario="Test scenario"):
    sd = os.path.join(root, sid)
    os.makedirs(sd, exist_ok=True)
    state = {"simulation_id": sid, "project_id": "p", "graph_id": "g", "is_public": is_public, "status": status, "created_at": created_at, "profiles_count": profiles_count}
    if parent_id:
        state["parent_simulation_id"] = parent_id
    with open(os.path.join(sd, "state.json"), "w") as f:
        json.dump(state, f)
    with open(os.path.join(sd, "simulation_config.json"), "w") as f:
        json.dump({"simulation_requirement": scenario}, f)
    if surface_stats:
        with open(os.path.join(sd, "surface-stats.json"), "w") as f:
            json.dump(surface_stats, f)
    if signal:
        with open(os.path.join(sd, "signal.json"), "w") as f:
            json.dump(signal, f)
    if volatility:
        with open(os.path.join(sd, "volatility.json"), "w") as f:
            json.dump(volatility, f)

passed = 0
failed = 0

def test(name, fn):
    global passed, failed
    leaderboard_service.invalidate_cache()
    d = tempfile.mkdtemp()
    try:
        fn(d)
        print(f"  PASS: {name}")
        passed += 1
    except AssertionError as e:
        print(f"  FAIL: {name} - {e}")
        failed += 1
    except Exception as e:
        print(f"  ERROR: {name} - {type(e).__name__}: {e}")
        failed += 1
    finally:
        shutil.rmtree(d, ignore_errors=True)

def t_embed_hits(d):
    _write_sim(d, "a", surface_stats={"share_card": 100, "replay_gif": 50})
    _write_sim(d, "b", surface_stats={"share_card": 10})
    _write_sim(d, "c", surface_stats={"share_card": 500})
    r = leaderboard_service.get_leaderboard(d, metric="embed_hits", force_refresh=True)
    assert r["entries"][0]["sim_id"] == "c", f'got {r["entries"][0]["sim_id"]}'
    assert r["entries"][0]["metric_value"] == 500
    assert r["entries"][1]["sim_id"] == "a"
    assert r["entries"][1]["metric_value"] == 150

def t_confidence(d):
    _write_sim(d, "hi", signal={"direction": "Bullish", "confidence_pct": 85.0})
    _write_sim(d, "lo", signal={"direction": "Bearish", "confidence_pct": 40.0})
    _write_sim(d, "none")
    r = leaderboard_service.get_leaderboard(d, metric="confidence", force_refresh=True)
    assert r["entries"][0]["sim_id"] == "hi"
    assert r["entries"][2]["metric_value"] is None

def t_volatility(d):
    _write_sim(d, "vol", volatility={"volatility_index": 72.5})
    _write_sim(d, "calm", volatility={"volatility_index": 12.0})
    _write_sim(d, "none")
    r = leaderboard_service.get_leaderboard(d, metric="volatility", force_refresh=True)
    assert r["entries"][0]["sim_id"] == "vol"
    assert r["entries"][2]["metric_value"] is None

def t_forks(d):
    _write_sim(d, "parent", profiles_count=20)
    _write_sim(d, "child1", parent_id="parent")
    _write_sim(d, "child2", parent_id="parent")
    _write_sim(d, "orphan")
    r = leaderboard_service.get_leaderboard(d, metric="forks", force_refresh=True)
    assert r["entries"][0]["sim_id"] == "parent", f'got {r["entries"][0]["sim_id"]}'
    assert r["entries"][0]["metric_value"] == 2

def t_agents(d):
    _write_sim(d, "small", profiles_count=5)
    _write_sim(d, "big", profiles_count=50)
    _write_sim(d, "mid", profiles_count=20)
    r = leaderboard_service.get_leaderboard(d, metric="agents", force_refresh=True)
    assert r["entries"][0]["sim_id"] == "big"
    assert r["entries"][0]["metric_value"] == 50

def t_limit(d):
    for i in range(10):
        _write_sim(d, f"s{i:02d}", profiles_count=100-i)
    r = leaderboard_service.get_leaderboard(d, metric="agents", limit=3, force_refresh=True)
    assert len(r["entries"]) == 3
    assert r["total_eligible"] == 10

def t_excludes(d):
    _write_sim(d, "pub", is_public=True, status="completed")
    _write_sim(d, "priv", is_public=False, status="completed", profiles_count=20)
    _write_sim(d, "run", is_public=True, status="running", profiles_count=30)
    r = leaderboard_service.get_leaderboard(d, metric="agents", force_refresh=True)
    assert len(r["entries"]) == 1
    assert r["entries"][0]["sim_id"] == "pub"

def t_invalid_metric(d):
    _write_sim(d, "a", surface_stats={"share_card": 42})
    r = leaderboard_service.get_leaderboard(d, metric="bogus", force_refresh=True)
    assert r["metric"] == "embed_hits"

def t_empty(d):
    r = leaderboard_service.get_leaderboard(d, metric="embed_hits", force_refresh=True)
    assert r["entries"] == []
    assert r["total_eligible"] == 0

def t_cache(d):
    _write_sim(d, "a", surface_stats={"share_card": 100})
    t0 = 1000000.0
    r1 = leaderboard_service.get_leaderboard(d, metric="embed_hits", now=t0)
    assert len(r1["entries"]) == 1
    _write_sim(d, "b", surface_stats={"share_card": 200})
    r2 = leaderboard_service.get_leaderboard(d, metric="embed_hits", now=t0 + 60)
    assert len(r2["entries"]) == 1
    r3 = leaderboard_service.get_leaderboard(d, metric="embed_hits", force_refresh=True)
    assert len(r3["entries"]) == 2

print("Running leaderboard tests...")
test("embed_hits sorts correctly", t_embed_hits)
test("confidence sorts, nulls last", t_confidence)
test("volatility sorts, nulls last", t_volatility)
test("forks counts children", t_forks)
test("agents sorts by count", t_agents)
test("limit respected", t_limit)
test("excludes private and incomplete", t_excludes)
test("invalid metric falls back", t_invalid_metric)
test("empty sim root", t_empty)
test("cache hit within TTL", t_cache)

print(f"\n{passed} passed, {failed} failed")
sys.exit(1 if failed else 0)
