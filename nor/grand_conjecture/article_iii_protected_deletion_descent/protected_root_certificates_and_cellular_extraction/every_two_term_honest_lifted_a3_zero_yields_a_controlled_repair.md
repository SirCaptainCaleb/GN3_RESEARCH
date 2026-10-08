# Every two-term honest lifted A3 zero yields a controlled repair

## Composition

(none yet)

## Development

Work in the coboundary-flat alternating ternary sector and in one exact A3 Coxeter block B={a,b,c,d}, with a fixed switch between the two internal ternary-window ranks. Consider a two-term positive zero of the honest switch-prism lifted labels:
(rho,+1)+(-rho,-1)=0.

Let rho=e_a-e_d. A pre-switch violating window with this root has the form (a,m,d), while a post-switch violating window with opposite root has the form (d,m',a).

If m=m', the two windows have the same physical middle coordinate on opposite sides of the switch. This is exactly a complementary signed-middle pair, so the cellular Tucker repair theorem applies.

Assume the middles differ. Rename them b and c. Then the two violating triples are
(a,b,d) on the pre-switch side
and
(d,c,a) on the post-switch side.
Let the pre-switch target be eta, so the post-switch target is 1-eta. Violation gives
alpha(a,b,d)=1-eta,
alpha(d,c,a)=eta.
By alternation, alpha(d,c,a)=1-alpha(a,c,d), hence
alpha(a,c,d)=1-eta.

Put
A=alpha(a,b,c),
D=alpha(b,c,d).
Coboundary flatness on the four-set {a,b,c,d} gives
A xor alpha(a,b,d) xor alpha(a,c,d) xor D=0.
The two middle terms are equal, so
A=D.

There are two cases.

Case 1: A=D=eta.
Start from the chamber whose pre-switch violating internal window is (a,b,d), namely the block order
a,b,d,c.
Swap the adjacent pair d,c to obtain
a,b,c,d.
The b-centered pre-switch window changes from (a,b,d), of color 1-eta, to (a,b,c), of color eta. Thus the tracked b-centered violation becomes satisfied on the same threshold side. This is an immediate-neighbor replacement event of the arbitrary-cell extraction theorem, hence gives either strict threshold-energy improvement or the controlled one-slot outward equality transport.

Case 2: A=D=1-eta.
Use the post-switch witness chamber
b,d,c,a,
whose c-centered post-switch window (d,c,a) has color eta and is therefore violating. Swap the adjacent pair b,d to obtain
d,b,c,a.
The c-centered post-switch window changes to (b,c,a). By cyclic invariance,
alpha(b,c,a)=alpha(a,b,c)=1-eta,
which is exactly the post-switch target. Again the tracked violation becomes satisfied by an immediate-neighbor replacement event, with the same strict-improvement/equality-transport dichotomy.

Therefore every two-term honest lifted zero contained in one ternary A3 block yields a controlled local repair event. The same-middle subcase is a complementary Tucker pair; the different-middle subcase is forced by flatness into one of the two explicit neighbor-replacement repairs above.

Consequently a support-minimal lifted A3 obstruction that is terminal under the controlled local repair dynamics cannot be a two-term root reversal pair. The remaining A3 possibilities, if any, must use a genuinely multi-edge side-balanced circulation.
