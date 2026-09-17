# A7C3 Spare Parts

This directory contains deliberately rescued reusable mathematics from discarded Engines, genuinely useful results that do not belong to a surviving Engine, and compact archived mechanisms whose statements and proofs are sufficiently self-contained to be useful independently of their original research lane. Spare-part identifiers use `S<N>` beginning at `S9001`.

Do not promote ordinary incremental research here merely because it passed audit. Prefer coherent Engine development. The admission test is intentionally a little permissive: a result may belong here when its surrounding Engine is being discarded, when no coherent Engine applies, or when an archived local theorem, finite classification, augmentation move, extremal bound, normalization lemma, or guardrail is independently reusable enough that future work should not have to rediscover it. Engine-sized frameworks and lane-specific bookkeeping still stay out.

## Two-tier organization

Spare Parts are organized by expected reuse, not by truth status or proof quality. Every admitted Spare Part remains durable mathematics.

### [`CORE_TOOLKIT/`](CORE_TOOLKIT/)

The default theorem shelf: broadly reusable, high-leverage lemmas and mechanisms likely to be useful across multiple A7C3 proof lanes. Ordinary Researcher initialization should skim [`CORE_TOOLKIT/STATEMENTS.md`](CORE_TOOLKIT/STATEMENTS.md). Open the individual `S####_*.md` file before relying on exact hypotheses, scope, conventions, proof, or provenance.

### [`SPECIALIZED_TOOLKIT/`](SPECIALIZED_TOOLKIT/)

Narrower but still reusable mathematics: special normal forms, exceptional guardrails, parameter-specific finite tools, and mechanisms whose hypotheses make them less likely to be useful in an arbitrary research session. [`SPECIALIZED_TOOLKIT/STATEMENTS.md`](SPECIALIZED_TOOLKIT/STATEMENTS.md) is available when a lane suggests one of these tools, but it is intentionally not part of ordinary startup.

The boundary between the tiers is pragmatic rather than permanent. A Spare Part may move tiers if repeated use shows that its expected utility was misjudged. Such a move does not change its mathematical status.

## Current allocation

**Core Toolkit (31):** `S9001-S9006`, `S9008-S9015`, `S9017`, `S9019-S9025`, `S9029-S9030`, `S9032-S9036`, `S9038-S9039`.

**Specialized Toolkit (9):** `S9007`, `S9016`, `S9018`, `S9026-S9028`, `S9031`, `S9037`, `S9040`.
