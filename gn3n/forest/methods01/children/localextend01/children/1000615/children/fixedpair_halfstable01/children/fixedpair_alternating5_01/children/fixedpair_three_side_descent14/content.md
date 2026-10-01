# From order fourteen every prescribed pair has a one-move descending small-side realization

## Statement

Let H be a minimum counterexample of order n>=14 and let L,R be distinct vertices. Then there exists x outside {L,R} and a spanning three-cover X|P|Q with X a tight three-vertex path on {L,R,x}, such that one legal pairwise repartition strictly decreases quadratic potential and replaces X together with one complementary path by a Hamiltonian support W of order four or five containing all of X. Moreover H-W is non-Hamiltonian with path-cover number two.

## Body

Apply fixedpair_alternating5_01 to L,R and choose the middle label x supplied by its alternating five-path. Then X={L,R,x} is a tight three-vertex path in one of the orders (L,x,R) or (R,x,L), and H-X is non-Hamiltonian with path-cover number two. Choose a two-cover P|Q of H-X. Since |P|+|Q|=n-3>=11, one component, say P, has order at least six. Apply threesidedescent6 to X|P|Q. It gives one legal pairwise repartition with strictly smaller quadratic potential. In the endpoint-extension branch the new small support is X plus one endpoint of P and has order four; in the double-endpoint branch it is X plus both endpoints of P and has order five. Thus in either case the new Hamiltonian support W contains all of X. The other new path from the X|P repartition together with Q gives a two-cover of H-W. If H-W were Hamiltonian then W together with that Hamilton path would two-cover H, impossible. Hence H-W is non-Hamiltonian with path-cover number exactly two.