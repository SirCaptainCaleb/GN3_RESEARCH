# A longest path forces a bi-anchored path-cover obstruction on its exterior

## Statement

Let H be a minimum counterexample and let P=(p_0,...,p_m) be a longest tight path. Put K=V(H)-V(P). Then K is non-Hamiltonian with path-cover number two and |K|>=4. For every y in K, (p_1,p_0,y) and (y,p_m,p_{m-1}) are tight.

More generally, the complement of every nonempty proper contiguous subpath of P is non-Hamiltonian with path-cover number two. In particular
L=K union {p_0,p_1},
R=K union {p_{m-1},p_m},
and, since |P|>=5,
S=K union {p_0,p_1,p_{m-1},p_m}
are non-Hamiltonian with path-cover number two.

No two-cover of L has a component ending with the ordered pair (p_0,p_1), and no two-cover of R has a component beginning with (p_{m-1},p_m). Moreover S has no Hamilton path beginning with (p_1,p_0) and ending with (p_m,p_{m-1}).

## Body

Since P is a proper Hamiltonian support in a minimum counterexample, its complement K is non-Hamiltonian with path-cover number two. Every boundary tournament of order at most three is Hamiltonian, so |K|>=4.

Fix y in K. If (y,p_0,p_1) were tight, then (y,p_0,p_1,...,p_m) would be a tight path longer than P. Hence (y,p_0,p_1) is non-tight, so boundary antisymmetry gives (p_1,p_0,y) tight. Similarly, (p_{m-1},p_m,y) is non-tight by maximality of P, and therefore (y,p_m,p_{m-1}) is tight.

Now let I be any nonempty proper contiguous subpath of P. The inherited order makes I Hamiltonian. If H-I were Hamiltonian, Hamilton paths on I and H-I would form a spanning two-cover of H, impossible. Since H-I is a proper induced subtournament of the minimum counterexample, it has path-cover number at most two; non-Hamiltonicity makes the number exactly two. Taking I to be P, the suffix p_2,...,p_m, the prefix p_0,...,p_{m-2}, and the middle p_2,...,p_{m-2} gives the asserted exact two-cover complements. The middle is nonempty because every minimum counterexample has order greater than ten and a longest path has order at least ceil((n-1)/2)>=5.

Suppose a two-cover of L had a component T ending with (p_0,p_1). Appending the inherited suffix (p_2,...,p_m) to T preserves tightness at the join because (p_0,p_1,p_2) and all later triples belong to P. Together with the other component of the cover of L this gives a spanning two-cover of H, contradiction. The right-anchor statement is symmetric: if a component of a two-cover of R begins with (p_{m-1},p_m), prepend the inherited prefix (p_0,...,p_{m-2}).

Finally, if S had a Hamilton path beginning with (p_1,p_0) and ending with (p_m,p_{m-1}), that path together with the inherited middle path (p_2,...,p_{m-2}) would be a spanning two-cover of H. Thus the two universal reversed endpoint families coexist on one smaller pc2 induced subtournament, but cannot be joined into a reverse-to-reverse Hamilton path.