# Linear antipodal detours inside connected switch components

- Stable ID: note_nori_antipodal_switch_component_long_detours_20261015
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: obstruction, counterexample, switch-graph
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r9344_2
- Updated session: session_nori_r9344_2
- Disposition: none
- Successor: none

## Related references

- subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths

## Research note

**Theorem (switch-component antipodal detour).** For every integer h>=1 and odd r>=1, put n=6h+r. An antipodally odd Boolean function f:Q_n -> F_2 can have an antipodally invariant connected component W of its switching-edge graph such that every path in W between antipodal vertices has length 10h+r=n+4h. Thus antipodal connectivity alone does not force a dimension-simple full antipodal switching geodesic, and the additive detour can grow linearly with dimension.

*Proof.* Let P be the 10-edge Q_6 path with binary-encoded vertices (0,1,3,7,6,14,12,13,29,31,63). Let S be the union of its vertex set and its bitwise complements under v -> 63-v. Direct Hamming-distance-one comparisons show that Q_6[S] is an induced 20-cycle, on which the complement is a half-turn. Its intrinsic distance from every vertex to its complement is therefore 10.

Set W=S^h x Q_r inside Q_n. As an induced Cartesian product of h copies of C_20 and Q_r, W is connected, antipodally invariant, and satisfies d_W(x,bar x)=10h+r for every x in W.

Define q(x)=0 on W and q(x)=1 outside W, and f(x)=q(x)+sum_i x_i modulo two. The function q is antipodally even and n is odd, so f is antipodally odd. On every cube edge uv the vertex parity changes, hence f(u)!=f(v) precisely when q(u)=q(v). Consequently the switch graph of f consists of the induced graphs on the two level sets of q, with W as one whole connected component. Its antipodal distances exceed n, prohibiting a full dimension-simple switching geodesic inside W. QED.

The near-capacity switch-packing theorem gives a stronger, dimension-simple witness from disjoint odd switch channels; the present example shows why antipodal connectedness without a capacity constraint is insufficient. This does not resolve NORI1.
