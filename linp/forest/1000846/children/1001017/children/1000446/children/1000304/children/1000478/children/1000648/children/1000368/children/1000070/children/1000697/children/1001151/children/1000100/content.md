# The rank-three entrance is universal across maximum paths in the first p=4 obstruction

## Statement

Assume phi(v)=4 and there are four potential-charged ascending nonspecial edges through v with ranks (3,4,4,4). Let e={x,v,u} be the unique rank-3 edge. Then for every maximum four-edge path P=(g_1,g_2,g_3,g_4) ending at v, one has x=g_2∩g_3. In particular phi(x)=2, and for each of the three rank-4 charged edges f there is a longest four-edge path ending in f with last vertex v whose middle joint is x.

## Body

The proof of fc5f50164b35 used only that P is a maximum four-edge path ending at v, together with the existence of the rank-3 potential-charged edge e and the path-relative witness lemma. It did not use any special property of the chosen last edge g_4. Therefore the same argument applies to every maximum four-edge path ending at v: the only possible witness position for e is g_2∩g_3, and that witness must be the entrance x. Hence x=g_2∩g_3 universally and phi(x)=2.

Now let f be any of the three rank-4 charged edges. Since v is a terminal snake vertex of f and phi(f)=4, there exists a longest four-edge path ending in f with physical last vertex v. Applying the universal conclusion to that path shows that its middle joint is again x.

Thus a hypothetical (3,4,4,4) counterexample forces all three rank-4 longest-path states at v to pass through the same low-potential vertex x exactly as their central joint.
