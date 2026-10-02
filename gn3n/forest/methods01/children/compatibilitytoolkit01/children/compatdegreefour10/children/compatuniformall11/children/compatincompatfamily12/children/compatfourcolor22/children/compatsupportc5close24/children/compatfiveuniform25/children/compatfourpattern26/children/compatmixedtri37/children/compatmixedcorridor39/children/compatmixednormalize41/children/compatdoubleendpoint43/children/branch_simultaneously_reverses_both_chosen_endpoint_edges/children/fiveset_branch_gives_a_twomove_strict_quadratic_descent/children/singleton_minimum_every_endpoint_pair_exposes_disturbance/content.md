# At a trapped deletion singleton minimum every endpoint pair exposes disturbance

## Statement

Let H be a minimum counterexample, let H-b=P|Q be a deletion cover with |P|,|Q|>=3, and suppose the singleton lift P|Q|{b} minimizes quadratic potential in its pairwise-repartition component. Choose arbitrarily one displayed endpoint a of P and one displayed endpoint c of Q, and choose arbitrary deletion covers of H-a and H-c. Then at least one endpoint comparison exposes an internal-restoration support crossing or ordered-cover disagreement, or an explicit reverse endpoint triple through b is tight. In particular the Hamiltonian-five-set alternative of 65298d96f1b2 cannot occur at such a trapped minimum.

## Body

Apply the endpoint-state trichotomy from deletion01 to the chosen endpoint a of P using the chosen deletion cover of H-a, and likewise to the chosen endpoint c of Q using the chosen deletion cover of H-c.

If either comparison exposes an internal-restoration support crossing or order disagreement, the stated conclusion holds.

Otherwise both comparisons are in the same-slot omission-replacement branch. Since |P|,|Q|>=3, the hypotheses of compatdoubleendpoint43 are satisfied. Hence either an explicit reverse endpoint triple through b is tight, which is one of the stated conclusions, or the corresponding five-set W={a,u,b,c,v} is Hamiltonian.

In the Hamiltonian-five-set branch, 7c2b036e7ecf supplies an explicit two-move pairwise-repartition path from the singleton lift P|Q|{b} to a spanning three-cover with strictly smaller quadratic potential. This contradicts the assumed minimality of P|Q|{b} inside its pairwise-repartition component.

Therefore the Hamiltonian-five-set branch is impossible, and every chosen endpoint pair with arbitrary endpoint-deletion covers exposes either support/order disturbance or an explicit reverse endpoint triple through b.