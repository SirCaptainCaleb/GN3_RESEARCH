# Singleton traps orient non full repairs in a four change cycle — preserved pre-item development

## Development

## Singleton traps orient non-full repairs in a four-change cycle

Let (C) be a minimum-variation cyclic order in a pure alternating ternary counterexample, with
[
q(C)=4.
]
Let (d_i=c_ioplus c_{i+1}) be its transition bits.

Suppose (d_i=1) is carried by a non-fully-curved tetrahedron and the last-pair endpoint repair is available. By the monotonic endpoint-repair theorem, the repair lowers (q) by two exactly when the old far-side packet
[
(c_{i+2},c_{i+3},c_{i+4})
]
has variation two, i.e.
[
c_{i+2}=c_{i+4}
e c_{i+3}.
]
Equivalently,
[
d_{i+2}=d_{i+3}=1.
]

Thus:

### Singleton-trap lemma

In a minimum four-change counterexample, a non-full transition admitting a rightward endpoint repair cannot lie two transition slots before a singleton color run.

By reversal, a non-full transition admitting a leftward endpoint repair cannot lie two transition slots after a singleton color run.

### Canonical (1,p,q,2) consequence

Consider a four-change cyclic word with run lengths
[
1,p,q,2
]
in cyclic order. Let (T) be the transition entering the final length-two run from the preceding run.

The two transitions after (T) are exactly the transition exiting the length-two run and the transition exiting the following singleton run. Hence they are adjacent:
[
d_{i+2}=d_{i+3}=1.
]

Therefore (T) cannot admit a rightward repair.

So (T) has only two possibilities:

1. its tetrahedron is fully curved; or
2. it is non-full, in which case the right repair fails and the left repair must succeed.

Write the four face colors at (T) in local order as
[
x=alpha(a,b,c),quad
u=alpha(a,b,d),quad
w=alpha(a,c,d),quad
y=alpha(b,c,d)=1-x.
]
Right repair would require (u=x); left repair requires (w=y). In the non-full counterexample case,
[
u=y,qquad w=y,
]
so the face pattern is
[
(x,y,y,y).
]
Hence (T) is singly curved with a specified directional (3)-(1) pattern.

### Interpretation

At the distinguished corner where the length-two run points toward the singleton run, the canonical four-change carrier has a forced curvature alternative:

[
oxed{	ext{fully curved universal switch}}
quad	ext{or}quad
oxed{	ext{directional singly-curved switch pointing away from the singleton}}.
]

This converts the global run profile into a local tetrahedral curvature constraint and gives the simplex-connector program a distinguished packet to attack.
