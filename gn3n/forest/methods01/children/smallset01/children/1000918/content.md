# Three-side singleton lifts have a six-way endpoint descent fan that exits the small-side regime

## Statement

Let C=P|(x)|Q be a spanning three-cover of a boundary tournament, where |P|=3 and Q=(q_0,...,q_{m-1}). Put X=V(P) union {x}.

For either displayed end of Q, define the one-label endpoint five-supports F_v and two-label endpoint five-supports F_Z exactly as in threeside_bounded_endpoint_five_repartition01. Let A be the set of v in X for which F_v is Hamiltonian, and B the set of Z in binom(X,2) for which F_Z is Hamiltonian. Then
|A|+|B| >= |A|+binom(4-|A|,2) >= 3.
Thus at least three endpoint-local five-supports are Hamiltonian at each end.

If m>=7, the left- and right-end candidate families are disjoint. Hence C has at least six distinct reachable support partitions of strictly smaller quadratic potential, each reached by at most two legal nonincreasing pairwise repartitions. A one-label support has profile (5,3,m-4) and Phi-drop 8m-40; a two-label support has profile (5,2,m-3) and Phi-drop 6m-28. Therefore every one of the six drops Phi by at least 6m-28.

The three-candidate equality case at one endpoint is rigid: either exactly three one-label candidates occur, or exactly two one-label candidates occur together with precisely the two-label candidate on their complementary pair. Consequently, if exactly six candidates occur over both endpoints, then either one label of X is one-label-good at both ends, or X splits into two pairs A_L,A_R and the two ends realize the crossed complementary 2+2 pattern.

If m>=10, each of the six endpoint-local descents continues, while preserving its Hamiltonian five-support F, to a distinct spanning three-cover F|A'|B' with min{|A'|,|B'|}>=4. The continuation uses at most two additional legal strict repartitions, never increases Phi, and ends with profile either (5,4,m-5) or (5,5,m-6). The total Phi-drop from C is at least 10m-56.

In particular, for a minimum counterexample deletion lift with m=n-4, the m>=7 conclusion gives six distinct descents each dropping Phi by at least 6n-52; when n>=14, m>=10 and all six continue to distinct same-component covers of minimum side at least four, each dropping Phi by at least 10n-96.

## Body

Fix one endpoint of Q. The prescribed-pair theorem threeside_bounded_endpoint_five_repartition01 says that for every pair {u,v} subset X, at least one of F_u,F_v,F_{uv} is Hamiltonian. If A is the set of one-label-good vertices, then every pair contained in X-A must lie in B. Hence, writing a=|A|,
|A|+|B| >= a+binom(4-a,2).
For a=0,1,2,3,4 this lower bound is respectively 6,4,3,3,4, proving the three-candidate minimum. The same argument applies independently at the other endpoint.

The parent theorem supplies an explicit at-most-two-step nonincreasing repartition route for every Hamiltonian candidate. Its one-label and two-label profiles and potential changes are respectively
(5,3,m-4), 40-8m,
and
(5,2,m-3), 28-6m.
For m>=7 both are strict and the smaller guaranteed drop is 6m-28. The left and right families are disjoint: they contain different endpoint blocks of Q, and one-label and two-label candidates meet X in different cardinalities.

If exactly three candidates occur at one endpoint, the displayed lower-bound table forces a=2 or 3. For a=3 there can be no two-label candidate; for a=2 the only possible two-label candidate is the complementary pair X-A. Applying this at both ends gives the stated six-candidate classification.

Now assume m>=10 and fix one of the six Hamiltonian five-supports F. If F is one-label type, its route gives profile (5,3,m-4) with drop 8m-40. Since m-4>=6, apply threesidedescent6 to the 3-side and the long side while keeping F fixed. The resulting profile is (5,4,m-5) or (5,5,m-6), and the additional drop is at least 2(m-4)-8=2m-16. Thus the total drop is at least 10m-56.

If F is two-label type, its route gives profile (5,2,m-3) with drop 6m-28. Let D be the 2-side and R the path of order r=m-3. For either displayed endpoint e of R, the three-set D union {e} has a tight Hamilton path. Repartition D|R into that three-path and the inherited path R-e. The drop is
4+r^2-[9+(r-1)^2]=2r-6=2m-12,
so the new profile is (5,3,m-4) and the cumulative drop is 8m-40. Apply threesidedescent6 as in the one-label case to obtain the same final profiles and total drop at least 10m-56.

Each continuation preserves its chosen F, so the six distinct five-supports produce six distinct final covers. Substituting m=n-4 gives the two minimum-counterexample bounds.