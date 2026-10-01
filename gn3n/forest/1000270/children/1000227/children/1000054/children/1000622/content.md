# Transfer invariants and the limits of support-only closure

## Statement

Deletion-cover size defects sum to 2lambda-(n-1); good-deletion defect-flipping transfers preserve the unordered maximum-path-order pair. In the half-order odd graph, closed-walk labels have uniform parity determined by walk length. An abstract allowable-support system satisfies the basic deletion, complement and full-transfer graph axioms while requiring three supports.

## Body

# What single-transfer dynamics preserve

Let H be a minimum counterexample of order n. For a nonempty support X let L(X) be its maximum tight-path order and d(X)=|X|-L(X). Let lambda=L(V(H)) and sigma=2lambda-(n-1).

## Proposition

1. Sigma is nonnegative. Every exact deletion two-cover has component orders lambda-a, lambda-b for nonnegative integers a,b with a+b=sigma. In particular sigma=0 forces lambda|lambda and sigma=1 forces lambda|(lambda-1).
2. Along any sequence of good-deletion transfers from the deficient support to the Hamiltonian support, the unordered pair of maximum path orders of the two supports is invariant. This assertion concerns this specified class of moves, not all possible reconfigurations of total deficit one.
3. In the equality case sigma=0, write G for the disjointness graph of Hamiltonian lambda-subsets, with each edge labelled by its unique omitted vertex. In every even closed walk of G, each label occurs an even number of times. In every odd closed walk, each vertex of H occurs as a label an odd number of times. Consequently an odd closed walk has length at least 2lambda+1, and every connected component whose edges omit at least one label is bipartite.

## Proof

For a deletion cover P|Q, both orders are at most lambda and their sum is n-1. Setting a=lambda-|P| and b=lambda-|Q| proves assertion 1.

For assertion 2, name the deficient side R and the Hamiltonian side S. Write |R|=r+1 and |S|=s, so their maximum path orders are r and s. Let v be a good deletion of R, meaning that R-v is Hamiltonian. The enlarged set S+v contains the Hamiltonian support S. It cannot itself be Hamiltonian, since then (R-v)|(S+v) would two-cover H. Thus L(S+v)=s, whereas L(R-v)=r. The two maximum orders have merely exchanged places. Iteration proves the assertion. No claim is made about transferring a vertex which is not a good deletion, or about transferring from the Hamiltonian support into the deficient support.

For assertion 3, let A_0,...,A_t=A_0 be a closed walk, with edge labels x_0,...,x_{t-1}. Regard characteristic vectors as vectors over F_2. Disjointness and the unique omitted label give
1_{A_{i+1}}=1_V+1_{A_i}+e_{x_i}.
Summing yields
sum_i e_{x_i}=(t mod 2)1_V.
Reading each coordinate proves the label parity assertions. An odd walk consequently uses all 2lambda+1 labels. A component missing a label has no odd cycle and is bipartite. This proves assertion 3.

## A support-only model with no two-cover

For any k>=5 take a set V of order 2k+1 and define an abstract family F of nonempty allowable supports by
F={X subset V:1<=|X|<=k}.
Define its cover number using partitions into members of F. This is a set system, not a claimed boundary tournament.

Its cover number on a nonempty m-set is ceil(m/k): each component has at most k vertices, and partitioning into pieces of at most k attains the bound. Thus V needs three allowable supports while every proper subset needs at most two. Every deletion of one vertex has a two-cover, and every such cover has sizes k,k. Every member of F has a complementary exact two-cover. The maximum allowable support size is k.

Define L_F(X)=min(|X|,k) and d_F(X)=|X|-L_F(X). Total-deficit-one bipartitions are exactly the size patterns k|(k+1). Every vertex of the larger side is a good deletion, and the defect-flipping transfer graph is the full odd graph KG(2k+1,k). Every vertex label occurs; each graph vertex has the maximum possible degree k+1. All of the displayed size and transfer identities hold, yet the abstract cover number remains three.

This model does not satisfy, and is not claimed to satisfy, the ordered triple axioms of a boundary tournament. Its purpose is exact: the specified support-level axioms, even with all k-subsets available and all transfers possible, cannot alone imply a two-cover. A successful argument must use an additional consequence of ordered tightness that excludes this abstract model. It may express that consequence in support language, but it has to prove it from the boundary relation.
