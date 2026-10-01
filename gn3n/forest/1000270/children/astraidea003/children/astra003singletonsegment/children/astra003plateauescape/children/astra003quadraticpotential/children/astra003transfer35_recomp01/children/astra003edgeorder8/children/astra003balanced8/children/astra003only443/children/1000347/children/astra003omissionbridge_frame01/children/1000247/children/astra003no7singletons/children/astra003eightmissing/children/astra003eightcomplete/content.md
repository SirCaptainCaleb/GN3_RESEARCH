# The eight-label omission graph is complete

## Statement

Let K be a trapped order-eleven Astra-003 component containing a 4|4|3 state, and suppose exactly eight labels occur as singletons of reachable 5|5|1 states. Then the reversible omission-swap graph on those eight labels is complete.

## Body

Let (S) be the eight reachable singleton labels and suppose, for contradiction, that the omission graph has a missing edge (xy).

By astra003eightmissing, in every reachable omission state
[
P|Q|(x)
]
the six labels of (S-{x,y}) are exactly the successful omission-swap labels, three on each five-side, while the four labels
[
E_x=(V(H)-S)cup{y}
]
are exactly the bad labels, split (2+2).

Fix such a state and consider
[
R_P=V(P)cup{x}.
]
Its good deletion set is therefore exactly
[
G(R_P)={x,a,b,c},
]
where (a,b,c) are the three labels of (S-{x,y}) lying on (P).

For each (din G(R_P)), choose a Hamilton path on (R_P-{d}) and combine it with the fixed untouched five-path (Q). The certified support-compatible deletion-clique theorem from the order-eleven stress test says these four exact (5|5) deletion covers are pairwise compatible.

Now take any three labels from
[
{x,a,b,c}.
]
The certified “compatible triangles are cyclic” theorem applies to their three pairwise-compatible deletion covers. Hence the precedence tournament induced on every three-subset of ({x,a,b,c}) is cyclic.

But this is impossible for a tournament on four vertices. Indeed, fix any vertex (v). Among the three edges incident with (v), at least two have the same direction relative to (v). If (v	o r) and (v	o s), or (r	o v) and (s	o v), then the triangle on ({v,r,s}) is transitive, not cyclic.

Thus no tournament on four vertices has all four of its three-subsets cyclic. This contradiction shows that the omission graph has no missing edge.

Therefore, when exactly eight singleton labels are reachable, their reversible omission-swap graph is the complete graph (K_8).
