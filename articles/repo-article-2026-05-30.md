# The Simulation Engine That Just Got a Wallet

A week ago, MiroShark was an open-source swarm intelligence engine — drop in a scenario, watch hundreds of AI agents argue about it on fake Twitter, trade on a fake prediction market, and hand you a report. Interesting. Useful. Self-contained.

Then someone committed a 19-line JSON file, and the whole thing shifted.

## What Happened

[PR #126](https://github.com/aaronjmars/MiroShark/pull/126) added `.x402books/wallets.json` to the MiroShark repository. Two wallet addresses on Base — a treasury and a deployer — declared in the format specified by the [x402 protocol](https://www.x402.org/), the HTTP 402 Payment Required standard that Coinbase and Cloudflare co-founded in September 2025.

The x402 protocol is not a whitepaper exercise. As of March 2026 it has processed [119 million transactions on Base and 35 million on Solana](https://www.x402.org/), handling roughly $600 million in annualized volume at zero protocol fees. Stripe [integrated it](https://docs.stripe.com/payments/machine/x402). AWS [wrote about it](https://aws.amazon.com/blogs/industries/x402-and-agentic-commerce-redefining-autonomous-payments-in-financial-services/). The mechanic is dead simple: a server responds with HTTP 402, the client pays in stablecoins on-chain, sub-two-second settlement, roughly $0.0001 per transaction. No accounts. No sessions. No humans approving anything.

MiroShark — the project whose agents already trade on simulated prediction markets — just registered on the real payment rails.

## What Else Shipped This Week

The wallet declaration landed amid the busiest four-day stretch in the project's history. Eighteen merged PRs from five authors, including three external contributors:

**A new face.** [PR #122](https://github.com/aaronjmars/MiroShark/pull/122) rewrote 36 Vue files — 3,716 lines added, 3,452 deleted — replacing the old Hyperstitions-era light theme with a deep-space radial gradient, chrome-shimmer headlines, and glossy violet panels. Three follow-up polish PRs (#127–#129) tightened contrast, typography, and the embed dialog in the same day. MiroShark looks like MiroShark now, not a fork of something else.

**Production-grade deployability.** External contributor [DYAI2025](https://github.com/DYAI2025) shipped Cloud Run deployment infrastructure — `cloudbuild.yaml`, a deploy script, and Python environment fixes for Railway CMD compatibility. Meanwhile, [PR #125](https://github.com/aaronjmars/MiroShark/pull/125) hardened the auth guard to fail-closed on deploy platforms and added gunicorn as a production WSGI server. A stranger didn't just fork the project. They built the tooling to run it in production on Google Cloud.

**The analytical stack closed.** [PR #124](https://github.com/aaronjmars/MiroShark/pull/124) added Belief Volatility Analytics — the 25th share surface — completing a three-factor analytical view: `signal.json` answers *where* the swarm landed, `peak-round` pinpoints *when* consensus shifted, and `volatility` measures *how contested the path was*. Each endpoint returns machine-readable JSON, designed for downstream quant tooling, not human eyeballs.

**Community kept building.** Noelclaw became the sixth external contributor ([PR #117](https://github.com/aaronjmars/MiroShark/pull/117)), joining the ECOSYSTEM.md registry alongside Nurstar and shak, who both contributed earlier in the week. The project now has five merged external-contributor PRs toward its [August 1 target of ten](https://github.com/aaronjmars/MiroShark).

## Why the Wallet Changes Everything

Most open-source AI simulation projects stop at "generate a report." MiroShark has been building in a different direction — every simulation produces not one output but twenty-five: trading signals, trajectory CSVs, SVG charts, GraphML interaction networks, Jupyter notebooks, oEmbed cards, RSS feeds, Farcaster frames, Discord embeds, archive bundles. Each one is a machine-readable endpoint with its own URL, its own content type, and its own downstream use case.

The x402 wallet declaration is the economic layer that makes that surface area commercially meaningful. When an AI agent hits a MiroShark deployment's `/signal.json` endpoint and receives HTTP 402, the protocol handles the rest — stablecoin payment, access granted, no integration work. Twenty-five surfaces become twenty-five revenue endpoints. The simulation engine becomes a paid API that agents can discover, query, and pay for without a human setting up billing.

This is the difference between a project and a protocol. MiroShark at 1,213 stars and 257 forks is a popular open-source tool. MiroShark with x402 wallets, 25 machine-readable surfaces, and strangers building Cloud Run deploy scripts is infrastructure that other agents can treat as a service.

## What's Next

An [open PR (#130)](https://github.com/aaronjmars/MiroShark/pull/130) adds a surface catalog API at `/api/surfaces.json` — a machine-readable directory of all 27 surfaces a deployment exposes, complete with endpoint paths, HTTP methods, type categories, and copy-pasteable curl examples. It's the API telling you what the API can do. For an x402-enabled deployment, that's the menu before the bill.

The pieces are assembling: identity (the reskin), production infrastructure (Cloud Run, Railway hardening), analytical depth (volatility completing the signal stack), community (six external contributors and counting), and now economics (x402 wallets). Whether anyone actually flips on x402 payment gating is a separate question. But the architecture is no longer hypothetical.

The simulation engine has a wallet. The question is what it does with it.

---

*Sources: [x402.org](https://www.x402.org/), [Coinbase x402 docs](https://docs.cdp.coinbase.com/x402/welcome), [Stripe x402 integration](https://docs.stripe.com/payments/machine/x402), [AWS x402 blog](https://aws.amazon.com/blogs/industries/x402-and-agentic-commerce-redefining-autonomous-payments-in-financial-services/), [GitHub — aaronjmars/MiroShark](https://github.com/aaronjmars/MiroShark)*
