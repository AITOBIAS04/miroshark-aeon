# Every Dependency Is a Handshake You Can't Take Back

On May 11, 2026, a group calling themselves TeamPCP compromised 170 npm packages and 2 PyPI packages in a single coordinated operation. They did not create fake packages. They did not typosquat popular names. They exploited a chain of three GitHub Actions vulnerabilities to extract OIDC tokens from runner process memory, then used those tokens to publish 404 malicious versions of real, trusted packages — TanStack, Mistral AI, OpenSearch, Guardrails AI. The payload spread through npm lifecycle hooks, stealing GitHub tokens, npm credentials, and AWS keys, then self-propagating through victim repositories in a worm-like pattern. Fifteen million users were in the blast radius before GitHub patched the vulnerability three days later.

The attack was not novel in kind. Three supply chain attacks had already hit npm, PyPI, and Docker Hub in a single 48-hour window the month before, all targeting developer credentials. PyTorch Lightning was compromised on PyPI in April. SAP's npm packages were hit in late April. What made the May 11 event different was its scale and its method: the attackers never needed a single stolen password. They used the infrastructure of trust itself — the CI/CD pipeline — as the weapon.

## The Architecture of Trust

Every dependency in a software project is a trust relationship. Not a technical relationship — a trust relationship. When you add `leftpad` or `is-even` or a date-formatting library to your dependency tree, you are not merely importing code. You are declaring: I trust the maintainer of this package, everyone who has commit access to its repository, every dependency that package itself depends on, and every CI/CD system that touches its release pipeline. You are trusting them today, and you are trusting whoever they will be next year.

This is not a new observation. But the May 2026 attacks gave it a new texture. The compromised packages were not obscure. OpenSearch had 1.3 million weekly npm downloads. TanStack Router is part of a framework used by thousands of production applications. The maintainers did nothing wrong. Their CI infrastructure was turned against them.

The common response is to add more security tooling: lockfile audits, provenance checks, dependency scanning. These help at the margin. They do not change the structural reality that every dependency is an attack surface you do not control.

## Thirty Pull Requests, Zero New Dependencies

MiroShark is an open-source simulation engine — 1,190 stars, 243 forks — that lets anyone model how opinions spread through social networks. Over the past six weeks, the project has merged 30 consecutive pull requests. Not one of them added a new dependency.

This is not a boast and it is not an accident. Every new service in the project — from a Telegram Bot notification system to a trading signal JSON endpoint to a Shields.io-style SVG badge renderer — is written using Python's standard library. The badge service uses `xml.etree.ElementTree`. The archive bundle uses `zipfile` and `hashlib`. The notification services use `urllib.request`. The trajectory export uses `csv` and `json`. No requests. No Flask extensions. No template engines. No image libraries.

The constraint is severe. Writing a Shields.io-compatible SVG renderer from scratch with ElementTree is harder than importing a library. Building five notification channels (webhook, Discord, Slack, SMTP, Telegram) without a single HTTP client library means writing the same boilerplate more than once. A developer raised on the "don't reinvent the wheel" maxim would find this approach perverse.

But the result is a project with exactly one trust relationship in its dependency chain: CPython itself. The attack surface is not zero — nothing is — but it is as small as a Python project can make it without writing its own interpreter.

## Composability Without Coupling

The deeper argument for zero-dependency design is not about security. It is about composability — and the distinction between composability and coupling.

MiroShark now has 13 independent "share surfaces": ways to consume, embed, or distribute a simulation's results. A share card. A chart SVG. A trajectory CSV. A Jupyter notebook. A trading signal JSON. A consensus badge SVG. An RSS feed. A Farcaster Frame. An archive bundle. Each is a standalone endpoint behind the same publish gate. Each can be consumed independently by a different tool: a README embeds the badge, a quant pipeline reads the signal JSON, a researcher downloads the archive ZIP.

The archive bundle is the telling case. It calls every other surface renderer — share card, chart, trajectory, transcript, notebook, signal — and assembles the results into a single ZIP with a SHA-256 manifest. This is composition in the Unix sense: small programs connected by pipes, where the output of one is the input of another. But unlike a typical microservice architecture, none of these surfaces depend on each other through package imports. They compose through data, not through code. The archive service calls functions in the same codebase; it does not import a third-party orchestration library.

As Dawid Prus argued in a recent essay on zero-dependency design: "Zero-dependency packages leave the model room to think. Dependency stacks fill it with noise." The insight extends beyond AI. Zero-dependency services leave the *system* room to compose. Every package you import is a joint you cannot bend.

## The Standard Library as a Declaration

There is a philosophical dimension here that the security framing misses. Choosing to build with only the standard library is not just risk mitigation. It is a declaration about what kind of software you are building and how long you expect it to last.

Dependencies rot. Not because their maintainers are negligent, but because the ecosystem moves. A library that targets Python 3.10 may not work on 3.14. An npm package that was maintained by one person in 2024 may be abandoned by 2027, or sold to a company that inserts telemetry, or compromised by an attacker who waits for the maintainer to lose interest. The half-life of a dependency is shorter than the half-life of the software that depends on it.

The standard library, by contrast, is a commitment. When CPython ships `json` and `csv` and `hashlib`, it is promising that those modules will work for as long as CPython exists. The interfaces may evolve, but they will not vanish. Building on stdlib is a bet that the language will outlast the ecosystem — a bet that has paid off for decades.

MiroShark's 30-PR streak is a small example of a large idea: that the most composable software is the software with the fewest external joints. Every dependency you avoid is a future you do not have to negotiate with. Every surface you build from stdlib is a surface that will still work when the npm registry has its next bad week.

And it will have another bad week. The only question is whether your software will notice.

---
*Sources:*
- *[Understanding the 314 npm Packages Compromise](https://dasroot.net/posts/2026/05/314-npm-packages-compromise-supply-chain-attack/) — dasroot.net, May 2026*
- *[The Rise of Zero-Dependency Powerhouses](https://medium.com/@zfoq/the-rise-of-zero-dependency-powerhouses-and-why-they-matter-more-in-the-age-of-ai-7baecaae3d8a) — Dawid Prus, Medium, March 2026*
- *[Three Supply Chain Campaigns Hit npm, PyPI, and Docker Hub in 48 Hours](https://blog.gitguardian.com/three-supply-chain-campaigns-hit-npm-pypi-and-docker-hub-in-48-hours/) — GitGuardian, April 2026*
- *[Mass npm Attack Hits TanStack and Mistral AI](https://dasroot.net/posts/2026/05/mass-npm-attack-tanstack-mistral-ai-dependency-security/) — dasroot.net, May 2026*
