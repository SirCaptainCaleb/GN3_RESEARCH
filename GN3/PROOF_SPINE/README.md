# GN3 proof spine

**Status: supervised migration reconstruction; not yet GN3-certified.**

This directory contains the current blank-page reconstruction of the active proof of the two-path-cover theorem. The organization is mathematical rather than historical: legacy Engine boundaries are not part of the intended GN3 exposition.

A hypothetical smallest counterexample `H` satisfies `|V(H)|>10` and `pc(H)=3`.

The present spine contains two complementary mechanisms arising from closely related local geometry.

1. [`FIXED_PAIR_RETURN.md`](FIXED_PAIR_RETURN.md) fixes two vertices `{a,c}` and repeatedly uses vertices `x` for which `(a,x,c)` or `(c,x,a)` is tight. For all but at most one vertex outside `{a,c}`, the construction records strict reductions of both incident ordered pairs in that tight ordered triple to the middle vertex. Any later four-vertex configuration made from two disjoint ordered pairs must therefore meet this recorded history. If the pair through the recorded vertex has a genuinely new second endpoint, a strict extension or reversed-contact configuration follows. The unresolved case is when that pair uses exactly one of the two old supports through `{a,c}`.

2. [`FIRST_SOURCE_DESCENT.md`](FIRST_SOURCE_DESCENT.md) now separates two different facts that were previously intertwined. A globally longest tight path gives the **shortest known route** to the current nonextendable three-path configuration; the Boolean cube is not needed for that. The longer cube construction is retained because it additionally yields a strict rank decrease relative to the finite family of maximum spanning three-path forests used in the comparison. That decrease is proved only once relative to its initial family and is not yet a recursive global order.

These mechanisms are not best viewed as unrelated branches. Both begin from abundant vertices with the same orientation through a fixed pair, but they use that geometry differently:

- the fixed-pair argument accumulates explicit reduction history at many vertices and constrains later reuse of the same physical supports;
- the cube/rank argument extracts a proper path or cycle from related exact two-path covers and obtains one strict rank decrease.

As a route merely to the current nonextendable three-path configuration, the cube construction is subsumed by the globally longest-path argument. Its reason for remaining in the spine is the additional rank and comparison information.

The two unresolved mathematical obligations are therefore:

- **fixed-pair line:** use the complete later four-vertex configuration to rule out indefinite recurrence on the two old supports through a previously reduced middle vertex, or force a spanning two-path cover or genuinely new geometry;
- **rank line:** starting from the nonextendable three-path configuration, construct a lawful recursive continuation to a spanning two-path cover or to a smaller state in a genuinely well-founded global order.

A possible synthesis, not yet a theorem, is to seek a recursive order that decreases strictly except in the exact old-support case, then use the fixed-pair reduction history to eliminate that equality case.

The mathematical files use ordinary graph-theoretic language wherever possible. Legacy result numbers are confined to provenance sections and are not intended to determine GN3 terminology or proof topology.
