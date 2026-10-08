# Complementary signed-middle Tucker edges are switch-crossing endpoint repairs — preserved pre-item development

## Composition

(none yet)

## Development

## Complementary signed-middle edges are switch-crossing endpoint repairs

This is a local theorem/bridge for the proposed signed-middle Tucker program. It does not by itself prove that the Tucker labeling extends admissibly to the whole triangulation.

Work in ternary arity. A switch state is a coordinate order pi together with a cut k between window positions k and k+1. Prescribe target color eta on windows i<=k and 1-eta on windows i>k. Assume the state is bad and label it by +b or -b, where b is the middle coordinate of a selected nearest violating window; the sign records whether that violating window lies before or after the cut.

### 1. A complementary edge cannot be vertical
Fix pi and compare consecutive cuts k and k+1. Only window k+1 changes its prescribed target color. Every physical coordinate b is the middle coordinate of at most one ternary window of pi. If the selected violating window with middle b is unchanged, its side relative to the cut cannot change sign across a single vertical move unless it is exactly window k+1; but that window's target color flips, so a violation at k becomes satisfied at k+1. Therefore adjacent vertical switch states cannot carry complementary labels +b,-b.

Hence any Tucker complementary edge must project to a genuine permutation adjacency.

### 2. A horizontal complementary edge must move b across the cut
Let pi' be obtained from pi by one adjacent transposition, with the cut fixed. Suppose the two endpoints are labeled +b and -b. If the transposition does not move b, then the window index having b as middle is unchanged, so its side of the cut cannot reverse. Thus b itself is one of the swapped coordinates.

Write the relevant local order before the swap as
...,a,b,c,d,...
and after swapping b,c as
...,a,c,b,d,....
Before the swap, the unique window centered at b is (a,b,c), at index p-1. After the swap, the unique window centered at b is (c,b,d), at index p. For its side sign to reverse, the cut must be exactly k=p-1. Thus the complementary edge literally moves the middle coordinate b across the proposed switch.

### 3. In the pure alternating sector the complementary edge is an endpoint repair
Now assume h=alpha is an alternating triangle orientation. Let the target color before the cut be eta. Since (a,b,c) is a violating pre-switch window,
alpha(a,b,c)=1-eta.
Since (c,b,d) is a violating post-switch window, whose target is 1-eta,
alpha(c,b,d)=eta.
Alternation gives
alpha(a,c,b)=1-alpha(a,b,c)=eta.
Therefore after the adjacent transposition b,c the two local consecutive statuses are
alpha(a,c,b)=eta,
alpha(c,b,d)=eta.
So the swap removes the local transition across the cut.

Equivalently, any signed-middle Tucker complementary edge in the pure-orientation sector is exactly a switch-crossing adjacent-swap repair of the kind studied in the flat-sector transport graph.

### Significance
This links the two strongest current programs:
- the general switch-prism / Tucker carrier is supposed to force a complementary edge;
- in ternary pure orientation, any such edge automatically extracts a concrete local repair move.

The remaining topological obligation is now sharper: construct an antipodal triangulation/labeling for which Tucker applies and whose complementary edge is an actual switch-state adjacency. The remaining flat-sector obligation is to show that repeated complementary/repair moves cannot stay forever in a closed equality component.

This theorem also explains why the middle-coordinate label is preferable to a root-only label: the sign change remembers which side of the switch the same physical memory coordinate occupies, and that forces an actual cut-crossing surgery rather than a tautological root circulation.
