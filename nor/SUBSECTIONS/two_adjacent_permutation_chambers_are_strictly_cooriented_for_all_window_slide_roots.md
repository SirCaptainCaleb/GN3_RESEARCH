# Two adjacent permutation chambers are strictly cooriented for all window slide roots

## Metadata

- ID: two_adjacent_permutation_chambers_are_strictly_cooriented_for_all_window_slide_roots
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 24
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

For any ordered-window arity r>=2, all actual length-r window-slide roots from two adjacent permutation chambers lie in one strict open halfspace. Using the negative average of the two rank functions, every slide endpoint gap remains at least r-1/2>0. Hence no positive physical-root dependence can be carried by one chamber or one adjacent chamber pair.

Thus a cut-changing wall is a necessary transport event but never by itself the positive-root cancellation. Any genuine carrier obstruction must propagate through larger chamber geometry.

## Development

## Two adjacent permutation chambers are strictly cooriented for all window-slide roots

Let h have ordered-window arity r>=2. Let
[
pi=(v_1,ldots,v_n)
]
and let (pi') be obtained by swapping two adjacent coordinates at ranks j,j+1.

For any permutation order (sigma), an actual consecutive-window slide root has the form
[
ho=e_{sigma_i}-e_{sigma_{i+r}},
qquad 1le ile n-r.
]
Its orientation is always from the dropped earlier coordinate to the entering later coordinate.

### Theorem

The union of all actual window-slide roots from (pi) and (pi') lies in one strict open halfspace of the type-A root space. Hence no positive root dependence can be supported on roots carried only by these two adjacent chambers.

### Proof

Let
[
p(v)=operatorname{pos}_pi(v),
qquad
p'(v)=operatorname{pos}_{pi'}(v),
]
and define the averaged rank
[
ar p(v)=rac{p(v)+p'(v)}2.
]
Use the linear functional
[
Phi(e_v)=-ar p(v)
]
(up to an irrelevant additive constant).

Take a slide root
[
ho=e_{pi_i}-e_{pi_{i+r}}
]
from (pi). In the original order its endpoints are exactly r ranks apart.

Because (pi') differs by one adjacent swap and r>=2, the two endpoints of this slide cannot be exactly the two swapped coordinates. Therefore at most one endpoint changes rank between p and p'. Its averaged rank shifts by at most 1/2. Consequently
[
ar p(pi_{i+r})-ar p(pi_i)ge r-rac12>0.
]
Thus
[
Phi(ho)>0.
]

The identical argument applies to every slide root of (pi').

Hence one functional is strictly positive on every actual window-slide root from both adjacent chambers. Their positive cone is pointed and cannot contain zero. QED.

### Consequences

1. A protected-root Radon zero cannot be carried by a single chamber or by a pair of adjacent chambers.

2. A cut-changing chamber wall, although necessary in any non-common-cut Radon carrier, is never by itself sufficient to support the zero. A minimal positive carrier must continue through at least one more chamber after crossing the wall.

3. Combined with the cut-ejection theorem, the first wall at which a prescribed cycle coordinate leaves the protected cut is a genuine transport event, not a place where the positive dependence can terminate. Any minimal carrier path must propagate the obstruction beyond that wall.

4. In ternary arity this rules out the hope that an isolated fully-curved barrier plus its immediately adjacent chamber already realizes the global protected-root cancellation. The two antipodal-provenance exits must interact through a larger cut-space configuration.

This is a carrier-pruning theorem only; it does not yet determine the sign of the transverse certificate in the next chamber or produce the desired threshold surgery.
