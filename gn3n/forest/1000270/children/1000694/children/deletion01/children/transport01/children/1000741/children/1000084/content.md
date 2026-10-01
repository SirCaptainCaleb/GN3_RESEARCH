# Two universal endpoint hooks force a Hamiltonian five-window or an endpoint cross triple

## Statement

Let H be a minimum counterexample and let H-x=P|Q be a deletion two-cover, where P=(p_0,...,p_m) has order at least four (m>=3). Then exactly one of the following orientation alternatives holds:

(1) (p_0,x,p_m) is tight. In this case
(p_1,p_0,x,p_m,p_{m-1})
is a tight Hamilton path on the five-set
W={p_0,p_1,x,p_{m-1},p_m}.
Hence W is proper Hamiltonian and H-W is non-Hamiltonian of path-cover number two.

(2) (p_0,x,p_m) is non-tight. Then boundary antisymmetry forces the tight cross triple
(p_m,x,p_0).

Thus every deletion-cover component of order at least four yields either a canonical Hamiltonian five-window supported on its two displayed end edges and the omitted vertex, or a direct tight cross triple joining its two endpoints through the omitted vertex. The same conclusion holds for Q.

## Body

By c38e8b5c48ee, the two endpoint-hook triples
(p_1,p_0,x)
and
(x,p_m,p_{m-1})
are tight.

Boundary antisymmetry gives exactly one of the reversal pair
(p_0,x,p_m), (p_m,x,p_0)
as tight.

If (p_0,x,p_m) is tight, then because m>=3 the five displayed vertices p_1,p_0,x,p_m,p_{m-1} are distinct, and the three consecutive triples in
(p_1,p_0,x,p_m,p_{m-1})
are precisely
(p_1,p_0,x), (p_0,x,p_m), (x,p_m,p_{m-1}),
all tight. Hence this is a tight Hamilton path on W.

Since a minimum counterexample has order greater than ten, W is proper. If H-W were Hamiltonian, its Hamilton path together with the displayed Hamilton path on W would two-cover H. Therefore H-W is non-Hamiltonian, and mincex01 gives path-cover number two.

If (p_0,x,p_m) is not tight, boundary antisymmetry gives (p_m,x,p_0) tight, which is the stated endpoint cross triple.

The argument for Q is identical.
