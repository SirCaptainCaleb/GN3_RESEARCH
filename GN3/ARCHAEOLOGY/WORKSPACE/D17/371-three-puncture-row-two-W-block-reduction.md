# Every three-spoke puncture row is two-W-block outside immediate component drop

**Workspace:** D17
**State:** established
**Key:** `three-puncture-row-two-W-block-reduction`

**Summary:** Let K=(x,a,y,c,z) be the retained three-spoke P5 and W=V(H)-V(K). For any root d in {x,y,z}, let S_d=V(K)-{d} and let T_d be any exact two-cover of H-d. R508 applied with deletion D={d}, absorbable block S_d, and extension path K forces T_d to select a crossing between S_d and W. Equivalently the restriction of T_d to W has at least two maximal W-blocks. If it has c>=3 W-blocks, these blocks form a literal c-cover of H[W], while smallest-counterexample minimality R4 supplies a literal cover of W with at most two components. R159 therefore gives a graph-intrinsic balanced pair. Hence outside component-drop geometry every puncture row d=x,y,z has exactly two W-blocks. The remaining G30 core is therefore a finite two-block crossing system to which R509 applies cut-by-cut when its outward incidences are present.

### 1. Source three-puncture setup
Retain the three-spoke source P5

  K=(x,a,y,c,z)

and put

  W=V(H)-V(K).

Fix any root d in {x,y,z}. Let

  S_d=V(K)-{d}.

Because K-d is a literal Hamilton tight path on S_d and K itself is a tight path on {d} union S_d, accepted R508 applies to every literal exact two-cover T_d of H-d. Therefore T_d selects at least one directed state crossing S_d|W. In particular the vertices of W cannot occupy a single maximal W-block inside the two rails of T_d.

### 2. W-block count
Delete the four vertices S_d from the two rails of T_d. The surviving nonempty path segments are exactly the maximal W-blocks of T_d. Let their number be b_d. Section 1 gives

  b_d >= 2.

These b_d blocks are vertex-disjoint tight paths whose supports partition W, so they form a literal b_d-cover of H[W].

### 3. Three or more W-blocks immediately give component-drop geometry
Assume b_d>=3. Since W is a nonempty proper induced subsystem of the smallest counterexample H, accepted minimality R4 supplies a literal path cover T of H[W] with at most two components. Comparing the b_d-cover formed by the W-blocks of T_d with this at-most-two cover gives a strict component drop. Accepted R159 therefore yields a graph-intrinsic balanced opposite-sign pair in H.

Thus every puncture row satisfies the dichotomy:

1. b_d>=3 and R159 component-drop geometry is already present; or
2. b_d=2 exactly.

No synchronization between the representatives T_x,T_y,T_z is asserted. The conclusion is row-wise and applies independently to every exact representative.

### 4. G30 consequence
Outside the already-compiled component-drop branch, the simultaneous three-puncture object of G30 may be normalized so that every chosen row H-x, H-y, H-z has exactly two maximal W-blocks. The surviving data are therefore finite: for each four-vertex petal K-d, one has a two-rail exact cover with exactly two W-blocks and at least one selected petal-to-W or W-to-petal crossing. R509 may then be applied at any crossing whose cut-indexed outward incidence hypotheses are met.

This section does not claim those partner incidences are automatic and does not itself close the two-block rows. It only removes all higher W-block multiplicity from the quiet three-puncture core. R24 and R5 are unused.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R4"
    },
    {
        "relation": "dependency",
        "revision_id": "R508"
    },
    {
        "relation": "dependency",
        "revision_id": "R159"
    }
]
```