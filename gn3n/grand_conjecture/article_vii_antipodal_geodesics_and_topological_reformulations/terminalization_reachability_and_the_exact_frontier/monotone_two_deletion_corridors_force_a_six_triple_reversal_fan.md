# Monotone two-deletion corridors force a six-triple reversal fan

## Composition

(none yet)

## Development

## Three legal corridor cuts amplify the two-deletion reversal constraints

Consider the genuine two-deletion reflected-double residue with corridor displayed as
[
C=(c_1,ldots,c_N),
]
and suppose its positive-word-free status word is the monotone type
[
1^u0^v,qquad u,vge2.
]

For this word,
[
p=u+1,qquad q=u.
]
Hence the exact inversion-window criterion permits all three cuts
[
j=u,qquad u+1,qquad u+2.
]

For each such j define the displayed corridor cover
[
P_j=(c_1,ldots,c_j),qquad
Q_j=(c_N,c_{N-1},ldots,c_{j+1}).
]
Both are tight.

Now assume kappa_2(H[J])=2 for
[
J=Ccup{x,y}.
]
Then for either exterior vertex e in {x,y}, the one-deletion tournament C+e has path-cover number greater than two. Consequently e cannot be appended to either component of **any** of the three displayed covers.

From failure of
[
(P_j,e)mid Q_j
]
we obtain
[
h(c_{j-1},c_j,e)=0
]
and therefore, by boundary antisymmetry,
[
h(e,c_j,c_{j-1})=1.
]
From failure of
[
P_jmid(Q_j,e)
]
we obtain
[
h(c_{j+2},c_{j+1},e)=0
]
and hence
[
h(e,c_{j+1},c_{j+2})=1.
]

Running through j=u,u+1,u+2 gives, for each e in {x,y},
[
egin{aligned}
&h(e,c_u,c_{u-1})=1,\
&h(e,c_{u+1},c_u)=1,\
&h(e,c_{u+2},c_{u+1})=1,
end{aligned}
qquad
egin{aligned}
&h(e,c_{u+1},c_{u+2})=1,\
&h(e,c_{u+2},c_{u+3})=1,\
&h(e,c_{u+3},c_{u+4})=1.
end{aligned}
]
Thus each exterior vertex carries a six-triple reversal fan around the unique 1-to-0 transition. In particular the central pair satisfies both
[
h(e,c_{u+2},c_{u+1})=1
quad	ext{and}quad
h(e,c_{u+1},c_{u+2})=1.
]

This is much stronger than the four exposed-end reversals obtained from one fixed corridor cut.

The exceptional corridor
[
1^u010^v
]
behaves differently: here
[
p=u+1,qquad q=u+2,
]
so the legal cut is unique. No cut-mobility amplification is available.

Hence the genuine two-deletion symmetric zero-root obstruction splits naturally into:

1. a **mobile-cut monotone residue**, carrying the six-triple reversal fan above for both exterior vertices; and
2. a **rigid 010-island residue**, with one canonical cut.

The next finite local analysis should treat these separately.
