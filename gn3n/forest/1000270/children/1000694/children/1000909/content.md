# Fully compatible deletion pairs reduce to endpoint reversal or a mixed Hamiltonian five-side

## Statement

Let H be a minimum counterexample, and let F_a,F_b be fully compatible exact two-covers of H-a and H-b. Then at least one of the following holds:

(1) the compatible insertion slots are adjacent, and H contains the explicit displayed component-end reversal supplied by 1000905;

(2) the compatible insertion slots are identical, and H contains a Hamiltonian five-set X with {a,b} subset X such that X-{a,b} meets both common ordered support classes of F_a,F_b on H-{a,b}. Moreover H-X is non-Hamiltonian with path-cover number exactly two.

Thus, in a minimum counterexample, a fully compatible deletion pair has no residual bounded K4/singleton-swap branch: it reduces directly to endpoint reversal or to a mixed Hamiltonian five-side.

If |V(H)|>=18, then in alternative (2) one may choose an exact two-cover P|Q of H-X with max{|P|,|Q|}>=7, and the mixed five-side state X|P|Q satisfies the five_side_arbitrary_escape01 trichotomy: strict quadratic-potential descent, a neutral endpoint/support exchange, or a displayed-edge reversal. This last trichotomy is attached to the produced five-side state and does not assert repartition-component reachability from the original deletion covers.

## Body

By the compatible-pair localization in 1000694, the two omitted labels a,b insert into one common ordered support class P while the other common class Q is unchanged. If they inserted into different classes, or into slots of P separated by at least two positions, the two augmented classes would form a spanning two-cover of H. Since H is a counterexample, those cases are impossible. Therefore the slots are either adjacent or identical.

If the slots are adjacent, 1000905 constructs two spanning three-covers differing by transfer of the unique intervening common vertex. That vertex is terminal on one side of the transfer and initial on the other, so singleton-transfer endpointization gives an explicit tight triple reversing a displayed component-end edge. This is alternative (1).

If the slots are identical, 1000908 applies. It produces a Hamiltonian five-set X through both omitted labels a,b such that the other three vertices of X meet both common support classes P and Q. Minimum-counterexample calculus gives pc(H-X)=2 and H-X non-Hamiltonian. This is alternative (2). In particular the earlier long-flank/short-flank matching-block taxonomy is not needed merely to reach a standard bridge input.

For n>=18, an exact two-cover P'|Q' of H-X has |P'|+|Q'|=n-5>=13, hence one component has order at least seven. Applying five_side_arbitrary_escape01 to X and that component gives strict Phi descent, a component-order-preserving endpoint/support exchange, or a displayed-edge reversal. As with 1000908, the resulting state need not lie in the original pairwise-repartition component, so no stronger reachability claim is made.
