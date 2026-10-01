# Compatible deletion pairs yield endpoint reversal or a mixed five-side

## Statement

Let H be a minimum counterexample, and let F_a,F_b be fully compatible deletion covers at distinct vertices a,b. Let P,Q be their two common ordered support classes on H-{a,b}.

Then the omitted labels cannot insert into different support classes, and they cannot insert into slots of the same class separated by at least two positions, because either situation would give a spanning two-cover of H. Hence the two insertion slots are adjacent or identical.

If the slots are adjacent, there are two spanning three-covers differing by transfer of the unique intervening common vertex. That vertex is a displayed endpoint on opposite sides of the transfer, so singleton-transfer endpointization forces an explicit displayed component-end reversal. If the flanking portions of P have orders l and r, the two covers differ in quadratic potential by 2(l-r).

If the slots are identical, there is a Hamiltonian five-set X containing {a,b} such that X-{a,b} meets both P and Q, and H-X is non-Hamiltonian with path-cover number exactly two. If |P|>=2, at least two such mixed five-sets occur inside one six-vertex window; if |P|=1, at least one occurs.

Consequently every fully compatible deletion pair reduces directly to an explicit endpoint reversal or to a mixed Hamiltonian five-side. If |V(H)|>=18, the latter state has a complementary path of order at least seven and therefore satisfies the five_side_arbitrary_escape01 trichotomy: strict quadratic-potential descent, neutral endpoint/support exchange, or a displayed-edge reversal. This final trichotomy concerns the produced five-side state and does not assert repartition-component reachability from the original deletion covers.

## Body

Use the compatible-pair localization from the defect-span interface. On H-{a,b}, the two covers have common ordered support classes P,Q. Each omitted label is inserted into one common class. If they insert into different classes, the two augmented common classes form a spanning two-cover. If they insert into the same class at slots separated by at least two positions, insert both labels at their respective slots; every consecutive triple is inherited from one deletion cover or the common order, again producing a spanning two-cover. Both cases contradict minimality.

Thus the slots are adjacent or identical.

For adjacent slots, write P=(L,z,R) and
F_b=(L,a,z,R)|Q,   F_a=(L,z,b,R)|Q.
Taking tight prefixes and suffixes gives the spanning three-covers
(L,a)|(z,b,R)|Q
and
(L,a,z)|(b,R)|Q.
The transferred singleton z is terminal in one realization and initial in the other, so singleton_transfer_endpointization01 gives a tight triple reversing a displayed component-end edge. If l=|L| and r=|R|, direct calculation gives
(l+2)^2+(r+1)^2-(l+1)^2-(r+2)^2=2(l-r).

For identical slots, write P=(L,R) and
F_b=(L,a,R)|Q,   F_a=(L,b,R)|Q.
The common class P is nonempty and Q has at least two vertices. If |P|>=2, choose two vertices of P and two of Q; together with a,b they form a six-set to which sixset_prescribed_pair_menu01 applies. At least two deletions among the four sampled support vertices leave Hamiltonian five-sets containing a,b, and every such deletion still meets both P and Q. If |P|=1, sample its unique vertex and three vertices of Q; at least two prescribed-pair Hamiltonian deletions exist, and at most one deletes the P-vertex, so at least one resulting five-set remains mixed across P and Q.

Every resulting X is a proper Hamiltonian support. Its complement has path-cover number at most two by minimum-counterexample calculus and cannot be Hamiltonian, else X together with its complement would two-cover H. Hence pc(H-X)=2.

Finally, if n>=18, a two-cover of H-X has total order n-5>=13, so one path has order at least seven. Applying five_side_arbitrary_escape01 gives the stated three-way escape. This composes the compatible-pair localization, adjacent-slot endpointization, and identical-slot five-side construction into one direct theorem.