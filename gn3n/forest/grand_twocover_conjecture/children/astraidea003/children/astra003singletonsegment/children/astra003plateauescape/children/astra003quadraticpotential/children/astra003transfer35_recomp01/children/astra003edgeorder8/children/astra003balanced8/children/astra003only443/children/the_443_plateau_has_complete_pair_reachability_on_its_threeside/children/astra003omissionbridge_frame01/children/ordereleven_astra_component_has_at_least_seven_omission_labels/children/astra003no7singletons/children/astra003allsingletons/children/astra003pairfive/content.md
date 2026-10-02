# Every vertex pair cohabits a reachable Hamiltonian five-side at order eleven

## Statement

Let K be a trapped order-eleven Astra-003 component containing a 4|4|3 state. For every pair of vertices {a,b}, K contains a reachable 5|5|1 state P|Q|(x) in which a and b lie together on one Hamiltonian five-side.

## Body


Fix a pair {a,b}. By 71c87221f4e3, the 4|4|3 surface in K has complete pair reachability on its three-side. Hence K contains a state

X|P|Q

with |X|=3, |P|=|Q|=4, and {a,b} subseteq X.

Apply the first move of bc22bd77b944 to the pair X|P. The bad-extension-pair theorem guarantees a pair {p,p'} subseteq P such that

R=X union {p,p'}

is Hamiltonian. The complementary two-set P-{p,p'} is automatically a tight path. Thus one legal Astra repartition replaces X|P by

R | (P-{p,p'}),

and the pair {a,b} remains together inside the Hamiltonian five-set R.

Now apply the second move of bc22bd77b944 to the residual two-side together with Q. Four-of-six supplies a 5|1 repartition of that six-set. This move leaves R untouched and produces a spanning state

R|F|(x)

of type 5|5|1.

Therefore K contains a reachable omission state with {a,b} together on the Hamiltonian five-side R. Since the pair was arbitrary, every vertex pair cohabits some reachable Hamiltonian five-side.
