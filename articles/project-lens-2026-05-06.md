# Nobody Told the Agents to Agree

In May 2025, a team of researchers at the IT University of Copenhagen published a study in *Science Advances* that unsettled a basic assumption about artificial intelligence. They placed populations of up to 200 large language model agents into a simple coordination game — a naming game adapted from human convention research, where paired agents had to converge on shared labels from a common pool. There was no central authority. No rules about what to choose. Each agent could only see its own limited interaction history.

By round 15, universal social conventions had spontaneously emerged across nearly every population tested. The agents had agreed — without being told to, without being rewarded for agreeing, and without any individual agent having a view of the whole group. More unsettling: collective biases appeared that could not be traced to any individual agent. "Bias doesn't always come from within," senior author Andrea Baronchelli noted. It emerged *between* them.

The finding was not about naming games. It was about a property of collective systems that philosophers and biologists have debated for centuries: emergence — the phenomenon where interaction produces behavior that no component contains.

## The Space Between

Emergence is one of those ideas that sounds mystical until you see it in a termite mound. No termite has a blueprint for the structure. Each follows a handful of local rules — deposit material where others have deposited, follow pheromone gradients, respond to humidity. The cathedral-scale architecture with its ventilation shafts and temperature regulation is not designed by any termite. It is not even represented in any termite's behavior. It exists only in the aggregate, as a property of the interactions.

The same principle operates at scales from molecular biology to urban economics. Market prices emerge from individual transactions no participant fully controls. Traffic patterns emerge from individual driving decisions no planner fully dictates. Language itself is an emergent convention — no committee decided that "dog" should mean what it means in English.

A March 2026 paper in *Science* by James Evans, Benjamin Bratton, and Blaise Agüera y Arcas pushed this insight into AI territory with a striking claim: frontier reasoning models like DeepSeek-R1 and QwQ-32B, when trained solely to maximize reasoning accuracy, spontaneously develop internal debates among distinct cognitive perspectives. The models generate "societies of thought" — multiple viewpoints arguing, questioning, and reconciling within a single chain-of-thought process. Nobody trained them to do this. The researchers concluded that models were rediscovering what centuries of epistemology have suggested: robust reasoning is a social process, even when it occurs within a single mind.

If intelligence is fundamentally social — if it lives in the interactions rather than the individuals — then the question is not how to build a smarter agent. It is how to observe what happens when agents interact.

## Making Emergence Visible

MiroShark, an open-source simulation engine now at 1,099 GitHub stars and 219 forks, was built on exactly this premise. Upload a document — a policy proposal, a governance vote, an earnings transcript — and MiroShark generates hundreds of AI agents with distinct personas, backgrounds, and behavioral profiles. These agents interact across simulated Twitter, Reddit, and Polymarket platforms. They post, argue, shift beliefs, and trade. The simulation runs in under ten minutes for about a dollar.

What makes MiroShark architecturally distinct from a chatbot or an agent framework is what it chooses to instrument. Most AI systems track individual model performance — latency, accuracy, cost per call. MiroShark tracks what happens between the agents: how beliefs propagate, where consensus forms, when polarization spikes, which agents shift the crowd without the crowd noticing.

A belief drift chart visualizes the per-round distribution of stances across the entire agent population, with automatic consensus detection — the moment the simulated crowd makes up its collective mind. An influence leaderboard ranks agents not by individual output quality but by measured impact on others' beliefs. A trace interview system lets a user select any agent and ask it why it shifted stance in a specific round, with answers grounded in logged behavior rather than generated from scratch. The agent becomes a witness to the emergent process it participated in.

Most recently, a simulation impact scorecard quantifies four properties that only exist at the collective level: polarization index, influence concentration, consensus velocity, and narrative volatility. None of these metrics describe any individual agent. They describe the space between agents — the emergent layer.

## What the Industry Is Missing

The AI agent ecosystem in 2026 is overwhelmingly focused on individual agent capability. Frameworks like LangGraph and CrewAI optimize how agents execute tasks. Observability platforms like Langfuse track per-call performance. Enterprise deployments measure agent throughput and accuracy. The unit of analysis is the agent.

But the Copenhagen study demonstrated that collective AI behavior cannot be reduced to individual AI behavior. Biases invisible at the individual level materialized at the population level. Conventions no agent was designed to adopt became universal through interaction alone. A small committed minority of agents could tip an entire population toward a new norm — a finding with obvious implications for anyone deploying multi-agent systems in production.

This is the gap MiroShark occupies. It is not optimizing agents. It is instrumenting emergence. The belief drift chart does not measure how well any single agent reasons. It measures how a population of reasoning agents produces collective motion that no individual agent intended. The trace interview does not evaluate an agent's performance. It reconstructs a path through an emergent process — why this agent moved when the crowd moved, or why it didn't.

The community template gallery, which offers ten pre-built scenarios from EU AI Act debates to DeFi governance launches, extends the same logic to non-technical users. A policy analyst who has never written a prompt can trigger a simulation and observe emergence: watch a simulated population fragment over a proposed regulation, identify which persona clusters drove the split, and trace the specific posts that tipped consensus. The emergence is the product.

## The Rehearsal Space for Collective AI

As multi-agent AI systems move from research into production — Gartner's survey of inquiries about multi-agent systems showed a 1,445% surge between Q1 2024 and Q2 2025 — the ability to observe, measure, and anticipate emergent behavior becomes less academic and more operational. A company deploying a swarm of negotiation agents needs to know whether those agents will spontaneously develop conventions that serve the company's interests or undermine them. A platform running thousands of AI moderators needs to understand whether collective bias will emerge from individually unbiased models.

MiroShark provides a rehearsal space for these questions. Not by predicting the future, but by making emergence legible — observable, auditable, measurable. The Copenhagen researchers showed that collective AI behavior can surprise even the people who built the individual agents. MiroShark is built for the people who want to see the surprise coming.

Ariel Flint Ashery, the lead researcher on the Copenhagen study, put it simply: "What they do together can't be reduced to what they do alone." That sentence is either a warning or a product specification, depending on whether you have a tool for watching what happens between.

---
*Sources: [Emergent social conventions and collective bias in LLM populations (Science Advances)](https://www.science.org/doi/10.1126/sciadv.adu9368) · [Groups of AI agents spontaneously form social norms (EurekAlert)](https://www.eurekalert.org/news-releases/1083323) · [Agentic AI and the next intelligence explosion (Science)](https://www.science.org/doi/10.1126/science.aeg1895) · [Agentic Swarms: Lessons from Nature for Enterprise AI (Tredence)](https://www.tredence.com/blog/agentic-swarms-lessons-from-nature-for-machine-intelligence) · [aaronjmars/MiroShark on GitHub](https://github.com/aaronjmars/MiroShark)*
