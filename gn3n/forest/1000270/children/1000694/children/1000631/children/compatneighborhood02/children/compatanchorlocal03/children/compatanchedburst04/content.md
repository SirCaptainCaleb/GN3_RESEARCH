# High compatibility degree forces a synchronized anchored incompatibility family

## Statement

In the setting of compatneighborhood02 and compatanchorlocal03, let d be a vertex of the compatibility graph with degree k>=1. Then there is a neighbor a of d that is incompatible with at least max{0,k-3} other neighbors b of d. For every such b, the restrictions of F_a and F_b become compatible after deleting d, so every support/order disagreement between F_a and F_b is carried by the same anchor label d.

## Body

# Proof

Let k=d_G(d). Assume k>=1. If k<=3, choose any neighbor a of d and take B=empty. Then |B|=0=max{0,k-3}, so the conclusion is immediate.

Now suppose k>=4. Let J=G[N_G(d)]. By compatneighborhood02, Delta(J)<=2, hence e(J)<=k. Therefore the complement of J on the same k vertices has

binom(k,2)-e(J) >= binom(k,2)-k

edges. Its average degree is

2[binom(k,2)-e(J)]/k >= 2[binom(k,2)-k]/k = k-3.

Hence some a in N_G(d) has at least k-3 nonneighbors inside N_G(d). Let B be any set of k-3 such nonneighbors. For every b in B, both ad and bd are compatibility edges while ab is not.

Apply compatanchorlocal03 to each triple a,b,d. The restrictions of F_a and F_b to V(H)-{a,b,d} are compatible, and every incompatibility witness on their full common domain V(H)-{a,b} involves d. Thus the entire family {F_a,F_b:b in B} has one common anchor label d carrying all of its support/order disagreement.

This conclusion is order-independent. It converts a single positive compatibility degree k into a family of at least max{0,k-3} pairwise incompatibilities synchronized at one common label, rather than merely producing unrelated disagreement witnesses.
