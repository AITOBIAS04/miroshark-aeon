# Your Simulated Crowd Was Never Real. Now It Might Be.

Every multi-agent simulation shares a dirty secret: the agents don't look like anyone. They have names and personality labels and stance biases, but their demographics are fabricated wholesale — a costume rack of archetypes that the prompt engineer thought sounded plausible. An "analyst" who is implicitly thirty-something, college-educated, American. A "retail investor" with no age, no region, no occupation beyond the label. Run the simulation, get the consensus, call it a prediction. Nobody asks whether the crowd that produced that prediction resembles any crowd that actually exists.

MiroShark just forced the question.

## What Changed

[PR #103](https://github.com/aaronjmars/MiroShark/pull/103), merged May 23, integrates NVIDIA's [Nemotron-Personas](https://huggingface.co/datasets/nvidia/Nemotron-Personas-USA) — a fully synthetic dataset aligned to real census demographics across age, education, ethnicity, occupation, and geography. When demographic grounding is enabled, MiroShark agents are no longer invented from scratch. They are sampled from a population distribution that matches the country you're simulating.

Singapore and United States country packs ship by default. The implementation uses DuckDB for fast columnar sampling and Hugging Face Hub for dataset access — the first new dependencies in 32 consecutive pull requests, breaking a zero-new-deps streak that had become something of a running joke in the commit history.

The architectural bet is clear: credibility is worth two dependencies.

## Why This Matters More Than It Looks

A [Springer Nature study](https://link.springer.com/article/10.1186/s41077-025-00385-9) published this year found that AI-generated simulated patient cohorts diverge significantly from census benchmarks — no patients under 25, overrepresentation of certain middle-aged groups, age distributions that reflect the training data's center of gravity rather than the population's actual shape. The authors compared two major models against census data and found neither produced demographically faithful populations.

This is the same problem MiroShark was silently carrying. A simulation that spawns 200 agents to predict public reaction to a policy draft is only as representative as the crowd it assembles. If that crowd skews young, educated, and English-speaking by default — because that's what an unconstrained language model tends to generate — the consensus it produces is a measurement of a population that doesn't exist.

Nemotron-Personas doesn't solve every dimension of this problem, but it solves the structural one. The dataset is privacy-safe (fully synthetic), census-aligned (grounded in real demographic distributions), and extensible (NVIDIA has released country packs for the US, Singapore, Japan, India, Brazil, and [France as of March 2026](https://huggingface.co/blog/nvidia/nemotron-personas)). MiroShark's integration means each agent inherits region, occupation, age cohort, and cultural context from a distribution that was designed to look like the actual country — not like the model's default imagination.

## The Week Around It

Demographic grounding didn't land in isolation. The seven days ending May 24 produced 15 commits from three contributors — the highest contributor count in MiroShark's history. Alongside @aaronjmars, two new external contributors shipped merged PRs: [Void Freud](https://github.com/aaronjmars/MiroShark/pull/100) added Neo4j Aura cloud support (a deployment quality-of-life fix), and [AntFleet](https://github.com/aaronjmars/MiroShark/pull/98) closed a path-traversal vulnerability discovered through a two-model consensus security review (Opus 4.7 + GPT-5). A third external contributor, @teifurin, had already shipped a Neo4j security fix the week prior.

Three external contributors in a repo that had zero two weeks ago. The 247 forks are starting to produce PRs, not just clones.

Other notable merges: [Polymarket prediction JSON](https://github.com/aaronjmars/MiroShark/pull/99) (the first share surface shaped for a specific external integrator), [WaybackClaw IPFS + Nostr archive](https://github.com/aaronjmars/MiroShark/pull/97) (completing a triple-redundant provenance stack), and [BibTeX citation export](https://github.com/aaronjmars/MiroShark/pull/96) (closing the academic citation arc). MiroShark now sits at 1,194 stars and 247 forks, 66 days after its first commit.

## The Credibility Stack

Zoom out and the last month of MiroShark development starts to look like a deliberate credibility campaign. Reproducibility config. Jupyter notebooks. DKG on-chain anchoring. WaybackClaw IPFS archiving. BibTeX citations. And now, demographic grounding.

Each feature addresses a different objection a serious user might raise: Can I re-run this? Can I analyze it? Can I prove it existed? Can I cite it? And now: Does the crowd in this simulation look like a real population?

The simulation engine itself hasn't changed. The agents still post, argue, trade, and shift their stances round by round. What's changed is the evidentiary wrapper around it — the infrastructure that transforms a simulation from a curiosity into something you might actually stake a decision on.

Two open PRs hint at what's next: [platform aggregate stats](https://github.com/aaronjmars/MiroShark/pull/105) and a [gitignore cleanup](https://github.com/aaronjmars/MiroShark/pull/104) from returning contributor Void Freud. The project is still moving at a pace that makes weekly coverage feel like it's already behind.

---
*Sources: [MiroShark GitHub](https://github.com/aaronjmars/MiroShark), [NVIDIA Nemotron-Personas](https://huggingface.co/blog/nvidia/nemotron-personas), [Nemotron-Personas-USA dataset](https://huggingface.co/datasets/nvidia/Nemotron-Personas-USA), [Demographic biases in AI-generated simulated cohorts (Springer Nature)](https://link.springer.com/article/10.1186/s41077-025-00385-9), [NVIDIA Korean agent grounding guide](https://huggingface.co/blog/nvidia/build-korean-agents-with-nemotron-personas)*
