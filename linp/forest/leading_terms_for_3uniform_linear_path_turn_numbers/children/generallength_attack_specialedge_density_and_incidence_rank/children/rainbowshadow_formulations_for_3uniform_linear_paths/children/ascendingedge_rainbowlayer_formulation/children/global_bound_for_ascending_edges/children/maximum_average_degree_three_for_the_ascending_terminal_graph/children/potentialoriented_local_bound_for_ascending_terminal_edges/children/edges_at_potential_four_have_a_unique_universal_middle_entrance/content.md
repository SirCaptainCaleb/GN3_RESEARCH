# Rank-three charged edges at potential four have a unique universal middle entrance

## Statement

Let v satisfy phi(v)=4. Among potential-charged ascending nonspecial edges e={x,v,u} with v terminal and phi(u)>=4, at most one can have edge rank 3. Moreover, if such an edge exists, then for every maximum four-edge path P=(g_1,g_2,g_3,g_4) ending at v, its unique entrance is x=g_2∩g_3.

## Body

Let e={x,v,u} be a charged ascending nonspecial edge of rank q=3. Then phi(x)=2.

Fix an arbitrary maximum four-edge path P=(g_1,g_2,g_3,g_4) ending at v. Thus v is private to g_4. Since phi(e)=3, e is not g_4.

Apply the certified terminal cumulative argument 0e550ff0eadd to e with q=3. Its latest non-v contact with P lies in the final q-2=1 precursor edge g_3, and it lies outside g_4. Equivalently, at least one of x,u lies in g_3\g_4.

We first show that x cannot be absent from P. If x is absent, charged transversality forces u∈P, and the latest-contact conclusion gives u∈g_3\g_4.

There are two possibilities.

If u is the private vertex of g_3, then e meets g_1,g_2,g_3 only at u in g_3: x is absent and v occurs only in g_4. Hence
g_1,g_2,g_3,e
is a four-edge linear path ending in e, contradicting phi(e)=3.

If u=g_2∩g_3, then
g_1,g_2,e
is a three-edge linear path ending in e through u. Since phi(e)=3 and e is nonspecial with unique longest-path entrance x!=u, this is impossible.

Thus x lies on P.

Now use the certified half-path endpoint-potential lemma on the four-edge path P. A private vertex of g_i has endpoint potential at least max{i,5-i}, and the joint g_i∩g_{i+1} has potential at least max{i,4-i}. Every position of P therefore has potential at least 3 except the middle joint g_2∩g_3, whose lower bound is 2. Since phi(x)=2, necessarily
x=g_2∩g_3.

The choice of P was arbitrary, so this pinning holds on every maximum four-edge path ending at v.

Finally, two distinct rank-3 charged edges through v cannot both exist: the argument would give them the same entrance x=g_2∩g_3, so both hyperedges would contain the pair {v,x}, contradicting linearity.

Hence at most one charged rank-3 edge exists at a potential-four terminal, and its entrance is universally the middle joint of every maximum v-ending four-edge path.