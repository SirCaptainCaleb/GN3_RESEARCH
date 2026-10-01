# Two barrier-free large-gap neighbors create a Hamiltonian three-vertex enlargement

## Statement

In the setting of f7b6b85feaa3, let X,Y,Z be the three blocks of a Phi-minimal trapped relocation state, with |X| at least |Y|+2 and at least |Z|+2, and |Y|,|Z| at least two. If neither unordered pair {X,Y} nor {X,Z} has a double-non-tight ordered interface, then X together with three endpoint vertices from Y and Z is Hamiltonian. More precisely, writing Y=(y_1,...,y_q), Z=(z_1,...,z_r), both (X,y_1),(y_q,X),(X,z_1),(z_r,X) are tight, and H[V(X) union {y_1,z_1,y_q}] is Hamiltonian (symmetrically one may use z_r instead of y_q). Its complement is covered by the inherited paths Y-{y_1,y_q} and Z-z_1, omitting empty remnants.

## Body

Apply f7b6b85feaa3 to X,Y and X,Z. Under the stated absence of barriers, y_1 and z_1 extend the same terminal end of X, while y_q and z_r extend the initial end. The certified three-extender Hamiltonization lemma e425e6ca5fe0 applied to the tight path X, with the two same-end extenders y_1,z_1 and the opposite-end extender y_q, shows that V(X) union {y_1,z_1,y_q} is Hamiltonian. Removing those vertices from H leaves the inherited interior path (y_2,...,y_{q-1}) when nonempty and the inherited suffix (z_2,...,z_r) when nonempty. Hence the complement has path-cover number at most two, with the displayed inherited cover.
