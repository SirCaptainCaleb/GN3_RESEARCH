# A missing edge in the eight-label omission graph recreates a four-bad-label equality shell

## Statement

Let K be a trapped order-eleven Astra-003 component containing a 4|4|3 state, and suppose exactly eight labels occur as singletons of reachable 5|5|1 states. Let G be the graph on these eight labels joining two labels when they are related by a reversible omission swap. Then delta(G)>=6, so the complement is a matching. If xy is a missing edge, then in every reachable omission state P|Q|(x), the six labels S-{x,y} are exactly the six good omission-swap labels, three on each side, while the four labels T union {y}, where T=V(H)-S, are exactly the four bad labels and split two plus two across P,Q.

## Body


Let (S) be the eight labels occurring as singletons in reachable (5|5|1) states of a trapped order-eleven Astra component, and put
[
T=V(H)-S,qquad |T|=3.
]
Let (G) be the reversible omission-swap graph on (S).

The certified order-eleven omission theorem gives at least six distinct omission-swap neighbors from every (5|5|1) state. Since no label of (T) ever occurs as a singleton, every such neighbor lies in (S). Hence
[
delta(G)ge6.
]
On eight vertices, the complement of (G) has maximum degree at most one, so it is a matching.

Assume (xy) is a missing edge of (G). Fix any reachable omission state
[
P|Q|(x).
]
No (T)-label is a successful omission swap by definition of (T), and (y) is not a successful omission swap from any (x)-state because (xy
otin E(G)). Thus the only possible successful labels are the six vertices of
[
S-{x,y}.
]

The omission theorem supplies at least three successful labels on (P) and at least three on (Q). Since there are exactly six possible successful labels total and (P,Q) are disjoint, each side contains exactly three of them and all six are successful. The remaining two vertices on each five-side come from the four-label set
[
E_x:=Tcup{y}.
]
Consequently
[
|Pcap E_x|=|Qcap E_x|=2.
]

Now consider the six-set (Pcup{x}). Deleting any of the three (S-{x,y}) labels lying on (P) gives a Hamiltonian five-set, because the corresponding omission swap is legal; deleting (x) leaves the Hamiltonian five-set (P). Thus these four deletions are good.

Deleting either vertex of (Pcap E_x) cannot be Hamiltonian: if it were, that label would be a legal omission-swap singleton reachable from the current state, contradicting either membership in (T) or the missing edge (xy). Therefore these two labels are precisely the two bad five-deletions of (Pcup{x}). The same holds on the (Q)-side.

Hence a missing edge (xy) forces every (x)-omission state into the same exact four-bad-label geometry as the former seven-label equality shell, with (E_x=Tcup{y}) playing the role of the excluded four-set.
