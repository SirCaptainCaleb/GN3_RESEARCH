# Unbounded cyclic sink components with seven branching directions are eliminable

- Stable ID: note_ec2d6f90162913dfeb02cff2
- Author: unspecified; session provenance retained
- Primary home: subsection:directed_influence_components_and_monotone_seam_lifting
- Labels: scc, unbounded-feedback, branching, profile-factorization
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10487_3
- Updated session: session_nori_r10487_3
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Let c be legal and K a nonempty sink set in its directed influence graph, with R=[n]\K nonempty. Put H={i in K: i influences at least two different direction rules}, L=K\H. Assume |H|<=7; no bound on |K|. Then W(c)=W(c_R) times F_2^K and ell(c)=ell(c_R)+|K|.

Single-edge repair lemma: If an antipodal walk uses direction i once and every out-neighbor of i also occurs at most once, and i has at most one out-neighbor j, its i-step can be assigned either color while retaining all other traversed edge colors. If j precedes i, move i to the last step, otherwise to the first. This crosses no direction whose color rule depends on bit i. For first i, replace root x, order (i,sigma) by root bar(x+e_i), order (i,reverse sigma); only the first edge becomes antipodal, the remainder is traversed backwards. For last i, replace root x, order (sigma,i) by root bar x+e_i, order (reverse sigma,i). This toggles only the last edge. Both manipulations preserve antipodality even when exterior directions repeat.

Profile factorization: Start with any full c_R geodesic realizing arbitrary exterior profile w, append each L direction once, and use the established B_k antipodal two-phase bridge on H (size<=7) to prescribe all H edge colors while retaining the ordered exterior skeleton. All R colors stay w, since K has no arcs into R. For each i in L, the only possible out-neighbor lies in K and is traversed once. Apply the single-edge repair lemma to set its profile bit, preserving all previous profile bits. Every (w,t_K) therefore occurs. Conversely every full c-geodesic projects to a full c_R geodesic with unchanged R colors.

Metric identity: The projection lower bound gives ell(c)>=ell(c_R)+|K|. Start from a shortest monochromatic R antipodal path, append the L steps once, prescribe color zero on H by the B_k bridge (allowing repeated R directions), then set each L step to zero using the same individual repair. R-edge colors are unchanged. This yields a monochromatic antipodal walk of length ell(c_R)+|K|, and loop-erasure proves equality.

Corollary: Every sink strongly connected component in a minimum-dimensional NORI1 counterexample must have at least eight directions with at least two outgoing influence neighbors. Otherwise this theorem deletes it and yields a smaller counterexample. A directed cycle of any length is therefore an eliminable sink component.
