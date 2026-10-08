# Theta honest lifted circuits strictly shorten by a branch bypass

## Composition

(none yet)

## Development

## Theta lifted circuits shorten by an honest branch bypass

Work in a full-support connected support-minimal honest lifted zero whose physical support is a theta graph.

By the cycle-rank theorem, after orienting the branch vertices suitably the physical support has three internally disjoint directed paths
[
P:u	o v,qquad Q:v	o u,qquad R:v	o u.
]

The two directed simple cycles are
[
C_Q=Pcup Q,qquad C_R=Pcup R.
]

Write their nonzero side imbalances as
[
A=S(P)+S(Q)>0,qquad B=S(P)+S(R)<0,
]
after swapping Q,R if necessary.

Because the support is connected and every support root is weakly forward in the carrier block order, positive circulation forces every support root to be block-neutral. Hence all physical coordinates lie in one tied carrier block. Since the support is full, this is the top permutahedron block. We may therefore realize arbitrary local coordinate windows inside the same product carrier cell.

### Honest bypass labels at the branch

Let
[
e=p	o v
]
be the last edge of P. Let
[
f=v	o q,qquad g=v	o r
]
be the first edges of Q and R.

Arrange the three coordinates (p,v,q) consecutively in a chamber of the same top carrier. Because the two threshold sides have complementary target colors, place this window on whichever side makes its actual ternary color violating. The honest selector may be chosen to select this window at that state, with the reversal-mate choice imposed equivariantly.

Thus we obtain a genuine honest lifted bypass label
[
widehatsigma_Q=(e_p-e_q,t_Q),qquad t_Qin{pm1}.
]

Similarly we obtain
[
widehatsigma_R=(e_p-e_r,t_R).
]

Let the side signs of e,f,g be s_e,s_f,s_g.

### Q-bypass

Replace the two-edge path
[
p	o v	o q
]
inside C_Q by the bypass p->q.

The resulting directed cycle D_Q uses P with its last edge removed, then the bypass, then Q with its first edge removed.

Its side imbalance is
[
S(D_Q)
=A+delta_Q,
qquad
delta_Q=t_Q-s_e-s_f.
]

Since all three entries are signs,
[
delta_Qin{-3,-1,1,3}.
]

The cycle C_R is unchanged and still has imbalance B<0.

If A+delta_Q=0, D_Q is a side-balanced simple physical cycle, already removable by the one-cycle parity-transversality theorem.

If A+delta_Q>0, then D_Q and C_R have opposite nonzero side imbalance. Their union carries a positive honest lifted dependence. Geometrically it is again a theta graph, but the common directed path is
[
P^- = Psetminus{e},
]
one edge shorter than P.

Therefore the Q-bypass fails to give either immediate balanced-cycle removal or strict theta shortening only if
[
A+delta_Q<0.
]

Because A is a positive integer and delta_Q is one of -3,-1,1,3, this can happen only when
[
delta_Q=-3
quad	ext{and}quad
Ain{1,2}.
]

In particular Q-failure forces
[
s_e=+1,
]
since delta_Q=-3 requires t_Q=-1 and s_e=s_f=+1.

### R-bypass

Symmetrically, replacing p->v->r by p->r changes the R-cycle imbalance to
[
S(D_R)=B+delta_R,
qquad
delta_R=t_R-s_e-s_gin{-3,-1,1,3}.
]

The Q-cycle remains of positive imbalance A.

This branch is successful if:
- B+delta_R=0, giving a balanced removable cycle; or
- B+delta_R<0, giving a theta with common path P^- one edge shorter.

So R fails only if
[
B+delta_R>0.
]

Since B is a negative integer, this requires
[
delta_R=+3
quad	ext{and}quad
Bin{-1,-2}.
]

In particular R-failure forces
[
s_e=-1,
]
because delta_R=+3 requires t_R=+1 and s_e=s_g=-1.

### Theta-shortening theorem

The two bypass branches cannot both fail: Q-failure forces s_e=+1, while R-failure forces s_e=-1.

Hence at least one honest branch bypass yields either:

1. a side-balanced simple cycle, removable by the one-cycle theorem; or
2. a new positive honest lifted theta dependence on the same physical vertex set whose common path has length one less.

Taking a support-minimal positive subdependence of the new relation can only simplify further; if it is one-cycle or disconnected it falls into already removable cases, while any connected theta residue has no longer common path than P^-.

Therefore repeated bypassing is a strict finite descent in the length of the common theta path.

When P has length one, P^- is trivial: the two surviving cycles meet only at u. Thus the terminal connected bicyclic shape is a figure-eight.

### Consequence

Theta supports are not terminal honest-lift obstructions.

After:
- balanced one-cycle removal;
- disjoint two-cycle transverse removal;
- theta common-path shortening,

the only remaining full-support dimension-saturated honest lifted circuit shape is a directed figure-eight: two oppositely side-imbalanced directed cycles meeting in exactly one physical vertex.

This conclusion is now valid despite the intersection-count audit: theta is eliminated by a strict bypass descent, not by an incorrect dimension count.
