# Absence of a protected shortcut forces a universal two-shore connector

## Composition

(none yet)

## Development

## Absence of a protected shortcut forces a universal two-shore connector

Fix distinct x,z and define the pair signature
d(u)=alpha(x,z,u)
on V\{x,z}.

Assume d is nonconstant; otherwise x,z are clones and the minimum-counterexample clone contraction closes NOR.

Put
A={u:d(u)=0},
B={u:d(u)=1}.
Both shores are nonempty.

Suppose there is no fully-curved four-coordinate carrier of the protected root x->z.

Take any u in A and v in B. Flatness gives
alpha(x,u,v) xor alpha(z,u,v)=d(u) xor d(v)=1,
so (x,u,v,z) is a transition carrier of x->z.

Since by hypothesis it is not fully curved, it is flat. For a flat transition the face values are forced:
alpha(x,u,v)=d(v)=1,
alpha(z,u,v)=d(u)=0
after the chosen normalization d(u)=0,d(v)=1.

The pair itself gives
alpha(u,x,z)=alpha(x,z,u)=d(u)=0
by cyclic invariance, and
alpha(x,z,v)=d(v)=1.

Therefore for EVERY u in A and v in B,
alpha(u,x,z)=0,
alpha(x,z,v)=1.

Equivalently every order fragment
u,x,z,v
has the exact central threshold word
0,1.

Reversing the pair gives the complementary universal connector:
u,z,x,v
has central word
1,0.

Thus failure of a protected x->z shortcut does not leave an arbitrary flat family. It produces a canonical bipartition
V\{x,z}=A disjoint union B
for which the ordered pair x,z is a universal 0-to-1 connector from A to B, independent of the chosen boundary vertices.

This isolates the remaining compatibility issue to the two shores themselves: choose good shore orders whose terminal/initial phases match the universal connector. The pair x,z contributes no further boundary uncertainty at the central junction.

This is the natural reversible connector structure suggested by the Hartman-style least-unreachable program.
