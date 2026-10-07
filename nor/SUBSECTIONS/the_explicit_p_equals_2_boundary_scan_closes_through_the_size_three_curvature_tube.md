# The explicit p equals 2 boundary scan closes through the size three curvature tube

## Metadata

- ID: the_explicit_p_equals_2_boundary_scan_closes_through_the_size_three_curvature_tube
- Parent Section: ternary_protected_bridges_and_scan_obstructions
- Position: 11
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## The explicit p=2 boundary scan closes through the size-three curvature tube

Continue the coboundary-flat alternating ternary sector. Suppose a blocked one-change deletion carrier has
[
O_0=(a,b,c,d,ldots)
]
with word
[
0^2 1^q
]
and omitted coordinate (x).

By the short-phase theorem, the only surviving insertion scan is
[
s=11,0,0cdots0.
]
Thus
[
alpha(x,a,b)=1,qquad
alpha(x,b,c)=1,qquad
alpha(x,c,d)=0,
]
and every later scan value is (0).

### First same-profile exchange

Form
[
O_1=(b,x,c,d,ldots),
]
omitting (a).

Its first two statuses are
[
alpha(b,x,c)=1-alpha(x,b,c)=0,
]
and
[
alpha(x,c,d)=0.
]
Every later status is the untouched old (1)-tail. Therefore (O_1) again has word
[
0^2 1^q.
]

Since the ambient instance is a counterexample, the omitted coordinate (a) blocks every insertion into (O_1). Applying the already-proved (p=2) classification to this new carrier forces its scan also to be
[
11,0,0cdots0.
]

In particular
[
alpha(a,b,x)=1,qquad
alpha(a,x,c)=1,qquad
alpha(a,c,d)=0.
]

### The three-state cycle

Apply the same construction again:
[
O_2=(x,a,c,d,ldots),
]
omitting (b), again with word (0^2 1^q). A third application returns to
[
O_0=(a,b,c,d,ldots),
]
omitting (x).

Thus the short-phase residue is the exact protected cycle
[
(a,b;x)	o(b,x;a)	o(x,a;b)	o(a,b;x).
]

### Reinterpretation as a whole-front three-circuit

Let
[
P=(c,d,ldots)
]
be the common tail. Because the deletion word is (0,0,1^q), the path (P) is (1)-monochromatic.

The three carriers give
[
alpha(a,b,c)=0,qquad alpha(b,c,d)=0,
]
[
alpha(b,x,c)=0,qquad alpha(x,c,d)=0,
]
[
alpha(x,a,c)=0,qquad alpha(a,c,d)=0.
]
Hence the three ordered pairs
[
(a,b),qquad(b,x),qquad(x,a)
]
are all (0)-tight into the common terminal pair ((c,d)).

If some ordering of all three residual vertices ({a,b,x}) were (0)-tight into ((c,d)), concatenating it with the (1)-monochromatic path (P) would give a spanning order with at most one change. Counterexamplehood therefore makes
[
U={a,b,x}
]
a genuine size-three (0)-front circuit at ((c,d)).

Moreover (U) is the entire omitted set of the monochromatic path (P).

The audited pure-orientation size-three curvature-tube theorem now applies: every such whole-front three-circuit over a monochromatic tail has an explicit spanning one-change weave. Contradiction.

Therefore no blocked flat ternary deletion carrier can have (p=2).

Together with the immediate exclusion of (p=1), every surviving flat ternary deletion carrier satisfies
[
pge3.
]
By reversal/color normalization,
[
qge3
]
as well.

### Consequence

The phase-length hypotheses of the arbitrary-scan flat replacement theorem hold automatically in any minimum flat ternary counterexample. The Article III applicability gap from short phases is therefore closed; the remaining unconditional flat-sector obstruction is the recurrent same-profile A2 exchange cycle and its two-window suffix reconnection.

## Frontier

- Development version when composed: None
- Development version now: 1
