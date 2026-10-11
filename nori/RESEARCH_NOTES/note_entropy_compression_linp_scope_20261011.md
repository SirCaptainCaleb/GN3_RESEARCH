# Speculative LINP application of entropy compression

- Stable ID: note_entropy_compression_linp_scope_20261011
- Author: unspecified; session provenance retained
- Primary home: project:nori
- Labels: approach, historical_scope
- Lifecycle: active
- Epistemic status: proposed
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r5005_1
- Updated session: session_nori_r5005_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Historical scope note extracted from entropy_compression_finite_reconstruction_and_combinatorial_algorithms. Application criteria only; no LINP algorithm or NORI implication proved.

## 6. Possible LINP use and limits

Entropy compression is naturally compatible with finite sparse constructions; it does not require dense pattern limits. This makes it a plausible tool for randomized lower-bound constructions or path-building procedures that sometimes undo earlier choices.

For LINP, a candidate is a construction whose failure exposes a specified repeated entrance label, forbidden extra contact, or other reconstructible incidence pattern. One would need to show that:
1. every proposed extension is an edge of the given hypergraph, when constructing a path in a fixed instance;
2. erasing or replacing part of the path preserves all required linearity and distinctness conditions;
3. the failure data determine enough discarded choices to reconstruct them;
4. record growth is strictly smaller than the supply of random extension choices.

These are proposed application requirements, not a proved LINP algorithm. Linearity alone does not give a uniform bound on how many edges meet a high-degree vertex. A global longest-path condition may produce many dependent failures. Randomization does not turn a nonextendible path into an extendible one without a legitimate repair.

Entropy compression may establish termination even when defect counts fluctuate, but it cannot repair an invalid move or recover boundary data that were never recorded. In contrast to flag-algebra averaging, its main output can be an actual successful finite construction, provided the algorithm and decoder have been proved.
