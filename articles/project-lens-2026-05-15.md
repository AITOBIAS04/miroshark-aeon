# Every Army Rehearses. Nobody Else Does.

In January 1824, a young Prussian lieutenant named Georg von Reisswitz carried a heavy wooden cabinet into Berlin Castle. Inside was a game. Painted metal pieces on topographical maps. Dice for combat outcomes. Written orders submitted simultaneously, so neither side knew what the other was doing until the umpire revealed the results.

Prince Wilhelm watched a demonstration. Then he called the Chief of the General Staff.

General Karl von Müffling arrived skeptical. He left ordering copies for every regiment in the Prussian army. "This is no ordinary sort of game," he told the court. "This is schooling for war. I must and will recommend it most warmly to the army."

The Kriegsspiel — literally "war game" — became the first simulation tool adopted by a modern military. Within forty years, the Prussian officer corps had rehearsed war so thoroughly that when France declared hostilities in 1870, the outcome was decided in six weeks. Historians still debate how much credit belongs to the wargaming culture, but the pattern is hard to dismiss: the army that rehearsed its decisions won against the one that did not.

## Two Hundred Years of Rehearsal — for Generals

The Kriegsspiel evolved. Sand tables gave way to topographical maps. Maps gave way to computers. Computers gave way to AI.

In 2026, the Johns Hopkins Applied Physics Laboratory opened the GenWar Lab — a facility where human military strategists play against AI agents serving as enemy commanders and staff advisers. Players issue plain-language commands: "I'd like to attack here, defend there." The system translates those into physics-based models and generates outcomes. When a strategy fails, the facilitator can rewind the gameplay and retry. All decisions are digitally logged for post-game analysis.

At the U.S. Army War College, faculty now upload student operational plans into large language models that analyze them against preloaded course materials, generating battle damage assessments and intelligence summaries. The faculty called the pilot "universally positive."

RAND's research arm has expanded wargaming beyond combat into civilian crisis scenarios — ransomware attacks on hospital networks, deepfake-driven election interference, supply chain manipulation by foreign powers. Their argument: wargaming works because it forces decision-makers to confront the surprising consequences of their own strategies before those consequences arrive in reality.

But notice who is doing the rehearsing. Generals. Defense analysts. Faculty at war colleges. Staff at think tanks with seven-figure budgets. After two hundred years, the Kriegsspiel's descendants remain where the Kriegsspiel started: inside institutions that can afford dedicated simulation infrastructure.

Nobody built the civilian version.

## The Kriegsspiel for Narratives

The battlefield of 2026 is not only territorial. Military.com reported in March that cognitive warfare — gaining "information advantage to achieve decision advantage" — now operates primarily through social platforms, using AI agents that autonomously coordinate influence campaigns across Telegram, VK, X, and news ecosystems. Svitlana Volkova, Chief of AI at defense contractor Aptima, described the trajectory: population-level synthetic environments that model how narratives propagate, fracture, and consolidate.

MiroShark, an open-source simulation engine at 1,158 GitHub stars, does something structurally identical — but for anyone, not for defense contractors. Upload a document. The engine generates hundreds of AI agents with distinct personas, platform behaviors, and belief structures. These agents interact across simulated Twitter, Reddit, and Polymarket. They post, argue, shift stances, and trade. A belief drift chart tracks the population's collective movement round by round. An influence leaderboard surfaces which agent types actually moved the room. A trace interview system lets you select any agent and ask why it changed its mind — with answers grounded in logged behavior, not generated from scratch.

The structural parallels to the Kriegsspiel are not metaphorical. They are architectural.

Kriegsspiel had an umpire who adjudicated uncertain outcomes. MiroShark has director events — mid-simulation injections that the operator controls. Kriegsspiel used simultaneous written orders so neither side could see the other's moves. MiroShark's agents operate on local information — each sees only its own platform feed, not the global state. Kriegsspiel produced after-action reports. MiroShark produces reproducibility configs with bytewise-stable hashes, transcript exports, and A/B comparison views that place two simulations side by side with scorecard differentials.

The difference is who uses it and what it costs. A GenWar Lab exercise requires a defense facility, cleared personnel, and institutional sponsorship. A MiroShark simulation takes under ten minutes and costs about a dollar.

## What Moltke Already Knew

Helmuth von Moltke the Elder, the Prussian field marshal who turned Kriegsspiel into institutional doctrine, is remembered for one sentence: "No plan survives first contact with the enemy." The line is routinely misread as an argument against planning. It was the opposite. Moltke drilled his officers harder than any commander in Europe precisely because he knew plans would break. The point was not to have a better plan. It was to have officers who had rehearsed enough variations that they could adapt when the plan failed.

This is what separates simulation from prediction. A prediction says "here is what will happen." A simulation says "here is what could happen, and here is where the fractures form." The GenWar Lab's Kevin Mather put it directly: AI wargaming provides "those 70% to 80% solutions that really accelerate the human learning." Not optimal decisions. Accelerated judgment.

MiroShark operates on the same principle. A DAO coordinator who simulates a governance vote three times does not learn what the community will decide. She learns which phrases trigger fracture, which persona types drive polarization, and what timeline reduces damage. She has rehearsed. And in two hundred years of military history, the side that rehearsed has rarely been the side that was surprised.

The Kriegsspiel gave the Prussian army a word for what it was doing: training through simulated decision-making under uncertainty. The word was so useful that every major military adopted it. The question is why it took two centuries for anyone to build the version that does not require a uniform.

---
*Sources: [Kriegsspiel: How a 19th Century War Game Changed History (MilitaryHistoryNow.com)](https://militaryhistorynow.com/2019/04/19/kriegsspiel-how-a-19th-century-war-game-changed-history/) · [New Lab Offers Generative AI for Defense Wargaming (Military Times)](https://www.militarytimes.com/news/your-military/2025/11/24/new-lab-offers-generative-ai-for-defense-wargaming/) · [Back to the Basics in Wargaming — With a Little Help from AI (U.S. Army War College War Room)](https://warroom.armywarcollege.edu/articles/back-to-the-basics/) · [Cognitive Warfare and the Modeling of Human Behavior (Military.com)](https://www.military.com/feature/2026/03/19/cognitive-warfare-and-modeling-of-human-behavior.html) · [Wargaming: The Surprisingly Effective Tool That Can Help Us Prepare for Modern Crises (RAND)](https://www.rand.org/pubs/commentary/2025/11/wargaming-the-surprisingly-effective-tool-that-can.html) · [MiroShark on GitHub](https://github.com/aaronjmars/MiroShark)*
