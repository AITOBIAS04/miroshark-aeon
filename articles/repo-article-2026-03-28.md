# Four Ways In: How MiroShark Made Multi-Agent Social Simulation Actually Accessible

Every major AI lab shipped an agent framework in 2026. OpenAI has the Agents SDK. Google released ADK. Anthropic launched the Agent SDK. Microsoft unified AutoGen and Semantic Kernel. But none of them let you simulate what happens when 100 AI agents with distinct personalities argue about your company's press release across Twitter, Reddit, and a prediction market — and then watch the market crash because a Reddit thread went viral. MiroShark does, and eight days after launch, it runs on everything from a beefy local GPU to a Claude Pro subscription.

## The Setup Problem That Killed MiroFish's Reach

MiroFish proved the concept. The original Chinese-language project hit 33,000 GitHub stars and secured $4.1 million in funding by demonstrating that swarm intelligence could simulate public opinion at scale. But running it required a specific cloud stack, Chinese documentation, and enough patience to reverse-engineer a rapidly evolving codebase. MiroFish-Offline by nikmcfly made local inference possible, but the ergonomics remained rough.

MiroShark — Aaron Mars's English-language fork — didn't just translate the README. It rebuilt the onboarding path entirely, and the result is four distinct setup options that each target a different developer profile.

## Four Doors, One Engine

**Cloud API** is the zero-GPU path. Only Neo4j runs locally; everything else routes through OpenRouter, OpenAI, or any compatible endpoint. A simulation costs roughly $0.50–$2.00 depending on model choice, and the recommended setup uses Qwen3-235B through OpenRouter. This is the path for researchers who want results without managing infrastructure.

**Docker Compose** is one command: `docker compose up -d`. Neo4j, Ollama, and the full stack come up together. Pull two models (`qwen3.5:27b` and `nomic-embed-text`), open `localhost:3000`, and you're running simulations. This is the path for developers who want to hack on the engine itself.

**Manual Ollama** gives full control — separate Neo4j, separate Ollama, separate frontend and backend processes. This is for teams integrating MiroShark into existing infrastructure or running custom model configurations.

**Claude Code** is the wildcard. If you have a Claude Pro or Max subscription and the Claude Code CLI installed, MiroShark routes all LLM calls through it. No API key. No GPU. No cloud billing. Just `claude` in your terminal and a Neo4j instance. A typical simulation runs 40 turns with 100+ agents, and it all runs through your existing subscription. This option doesn't exist in any competing framework.

## Why Accessibility Matters for Simulation

The multi-agent simulation space has a participation problem. Academic projects like CAMEL-AI's OASIS push the theoretical frontier but require deep familiarity with the framework to produce useful results. Enterprise tools remain locked behind sales calls. The gap between "this is theoretically possible" and "I can try this on my laptop tonight" has kept multi-agent social simulation in the hands of a small research community.

MiroShark's four setup paths are a deliberate attempt to close that gap. The Docker path means a product manager can run a simulation of how Twitter would react to a product announcement without filing an infrastructure ticket. The Claude Code path means a student with a $20/month subscription can run the same simulation that a funded research lab would.

This matters because the value of social simulation increases with the diversity of people using it. A comms team stress-testing a crisis response generates different insights than a political scientist modeling opinion polarization. Both need access to the same underlying engine, but neither should need to configure Neo4j connection pooling to get started.

## 322 Stars in Eight Days

The numbers tell a clear story: 322 stars and 53 forks in eight days, with the star count climbing 15–20 per day. Two open pull requests — JSON/CSV data export and preset simulation templates — focus on reducing friction for new users. The preset templates offer six one-click scenarios (political debate, crypto token launch, corporate crisis, product announcement, historical what-if, campus controversy) that let someone run their first simulation in under a minute after setup.

MiroShark is now listed on [Microlaunch](https://microlaunch.net/p/miroshark), positioning alongside indie products rather than academic repos. The project's `package.json` declares version 0.1.0, but the feature surface — cross-platform simulation with market-media feedback loops, graph-based persona generation, belief state tracking, ReACT report agents — suggests something considerably more mature.

## The Bigger Picture

The 2026 agent framework landscape is crowded. CrewAI has 44,000 stars. LangGraph dominates Python orchestration. n8n crossed 150,000 stars as the default action layer for AI workflows. But these are general-purpose agent orchestration tools. None of them model emergent social dynamics — the specific phenomenon where individual agent behaviors compound into collective opinion shifts, market movements, and narrative cascades.

MiroShark is the most accessible entry point into that specific capability. It inherited the simulation architecture that made MiroFish a breakout success, stripped away the barriers that limited who could use it, and added the cross-platform intelligence (Twitter + Reddit + Polymarket running simultaneously with shared context) that MiroFish never shipped. Whether you're a researcher with a GPU cluster or a curious developer with a Claude subscription, the door is open.

---
*Sources: [aaronjmars/MiroShark on GitHub](https://github.com/aaronjmars/MiroShark), [MiroShark on Microlaunch](https://microlaunch.net/p/miroshark), [@aaronjmars on X](https://x.com/aaronjmars/status/2035881020302430571), [MiroShark roadmap](https://x.com/aaronjmars/status/2036818584937095581), [MiroFish: Swarm Intelligence with 1M Agents (Medium)](https://agentnativedev.medium.com/mirofish-swarm-intelligence-with-1m-agents-that-can-predict-everything-114296323663), [MiroFish $4M funding (emelia.io)](https://emelia.io/hub/mirofish-ai-swarm-prediction), [Best Open Source Agent Frameworks 2026 (Firecrawl)](https://www.firecrawl.dev/blog/best-open-source-agent-frameworks), [120+ Agentic AI Tools 2026 (StackOne)](https://www.stackone.com/blog/ai-agent-tools-landscape-2026/)*
