# A protected-shortcut-free pair is a tournament switching split

## Metadata

- ID: a_protected_shortcut_free_pair_is_a_tournament_switching_split
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 332
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## A protected-shortcut-free pair is a tournament switching split

Use the valid tournament representation from §328/§329:
alpha(a,b,c)=t(a,b) xor t(b,c) xor t(c,a),
with switching preserving alpha.

Fix a pair x,z with no protected x->z shortcut. By §330 its nonconstant signature
d(u)=alpha(x,z,u)
splits W=V\{x,z} into nonempty shores
A=d^{-1}(0), B=d^{-1}(1),
and every u in A, v in B satisfies the universal flat-connector identities.

Let c=t(x,z). For each u in W put a_u=t(x,u).
Switch the tournament by the vertex bits
s_x=0,
s_z=c,
s_u=a_u for u in W.

Then:

1. x becomes a sink:
t'(x,u)=t(x,u) xor s_u=0
for every u in W, and
t'(x,z)=c xor s_z=0.

2. The z-shore relation is determined by d. Since
d(u)=1 xor c xor t(x,u) xor t(z,u),
one gets
t'(z,u)=1 xor d(u).
Hence
- z -> u for u in A;
- u -> z for u in B.

3. Cross-shore edges are uniform. For u in A and v in B, the flat universal-connector identity gives
alpha(x,u,v)=1.
Substituting the tournament formula and the chosen switching bits yields
t'(u,v)=0.
Thus every v in B points to every u in A.

Consequently the switched tournament has the strict block dominance pattern
B -> z -> A -> x,
and all B-to-A edges also point forward.

The induced tournaments inside A and B remain arbitrary.

Thus absence of a protected shortcut is not merely a local flatness condition. It is a genuine switching decomposition with two proper shores and two singleton separators.

### Strategic consequence

The coboundary-flat ternary problem admits a structural dichotomy around every ordered pair x,z:

- either a fully-curved four-set realizes the protected shortcut x->z;
- or the tournament switching class splits as B -> z -> A -> x.

This suggests a recursive proof architecture: decompose along switching splits whenever they exist; the irreducible switching-prime case has protected shortcut cells for every ordered pair and should be attacked by the common-A3 exchange machinery.

The remaining composition theorem must preserve the one-change status condition when good solutions on A and B are assembled across the split.

## Frontier

- Development version when composed: None
- Development version now: 1
