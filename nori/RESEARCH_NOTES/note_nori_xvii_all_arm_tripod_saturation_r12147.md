# Saturated and balanced equality plateaus

- Stable ID: note_nori_xvii_all_arm_tripod_saturation_r12147
- Author: session_nori_r12147_4
- Primary home: subsection:central_freudenthal_subdivision_and_the_all_root_geodesic_chamber_sphere
- Labels: NORI1, balanced, selector, method-obstruction
- Lifecycle: active
- Epistemic status: proved
- Current version: 3
- Retention: current and at most one previous snapshot
- Created session: session_nori_r12147_4
- Updated session: session_nori_r12147_4
- Disposition: none
- Successor: none

## Related references

- None

## Research note

For each integer k>=2, partition [3k] into three k-element blocks A0,A1,A2. Set m=0, p_i=1_(A_i). On the doubled full geodesic use the six successive blocks: A1 blue, A0 red, A2 blue, A1 red, A0 blue, A2 red, with the same internal order at antipodal block occurrences. It is a consistent antipodally odd 6-run cycle; its half-path P has twisted defect 3, and its red-to-blue seams are p0,p1,p2. On each median-arm face F_i (other block bits zero), prescribe color 0 for edges leaving rank 0, color 1 for edges leaving positive rank. Hence EVERY arm H_i:m->p_i, in any order, has word 0 1^(k-1), internal switch count 1, initial color 0, final color 1. The doubled P cycle uses block-direction edges with the other two blocks fixed to (0,1) or (1,0), whereas F_i and its antipode use (0,0) or (1,1). These edge orbits are disjoint, so the prescriptions extend arbitrarily to a legal odd coloring. Each short backward seam connector C_i:p_i->bar(p_(i+1)) is a red k-edge block. Consequently EVERY median three-route recombination R_i=H_i*C_i*reverse(bar(H_(i+1))) has word 0 1^(k-1) 0^k 0^(k-1) 1 and twisted defect 3. Its blue selector difference support B_i=D(m,q(R_i)) has size k, and B0,B1,B2 partition [3k]. All (k!)^3 arm triples saturate S+Delta/2=3 and retain nonempty selector parts. For even k the family lies in even cube dimension. This refutes any descent/selector-zero theorem based solely on the entire arm-order product at one arbitrary defect-three P; P need not be globally minimum, so unrestricted NORI1 remains unaffected. The relevant next input must couple other global minimizers and their overlapping seam triangles.

Paired-square transfer: if one arm H_j is changed across its original square in directions a,b based at u, put eta_a=c_a(u)+c_a(u^b) and eta_b=c_b(u^a)+c_b(u) (mod 2). Both reconstructed paths R_j and R_(j-1) change their selector by eta_a e_a+eta_b e_b; the third selector is unchanged. The two altered selector parts exchange these directions. This follows since one reconstruction uses the arm and the other uses its antipodal reversal; complementing both old/new edge colors preserves each derivative. The transfer respects original shared-edge consistency and XOR selector conservation.

## A complete binary-word plateau at seam radius one

A secondary-minimal defect-three path can retain equality under all three recombinations, even when its entire cyclic color-word type is used as a potential. Partition seven directions into blocks \(A_0,A_1,A_2\) of sizes \(1,2,4\), put \(m=0\), and use the six-run doubled seam cycle from the preceding construction, starting at \(p_0=\mathbf1_{A_0}\). Its first half has word \(w(P)=1101111\). On the three median faces prescribe particular arms \(H_0,H_1,H_2\) with words \(1,00,0110\), respectively, in their chosen block direction orders.

The doubled-cycle edges and all three arm faces use disjoint antipodal edge orbits (their two exterior block values are respectively mixed and equal). Therefore these prescriptions extend to a legal antipodally odd coloring. All short backward seam connectors are red, and the three legal reconstructed full antipodal geodesics have words
\[
\boxed{w(R_0)=1000011,\quad w(R_1)=0001001,\quad w(R_2)=0110000.}
\]
Each has twisted defect three. Their antiperiodically doubled words are equivalent to the doubled word of \(P\) under cyclic rotation and reversal: all have the same three cyclic run lengths \(1,2,4\), up to dihedral permutation. In particular every run-length statistic and every invariant of the abstract unrooted binary color cycle takes the same value on \(P,R_0,R_1,R_2\). The seam-radius value is one for all four, already the smallest possible positive radius for defect-three paths. Their selector supports are nonempty: \(B_0=A_0\sqcup A_1\), while \(B_1,B_2\) split \(A_2\) into two 2-element parts. Also \(q(R_0)=\bar p_2\) lies on \(P\), while \(q(P)=\bar m\) is an endpoint of \(R_0\), yielding mutual cross-path selector incidence without self-incidence.

**Scope.** This is a dimension-seven legal local realization. It need not be globally defect-minimal and may admit defect-one paths elsewhere. Consequently it rules out a descent proof from the four abstract color-cycle words or their refined run profiles alone. To exploit global minimum defect, the argument must use further paths in the same coloring, original direction placement, transverse square derivatives, or another shared-edge-consistent transfer. This addresses the live equality plateau and avoids further scalar-word potential refinements without a new structural ingredient.

## Balanced eight-cube equality realization

All binary arithmetic is modulo two. Pair directions (0,3),(1,5),(2,6),(4,7), with c_a=f_ab and c_b=1+f_ab:
f03=1+x2; f15=x0; f26=x3+x7+x0*x1+x0*x3+x1*x3; f47=x0+x2+x6.
Each f_ab ignores its paired bits and is odd under global complementation. Hence each edge coloring is well-defined and antipodally odd, and each vertex has four incident edges of each color.

Choose m=0, blocks A0=(0), A1=(1,2), A2=(3,4,5,6,7), in these internal orders. The doubled cycle A1 blue, A0 red, A2 blue, A1 red, A0 blue, A2 red has first-half word w(P)=11011111 and twisted defect three. The three canonical arms from m have words 1,00,00100. The three direction-simple antipodal recombinations have words
w(R0)=10000011, w(R1)=00011011, w(R2)=00100000.
All four twisted defects equal three; their doubled binary words lie in one dihedral orbit, with complete seam-length multiset (1,2,5). Therefore vertex balance and all single-tripod selector equalities coexist with total color-cycle-word saturation, so any potential depending solely on the unrooted color words cannot strictly descend.

The coloring has a red full antipodal geodesic rooted at zero with direction order (3,6,1,2,4,0,5,7), verified by substitution. This obstructs only local or balance-only strengthening, preserving the unrestricted NORI1 target requiring absence of all monochromatic geodesics.
