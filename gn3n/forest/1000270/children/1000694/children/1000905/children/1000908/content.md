# Every same-slot compatible deletion pair has a mixed Hamiltonian five-support through both omitted labels

## Statement

Let H be a minimum counterexample and suppose fully compatible exact deletion covers of H-a and H-b have identical insertion slot in one common ordered support class P, with the other common class Q unchanged. Thus, in the notation of 1000905,
F_b=(L,a,R)|Q,   F_a=(L,b,R)|Q,
with P=(L,R).

Then P is nonempty and |Q|>=2. Moreover there is a Hamiltonian five-set X containing {a,b} such that X-{a,b} meets both P and Q. If |P|>=2, there are at least two such mixed Hamiltonian five-sets inside one six-vertex window. If |P|=1, at least one such mixed Hamiltonian five-set exists.

In a minimum counterexample every such X has non-Hamiltonian complement of path-cover number exactly two. Hence the identical-slot branch of a fully compatible deletion pair always produces a mixed five-side standard input, without any flank-length case split or matching-block analysis. For n>=18, choosing an exact two-cover of H-X gives a complementary path of order at least seven, so five_side_arbitrary_escape01 applies to this mixed five-side state.

## Body

Write the common support classes on H-{a,b} as P and Q. In the identical-slot representation,
F_b=(L,a,R)|Q and F_a=(L,b,R)|Q,
where P=(L,R). Since F_b is an exact two-cover of H-b and exact deletion covers in a minimum counterexample have no singleton component, |P|+1>=2 and |Q|>=2. Hence |P|>=1.

First suppose |P|>=2. Choose distinct p_1,p_2 in P and q_1,q_2 in Q, and put
U={a,b,p_1,p_2,q_1,q_2}.
Apply sixset_prescribed_pair_menu01 to U with prescribed pair {a,b} and A={p_1,p_2,q_1,q_2}. At least two distinct d in A make U-{d} Hamiltonian. Every such five-set contains a,b, and deleting one element from a 2P+2Q sample leaves at least one vertex from P and at least one from Q. Thus both guaranteed Hamiltonian five-sets are mixed across the two common support classes.

Now suppose |P|=1, say P={p}. Because n>10 by mincex01 and V(H)={a,b} disjoint union P disjoint union Q, |Q|=n-3>=8. Choose distinct q_1,q_2,q_3 in Q and put U={a,b,p,q_1,q_2,q_3}. Again sixset_prescribed_pair_menu01 gives at least two Hamiltonian deletions U-{d}, d in {p,q_1,q_2,q_3}. At most one of those deletions can be d=p, so at least one Hamiltonian five-set deletes a q_i and therefore retains p together with two Q-vertices. It is mixed across P and Q.

Every resulting X is a proper Hamiltonian support. Minimum-counterexample calculus gives pc(H-X)<=2, and H-X cannot be Hamiltonian because then X together with H-X would two-cover H. Hence pc(H-X)=2 and H-X is non-Hamiltonian.

Finally, if n>=18, any exact two-cover P'|Q' of H-X has total order n-5>=13, so one side has order at least seven. Therefore five_side_arbitrary_escape01 applies to X together with that side, giving its strict-descent / neutral endpoint-support exchange / displayed-edge reversal trichotomy. As in 1000907, this last statement concerns the produced five-side state and does not assert reachability from the original same-slot cover.