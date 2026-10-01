# Minimum counterexamples already satisfy a stronger n-minus-one version of Astra 009

## Statement

Let H be a minimum-order counterexample to the grand two-cover conjecture, with n vertices. Then for every vertex v, H-v has a spanning two-cover. Consequently H contains two vertex-disjoint tight paths whose union has n-1 vertices, with an arbitrarily prescribed omitted vertex v. Thus Astra idea 009 is already true on every minimum counterexample with error 1/n; as a route to the grand theorem, its bare packing conclusion gives no new reduction beyond minimum-counterexample calculus.

## Body

By minimum-counterexample calculus, every proper induced subtournament of H has path-cover number at most two. In particular, for every v in V(H), the induced subtournament H-v has a spanning cover by two tight paths P_v|Q_v. Their supports are disjoint and have union V(H)-{v}, so together they cover exactly n-1 vertices of H.

Hence for every epsilon>0 and every n>1/epsilon, the two paths P_v,Q_v cover more than (1-epsilon)n vertices; moreover the omitted vertex can be prescribed arbitrarily.

Therefore the quantitative packing conclusion sought in Astra 009 is not the missing ingredient in a minimum-counterexample proof. The unresolved step is absorption/reconfiguration of the single omitted vertex while preserving two components. Any strategically stronger asymptotic formulation must encode endpoint flexibility, multiple compatible path orders, or another absorption-ready invariant rather than covered cardinality alone. ∎
