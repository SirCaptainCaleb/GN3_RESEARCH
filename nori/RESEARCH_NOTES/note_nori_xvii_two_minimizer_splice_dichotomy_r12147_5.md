# Global-minimizer cross-splicing and coherent seam phases

- Stable ID: note_nori_xvii_two_minimizer_splice_dichotomy_r12147_5
- Author: session_nori_r12147_5
- Primary home: subsection:central_freudenthal_subdivision_and_the_all_root_geodesic_chamber_sphere
- Labels: NORI1, global-minimizer, path-exchange, topology, shared-edge-consistency
- Lifecycle: active
- Epistemic status: proved
- Current version: 8
- Retention: current and at most one previous snapshot
- Created session: session_nori_r12147_5
- Updated session: session_nori_r12147_5
- Disposition: none
- Successor: none

## Related references

- subsection:central_freudenthal_subdivision_and_the_all_root_geodesic_chamber_sphere
- note:note_nori_xvii_median_three_route_telescoping_r12024_2

## Research note

Let \(c\) be an arbitrary antipodally odd binary edge coloring of \(Q_n\), \(n\ge2\). For a rooted full geodesic with edge colors \(w_1,\ldots,w_n\), put
\[
D=\sum_{j=1}^{n-1}[w_j\ne w_{j+1}]+[w_n=w_1],\qquad d=\min_{x,\pi}D(P(x,\pi)).
\]
Each \(D\) is odd, and \(D=1\) is equivalent, after a root slide, to a monochromatic full geodesic.

**Theorem (two-minimizer four-port identity).** Let \(P,Q:x\to\bar x\) be globally minimizing full antipodal geodesics rooted at the same original vertex \(x\). Suppose both visit an internal vertex \(v\). Denote the first/last colors of \(P,Q\) by \((a,u),(b,z)\), and their respective incoming/outgoing colors at \(v\) by \((p,q),(r,s)\). Exchange suffixes at \(v\), obtaining \(P\#Q,Q\#P\). Both are full direction-simple geodesics, and
\[
\begin{split}
D(P\#Q)+D(Q\#P)-2d
&=\big([p\ne s]+[r\ne q]-[p\ne q]-[r\ne s]\big)\\
&\quad+\big([z=a]+[u=b]-[u=a]-[z=b]\big).
\end{split}\tag{1}
\]
The first parenthesis equals \(-2\) precisely for opposite switch orientations \((p,q)=(0,1),(r,s)=(1,0)\), in either order; it equals \(+2\) precisely for opposite constant phases \((0,0),(1,1)\); otherwise it is zero. The second parenthesis equals \(-2\) precisely when \(a\ne b,u=a,z=b\); it equals \(+2\) precisely when \(a\ne b,u=b,z=a\); otherwise it vanishes.

**Consequences.**
1. If the first colors agree (\(a=b\)) **or the last colors agree** (\(u=z\)), then the closing correction vanishes. Opposite interior switch orientations are impossible. If in addition the incoming colors agree (\(p=r\)) or the outgoing colors agree (\(q=s\)), **both** recombinations retain defect \(d\). Neither conclusion is asserted without the endpoint hypothesis.
2. If \(P,Q\) have opposite first colors and each has matching first and last colors, then at every common internal vertex each path must be locally constant, with opposite colors. Both recombinations have defect \(d\).
3. If \(P,Q\) make opposite switches at \(v\), then necessarily their initial and terminal pairs are \((a,u)=(0,1),(b,z)=(1,0)\), up to exchanging \(P,Q\). Both recombinations are globally minimizing.
4. If the paths have matching first colors, and their local phases at \(v\) are constant but opposite, the two recombinations have defects \(d\) and \(d+2\) in some order.

*Proof.* Since \(P,Q\) start at the same \(x\), their common internal vertex \(v\) determines the common prefix direction support \(S=\{i:x_i\ne v_i\}\). Each prefix uses precisely \(S\), each suffix precisely \([n]\setminus S\), so both splices use every original dimension once. Their edges retain the prescribed original colors. Ordinary color changes away from the splice point are merely redistributed. The new junction terms give the first parenthesis of (1), and the twisted closing terms give the second. Direct inspection of the two binary port pairs yields the stated classification. Global minimality forces the right side of (1) to be nonnegative, with equality implying both splices again attain \(d\). Consequences 1–3 follow from the possible pairs of values \(-2,0,+2\). For consequence 4, the sum of defects is \(2d+2\), and each defect is odd and at least \(d\), so they equal \(d,d+2\). \(\square\)

**Topological interface and gap.** Every rooted permutohedral family of geodesics through one original vertex \(v\) has common prefix support and admits these cross-splices, while global minimizers satisfy the four-port constraints. In particular the binary turn relation at any fixed \((x,v)\) is constrained by the endpoint phases, and same-first-color or same-last-color fibers obey a coherent local seam restriction. Opposite interior seams can survive only with the exceptional opposite endpoint phases of consequence 3; then the splice produces further global minimizers. These constraints use global optimality on the same coloring, arbitrary nonlinear dependence, shared-edge consistency, and original direction simplicity. They do not prohibit defect three on one arbitrarily selected path. A forcing argument must combine them with the topological incidence among different minimizing paths, producing a forbidden four-port configuration or an independent descent. Root changes cannot be treated as free suffix splices: paths with different roots generally have different prefix direction supports at the same vertex.


## Multiway minimum-path transport and its projective two-intersection form (session session_nori_r12147_5)

Let \(d\) be the global minimum twisted defect. Let \(P_1,\ldots,P_k:x\to\bar x\) be full geodesics attaining \(d\) and meeting at an internal vertex \(v\). Write \((a_i,u_i)\) for the first/last colors of \(P_i\), and \((p_i,q_i)\) for the incoming/outgoing colors at \(v\).

**Theorem (simultaneous suffix exchange).** For every permutation \(\sigma\in S_k\), combining the prefix of \(P_i\) ending at \(v\) with the suffix of \(P_{\sigma(i)}\) beginning there gives a full antipodal direction-simple geodesic \(R_i^\sigma\), and
\[
\sum_iD(R_i^\sigma)-kd=
\sum_i\{[p_i\ne q_{\sigma(i)}]+[u_{\sigma(i)}=a_i]-[p_i\ne q_i]-[u_i=a_i]\}\ge0.
\tag{MW1}
\]
Writing \(L_i=(p_i,a_i)\), \(T_i=(q_i,1-u_i)\) in \(\{0,1\}^2\subset\mathbb R^2\), this is equivalent to
\[
\boxed{\sum_i L_i\cdot T_i\ge\sum_iL_i\cdot T_{\sigma(i)}\quad(\forall\sigma\in S_k).}
\tag{MW2}
\]
Thus the port pairing of the global minimizers is cyclically monotone.

*Proof.* Their common root and meeting vertex determine the same prefix direction support \(S=\{j:x_j\ne v_j\}\) and complementary suffix support for every path. All the recombinations use each original direction once and inherit their edge colors. Let \(A_i,B_i\) count ordinary switches strictly inside the prefix and suffix, respectively. Then
\(D(R_i^\sigma)=A_i+B_{\sigma(i)}+[p_i\ne q_{\sigma(i)}]+[u_{\sigma(i)}=a_i]\).
Sum and use \(D(R_i^\sigma)\ge d\). The identity
\[
[p\ne q]+[u=a]=1+(p+a)+(q-u)-2\big(pq+a(1-u)\big)
\]
shows that row- and column-dependent terms cancel in every permutation sum, giving (MW2). \(\square\)

**Strict three-way condition invisible to pairwise total inequalities.** Consider hypothetical signatures
\[
(a_i,u_i,p_i,q_i)=(0,0,0,0),(0,1,1,0),(1,0,0,1).
\tag{MW3}
\]
Their port exchange cost matrix \(C_{ij}=[p_i\ne q_j]+[u_j=a_i]\) equals
\(\begin{psmallmatrix}1&0&2\\2&1&1\\0&1&1\end{psmallmatrix}\).
Every two-path suffix transposition changes the combined port cost by zero. The cyclic reassignment \(1\mapsto2\mapsto3\mapsto1\) changes it from \(1+1+1=3\) to \(0+1+0=1\), contradicting (MW1). These signatures therefore cannot coexist in a family of global minimizers through \((x,v)\); no claim is made that they are simultaneously realized by a legal coloring. This is a ternary obstruction missed by pairwise total-cost testing.

If all first colors agree, or all last colors agree, the closing contribution is invariant under every suffix permutation. The remaining matching problem is one-dimensional: pairwise monotonicity \((p_i-p_j)(q_i-q_j)\ge0\) implies all permutation inequalities by rearrangement. The ternary obstruction consequently requires simultaneous variation of the first and last color phases.

**Two shared projective vertices suffice for the common-root hypothesis.** Let \(n\ge3\) and \(H=\mathbb F_2^n/\langle\mathbf1\rangle\). Any two essential projective rainbow \(n\)-cycles containing distinct vertices \([x],[y]\) have, between those vertices, two complementary arc direction supports \(S\) and \([n]\setminus S\): the sole dependence of the folded-cube generators is their full sum. Choose the same support \(S\) on each cycle, orient both from \([x]\) through the \(S\)-arc, and lift them from the same original vertex \(x\). They then both pass through \(v=x\oplus\mathbf1_S\) and end at \(\bar x\). This allows the two-path exchange and all its port restrictions to be applied to initially unrooted projective cycles. The same alignment applies to any family of cycles sharing the same two projective vertices. Root slides and traversal reversal preserve twisted defect.

**Unresolved topological forcing.** The all-root Freudenthal and marked-gallery complexes supply compatible paths through prescribed original vertices, making (MW2) an integral constraint with a topological incidence interpretation. Their existing projective index does not imply that paths through those vertices simultaneously attain the unrestricted global minimum, or that their port relation violates cyclic monotonicity. Producing this same-coloring minimum-path incidence is the missing step. The theorem applies to arbitrary nonlinear antipodally odd edge colorings and preserves shared-edge consistency.



## Projective crossing-sign law and its topological limitation (session session_nori_r12147_5)

Let \(P,Q:x\to\bar x\) minimize the global twisted defect \(d\). At an internal vertex \(v\) shared by both paths, denote their incoming/outgoing original-edge colors by \(I_P,O_P,I_Q,O_Q\). At their common projective root \(x\), put \(I_P(x)=1-u_P,\ O_P(x)=a_P\), where \(a_P,u_P\) are the first and last colors of \(P\), and analogously for \(Q\). Define
\[
\kappa(v)=(I_P(v)-I_Q(v))(O_P(v)-O_Q(v))\in\{-1,0,1\}.
\tag{XS1}
\]
**Two-site exchange theorem.** If \(v,w\) are different common projective vertices and both paths meet the same original lifts, then
\[
\boxed{\kappa(v)+\kappa(w)\ge0.}\tag{XS2}
\]
At most one common projective vertex has \(\kappa=-1\); if one does, all other common projective vertices have \(\kappa=+1\). If \(\kappa(v)=-1,\kappa(w)=+1\), exchanging the segments between \(v,w\) gives two more global minimizers and reverses the signs at those endpoints while preserving the signs at the other common vertices.

*Proof.* Common vertices have increasing Hamming ranks in the same order along both paths. The segments between any two common vertices traverse the same set of original directions; segment swapping retains every direction once and every edge's prescribed color. All combined changes away from the splice boundaries cancel. At each interior boundary, the junction change equals
\[
[I_P\ne O_Q]+[I_Q\ne O_P]-[I_P\ne O_P]-[I_Q\ne O_Q]=2\kappa.
\]
The twisted closing seam gives the same formula at the projective root, using incoming colors \(1-u\). Global minimality proves (XS2). If signs sum to zero, each resulting defect equals \(d\), since their sum is \(2d\) and neither is smaller than \(d\). Swapping an interval exchanges one of the two in/out factors at either endpoint and both factors elsewhere in the exchanged interval; hence the sign migration. \(\square\)

**Reversal and port monotonicity.** The cyclic-monotonicity ports are \(L=(p,a)\), \(T=(q,1-u)\). Antipodal translation maps them to \((\mathbf1-L,\mathbf1-T)\). The projective reversal \(\widetilde P=\overline{\operatorname{rev}P}\), now meeting \(\bar v\), acts by
\[
(L,T)\longmapsto(J(T),J(L)),\qquad J(s,t)=(1-s,t).
\tag{XS3}
\]
Both operations preserve (MW2): reflecting both factors by \(J\) alters total inner products only by summands independent of the matching permutation, and swapping left/right transposes that permutation. The abstract diagonal relation \(L=T\) respects both operations. Hence projective reversal symmetry is algebraically compatible with cyclic monotonicity and does not independently force an exchange violation. No realization claim about this abstract port relation is made.

**Three-route median-arm overlap.** If \(R_j=H_j*C_j*\operatorname{rev}(\bar H_{j+1})\), then \(\overline{\operatorname{rev}R_{j-1}}\) begins with \(H_j\), as does \(R_j\). They share this initial arm and therefore have \(\kappa=0\) at its root, interior vertices, and endpoint. The canonical shared-arm incidence alone supplies no negative crossing; strict descent needs further transverse overlapping minimizers with conflicting port colors. Essential projective one-cycles have no homologically compelled mutual intersections in projective dimension at least three. The missing argument must use more of the original antipodally odd shared-edge coloring.



## Near-minimizer budget and the one-square degeneracy (session session_nori_r12147_5)

Retain the projective crossing signs (XS1). Let \(P\) be globally minimizing with \(D(P)=d\), and let \(Q\) be another full geodesic with the same root, \(D(Q)=d+2k\), \(k\ge0\). For any two shared projective vertices \(v,w\) with common original lifts, the segment exchange gives
\[
\boxed{\kappa_{P,Q}(v)+\kappa_{P,Q}(w)\ge-k.}\tag{NM1}
\]
When equality holds, both recombined paths attain \(d\), because their combined defect is \(2d\). In particular, a defect-\((d+2)\) path cannot exhibit \(\kappa=-1\) at two shared vertices alongside a global minimizer; if it has signs \(-1,0\), their interval exchange produces two new global minimizers.

*Proof.* The combined defect of the two interval-exchanged paths is \(2d+2k+2\kappa(v)+2\kappa(w)\), while each resulting path has defect at least \(d\). This proves (NM1) and the equality assertion. \(\square\)

**Single-square variation bound.** Swapping two consecutive original directions of a full geodesic changes only the two corresponding original edges. The binary twisted color word consequently changes at two adjacent positions, affecting no more than three cyclic junction indicators. Since every twisted defect is odd, its change belongs to \(\{-2,0,2\}\). Thus each single-square neighbor \(Q\) of a global minimizer \(P\) has \(D(Q)\in\{d,d+2\}\).

However, such a pair has \(\kappa_{P,Q}(v)=0\) at EVERY shared projective vertex: the paths have all original vertices in common except their different rank-\(h\) intermediate vertices in the exchanged square. At the shared square endpoints, only the outgoing edge or only the incoming edge changes, and elsewhere both incident edges agree; the same observation holds at the projective closing junction for a square at either end. Therefore the near-minimizer theorem yields no crossing-sign descent from a single adjacent-order swap. Nonzero crossing signs require changing both incoming and outgoing port colors at a shared vertex, involving exchanges on both sides or a global root/median recombination. This identifies the further incidence needed when combining (NM1) with the all-root Freudenthal topology.



## Defect-three median recombinants give a projective tetrahedral graph (session session_nori_r12147_5)

Let \(P\) be any direction-simple antipodal full path with twisted defect three, and let \(E_0,E_1,E_2\) be its three nonempty red-run direction blocks. Let \(m\) be the canonical seam majority and \(p_j\) its red-to-blue seam vertices, with \(A_j=D(m,p_j)=E_{j+1}\) (indices modulo three). Choose arbitrary direction-simple arms \(H_j:m\to p_j\). Let \(K_j:p_j\to\bar p_{j+1}\) be the red \(E_j\)-run connector. Define the full original-cube geodesics
\[
\Gamma_j=H_j*K_j*\operatorname{rev}(\bar H_{j+1})\quad(j\in\mathbb Z/3).
\tag{TG1}
\]

**Theorem (tetrahedral incidence with neutral overlaps).** (i) Two different \(\Gamma_j\) share only their original endpoints \(m,\bar m\), regardless of arm order and arm colors. (ii) In the folded cube \(Q_n/(v\sim\bar v)\), the union of their three images is a subdivided \(K_4\) with branch vertices \([m],[p_0],[p_1],[p_2]\). Its six branches are the three median arms \(H_j\) and three seam connectors \(K_j\), whose interiors are pairwise disjoint in this quotient. Each \([\Gamma_j]\) is a triangular circuit consisting of two spokes and one seam connector. (iii) After orienting and lifting any two of these projective circuits from \(m\), they share one initial or terminal median arm and no other internal vertices. At every shared projective vertex their two-path crossing sign \(\kappa\) of (XS1) is zero. Thus even if all three routes attain global minimum defect, their mutual incidences alone cannot violate the two-site crossing inequality or generate the multiway port exchange obstruction.

*Proof.* The direction-block orders of \(\Gamma_0,\Gamma_1,\Gamma_2\) are
\((E_1,E_0,E_2),(E_2,E_1,E_0),(E_0,E_2,E_1)\), respectively. For two different cyclically shifted orders, a nonempty proper prefix support of one cannot equal a prefix support of the other: the second ordering must finish another nonempty block before acquiring all blocks of that prefix. The argument also includes prefixes strictly inside individual blocks. Thus the original routes share only endpoints.

In the projective quotient the last piece \(\operatorname{rev}(\bar H_{j+1})\) becomes the same path as spoke \(H_{j+1}\), with opposite traversal, while \(K_j\) joins \([p_j]\) to \([p_{j+1}]\). Supports of points on \(H_j\) are subsets of \(A_j\). Supports of points on \(K_j\) have form \(A_j\cup T\), \(T\subseteq E_j\). The three blocks \(E_j\) partition all directions and are nonempty. Comparing these supports and their complements shows that distinct spokes and connectors have no interior vertices in common in the folded quotient; their only intersections are the stated endpoints. This establishes the subdivided \(K_4\). Any two of its triangular routes share one spoke. Aligning the corresponding rooted paths by projective reversal turns this into a common prefix or common suffix, where either both incoming edge colors or both outgoing colors agree at every common vertex. Hence \(\kappa=0\). \(\square\)

**Holonomy does not force a crossing sign.** Gauge the double cover by lifting all spokes from \(m\). Each spoke has monodromy zero, whereas each seam link \(K_j:p_j\to\bar p_{j+1}\) has monodromy one. Each triangular circuit \([\Gamma_j]\), and also the outer seam triangle, evaluates to one under the projective covering cocycle. Nontrivial projective holonomy thus coexists with vanishing crossing signs on all pairwise overlaps of the canonical tripod. Applying the variational exchange theorem in a proof of NORI1 requires further original-edge information involving other globally minimizing paths, transverse square transport, or root-facet incidence. The chosen \(P\) and the three recombinants are not assumed globally minimizing.
