# A three-side singleton lift has a six-way strict descent fan

## Statement

Let C=P|(x)|Q be a spanning three-cover of a boundary tournament, where |P|=3 and Q=(q_0,...,q_{m-1}) has m>=7. Put X=V(P) union {x}.

At the left end define, for v in X and Z in binom(X,2),
L_v={v,q_0,q_1,q_2,q_3},
L_Z=Z union {q_0,q_1,q_2}.
At the right end define
R_v={v,q_{m-4},q_{m-3},q_{m-2},q_{m-1}},
R_Z=Z union {q_{m-3},q_{m-2},q_{m-1}}.

At least three distinct members of the left family {L_v} union {L_Z} are Hamiltonian, and at least three distinct members of the right family {R_v} union {R_Z} are Hamiltonian. Every Hamiltonian member produces, by at most two legal pairwise repartitions from C, each nonincreasing in quadratic potential, a spanning three-cover in the same pairwise-repartition component with that member as a five-vertex component. For L_v or R_v the new component orders are (5,3,m-4) and the total potential change is 40-8m; for L_Z or R_Z they are (5,2,m-3) and the change is 28-6m.

The left and right candidate families are disjoint when m>=7. Consequently C has at least six distinct reachable support partitions of strictly smaller quadratic potential, each within pairwise-repartition distance at most two. Every one lowers the potential by at least 6m-28.

Moreover, suppose exactly six candidates across the two endpoint families are Hamiltonian. Let A_L be the set of v in X for which L_v is Hamiltonian and define A_R analogously. Then either A_L intersects A_R, so one label of X occurs in a one-label Hamiltonian five-support at both ends, or X has a partition X=A disjoint_union B into two pairs such that the left Hamiltonian candidates are exactly {L_v:v in A} together with L_B, while the right Hamiltonian candidates are exactly {R_v:v in B} together with R_A.

In particular, if H is a minimum counterexample and H-x=P|Q is an exact deletion cover with |P|=3, then m=|Q|=|V(H)|-4>=7. Its singleton lift P|(x)|Q is therefore never quadratic-potential-minimal in its pairwise-repartition component; indeed it has at least six distinct descents, each decreasing potential by at least 6|V(H)|-52>=14.

## Body

Use threeside_bounded_endpoint_five_repartition01 at the left endpoint for every prescribed pair Z={u,v} subset X. Write A_L for the set of labels v for which L_v is Hamiltonian, and B_L for the set of pairs Z for which L_Z is Hamiltonian. The cited theorem says, for every pair {u,v}, that at least one of L_u,L_v,L_{uv} is Hamiltonian. Hence every pair contained in X-A_L belongs to B_L.

Put a=|A_L|. Since |X|=4,
|A_L|+|B_L| >= a + binom(4-a,2).
For a=0,1,2,3,4 the right side is respectively 6,4,3,3,4. Thus at least three distinct left candidates are Hamiltonian. The same argument at the right endpoint gives at least three right candidates.

For each Hamiltonian candidate, threeside_bounded_endpoint_five_repartition01 supplies the explicit at-most-two-step pairwise-repartition route and its complementary inherited paths. A one-label candidate has profile (5,3,m-4) and potential change 40-8m; a two-label candidate has profile (5,2,m-3) and change 28-6m. For m>=7 both are negative, and
min(8m-40,6m-28)=6m-28,
so every route decreases potential by at least 6m-28.

The two endpoint families are disjoint. Left and right one-label candidates contain different four-vertex Q-blocks when m>=7; left and right two-label candidates contain different three-vertex Q-blocks; and a one-label candidate cannot equal a two-label candidate because they contain different numbers of vertices from X. Hence the three left descents and three right descents give at least six distinct support partitions.

For the equality statement, suppose there are exactly three Hamiltonian candidates at one endpoint. If a=|A_L|, the inequality above shows a is 2 or 3. If a=3 then B_L is empty; if a=2 then B_L consists exactly of the unique pair on X-A_L. The same holds on the right.

Now suppose there are exactly six Hamiltonian candidates total and A_L cap A_R is empty. Both endpoint families have exactly three candidates, hence |A_L|,|A_R|>=2. Their disjointness inside the four-set X forces |A_L|=|A_R|=2 and X=A_L disjoint_union A_R. The equality description from the preceding paragraph then gives B_L={A_R} and B_R={A_L}, which is precisely the crossed two-pair pattern in the statement. Otherwise A_L cap A_R is nonempty and supplies a label good at both ends.

Finally, in a minimum counterexample the certified minimum-counterexample calculus gives |V(H)|>10, so an exact deletion cover with a three-vertex component has m=|V(H)|-4>=7. Substituting m=n-4 into 6m-28 gives 6n-52>=14. Thus its singleton lift cannot be a quadratic-potential minimum in its pairwise-repartition component.