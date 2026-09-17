# GN3 research state

This is the compact big-picture entry point after `ARCHITECTURE.md`. It is not a substitute for the proof spine and does not define mathematical objects by proof history.

## Problem

Prove that every finite 3-uniform boundary tournament has path-cover number at most two.

The canonical proof attempt is `PROOF_SPINE/TWO_TIGHT_PATHS.md`. Its exact status is recorded in `STATUS.md`.

## Present proof picture

Assume a smallest counterexample `H`. The audited spine establishes the following route in ordinary mathematical language.

1. Minimality forces `pc(H)=3`, gives exact two-path covers after deleting one vertex or a fixed pair, and bounds every tight path and cycle by `n-4` vertices.
2. Small-order arguments using the comparison orientation of the line graph, five-vertex edge orders, a fixed-three-vertex-path extension lemma, and a Johnson-graph cut bound show `n>10`.
3. Endpoint transfers lead to spanning three-path covers with a longest component whose ends cannot absorb endpoints of the other components. A lexicographically maximal spanning three-path cover has a globally longest first component and forbids every transfer from a donor into a recipient of at least equal order.
4. For a fixed pair `{a,c}`, every other vertex belongs to one of two orientation classes according as `(a,s,c)` or `(c,s,a)` is tight. The two associated source paths have explicit fixed-pair restrictions. When genuine reachability is required, Section 4 uses an intrinsically defined relation on oppositely extended path pairs; endpoint reductions, one-vertex shortenings, and prescribed singleton replacements are the only allowed transitions.
5. Comparing two-path covers before and after deleting an internal vertex produces an explicit crossing of ordinary edges and one forced tight orientation. Separate fixed-pair arguments provide same-orientation internal vertices and useful five-vertex tight paths.
6. For a lexicographically maximal spanning three-path cover `A|B|C`, Proposition 6.2 combines the longest-component end restrictions with the fixed-pair reduction machinery at four specified end vertices.

## Earliest unresolved step

The current load-bearing gap is the augmentation statement stated after Proposition 6.2:

Given a spanning three-path cover `F` of a smallest counterexample for which no endpoint can be transferred from one component into another component of at least equal order, prove that either a spanning two-path cover exists or there is a spanning three-path cover `F'` with `lambda(F')` lexicographically larger than `lambda(F)`.

For the extremal `F` already chosen in Section 6, the second outcome is impossible. Thus this bridge would close the conjecture.

The missing work is not another local contact statement. A successful argument must construct a literal spanning replacement: every retained subpath, every join, every required tight triple, disjointness of the resulting components, and the disposition of every vertex must be explicit.

## Research priorities

The Director default is the augmentation gap above. Bounded alternative work is welcome when it could replace that bridge with a simpler parent theorem or expose a genuinely different global mechanism.

Researchers should use the proof spine as mathematics, not reconstruct A7C3 terminology. The most relevant existing inputs are the extremal-cover restrictions of Section 6, the fixed-pair continuation results of Section 4, the deletion/crossing mechanism of Section 5, and the ordinary ordered-path intersection lemmas in Appendix A.

A search that finds no proof is an acceptable outcome. Distinguish a counterexample, a necessary missing hypothesis, a concrete structural obstruction, and merely “no proof found.” Only the first three defeat an abstraction.

## Reusable results

The small selected reusable shelf is indexed in `TOOLKIT/README.md`. Proof-local statements remain in the proof spine rather than being duplicated into a second theorem graph.
