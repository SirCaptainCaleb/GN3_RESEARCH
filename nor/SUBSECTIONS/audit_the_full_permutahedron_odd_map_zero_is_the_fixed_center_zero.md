# Audit: the full permutahedron odd map zero is the fixed center zero

## Metadata

- ID: audit_the_full_permutahedron_odd_map_zero_is_the_fixed_center_zero
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 18
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Audit: the full-permutahedron odd-map zero is the fixed-center zero

Subsection 14 constructs an odd piecewise-affine descent-root map on the entire centered permutahedron
[
widetilde R:P_V	o W_V
]
and invokes an odd-degree argument to force a zero.

The zero existence is correct, but it does not by itself solve the protected-carrier problem.

### Fixed-point issue

Central inversion on the full permutahedron is not free. The center (0in P_V) is fixed. Therefore every odd map on the whole permutahedral ball satisfies
[
widetilde R(0)=-widetilde R(0),
]
hence
[
widetilde R(0)=0
]
tautologically.

In the specific barycentric extension of subsection 14 this is completely explicit: the barycenter of the top-dimensional face (P_V) is labeled by the average of all permutation-vertex labels. Reversal pairs the permutation vertices and sends every descent-root label to its negative, so that average is exactly zero.

Thus the degree argument is valid but detects the unavoidable fixed-center zero already built into any odd extension on the full ball.

### What remains valid

Expanding the center zero does produce a positive dependence among genuine physical 10-descent roots. Hence the circulation and graphic-cycle conclusions are valid.

However the largest carrier face for this zero may simply be the whole permutahedron, whose unique tied block is all of (V). In that case Coxeter-block localization gives no protected outside order. A support-minimal positive circuit extracted algebraically from the global dependence need not come from a small or boundary-compatible carrier.

### Consequence

The full-permutahedron construction is a useful canonical source of global root relations, but it does not replace the missing free antipodal carrier/extraction theorem.

For topological localization one still needs a domain on which the involution is free, such as the boundary of the switch prism, or an equivalent protected state complex. The cellular Tucker program remains meaningful precisely because the switch-prism boundary has no fixed center.

Any future claim that subsection 14 supplies the previously missing global protected carrier should therefore be weakened to:

> it supplies a canonical global odd root field and a tautological center dependence; compatibility/localization of a zero remains open.

This distinction is especially important for the flat-sector barrier program, where the desired root circuit must retain antipodal provenance and ordered boundary pairs rather than merely exist somewhere in the full permutation set.

## Frontier

- Development version when composed: None
- Development version now: 1
