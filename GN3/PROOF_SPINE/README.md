# GN3 proof spine

**Status: supervised migration reconstruction; not yet GN3-certified.**

This directory contains the current blank-page reconstruction of the active proof of the two-path-cover theorem. The organization is mathematical rather than historical: legacy Engine boundaries are not part of the intended GN3 exposition.

Read the spine in this order.

1. [`PRELIMINARIES.md`](PRELIMINARIES.md) gives the common starting argument. From a smallest counterexample it proves `pc(H)=3`, the order bound `|V(H)|>10`, the exact two-path-cover structure after deleting any two vertices, and the orientation-class facts through a fixed pair. In particular, any exact two-path cover of `H-{a,c}` has at least five internal vertices and therefore three internal vertices with the same orientation through `{a,c}`.
2. [`FIXED_PAIR_RETURN.md`](FIXED_PAIR_RETURN.md) uses a fixed pair `{a,c}` and retains explicit path-contact certificates at all but at most one other vertex. These certificates constrain how a later four-vertex configuration can reuse the same two-vertex supports.
3. [`FIRST_SOURCE_DESCENT.md`](FIRST_SOURCE_DESCENT.md) contains two distinct routes. The globally longest-path argument is the shortest universal route to the present nonextendable three-path configuration. Separately, the longer Boolean-cube argument is retained because it supplies a strict one-step numerical decrease relative to the finite family of maximum three-path forests used in that comparison.

The topology is important. The **fixed-pair argument** and the **Boolean-cube comparison** share the same local setup: many vertices have one of the two orientations `(a,x,c)` or `(c,x,a)` through a fixed pair `{a,c}`. The **globally longest-path argument does not use that setup**; it reaches the same nonextendable three-path configuration directly from a longest tight path.

The two fixed-pair-based constructions use their common geometry differently:

- the fixed-pair argument retains concrete earlier-path certificates at many vertices and constrains later reuse of the same physical supports;
- the cube argument compares related exact two-path covers, extracts a proper path or cycle, and obtains one strict numerical decrease relative to the finite initial family.

As a route merely to the current nonextendable three-path configuration, the cube construction is subsumed by the globally longest-path argument. Its reason for remaining in the spine is the additional source-relative comparison information. That numerical decrease is not yet an intrinsic recursive rank and cannot simply be restarted from the terminal configuration.

The two unresolved mathematical obligations are therefore:

- **fixed-pair line:** use the complete later four-vertex configuration to rule out indefinite recurrence on the two old supports through a vertex carrying both retained path-contact certificates, or force a spanning two-path cover or genuinely new geometry;
- **descent line:** starting from the nonextendable three-path configuration, construct a valid recursive transformation to a spanning two-path cover or to a smaller state in a genuinely well-founded global order.

A possible synthesis, not yet a theorem, is to seek a recursive order that decreases strictly except in the exact old-support case, then use the fixed-pair retained path-contact certificates to eliminate that equality case.

The mathematical files use ordinary graph-theoretic language wherever possible. Legacy result numbers are confined to provenance sections and are not intended to determine GN3 terminology or proof topology.
