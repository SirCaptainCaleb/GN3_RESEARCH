# Every prescribed pair has a descending three-side whenever one complementary component has order at least six

## Statement

Let H be a minimum counterexample and let L,R be distinct vertices. Then there exists a vertex x outside {L,R} such that X={L,R,x} is a tight three-vertex path and H-X is non-Hamiltonian with path-cover number two. For any displayed two-cover H-X=P|Q for which max{|P|,|Q|}>=6, the spanning three-cover X|P|Q admits one legal pairwise repartition with strictly smaller quadratic potential. The new Hamiltonian support created by that move has order four or five and contains all of X, hence contains the prescribed pair L,R. In particular the hypothesis max{|P|,|Q|}>=6 is automatic when |H|>=14.

## Body

Apply fixedpair_three_side_cover01 to L,R. It gives x such that X={L,R,x} is a tight three-side and H-X is non-Hamiltonian with path-cover number two. Choose any displayed two-cover P|Q of H-X with a component of order at least six, and relabel so |P|>=6. Apply threesidedescent6 to X|P. It performs one legal pairwise repartition with strict quadratic-potential decrease; in its endpoint-extension branch the drop is 2|P|-8>0, and in its five-side branch the drop is 4|P|-20>0. The new Hamiltonian support has order four or five and contains all three vertices of X. Thus it contains L,R.

If |H|>=14, then |P|+|Q|=|H|-3>=11, so one of P,Q has order at least six. Hence fixedpair_three_side_descent14 is the immediate order-threshold corollary.
