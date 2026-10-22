# Median three-route telescoping and color-sensitive defect descent

- Stable ID: note_nori_xvii_median_three_route_telescoping_r12024_2
- Author: unspecified; session provenance retained
- Primary home: subsection:central_freudenthal_subdivision_and_the_all_root_geodesic_chamber_sphere
- Labels: NORI1, topology, median, switch-defect, geodesic
- Lifecycle: active
- Epistemic status: proved
- Current version: 8
- Retention: current and at most one previous snapshot
- Created session: session_nori_r12024_2
- Updated session: session_nori_r12147_2
- Disposition: none
- Successor: none

## Related references

- note:note_nori_twisted_minimizer_prefix_barrier_rank_slices_20261020_r12020
- article:nori_article_xiv_type_a_rook_gallery_topology

## Research note

# Median three-route telescoping for arbitrary antipodally odd edge colorings

Let P be a full antipodal cube geodesic of odd twisted defect d>=3, with D(P)=sum_{j<n}[w_j!=w_{j+1}]+[w_n=w_1]. Extend P antipodally to its closed alternating 2d-run cycle. Choose three run-boundary vertices p_0,p_1,p_2 in circular order, with run gaps g_i in {1,...,d-1}, summing to 2d. Their cubical hull is Q_n. Their coordinatewise median m has disjoint nonempty support sets D(m,p_i) partitioning [n].

Choose ANY geodesic Q_i from m to p_i. Let s_i be its ordinary color-change count, alpha_i its first edge color, beta_i its final edge color. Let C_i be the backward short arc from p_i to bar(p_(i+1)) on the doubled P cycle. It has h_i=d-g_i>0 monochromatic runs, uses the third support D(m,p_(i+2)), and has first/last colors f_i,l_i. Since the run colors alternate, d is odd, and C_i ends at the antipode of p_(i+1), we have l_i=f_(i+1). Also sum h_i=d.

Concatenate Q_i, C_i, and the antipodal reversal of Q_(i+1), obtaining a direction-simple full antipodal geodesic R_i rooted at m. Put X_i=[beta_i!=f_i], Z_i=[alpha_i!=alpha_(i+1)]. Counting its two joins and twisted seam yields the integer identity
D(R_i)=h_i+s_i+s_(i+1)+X_i-X_(i+1)+Z_i.

Summing cyclically cancels the endpoint potentials:
sum_i D(R_i)=d+2(s_0+s_1+s_2)+Delta,
Delta=Z_0+Z_1+Z_2 in {0,2}.

UNRESTRICTED DESCENT RULE. If S=s_0+s_1+s_2 and S+Delta/2<d, then some R_i satisfies D(R_i)<D(P), and the decrease is at least two because all twisted defects are odd. In particular, S<=d-2 always suffices; S=d-1 also suffices if all alpha_i agree.

MINIMUM-PATH OBSTRUCTION. If d is globally minimum, every spanning triangle among its run-boundary vertices and every choice of median geodesic arms has S+Delta/2>=d. Consequently the three minimum switch-distance arms satisfy S>=d-1. If S=d-1, their initial colors must be nonconstant and all three reconstructed R_i also achieve defect d, producing three simultaneous global minimizers rooted at m.

This two-switch improvement over the elementary geodesic triangle inequalities comes from the antipodal seam and the cyclic telescoping X_i-X_(i+1). It retains arbitrary nonlinear shared-edge color dependence. The still-open forcing task is to produce at least one spanning triangle whose intrinsic median-arm energy min_Q (S+Delta/2) is <d, possibly through the central Freudenthal/projective w_1^2 obstruction. No such universal existence theorem is established.

## Arbitrary-cut three-route conservation

Let P be a full antipodal geodesic with twisted defect d and double its color word to the antiperiodic cyclic 2n-word (w,1-w). Choose p_0,p_1,p_2 in cyclic order along this doubled path, with all three forward cyclic gaps strictly between 0 and n. Their coordinatewise median m has three nonempty disjoint direction supports S_i=D(m,p_i) partitioning [n]. For arbitrary geodesics Q_i:m to p_i let s_i count internal color changes, alpha_i their first colors, beta_i their final colors. Let C_i:p_i to tau(p_(i+1)) be the short backward arc of the doubled path, with first color f_i, last color g_i, and t_i internal changes. Then R_i = Q_i, C_i, (tau Q_(i+1)) reversed is a full direction-simple antipodal geodesic.

Define S=sum_i s_i, Delta=sum_i [alpha_i != alpha_(i+1)] in {0,2}, and q=# {i: p_i is strictly inside a monochromatic run of P's doubled color word and beta_i != f_i}. Then

sum_(i=0)^2 D(R_i) = d + 2S + Delta + 2q.  (AC1)

Proof. The first/last colors of the third segment of R_i are 1-beta_(i+1),1-alpha_(i+1). Counting internal changes, two junctions, and its twisted seam gives
D(R_i)=s_i+t_i+s_(i+1)+[beta_i!=f_i]+[g_i=beta_(i+1)]+[alpha_i!=alpha_(i+1)].
The three C_i arcs and their antipodal images partition the doubled cycle, with endpoints at p_i and tau p_i. A seam pair is omitted from the internal C_i seams precisely when one p_i is a seam boundary. If r of the three p_i are such boundaries, sum_i t_i=d-r. At each p_i, f_i is the color of the preceding forward edge, while g_(i-1) is the complement of the following forward edge. At a seam boundary f_i=g_(i-1), and
[beta_i!=f_i]+[g_(i-1)=beta_i]=1.
At a cut strictly inside a color run, f_i!=g_(i-1), and the same sum equals 2[beta_i!=f_i]. Therefore all junction contributions total r+2q, proving AC1.

If P minimizes d=D(P) over all roots and full direction orders, then each D(R_i)>=d and hence
S+Delta/2+q >= d.  (AC2)
A triple violating this inequality supplies a full antipodal geodesic with strictly smaller odd twisted defect. This extends the seam-boundary median three-route formula already recorded in this note to cut vertices anywhere on the doubled path, preserving arbitrary nonlinear original-edge color dependence. For fixed P and p_i, the minimum of the left side of AC2 over the three geodesic arms Q_i defines a phase-resolved median energy. Showing that one minimizing P admits a triangle of energy below d remains open.


## Synchronized-seam descent and median sweep

Let P be a full antipodal geodesic of twisted defect d, continued antipodally to a 2n-cycle. Choose two color-change boundary vertices p,q on the doubled cycle, separated by a forward arc of length k in {2,...,n-1}, with direction order pi=(i_1,...,i_k), support S, and color word a_1,...,a_k. Put T=[n]\S. Let M be the geodesic from q to p traversing pi in the same order, with color word b_1,...,b_k. Let m_j be its vertex after j steps, and u_j=m_j xor T. For 1<=j<k, the vertex u_j is the j-th vertex of the antipodal image of the forward arc from p to q, and m_j=med(p,q,u_j) (bitwise majority). Its three median-arm supports to p,q,u_j are {i_(j+1),...,i_k}, {i_1,...,i_j}, and T, respectively, disjoint and covering [n].

**Synchronized-seam descent.** If there exists j with a_j!=a_(j+1) and b_j!=b_(j+1), and a monochromatic geodesic H:m_j to u_j exists with sigma(M)<d, then a full antipodal geodesic with twisted defect smaller than d exists.

Proof. Apply the arbitrary-cut three-route identity AC1 to the triple (u_j,p,q), with median m_j. Choose median arms H, the terminal piece of M from m_j to p, and the reversed initial piece of M from m_j to q. Their internal switch count totals sigma(M)-1, because the split occurs at a switch of M. The first colors of the two M arms differ, hence Delta=2. The three selected vertices are seam boundaries of the doubled P, so the interior-cut penalty vanishes. The identity gives sum_r D(R_r)=d+2(sigma(M)-1)+2=d+2sigma(M). If sigma(M)<d, one of these three direction-simple antipodal geodesics has defect below d. QED.

**Globally minimal consequence.** If P globally minimizes d and sigma(M)<d, then every synchronized switch j forces the T-face from m_j to u_j to have no monochromatic spanning path of either color. When |T|=1 the T-path consists of a single original edge, so the switch sets of a and b must be disjoint. When |T|=2, both two-edge routes across the T-square are mixed, forcing vanishing square curvature there.

The median points m_0,...,m_k traverse M. As j increases by one, direction i_(j+1) moves from the median arm toward p into the median arm toward q; the third arm retains direction set T. This provides a coherent family of median inequalities over a direction-simple path and retains original shared-edge data. The unresolved step is to force a synchronized switch with a monochromatic T-arm and sigma(M)<d for some globally minimum-defect P.


## Canonical seam-circle incidence and odd-cycle defect conservation (session session_nori_r12118_3)

Let \(P\) be an arbitrary full antipodal geodesic of a legal antipodally odd binary cube-edge coloring, with twisted defect \(d=2r+1\ge3\). Double its edge word by antipodal translation, and enumerate its red-to-blue seam vertices \(z_j\), \(j\in\mathbb Z/d\), in cyclic order. Let \(m\) be their unique majority vertex, as in the proved first-Walsh seam identity of the central Freudenthal subsection. Put \(A_j=D(m,z_j)\subseteq[n]\), the support of their bit difference.

**Theorem 1 (cyclic median supports).** For each original dimension \(i\), the set \(\{j:i\in A_j\}\) is a cyclic interval comprising \(r\) consecutive seam indices. Consequently
\[
\sum_j |A_j|=rn,\qquad A_j\cap A_{j+r}=\varnothing,\qquad m\in I(z_j,z_{j+r}).
\tag{CS1}
\]
The forward original path arc from \(z_j\) to \(z_{j+r}\) consists of \(d-1=2r\) monochromatic runs, starting blue and ending red, and uses the directions \(A_j\sqcup A_{j+r}\). Its continuation from \(z_{j+r}\) to \(\bar z_j\) is one monochromatic blue run using the remaining directions.

*Proof.* Along the doubled path the bit in each dimension flips on precisely two antipodal edges, separated by half the circuit. Its value among cyclically ordered \(z_j\) therefore differs from the majority on a contiguous cyclic interval. The first-Walsh identity says each dimension has precisely \(r\) minority seams, proving the interval assertion. Such an interval cannot contain both \(j\) and \(j+r\) in a circle of \(2r+1\) positions. This gives disjointness, the interval median claim, and the incidence sum. Consecutive red-to-blue seams are separated by two monochromatic runs; after \(r\) such intervals there are \(2r=d-1\) runs, leaving one final blue run before the antipode \(\bar z_j\). Each directed arc is part of a doubled full geodesic and hence traverses each original direction at most once. Its used directions are \(D(z_j,z_{j+r})=A_j\sqcup A_{j+r}\). \(\square\)

For \(d\ge3\), each \(A_j\) is nonempty: if \(m=z_j\), its projective class would lie on the projective cycle, which by the established canonical-selector criterion forces defect one.

Choose arbitrary direction-simple geodesics \(H_j:m\to z_j\) simultaneously. Write \(s_j\) for each arm's internal color changes and \(\alpha_j,\beta_j\) for its first and last colors. Define
\[
R_j=\operatorname{rev}(H_j)*H_{j+r}*
P[z_{j+r},\bar z_j].
\tag{CS2}
\]
The final piece is the doubled \(P\)'s surviving blue run. By (CS1), \(R_j\) traverses all original directions once and ends at the antipode of its initial vertex.

**Theorem 2 (odd-cycle \(d\)-route telescoping).** For every joint choice of the \(H_j\),
\[
D(R_j)=s_j+s_{j+r}+[\alpha_j\ne\alpha_{j+r}]
+[\beta_{j+r}\ne1]+[\beta_j=1],
\tag{CS3}
\]
and therefore
\[
\boxed{\sum_jD(R_j)=d+2\sum_j s_j+
\sum_j[\alpha_j\ne\alpha_{j+r}].}
\tag{CS4}
\]
If \(P\) globally minimizes defect \(d\), then
\[
\boxed{\sum_j s_j+\frac12\sum_j[\alpha_j\ne\alpha_{j+r}]
\ge dr=\frac{d(d-1)}2.}
\tag{CS5}
\]
Because \(\gcd(r,d)=1\), the \(j\leftrightarrow j+r\) incidence forms one odd cycle. Thus its number of \(\alpha\)-disagreements is even and at most \(d-1\), forcing \(\sum_j s_j\ge(d-1)^2/2\). Any arms violating (CS5) construct a strictly lower-defect full antipodal geodesic.

*Proof.* The reversed \(H_j\) starts with \(\beta_j\), ends with \(\alpha_j\), and has \(s_j\) internal changes. The next arm starts with \(\alpha_{j+r}\), ends with \(\beta_{j+r}\), and has \(s_{j+r}\) changes. The final blue run contributes the last internal junction, while the twisted closing seam tests equality of blue and \(\beta_j\). Counting gives (CS3). Summation counts every \(s_j\) twice and uses
\(\sum_j([\beta_{j+r}\ne1]+[\beta_j=1])=d\).
Minimality gives \(D(R_j)\ge d\) for all \(j\), proving (CS5). Binary disagreements around the single odd cycle are even and bounded by \(d-1\). \(\square\)

For \(d=3\), the \(A_j\) partition \([n]\) and (CS4) recovers the existing three-route telescoping identity on the canonical red-to-blue seam triangle. For all odd \(d\), the result preserves shared original-edge colors, unrestricted nonlinear dependence, and direction simplicity, while coupling **all** canonical median arms through one odd-cycle exchange family.

**Forcing gap.** Prove that a hypothetical globally minimizing bad path admits a joint family of arms violating (CS5), or combine these necessary inequalities across other minimizing paths in the same coloring. Neither conclusion follows from the cyclic interval incidence alone. The elementary bound \(s_j\le|A_j|-1\) recovers only the previously established dimension restriction \(n\ge d+2\). The new operation is the simultaneous legal \(d\)-route recombination, with canonical cross-root incidence and telescoping endpoint terms.


## Weighted crossing-edge carrier and canonical seam equator (session session_nori_r12118_3)

Fix a cube root m and positive weights a_i whose total A has no subset sum A/2. Realize the outer cube as B=[0,2]^n and set h(y)=sum_i a_i(2m_i-1)(y_i-1), K=B intersect {h=0}, E=boundary(K). Then K is an (n-1)-dimensional centrally symmetric convex polytope, E is an antipodal (n-2)-sphere, and each vertex of K lies on one original cube edge with endpoints of opposing h-sign.

THEOREM (variable-position edge carrier). Every direction-simple full path from m to bar(m) crosses E within a unique original edge, e(pi). Reversing the direction order selects the antipodal edge. Adjacent transposition of two directions either preserves the crossing edge or changes it across their common original square, giving adjacent vertices in K. Conversely every vertex and edge of K can be realized by these rooted geodesics and their square exchanges. The assignment pi -> e(pi) intersect E extends to an antipodal continuous map boundary(P_n) -> E of odd degree, where P_n is the rooted order permutohedron.

PROOF. At each root-directed step h decreases by 2a_i>0, from A to -A. Genericity avoids h=0 at original vertices. Each crossing edge e can be used after first traversing the directions flipped at its positive-height endpoint. Every K edge comes from intersecting h=0 with an original cube square; its two crossing original edges are realized by the two alternative direction orders within that square, with common preceding and subsequent directions. For the boundary extension, let F_S be a facet of P_n whose permutations place a nonempty proper S first. If a(S)<A/2, all selected crossing edges have S already flipped, and their intersection points belong to the proper K face fixing s_i=-1 for i in S. If a(S)>A/2, all crossings occur before finishing S and the selected points belong to the proper K face fixing s_i=+1 for i outside S. Each proper face of P_n is contained in a facet F_S. For every proper face F take the minimal face of K containing its selected crossing vertices; these carriers are proper and nested under inclusion. Map the barycenter of F to the arithmetic mean of these vertices and extend affinely along chains of proper faces in the barycentric subdivision. Each simplex maps into its largest proper carrier, so the image lies in E. Reversal sends every selected crossing edge to its antipode, so the extension is odd. Both boundaries are antipodal spheres of dimension n-2; the degree is therefore odd. QED.

Every selected vertex corresponds to an ORIGINAL edge and carries its one shared prescribed color. The threshold step depends on direction order, explaining why its carrier exists despite the known failure of a fixed intermediate-step rectified carrier.

THEOREM (seam-normalized intersection representation). Let P have twisted color defect d=2r+1, with blue-run direction blocks B_0,...,B_(d-1) in its doubled antiperiodic cycle and canonical red-to-blue seam majority m. Choose positive weights with sum_(i in B_j) a_i=1 for every j, generically within the blocks. Then the no-half-subset-sum condition can be imposed, total A=d, and h(z_j)=+1 at every red-to-blue seam outer vertex, while h(bar z_j)=-1 at every antipodal seam. Along the doubled P, h increases on red edges and decreases on blue edges. Each of its 2d monochromatic runs crosses E once, in an original cube edge. Hence the projective quotient of P intersects E/antipodality in d points, one from each antipodal pair of monochromatic runs.

PROOF. The proved seam-window majority formula states that each red-to-blue seam differs from m on r whole blue-run blocks. Each has weight one, so its h-height is d-2r=1. The signed direction profile relation m_i=1+x_i+c_i(e_i) implies red steps approach m and blue steps move away, also after antipodal continuation. Thus every red run raises h from -1 to +1, and every blue run lowers it from +1 to -1. Each traversed run block has total weight one, so its height changes by two. Genericity prevents crossing at cube vertices. Every union of whole blocks has integer weight, unequal to d/2; all other finitely many subset-sum equalities can be avoided by generic positive within-block weights. QED.

COROLLARY (defect-three separation). For d=3, the median-to-seam face at each red-to-blue seam fixes two of the three B-blocks at their m values and frees the third. Its h-height is at least 1, while its antipodal face has height at most -1. Thus E avoids the entire six-face median-arm cover U. The antipodal index of boundary(B) minus U is n-2: the complement contains E, and it lies in the doubly punctured boundary sphere, which admits an antipodal map to S^(n-2).

LIMITATION. This geometrizes the selected P's twisted defect as its number of intersections with a self-selected central hypersimplex and gives an odd-degree carrier with a witness on one shared original edge. Other geodesics can have color transitions differing from their h-height turns. Forcing compatible low-switch paths on the two sides of a crossing edge remains the needed color-sensitive transfer, particularly under the simultaneous minimum-defect inequalities.


## Independent programmability of transverse derivative words (session session_nori_r12147_2)

Fix the colors along the doubled cycle of an arbitrary direction-simple antipodal geodesic \(P\) of twisted defect \(d=2r+1\ge5\). Let \(E_0,\ldots,E_{d-1}\) be its nonempty disjoint red-run direction supports partitioning \([n]\), and \(R_j\) the red run on \(E_j\). For \(i\in E_j\), denote the unique direction-\(i\) edge of \(R_j\) by \(e_{j,i}\). For a direction-\(i\) edge \(e\) and \(T\subseteq[n]\setminus\{i\}\), let \(D_Tc(e)=c(e\oplus\mathbf1_T)+c(e)\) in \(\mathbb F_2\).

**Theorem (independent transverse samples).** Keeping all colors along the doubled \(P\)-cycle fixed, the \(2n\) bits
\[
\{D_{E_{j+r}}c(e_{j,i}),\ D_{E_{j-r}}c(e_{j,i}):j\in\mathbb Z_d,\ i\in E_j\}
\]
can be assigned arbitrarily and independently in a legal antipodally odd coloring of every remaining original edge. These are the \(2d\) transverse derivative words sampled by the canonical seam-triangle median-arm construction.

*Proof.* Two direction-\(i\) edges lie in the same antipodal orbit if and only if their exterior \(([n]\setminus\{i\})\)-bit vectors agree or are complementary. For fixed \(i\in E_j\), consider \(e_{j,i}\) and its translations by \(E_{j+r}\) and \(E_{j-r}\). Both translating blocks are nonempty, disjoint from \(E_j\), and distinct. Neither is all of \([n]\setminus\{i\}\), and their symmetric difference \(E_{j+r}\sqcup E_{j-r}\) also omits at least two nonempty blocks when \(d\ge5\). Consequently these three edges belong to three different antipodal orbits, with both translated orbits outside the doubled \(P\)-cycle. The supports \(E_j\) partition \([n]\), so different source pairs \((j,i)\) have different direction indices \(i\); their orbit assignments cannot collide. Since each source edge is red, assign the color on each translated orbit to equal the desired derivative bit, complement it on the antipodal mate, and assign remaining orbits arbitrarily. This independently realizes all \(2n\) bits. \(\square\)

**Defect-three exception.** For \(d=3\), the two translated samples of a direction \(i\in E_j\) remain independent if \(|E_j|\ge2\). If \(E_j=\{i\}\), the two translating blocks partition \([n]\setminus\{i\}\), so their translated edges are antipodal mates and the two derivative bits sum to \(1\) in \(\mathbb F_2\). Different directions still yield independent orbits.

**Implication.** A switch-variation restriction on these first-order derivative words cannot follow solely from the colors on the selected geodesic, the odd seam incidence, and consistency of the sampled translated edges. Such words admit arbitrary variation for \(d\ge5\). This does not rule out a contradiction using the additional inequalities from global defect minimality, the unsampled edges of complete square-exchange grids, or other geodesics of the same coloring. Those are the necessary sources of further forcing information.


## Terminal-phase rigidity of tight canonical median spokes (session session_nori_r12147_2)

Suppose P globally minimizes twisted defect d=2r+1>=3 in a legal original-cube coloring. Use the canonical red-to-blue seam vertices z_j (j modulo d), their common majority vertex m, and the recombinations R_j of (CS3). Set q_j=min_H sigma(H) over all direction-simple geodesics H:m->z_j, with unrestricted initial and final colors.

**Theorem (tight-edge matching).** For every j, q_j+q_(j+r)>=d-3. If equality holds for j, EVERY pair of minimum-switch arms H_j,H_(j+r) has terminal colors beta_j=1 and beta_(j+r)=0 and opposite initial colors. The recombination R_j then also minimizes twisted defect. The tight edges T={j->j+r:q_j+q_(j+r)=d-3} are pairwise nonincident in the odd cyclic graph j->j+r, and |T|<=r.

*Proof.* Pick independent minimum-switch arms. The established formula is
D(R_j)=q_j+q_(j+r)+[alpha_j!=alpha_(j+r)]+[beta_(j+r)=0]+[beta_j=1].
Its three indicator terms are at most one. Since D(R_j)>=d, the lower bound follows. If q_j+q_(j+r)=d-3, all three indicators equal one, hence the asserted phases and D(R_j)=d. This holds for every minimizing arm choice. A tight outgoing edge at j forces ALL minimizing arms H_j to finish in color one; a tight incoming edge at j forces all of them to finish in color zero. Thus consecutive directed cycle edges cannot both be tight. Because gcd(r,2r+1)=1, the directed graph is one odd cycle, giving |T|<=r. QED.

For d=3 the threshold is zero, so at most one of the three canonical opposing spoke pairs admits two monochromatic arms; two individual monochromatic spokes may coexist. For d>=5, no opposing pair admits two monochromatic arms. The condition applies to an arbitrary nonlinear coloring and the same globally minimizing path. It retains terminal phases lost under the CS4 telescoping sum. Producing adjacent tight edges or proving a contradiction from equality-preserving R_j across overlapping median spokes remains open.


## Near-tight pairs and monotone terminal-phase transport

Retain globally minimum P, odd twisted defect d=2r+1>=3, common seam-majority root m, seam vertices z_j, and q_j=min sigma(H) over arms H:m->z_j. Let B_j be the nonempty set of possible final colors of minimum-switch arms, viewed as a subset of {0,1} ordered 0<1.

**Proposition (two-level phase transport).** For k=j+r modulo d:
(i) If q_j+q_k=d-3, then B_j={1}, B_k={0}, and every pair of minimum arms recombines to a global minimizer R_j.
(ii) If q_j+q_k=d-2, then min(B_j)>=max(B_k), and every pair of minimum arms recombines to a global minimizer R_j.
Thus all oriented seam-cycle edges with q_j+q_k<=d-2 transmit nonincreasing terminal colors, and edges at d-3 enforce strict decrease. Every directed closed cycle of such low-budget edges avoids strict decrease. In particular the canonical odd cycle contains an edge with q_j+q_(j+r)>=d-1.

*Proof.* Part (i) is the prior tight-edge theorem. For (ii), q_j+q_k is odd, so the minimum switch-count parities differ. Along every arm, alpha=beta XOR (sigma mod 2). Hence the [alpha_j!=alpha_k] term in (CS3) equals one when beta_j=beta_k, and zero otherwise. The combined three endpoint indicators of (CS3) equal two when (beta_j,beta_k) is (0,0), (1,0), or (1,1), and zero for (0,1). The last option gives D(R_j)=d-2<d, violating global minimality. Every remaining option gives D(R_j)=d. Since the two minimum arms may be selected independently, all elements of B_j must be >= all elements of B_k. The cycle consequence follows by composing these inequalities; one strict drop cannot return to its starting value along a nonincreasing cycle. QED.

**Research scope.** The terminal-phase monotonicity is an integer two-state law for minimum-switch arms in the same coloring, lost under the cyclic telescoping sum. No universal bound showing that enough opposite spoke pairs have budgets <=d-2 has been proved. The next forcing task is to use cross-root topology and globally minimizing recombinations to produce or constrain those low-budget pairs. Vertex balance and isolated proper-face data alone cannot do so.
