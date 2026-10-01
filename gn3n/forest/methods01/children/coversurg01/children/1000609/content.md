# Every 4|4|3 state reaches an equitable 5|5|1 omission state in two moves

## Statement

Let H be an eleven-vertex boundary tournament and let X|P|Q be a spanning 3|4|4 tight-path cover. Then two legal Astra-003 pairwise repartitions transform it into a spanning 5|5|1 cover. More precisely, X|P can always be repartitioned as 5|2, and then the resulting 2-side together with Q can always be repartitioned as 5|1.

## Body

# A universal two-move bridge from 4|4|3 to 5|5|1

Let

X|P|Q

be a spanning three-path cover with

|X|=3,  |P|=|Q|=4.

Choose and fix a tight order on the three-set X. Apply the certified bad-extension-pair theorem to this tight three-path with the four vertices of P as exterior vertices. The bad-pair graph on V(P) is triangle-free. A triangle-free graph on four vertices has at most four edges, while there are six vertex pairs in P. Hence at least two pairs {p,p'} subset V(P) satisfy

H[X union {p,p'}]

Hamiltonian.

Choose one such pair. Let {r,s}=V(P)-{p,p'}. The two-set {r,s} is a tight path. Thus the union X union P has an exact 5|2 cover

R | (r,s),

where R is a Hamilton path on X union {p,p'}. Replacing X|P by this cover is one legal Astra-003 move. The full state is now

R | (r,s) | Q

with component orders 5,2,4.

Now consider the six-set

U={r,s} union V(Q).

By the four-of-six theorem, at least four of the six five-vertex subsets of U are Hamiltonian. Choose any Hamiltonian five-set F subset U and let u be its complementary singleton. Then F|(u) is an exact 5|1 cover of U. Replacing (r,s)|Q by F|(u) is a second legal Astra-003 move.

The resulting spanning state is

R | F | (u),

with component orders 5,5,1.

Therefore every 4|4|3 state lies within Astra distance two of the equitable omission-state surface. In particular, any trapped Astra component containing a 4|4|3 state also contains a 5|5|1 state, so the certified order-eleven omission-graph and deletion-clique machinery applies inside the same connected component.
