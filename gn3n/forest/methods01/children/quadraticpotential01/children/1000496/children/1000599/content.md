# Both endpoints of an oversized quadratic-minimal component disturb the same complementary pair

## Statement

Let H be a counterexample minimal by order, and let A|B|C be a spanning three-cover that minimizes Phi in a trapped pairwise-repartition component, with |A|=a>=b=|B|>=c=|C| and a>=b+2. For either displayed endpoint x of A, every two-cover F_x of H[V(B) union V(C) union {x}] yields one of two genuine disturbances relative to the fixed cover B|C: either x is internal in F_x and B|C has an ordinary edge crossing the three path supports of F_x-x, or x is an endpoint and the induced two-cover F_x-x differs from B|C, hence exposes a support-partition crossing or relative-order disagreement. In particular the neutral endpoint-attachment branch is impossible at both ends of A, against the same complementary pair B|C.

## Body

Write A=(a_0,...,a_{a-1}) and fix x in {a_0,a_{a-1}}.

Because A-x is a nonempty proper displayed path, minimality of H gives a two-cover of the complementary induced subtournament
K_x=H[V(B) union V(C) union {x}].
Also H[V(B) union V(C)] has no spanning path, since such a path together with A would two-cover H.

Choose any two-cover F_x=R|S of K_x.

First suppose x is internal in its F_x-component. Deleting x splits that component into two nonempty displayed subpaths, while the other F_x-component remains nonempty. Thus F_x-x is a three-path cover of V(B) union V(C). The fixed two-cover B|C cannot have every ordinary edge contained inside one of these three supports: otherwise each connected path B and C would lie inside a single support, so two paths could cover at most two of the three nonempty supports. Hence some ordinary edge of B|C joins two different supports of F_x-x.

Now suppose x is an endpoint of its F_x-component. That component is not the singleton {x}, because otherwise the other component would be a spanning path of H[V(B) union V(C)], contrary to the preceding paragraph. Therefore deleting x gives a two-cover T_x=F_x-x of H[V(B) union V(C)].

If T_x differs from B|C as an ordered two-cover, the certified two-cover disagreement theorem applies: either their support partitions differ, giving an ordinary crossing edge, or the support partitions agree but one common support has relative-order disagreement, yielding a reversed common edge, a reversing triple, or a vertex-simple cycle.

It remains to exclude T_x=B|C up to swapping component names. In that case F_x is obtained by adjoining x to one displayed endpoint of B or C. If x adjoins B, then
(A-x) | (B+x) | C
is a legal pairwise repartition of A|B|C. Its quadratic contribution on the changed pair is
(a-1)^2+(b+1)^2-a^2-b^2 = 2(b-a+1) <= -2,
because a>=b+2. If x adjoins C, the same computation gives
2(c-a+1) <= -2,
because c<=b<=a-2.
Either way Phi strictly decreases inside the same pairwise-repartition component, contradicting the choice of A|B|C.

Thus every complementary cover at either endpoint of A produces genuine crossing or order disturbance relative to the same fixed pair B|C. The argument is independent of the actual component orders.