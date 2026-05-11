# The Twelfth Category Nobody Drew on the Map

In January 2026, StackOne published the most comprehensive landscape map of the AI agent ecosystem to date. Over 120 tools, sorted into 11 categories: frameworks, no-code builders, observability, memory, tool integrations, browser agents, protocols, coding agents, enterprise platforms, inference clouds, and foundation models. The map was clean, thorough, and widely circulated. It became the default reference for anyone asking "where does this agent tool fit?"

It also had a hole in it large enough to drive a research program through.

## Eleven Categories, Zero Simulations

Every category on StackOne's map describes agents that do things. Frameworks build agents that act. Observability tools monitor agents that act. Enterprise platforms deploy agents that act at scale. Protocols standardize how acting agents talk to each other. The entire map is organized around a single premise: the value of an AI agent is what it executes.

This is not a criticism of the map. It is an accurate reflection of where the money is. Gartner projects 40% of enterprise applications will include task-specific AI agents by end of 2026. Salesforce Agentforce hit $540 million in ARR. The market for agents that do things is real and growing.

But while the execution ecosystem was being mapped, a parallel ecosystem was growing underneath it — one that uses the same underlying technology (large language models, multi-agent orchestration, persona generation) for a fundamentally different purpose. Not agents that act in the world. Agents that model it.

## The Unmapped Ecosystem

The list is longer than most people realize.

**OASIS**, built by a consortium spanning CAMEL-AI, Shanghai AI Lab, Oxford, Imperial College London, and the Max Planck Institute, simulates social media dynamics with up to one million LLM-powered agents. Agents perform 23 distinct actions — following, commenting, reposting, quoting — across replicated Twitter and Reddit environments. The research team has used it to replicate information cascading, group polarization, and herd effects at population scale.

**AgentSociety**, from Tsinghua University's Future Intelligence Lab, generates social lives for over 10,000 agents engaging in 5 million interactions. It models responses to policy interventions — universal basic income, hurricane response, inflammatory speech — by watching how a synthetic population reorganizes under pressure.

**Concordia**, Google DeepMind's simulation library, provides a framework for building social interaction simulations where agents with distinct personalities and goals interact in open-ended environments. **Project Sid**, from Altera, placed 1,000 LLM agents into Minecraft and watched them autonomously develop specialized roles, cultural norms, and governance structures.

**PolicySim** models bidirectional dynamics between user behavior and platform interventions. **SAPIENT** links a sentinel layer over public text streams with a simulation layer running moderated focus-group sessions. **WarAgent** simulates international conflict and diplomacy. **Sotopia**, an ICLR 2024 spotlight, measures social intelligence through open-ended agent interactions. **Generative Agents** — the Stanford paper that started much of this — showed that believable human behavior could emerge from agents that remember, reflect, and interact in a shared environment.

A GitHub repository tracking AI synthetic society experiments now lists over 30 distinct projects spanning civilization simulations, virtual agent towns, sociological modeling, and domain-specific environments from hospitals to prediction markets.

This is not a fringe. It is a field — one that simply does not appear on the map that everyone is using.

## Why the Map Misses It

The gap is not accidental. It is structural.

Landscape maps are typically drawn by companies selling infrastructure. StackOne sells agent integrations. Salesforce sells agent deployment. Langfuse sells agent observability. The people drawing the maps are measuring the ecosystem by what their customers need, and their customers need agents that execute tasks. Simulation does not fit into the purchase order.

The simulation ecosystem also straddles an awkward boundary. Half of it lives in academic labs (Tsinghua, Stanford, Oxford, DeepMind) and publishes in venues like ICLR, CHI, and Science Advances. The other half lives on GitHub as open-source projects with growing star counts and no venture capital narrative. Neither half speaks the language of enterprise software categories.

A March 2026 position paper on arXiv made this tension explicit. Titled "AI Agents Are Not (Yet) a Panacea for Social Simulation," it argued that plausible-sounding agent behavior does not guarantee valid simulation — that results can be dominated by interaction protocols, scheduling, and initial priors rather than authentic behavioral dynamics. The paper proposed formalizing social simulation as an environment-involved Markov game with explicit exposure mechanisms. This is the kind of self-critical methodological debate that marks a maturing discipline, not a fad.

## Where the Dollar Simulation Sits

MiroShark, now at 1,133 GitHub stars and 224 forks, occupies a specific position on this unmapped landscape: the accessibility layer.

OASIS scales to a million agents. AgentSociety generates 5 million interactions. These are research instruments built for researchers with research budgets and research timelines. MiroShark runs hundreds of agents across simulated Twitter, Reddit, and Polymarket for about a dollar in under ten minutes. A community template gallery offers one-click scenarios. Share links let anyone embed a pre-configured simulation in a tweet. The audience is not the lab — it is the policy analyst, the DAO coordinator, the journalist, the community manager.

But the feature stack that has accumulated over the last six weeks positions MiroShark closer to the research end than it first appears. A reproducibility config export (`reproduce.json`) captures every parameter of a simulation run with bytewise-stable output — the file hash serves as a citation key. A lineage navigator traces bidirectional fork and counterfactual relationships across simulation families. A trace interview system reconstructs agent decision paths from logged behavior. A simulation impact scorecard quantifies four collective-level metrics — polarization index, influence concentration, consensus velocity, narrative volatility — that exist only at the population level. An A/B comparison view, the latest addition, places two simulations side by side with dual belief drift charts and scorecard differentials.

These are not features designed to make a demo impressive. They are features designed to make a simulation auditable, reproducible, and comparable — the infrastructure that CHI 2026's PoliSim workshop identified as the preconditions for simulation to matter in policy.

## The Map Is About to Change

The execution ecosystem and the simulation ecosystem are converging whether the landscape maps recognize it or not.

The convergence point is risk. As multi-agent systems move into production — Gartner's survey of inquiries about multi-agent systems showed a 1,445% surge between Q1 2024 and Q2 2025 — the question of "what will these agents do before we deploy them" becomes operational, not academic. A company rolling out negotiation agents needs to know whether they will spontaneously develop pricing conventions that violate antitrust guidelines. A platform deploying AI moderators at scale needs to understand whether collectively biased enforcement will emerge from individually unbiased models.

The 12th category will not be called "simulation." It will probably be called something like "agent testing and scenario modeling" or "pre-deployment behavioral analysis." It will be the category where you model what agents would do before you let them do it. The tools in it will borrow from both ecosystems — the orchestration patterns of LangGraph and CrewAI, the behavioral modeling of OASIS and AgentSociety, the accessibility of MiroShark's dollar simulation.

The first 11 categories answer the question "how do we build agents that act?" The 12th answers the question that comes right before it: "how do we know what they'll do?"

Every map is a theory of what matters. The current map says execution matters. The next version will have to account for the fact that rehearsal matters too — and that a surprisingly large number of people have already been building it.

---
*Sources: [120+ Agentic AI Tools Mapped Across 11 Categories (StackOne)](https://www.stackone.com/blog/ai-agent-tools-landscape-2026/) · [OASIS: Open Agent Social Interaction Simulations with One Million Agents (CAMEL-AI)](https://github.com/camel-ai/oasis) · [AgentSociety: Large-Scale Simulation of LLM-Driven Generative Agents (Tsinghua)](https://github.com/tsinghua-fib-lab/AgentSociety) · [AI Synthetic Society Experiments Resource List (GitHub)](https://github.com/danielrosehill/AI-Synthetic-Society-Experiments) · [AI Agents Are Not (Yet) a Panacea for Social Simulation (arXiv)](https://arxiv.org/abs/2603.00113) · [The AI Agent Ecosystem in 2026: What's Actually Working (DEV Community)](https://dev.to/nathanhamlett/the-ai-agent-ecosystem-in-2026-whats-actually-working-and-whats-getting-canceled-2bl) · [MiroShark on GitHub](https://github.com/aaronjmars/MiroShark)*
