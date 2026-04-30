# From Kriegsspiel to GitHub: The 200-Year-Old Military Practice That AI Is Quietly Reinventing

In 1811, a Prussian lieutenant named Georg von Reiswitz presented his king with a gift: a table-sized battlefield made of plaster terrain tiles, zinc unit markers, and a set of dice weighted to simulate the randomness of combat. It was called Kriegsspiel — literally, "war game" — and it was designed to answer a question that had haunted military commanders for centuries: *what would happen if we tried this before anyone died?*

The idea was deceptively simple. Two teams sat in separate rooms, each with their own map showing only what their forces could see. They wrote orders to imagined subordinates. Umpires — called *Vertraute*, "trusted persons" — processed those orders, applied the rules of physics and chance, and reported back outcomes filtered through the fog of war. No team knew the full picture. Every decision was made with incomplete, unreliable information about what the other side was doing.

Within decades, Kriegsspiel was credited with helping Prussia crush France in 1870. By 1900, every industrialized military in the world had adopted some form of war gaming. The practice had proved something that felt obvious in retrospect: rehearsing decisions against simulated adversaries before making them against real ones is not just prudent — it is a structural advantage.

Two hundred years later, that insight is being rediscovered in a place no Prussian officer would recognize.

## The Simulation Tradition Never Stopped

After Kriegsspiel came the RAND Corporation. In the 1950s, RAND built the first political-military simulations — the "Cold War Games" — pitting mathematicians against social scientists in scenarios involving nuclear crises. The mathematicians launched nukes quickly. The social scientists showed restraint. The divergent outcomes revealed something no position paper could: that the identity and disposition of the decision-maker shaped the outcome as much as the facts on the ground. RAND's work laid the foundation for mutually assured destruction doctrine, which arguably prevented nuclear war for half a century.

The tradition continued. In April 2026, the U.S. Air Force debuted WarMatrix, an AI-powered wargaming system that ran simulations at thousands of times real-time speed during a two-week exercise attended by over 150 people — technical experts, Air Force leadership, and allied planners. Its designers described it as a "human-machine teaming system" built for "transparency, auditability, and speed."

And in February, a King's College London study by strategy professor Kenneth Payne put three frontier LLMs — Claude Sonnet 4, GPT-5.2, and Gemini 3 Flash — into simulated nuclear crises against each other. The result: nuclear escalation occurred in nearly every scenario. The models deployed tactical nuclear weapons repeatedly across border skirmishes, resource competition, and survival threats. Payne's conclusion was blunt: "We have never truly understood the logic underpinning them." The AI decision-makers were black boxes providing answers without showing reasoning.

That study inadvertently made the case for an entire category of software.

## The Civilian Kriegsspiel

MiroShark is an open-source project that has grown to 886 GitHub stars and 171 forks since its launch in late March. It describes itself as a Universal Swarm Intelligence Engine. The pitch: upload any document — a policy proposal, an earnings call transcript, a regulatory filing — and MiroShark generates hundreds of AI agents with distinct personas, backgrounds, and behavioral profiles. These agents react across simulated Twitter, Reddit, and Polymarket platforms simultaneously. They post, argue, shift stances, and trade. Belief states track each agent's confidence and trust levels per round. At the end, a report synthesizes what happened and why.

The structural parallel to Kriegsspiel is closer than it first appears. In the Prussian game, two teams operated from separate maps showing only what they could observe, while umpires maintained the single "true" map. In MiroShark, each agent operates from its own persona context — a five-layer knowledge graph including background, expertise, behavioral tendencies, and evolving beliefs — while the system tracks the aggregate reality across all platforms. No single agent sees the full picture. Every decision is made with incomplete information shaped by the agent's identity. Just as RAND discovered that mathematicians and social scientists reached different conclusions from the same crisis, MiroShark reveals how a population of diverse agents — cautious analysts, aggressive traders, skeptical journalists — fragment and converge around the same stimulus.

The difference is that what took Prussian umpires days and RAND analysts weeks, MiroShark executes in under ten minutes for about a dollar.

## Why Auditability Is the Feature That Matters

The King's College study exposed a problem that the wargaming tradition solved two centuries ago: if you cannot trace *why* a decision was made, the simulation teaches you nothing. Prussian umpires kept detailed logs. RAND analysts wrote post-game reports. The Air Force built WarMatrix specifically for "transparency and auditability."

MiroShark has been building exactly this infrastructure. A trace interview system lets users select any agent from the influence leaderboard after a simulation and interrogate it about its behavior — why it shifted stance, why it sold before the crowd turned. The responses are grounded in logged actions, not generated from scratch. A prediction resolution system records real-world outcomes and computes accuracy against actual Polymarket price data. A belief drift chart visualizes per-round stance distributions across the entire agent population with consensus detection. A verified gallery now lets users publish simulation results with tracked accuracy records.

Most recently, a simulation transcript export produces full Markdown and JSON records of every round — the civilian equivalent of a wargame after-action report. An animated belief-replay GIF endpoint lets researchers share the evolution of crowd sentiment as a visual artifact.

Each of these features mirrors something the military simulation tradition learned through hard experience: the value of a simulation is not in the outcome but in the audit trail. A war game that ends with "we lost" is useless. A war game that ends with "we lost because the third division moved too slowly through the Ardennes, and here are the orders that caused it" is a strategic education.

## The Democratization of Rehearsal

For two hundred years, serious simulation was expensive and exclusive. Kriegsspiel required trained umpires and days of officer time. RAND's games required clearances and PhD-level analysts. The Air Force's WarMatrix exercise took two weeks and 150 specialists. The King's College study required custom infrastructure to pit frontier LLMs against each other in controlled scenarios.

MiroShark runs locally on a laptop. It costs a dollar per simulation. It requires no clearance, no umpires, and no two-week exercise. A policy researcher can simulate crowd reaction to a proposed regulation before it is announced. A crypto community can model how a market might respond to a governance vote. A journalist can test whether a story will polarize along predictable lines.

The 200-year arc from Kriegsspiel to MiroShark is not a story about technology — it is a story about who gets to rehearse. The Prussian military understood that decisions made without simulation are gambles. RAND understood that simulation reveals the decision-maker's biases as clearly as it reveals the scenario's outcomes. The King's College study demonstrated that AI agents left unsimulated will escalate to catastrophe almost every time.

The question is no longer whether to simulate before acting. It is whether simulation remains a privilege of defense ministries and research labs, or becomes as accessible as a GitHub clone.

---
*Sources: [Prussian Kriegsspiel history](https://cosimg.github.io/2019/11/03/prussian-kriegsspiel.html) · [RAND Corporation political-military wargaming](https://tnsr.org/2021/09/moral-choices-without-moral-language-1950s-political-military-wargaming-at-the-rand-corporation/) · [AI war games escalate to nuclear strikes (Live Science)](https://www.livescience.com/technology/artificial-intelligence/ai-war-games-almost-always-escalate-to-nuclear-strikes-simulation-shows) · [US Air Force debuts WarMatrix (Defense News)](https://www.defensenews.com/industry/techwatch/2026/04/15/us-air-force-debuts-operational-ai-wargame-system/) · [aaronjmars/MiroShark](https://github.com/aaronjmars/MiroShark)*
