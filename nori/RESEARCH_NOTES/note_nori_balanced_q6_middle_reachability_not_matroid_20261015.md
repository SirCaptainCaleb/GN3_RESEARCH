# Balanced middle half-geodesic direction sets violate matroid basis exchange in every even dimension

- Stable ID: note_nori_balanced_q6_middle_reachability_not_matroid_20261015
- Author: session_nori_r9962_8
- Primary home: subsection:odd_girth_and_frustration_of_switch_component_quotients
- Labels: proved, dimension-uniform, balanced, interaction-connected, matroid-exchange, rooted-reachability
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r9962_8
- Updated session: session_nori_r9962_8
- Disposition: none
- Successor: none

## Related references

- subsection:odd_girth_and_frustration_of_switch_component_quotients
- section:nori_matroid_generalizations_conjectures

## Research note

Let n=6, write χ_j(x)=(-1)^{x_j}, and put M(a,b,c)=1 if at least two bits are one. Define signed zero-edge rules
\[
s_0(x)=χ_3(x),\quad s_1(x)=-χ_3(x),\quad
s_2(x)=(-1)^{M(x_0,x_4,x_5)},\quad s_3(x)=-s_2(x),\quad
s_4(x)=-(-1)^{M(x_0,x_2,x_3)},\quad s_5(x)=-s_4(x).
\]
An edge in direction i has color zero precisely when s_i(x)=+1. Every s_i ignores x_i and reverses sign under antipodal complementation; each paired pair sums to zero. Hence this is a legal vertex-balanced antipodally odd Q6 coloring.

At root 0, define a feasible direction set S as one admitting an all-zero geodesic from 0 using each direction in S once. The reachable subsets through rank three, obtained recursively by adjoining i when s_i(1_S)=+1, are
\[
\mathcal F_0=\{\varnothing\},\quad
\mathcal F_1=\{\{0\},\{2\},\{5\}\},\quad
\mathcal F_2=\{\{0,2\},\{0,5\},\{2,5\}\},
\]
\[
\boxed{\mathcal F_3=\{\{0,2,4\},\{0,2,5\},\{0,3,5\}\}.}
\]
This recurrence supplies a short exhaustive certificate: a rank-k set is reachable if and only if some i in it has its rank-(k−1) deletion reachable and s_i(1_{S\setminus\{i\}})=+1.

Take A={0,2,4} and B={0,3,5} in F_3, and i=2 in A\setminus B. The only candidates for base exchange are A−2+3={0,3,4} and A−2+5={0,4,5}; both are absent from F_3. Thus the middle-rank zero-reachable direction sets need not be bases of any matroid, even for vertex-balanced antipodally odd colorings.

This refutes a direct matroid-intersection/Hall reduction in which the two rooted half-geodesic direction families are assumed to be matroid base families. It leaves open exchange principles retaining endpoint information, path orders, or interactions between the two colors.

**Dimension-uniform strengthening (all even dimensions and connected direction interaction).** For any even n>=6, retain the six signed direction rules above, independent of all new bits. For every even k in {6,8,...,n-2}, append s_k(x)=(-1)^{x_0} and s_{k+1}(x)=-(-1)^{x_0}. Each new rule ignores its own bit and reverses under antipodal complementation. The pairs sum to zero, so the full coloring is balanced and antipodally odd. Its direction-interaction graph is connected: the first six directions are connected through their reader dependencies, and every new direction depends on bit 0.

Put L={6,8,...,n-2}. From root 0 all the directions in L can be traversed first with color zero, since s_k(0)=+1 and the new steps leave x_0 unchanged. The original Q6 zero half-geodesics then yield the two feasible middle-rank direction sets A_n={0,2,4} union L and B_n={0,3,5} union L, each of size n/2. For i=2 in A_n minus B_n, the only replacement candidates from B_n minus A_n are 3 and 5. Neither (A_n minus {2}) union {3} nor (A_n minus {2}) union {5} is feasible: deleting all new-direction steps from a supposed zero path would leave a zero path in the original Q6 using respectively {0,3,4} or {0,4,5}, both ruled out by the rank-three certificate above. Thus the matroid basis-exchange axiom fails for the zero-reachable middle layer in an interaction-connected, vertex-balanced, antipodally odd coloring in every even dimension n>=6. This blocks a dimension-uniform matroid-Hall argument based solely on those rooted direction-set families, including after reduction to interaction-connected legal matrices.
