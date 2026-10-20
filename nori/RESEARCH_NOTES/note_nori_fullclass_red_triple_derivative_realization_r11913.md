# Red-triple realization of pair influences and sharp uniform count

- Stable ID: note_nori_fullclass_red_triple_derivative_realization_r11913
- Author: Independent NORI1 researcher session_nori_r11913_3
- Primary home: subsection:creative_routes_to_unrestricted_forcing_and_a_carry_forward_map
- Labels: nori1, unrestricted, red-matching, triple-influence, q-dependency, dimension-uniform
- Lifecycle: active
- Epistemic status: proved
- Current version: 3
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11913_3
- Updated session: session_nori_r11913_3
- Disposition: none
- Successor: none

## Related references

- note:note_nori_prescribed_midparity_fiber_dependency_reduction_20261019_r11913
- note:note_a33d0ec0d34a24ff85f2b99b

## Research note

# Red three-step witnesses for all pair influences

Fix n=2m≥4 and an arbitrary legal antipodally odd paired-flat coloring. Pair i consists of original directions 2i and 2i+1. Its selector f_i is independent of its own pair and satisfies f_i(bar x)=1⊕f_i(x). Let U_i(x) flip direction 2i+f_i(x), the red matching step. For i≠j and k in pair j, let E_(i,k) be the set of undirected k-edges on which f_i changes. Let T_(i,j) count rooted oriented red walks with pair-index word i,j,i using three distinct original directions.

**Theorem 1.** For every k in pair j, half of E_(i,k) is red and half blue. Moreover
T_(i,j)=|E_(i,2j)|+|E_(i,2j+1)|.
Thus a rooted red dimension-simple i,j,i walk exists if and only if f_i depends on at least one original bit in pair j.

Proof. The derivative of f_i across an edge is invariant under antipodality; the red/blue color is reversed. Each antipodal two-edge orbit inside E_(i,k) contains one red edge and one blue edge. Each oriented red j-edge x→y on which f_i changes provides the red walk U_i(x)→x→y→U_i(y). Its first and last directions in pair i are different because f_i(x)≠f_i(y). Conversely any red walk with pair word i,j,i using distinct directions has this form, because the red matching step is uniquely determined. Both orientations of every red derivative edge are allowed. The displayed count follows.

**Theorem 2 (sharp count).** For each i,
sum_(j≠i) T_(i,j)≥2^(n−1).
Summing over i yields at least m·2^(2m−1) rooted oriented red dimension-simple three-step walks with one pair appearing twice, in every such coloring. The bound is attainable.

Proof. Fix one order of the n−2 outside directions of pair i. Starting from any cube vertex x, traverse these directions once. The selector f_i changes between the endpoints because it ignores pair i and is globally odd, so some traversed edge changes f_i. Sum this assertion over all 2^n roots. At each fixed step position, the vertex before that step runs through all cube vertices; the derivative support for direction k is counted twice per undirected edge. Hence 2·sum_(k outside i)|E_(i,k)|≥2^n. Apply Theorem 1. For equality in every pair, choose cyclic readers f_i=x_(2((i+1) mod m)), all legal and odd.

**Transfer to minimal-counterexample geometry.** Form the directed red-triple graph D_3 on pair labels, with arc j→i iff a rooted red dimension-simple i,j,i walk exists. Theorem 1 identifies D_3 with the full-pair influence graph of the selectors. The q-dependency graph D_q, whose arc j→i records dependence on q_j=x_(2j) while fixing p_j=x_(2j)⊕x_(2j+1), is a subgraph of D_3. Every terminal SCC of D_3 contains a terminal SCC of D_q: the former is D_q-outgoing-closed and hence contains a sink SCC of the D_q condensation. Therefore the established conditional restriction that every terminal D_q SCC in a least-dimensional NORI1 counterexample has at least four pair labels also holds for D_3. Every D_3 arc now comes with a red three-step path in the shared original coloring.

**Nonlinear overlap obstruction.** On Q8 set q_i=x_(2i), p_2=x_4⊕x_5, and
f_0=(p_2=0 ? q_1 : q_2),
f_1=(p_2=0 ? q_2 : q_0),
f_2=q_3, f_3=q_0.
These are legal odd pair gates. The q-dependency graph has outgoing sets D_q(0)={1,3}, D_q(1)={0}, D_q(2)={0,1}, D_q(3)={2}; it is strongly connected. Nevertheless,
{x:f_0(U_1x)≠f_0(x)}={x:p_2=0,q_2=0},
{x:f_1(U_0x)≠f_1(x)}={x:p_2=1,q_2=0}.
Each set contains 64 vertices and their intersection is empty. Thus mutual dependencies need not create two red matching derivatives at the same vertex, even inside a strongly connected four-label core. The example does not rule out other square exchanges: root 1 and original direction word (7,0,4,6,2,5,3,1) give a red full one-gap geodesic.

**Scope and verification.** An independent verifier checks the derivative-count identity and all red three-step paths on sampled legal Q4–Q10 gates and checks the nonlinear Q8 support and red full word. The theorem provides full-class local path witnesses and a geometric form of the published q-core restriction. No extension of one of these local triples to a full antipodal red geodesic is established; NORI1 remains open.

## Uniform strongly connected q-core with nonextendable red triples

**Theorem (full-dimensional obstruction to universal local-to-global extension).** For every m≥4 there is a legal paired-flat antipodally odd coloring of Q_(2m) whose D_q is strongly connected, which has a rooted red three-edge direction-simple walk of pair type (0,2,0) that lies in no red full antipodal geodesic, yet which has a red full direction-simple antipodal geodesic from root zero.

**Explicit gates.** Write q_j=x_(2j), let
χ0(x)=1 iff (x_2,...,x_7)=000000 or 111111;
χ1(x)=1 iff (x_0,x_1,x_4,x_5,x_6,x_7)=(0,0,0,1,0,0) or (1,1,1,0,1,1).
Both indicators are invariant under global complementation, and χ0 (respectively χ1) ignores pair zero (respectively pair one). Put
f_0=x_5 ⊕ χ0(x)·[1 ⊕ ⊕_(t=4,...,m−1)(q_t⊕q_2)],
f_1=x_7⊕χ1(x), f_2=1⊕x_1, f_3=x_2,
f_t=x_0 for 4≤t<m.
The empty XOR sum equals zero. Each gate ignores its own pair. Each q_t⊕q_2 is invariant under global complementation, so the displayed gates are antipodally odd. No pair-gate independence, affine form, or root restriction is assumed in the obstruction's conclusion.

**Strong connectivity of the q-dependency digraph.** Here j→i records dependence of f_i on q_j at fixed p_j. The base four labels have directed arcs
0→1 (χ1), 1→3 (f_3), 3→0 (χ0),
0→2 (f_2), 2→0 (x_5).
Each appended t≥4 has 0→t (f_t=x_0) and t→0 (χ0 times q_t). These arcs alone form a spanning strongly connected graph; extra arcs may also occur.

**Trapped red region.** Let
C={x:x_2=0, x_7=1, (x_1=0 OR x_5=1)},
with all remaining bits unrestricted. It has 3·2^(2m−4) vertices. On C both χ0 and χ1 vanish. Therefore f_0=x_5, f_1=1, f_2=1⊕x_1, f_3=0, and f_t=x_0. For pair zero, if x_5=0 then x_1=0 and the red step changes x_0; if x_5=1 the red step changes x_1, preserving x_5=1. For pair two, if x_1=0 its red step changes x_5 while x_1 stays zero; if x_1=1 then x_5=1 and the red step changes x_4. The red steps in pair one change only x_3; those in pair three change only x_6; all appended pairs change only their own new bits. Thus every red edge incident with C has both endpoints in C. But no antipodal pair belongs to C because x_2=0 and x_7=1 throughout it. Hence **no red full antipodal geodesic passes through any vertex of C**.

In particular
129→128→160→162
is a red walk with original direction sequence (0,5,1), three distinct directions and pair word (0,2,0). It lies in C and therefore cannot extend to any red antipodal geodesic under any choice of root or direction order.

**Explicit global red success.** From root zero, the original direction word
(6,2,7,3, 8,10,...,2m−2, 0, 9,11,...,2m−1, 5,1,4)
uses every original direction once and is red. The new even steps precede direction zero, where f_t=x_0=0, and the new odd steps follow it, where f_t=x_0=1. The original pair-zero steps occur at old states where χ0=0; the pair-one steps occur where χ1=0. All other old selectors take the required values. Thus the coloring satisfies NORI1 while exhibiting the trapped red triple.

**Scope.** This refutes the claim that every red dependency triple, even in a single strongly connected full q-core, admits extension to a red original-direction-simple full antipodal geodesic. It does not refute the much weaker existential statement that *at least one* appropriately chosen triple can be extended; that remains the missing full-class forcing mechanism. In particular the example cannot be a bad coloring, since the displayed full red geodesic succeeds.

**Reproducibility.** An independent all-vertex checker verifies the gates are odd and pair-independent, D_q strongly connected, C red-invariant and antipode-free, and both rooted words valid on Q8, Q10 and Q12. The finite tests are supplemental to the preceding all-dimensional algebraic proof.


## Strongly connected q-core can have a dependency arc with no extendable red triple

**Theorem (all m≥6).** There is a legal antipodally odd paired-flat coloring of Q_(2m), with strongly connected q-dependency graph, for which the arc 5→4 is witnessed by red direction-simple (4,5,4) triples, but no such triple is contained in any red full antipodal geodesic. The same coloring has a red full antipodal geodesic.

**Construction.** Reuse the preceding four base gates f_0,...,f_3, with f_0 using its previously defined sum over added labels 4≤t<m. Put
C={x:x_2=0,x_7=1,(x_1=0 OR x_5=1)}, χ=1_(C∪bar C), q_j=x_(2j).
Define f_4=x_0 ⊕ χ·(q_5⊕q_2), f_5=x_2, and f_t=x_0 for t≥6.
χ is antipodally even and independent of the added pair directions. Each selector omits its own pair; each is antipodally odd. The old gate rules keep C closed under every red pair step and disjoint from its antipode. New pair steps cannot alter its defining four old bits.

For every vertex x, the red matching step U_5 toggles q_5 iff f_5(x)=0, i.e. x_2=0. Consequently, because χ is independent of pair 5,
f_4(U_5x)⊕f_4(x)=χ(x)·[x_2=0]=1_C(x).
The equivalence uses C⊂{x_2=0} and bar C⊂{x_2=1}. Thus every red (4,5,4) triple has its red middle edge within C; the adjoining pair-4 edges also lie within C. A red full antipodal geodesic cannot contain any vertex of C because C is red-invariant and contains no antipodal pair. Therefore **all** red witnesses of dependency 5→4 are nonextendable, not merely one chosen witness. The number of rooted oriented red (4,5,4) triples equals |C|=3·2^(2m−4)>0.

The q-dependency graph is strongly connected: the old four labels contain cycles 0→1→3→0 and 0↔2; label 4 has 0→4 and 4→0; label 5 has 1→5→4. Every further label t≥6 has 0↔t through f_t=x_0 and the q_t term in f_0. All arrows denote dependence with fixed pair parities.

**Successful full geodesic.** From root 0, the original direction order
(6,10,2,11,7,3, 8,12,14,...,2m−2, 0, 9,13,15,...,2m−1, 5,1,4)
uses each direction once, omitting 10,11 from the displayed increasing tails because they occur earlier. Every step is red: the pair-5 red choices straddle direction 2, other appended pairs straddle direction 0, and χ vanishes at the pair-4 steps. All old selectors evaluate as in the preceding base success witness.

**Interpretation.** Even an all-label strongly connected q-core does not imply that each one of its dependency arcs has a red three-step witness embeddable in a full antipodal geodesic. The existential possibility that **some** arc has an extendable red triple is not challenged. Independent exhaustive vertex-level checks in dimensions 12,14,16 confirm legality, q-connectivity, red invariance, red-derivative support, and the displayed full word.
