# Hot shelf

**Status: PROVISIONAL STRATEGIC DELTA SURFACE.**

This directory is not an audited mathematical shelf and does not confer certification.

SHELVES/CORE/ and SHELVES/UTILITY/ remain the only certified staging shelves. SHELVES/HOT/ exists to give Astra and the Vice Director a compact, version-controlled view of recent mathematics that materially shapes the live strategic state but has not yet settled into an ordinary shelf candidate.

## Purpose

Before an Astra escalation, the Vice Director should make the project mathematically compressive in this order:

1. complete ordinary integration of already-certified mathematics that is ready for SHELVES/CORE/ or SHELVES/UTILITY/;
2. update the relevant ordinary shelf candidates/admissions under the normal audit gate;
3. place only the remaining recent, state-shaping mathematics into the hot shelf;
4. provide Astra the Git shelf delta since Astra's previous synchronization baseline.

The hot shelf prevents Astra from spending scarce context reconstructing the current frontier from Slack.

## Content standard

The hot shelf contains only mathematics or strategic mathematical facts that Astra may need to understand the live frontier and that are not yet represented adequately in the current ordinary shelves.

Suitable hot-shelf content includes:

- newly certified results whose conceptual placement is not yet stable enough for an ordinary shelf composition;
- important provisional results that materially affect the current strategic picture;
- decisive counterexamples, retractions, or negative evidence that change what routes remain plausible;
- a concise exact statement of the present unresolved mathematical obstruction when it is not yet represented in ordinary shelves;
- a small number of competing parent formulations when Astra is being asked to choose between them.

Do not use the hot shelf for:

- routine Slack chronology;
- worker status;
- audit transcripts;
- clerical notes;
- every recent lemma;
- material already represented adequately in SHELVES/CORE/ or SHELVES/UTILITY/;
- speculative side ideas that do not affect the strategic frontier.

Each hot item should state the mathematics intrinsically and, when relevant, mark its certification state as CERTIFIED, PROVISIONAL, or RETRACTED/NEGATIVE. Exact Slack or Git coordinates may be included sparingly for retrieval, but they are not substitutes for the mathematical statement.

## Astra file

SHELVES/HOT/ASTRA.md is the rolling Astra-facing hot shelf.

It is deliberately mutable and version-controlled. The Vice Director refreshes it before every Astra escalation. Old hot material should be removed when it becomes represented in an ordinary shelf, is subsumed, is defeated, or ceases to affect the strategic frontier.

The file should remain compact enough that Astra can read it in full cheaply.

## Delta protocol

Every Astra escalation should identify:

- the Git commit corresponding to Astra's last trustworthy shelf synchronization, when known;
- the current handoff commit after the Vice Director's ordinary shelf updates and hot-shelf refresh.

Astra should inspect the Git delta between those commits restricted to:

- SHELVES/CORE/;
- SHELVES/UTILITY/;
- SHELVES/HOT/ASTRA.md.

That shelf delta is Astra's default mathematical catch-up surface.

If no trustworthy prior Astra baseline exists, Astra reads the current relevant ordinary shelf files plus SHELVES/HOT/ASTRA.md rather than reconstructing the state from Slack.

Slack is a fallback only when the curated shelf delta leaves a strategically necessary ambiguity or when an exact live statement has not yet been incorporated into the hot shelf.
