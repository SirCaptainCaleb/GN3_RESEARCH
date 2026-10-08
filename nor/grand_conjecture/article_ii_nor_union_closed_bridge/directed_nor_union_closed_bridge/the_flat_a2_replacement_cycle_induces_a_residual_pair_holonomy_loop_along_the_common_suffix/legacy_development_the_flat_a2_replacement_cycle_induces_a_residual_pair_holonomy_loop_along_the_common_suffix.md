# The flat A2 replacement cycle induces a residual pair holonomy loop along the common suffix — preserved pre-item development

## The flat A2 replacement cycle induces a residual pair-holonomy loop along the common suffix

Assume the nontrivial same-profile (d=e=2) replacement cycle of §§207–209 occurs in a minimum coboundary-flat ternary counterexample.

Write the three residual coordinates as
[
U={x,y,z},
]
and let the common local deletion carriers be
[
ldots,A,B,z,y,T qquad(	ext{omit }x),
]
[
ldots,A,B,y,x,T qquad(	ext{omit }z),
]
[
ldots,A,B,x,z,T qquad(	ext{omit }y),
]
where
[
T=(t_1,t_2,ldots)=(C,D,E,ldots)
]
is the common suffix, lying in the color-1 phase.

The local identities imply
[
alpha(B,z,y)=alpha(B,y,x)=alpha(B,x,z)=1,
]
so the residual pair relation at pivot (B) is a directed 3-cycle. They also imply
[
alpha(z,y,C)=alpha(y,x,C)=alpha(x,z,C)=1,
]
and
[
alpha(u,C,D)=1
qquad(uin U).
]

For each residual vertex (uin U), define the suffix scan
[
s_u(j)=alpha(u,t_j,t_{j+1}).
]

### Endpoint values

At the front,
[
s_x(1)=s_y(1)=s_z(1)=1.
]

At the rear, each (u) is the omitted vertex of one of the three one-change deletion carriers above. Appending (u) to that carrier adds one window after a final color-1 run. Since the full instance is a counterexample, that appended window must have color (0). By cyclic invariance,
[
s_u(	ext{last})=0.
]
Hence all three scans also agree at the rear.

### Flat transport identity

For distinct (u,vin U), apply zero tetrahedral coboundary to
[
{u,v,t_j,t_{j+1}}.
]
With compatible ordered-face conventions the four-face XOR identity gives
[
oxed{
s_u(j)oplus s_v(j)
=
alpha(u,v,t_j)oplusalpha(u,v,t_{j+1}).
}
	ag{1}
]

Thus the difference between the two vertex scans across the edge
[
(t_j,t_{j+1})
]
is exactly the indicator that the ordered residual pair ((u,v)) changes color when the pivot moves from (t_j) to (t_{j+1}).

Equivalently, the tournament on (U) defined by
[
u	o_j v
quadLongleftrightarrowquad
alpha(u,v,t_j)=1
]
evolves along the suffix by toggling precisely those residual edges whose endpoint scans disagree.

### Holonomy consequence

At (t_1=C), the tournament on (U) is the directed cycle
[
x	o z	o y	o x.
]

Because all three scans agree again at the rear, every pairwise scan difference is zero there. Iterating (1) shows that the rear tournament is again the same directed 3-cycle.

Therefore the last recurrent flat replacement obstruction carries a genuine **pair-holonomy loop** along the common suffix:
[
	ext{directed 3-cycle}
longrightarrow
	ext{possibly other tournaments}
longrightarrow
	ext{the same directed 3-cycle}.
]

### Closure target

If the tournament never changes, all three scans are identical throughout the suffix; then one common (1	o0) scan transition controls all three residual vertices simultaneously.

If it changes, let (j) be the first excursion index and (k>j) the first return to the original 3-cycle. The interval
[
t_j,ldots,t_k
]
is a full-support, suffix-preserving holonomy packet. The next target is to use the first excursion/return to construct either:
1. a spanning one-change weave retaining every outside suffix vertex; or
2. a protected replacement escaping the (A_2) cycle.

This formulation preserves the whole ambient ground set and avoids the invalid tail-truncation arguments from Article I.
