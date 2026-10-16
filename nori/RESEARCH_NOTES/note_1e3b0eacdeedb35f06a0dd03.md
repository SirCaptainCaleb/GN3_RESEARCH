# Polynomial-density Hamilton cycle of red-compatible directions in every balanced cube

- Stable ID: note_1e3b0eacdeedb35f06a0dd03
- Author: unspecified; session provenance retained
- Primary home: subsection:folded_cube_line_graphs_and_local_generation_of_binary_dependencies
- Labels: NORI1, balanced, unrestricted, Hamilton-cycle, Boolean-Poincare, robust-compatibility
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10712_1
- Updated session: session_nori_r10712_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

QUANTITATIVE HAMILTON CYCLE THEOREM. Let n>=4 even, and c be any vertex-balanced antipodally odd undirected edge coloring of Q_n. Write s_i(x)=(-1)^(c_i(x)) and for distinct directions i,j let p_ij=Pr_(uniform x)[s_i(x)=s_j(x)=+1]. Define G_theta on [n] by ij present if p_ij>=theta, where theta=1/(32n). Then G_theta has a Hamilton cycle. Consequently the n directions can be arranged cyclically so that EACH adjacent pair admits a red two-edge cube path at no fewer than 2^n/(32n) starting center vertices. The blue analogue follows by antipodal reflection. No bound on nonlinear rule complexity is assumed.

Proof. Antipodal oddness implies Pr[s_i=+1]=1/2 for every i. If three distinct directions i,j,k were pairwise nonadjacent in G_theta, the union bound with first two inclusion-exclusion terms would give
1>=Pr[any of i,j,k is red]>=3/2-p_ij-p_ik-p_jk>3/2-3theta>1,
a contradiction. Hence alpha(G_theta)<=2.

We prove G_theta has no articulation vertex. Suppose for some v the deletion G_theta-v is disconnected, and partition the remaining directions into two nonempty sets A,B with no cross edge. Then p_ij<theta for all i in A,j in B. Since antipodal inversion interchanges red-red with blue-blue, one has Pr[s_i=s_j]=2p_ij<2theta for all cross pairs. Choose i0 in A, j0 in B and set f=s_i0, an odd mean-zero sign function.

For every i in A, the triangle inequality for sign-disagreement gives Pr[s_i != f]<=Pr[s_i != -s_j0]+Pr[-s_j0 != f]<4theta, and for j in B we have Pr[s_j != -f]<2theta. Let a=|A|,b=|B|, a+b=n-1. The event E on which all these alignments hold has probability at least 1-4(n-1)theta>0. Pointwise vertex balance says sum_i s_i(x)=0. On E this becomes (a-b)f+s_v=0. Because a+b is odd, a-b is odd; since f and s_v are signs, E nonempty forces a-b=+1 or -1, and on E we have s_v=-(a-b)f. Thus for each direction i there exists a constant sign eta_i in {+1,-1} such that Pr[s_i != eta_i f]<=4theta when i !=v, and Pr[s_v != eta_v f]<=4(n-1)theta.

Each s_i is independent of bit i by edge consistency. Thus Boolean influence Inf_i(f)=Pr[f(x) != f(x xor e_i)] obeys Inf_i(f)<=2Pr[s_i != eta_i f], since the comparison at x and at its bit-i flip has the same distribution. Summing over i gives
sum_i Inf_i(f)<=2*(4(n-1)theta+4(n-1)theta)=16(n-1)theta<1.
But f is antipodally odd, hence mean zero and variance one. The Boolean Poincare inequality yields sum_i Inf_i(f)>=Var(f)=1, contradiction. Therefore G_theta-v remains connected for every v. With n>=4 this implies G_theta is 2-connected and kappa(G_theta)>=2.

Finally the Chvatal--Erdos Hamiltonicity theorem states that every graph with vertex connectivity at least its independence number is Hamiltonian. Apply kappa>=2>=alpha to G_theta.

SHARPNESS LIMIT OF CONSTANT DENSITY. In the majority-paired family recorded in note_74cf251b5aa0830cadf4d053, every cross pair between the two blocks of n/2 directions has witness density O(n^(-1/2)). Thus no replacement of theta=1/(32n) by a fixed positive constant is possible in this theorem. The bound may perhaps be improved as a function of n. The conclusion is a global cyclic order with individually many local two-step red witnesses, NOT a simultaneous root-consistent red full geodesic. A separate exchange or transport theorem is required to glue its witnesses.

UNRESTRICTED CONNECTIVITY COMPANION. Vertex balance is not needed to force a robust connected compatibility graph. For ANY antipodally odd legal coloring of Q_n, n>=3, put theta=1/(16n) and connect directions i,j when p_ij>=theta. Then this threshold graph is connected, has independence number <=2, and has diameter <=3. Proof of connectedness: If it split into nonempty A,B, select i0 in A and set f=s_i0. Every i in A has disagreement Pr[s_i!=f]<4theta, and every j in B has disagreement Pr[s_j!=-f]<2theta. Each rule s_i ignores its own bit. Therefore the Boolean influence bound gives sum_i Inf_i(f) <=2*4(n-1)theta <1, contradicting the Boolean Poincare inequality for the balanced odd sign function f. The independence bound uses the same three-red-events Bonferroni inequality as in the main theorem because theta<1/6. Any connected graph of independence number <=2 has diameter <=3: if a shortest path had length at least four, its first, third, and fifth vertices would be pairwise nonadjacent, impossible. Thus antipodal oddness already enforces uniform 3-step robust connectivity of the direction compatibility network; pointwise vertex balance strengthens this to two-connectivity and Hamiltonicity at a comparable scale.
