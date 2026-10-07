# A fully curved cross tetrahedron closes a maximal monochromatic tail

## Metadata

- ID: a_fully_curved_cross_tetrahedron_closes_a_maximal_monochromatic_tail
- Parent Section: directed_nor_union_closed_bridge
- Position: 80
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development


## A fully curved cross tetrahedron closes a maximal monochromatic tail

Work first in the pure-orientation sector h=alpha, with alpha alternating.

Let

P=(f_1,f_2,f_3,...,f_m)

be a sigma-monochromatic path, so every consecutive alpha-status on P equals sigma. Let a,b lie outside P.

### Proposition
If the tetrahedron

Q={a,b,f_1,f_2}

is fully curved, then P union {a,b} has a one-change spanning order on its support.

### Proof
Use the unique-predecessor property of a fully curved tetrahedron with prescribed exit.

Take the ordered pair (c,d)=(f_1,f_2) and exterior continuation vertex v=f_3. Since

alpha(f_1,f_2,f_3)=sigma,

exactly one ordering of {a,b}, say (a,b), satisfies

alpha(b,f_1,f_2)=sigma.

Full curvature then forces

alpha(a,b,f_1)=1-sigma.

Therefore

(a,b,f_1,f_2,f_3,...,f_m)

has status word

(1-sigma), sigma, sigma, ... , sigma,

with exactly one change. QED.

The short-tail cases are immediate separately.

### Counterexample consequence

Let P be an inclusion-maximal monochromatic path in a pure-orientation counterexample, with omitted set X and exposed front pair F={f_1,f_2}.

Then for every distinct a,b in X, the cross tetrahedron

{a,b,f_1,f_2}

is not fully curved.

Hence every such cross tetrahedron is either flat or singly curved.

This is a significant simplification because on these cross tetrahedra there is no invisible even-curvature branch: their entire nonflatness is detected by the coboundary bit kappa=delta f.

### Cross-curvature interpretation

Maximality gives

alpha(x,f_1,f_2)=1-sigma

for every x in X.

Thus in the four-face parity for {a,b,f_1,f_2}, the two faces containing the front edge have equal alpha-sign and cancel mod 2. Consequently the cross curvature is controlled by the disagreement between the two remaining faces, equivalently by the disagreement between the pair relation of a,b as seen from the two front coordinates.

So over a maximal monochromatic tail, the omitted-pair obstruction becomes a graph of singly-curved cross tetrahedra with no fully-curved edges. This is a much cleaner setting for a Connector argument than the unrestricted tetrahedral curvature complex.


## Frontier

- Development version when composed: None
- Development version now: 1
