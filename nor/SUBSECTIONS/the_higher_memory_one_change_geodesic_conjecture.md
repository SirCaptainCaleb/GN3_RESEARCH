# The ordered-tuple one-change conjecture

## Metadata

- ID: the_higher_memory_one_change_geodesic_conjecture
- Parent Section: higher_memory_norine_geodesics
- Position: 1
- Row version: 7
- Development version: 4
- Composition version: 3
- Composition stale: False

## Composition


(N_k) is indexed by the arity of the colored cube-vertex tuple. It colors ordered
[
(X_0,ldots,X_{k-1})
]
of (k) consecutive vertices and asks for an antipodal geodesic whose sliding (k)-tuple color word changes at most once.

Thus (N_1) is vertex coloring, (N_2) is edge coloring, (N_3) colors three-vertex/two-step windows, and (N_4) colors four-vertex/three-step windows.

When an (N_k) coloring is translation-invariant, it may be represented by a coordinate label
[
h(v_1,ldots,v_{k-1}),
]
so the coordinate-label arity is one less than the NOR index. In particular, ternary coordinate data such as GN3 belong to (N_4).


## Development


## Grand conjecture: tuple arity is the index

Let (Q_V) be the Boolean cube on coordinate set (V), and fix (kge 1).

A **colored (k)-tuple** is an ordered tuple
[
(X_0,ldots,X_{k-1})
]
of (k) consecutive vertices on a cube geodesic. Thus it contains (k-1) cube steps. The project index (k) is always the arity of this colored tuple.

A binary (N_k) coloring assigns
[
chi(X_0,ldots,X_{k-1})in{0,1}
]
to every permitted ordered geodesic (k)-tuple, subject to the active antipodal rule
[
chi(ar X_{k-1},ldots,ar X_0)=1-chi(X_0,ldots,X_{k-1}).
]

For an antipodal geodesic
[
G=(X_0,ldots,X_n),qquad X_n=ar X_0,
]
its (N_k) word is the sliding (k)-tuple word
[
chi(X_0,ldots,X_{k-1}),
chi(X_1,ldots,X_k),
ldots,
chi(X_{n-k+1},ldots,X_n).
]

### Grand Conjecture (N_k)

Every admissible (N_k) coloring has an antipodal geodesic whose sliding (k)-tuple word changes value at most once, equivalently is of the form
[
0^*1^*qquad	ext{or}qquad1^*0^*.
]

### Indexing examples

- (N_1) colors cube vertices.
- (N_2) colors consecutive vertex pairs, i.e. cube edges.
- (N_3) colors consecutive vertex triples, i.e. two-step windows.
- (N_4) colors consecutive vertex quadruples, i.e. three-step windows; the GN3 coordinate-triple model lives here.

### Translation-invariant coordinate form

A (k)-tuple window has (r=k-1) successive flipped coordinates
[
v_1,ldots,v_r.
]
If its color is invariant under global symmetric-difference translation, then it has a coordinate representation
[
chi(X_0,ldots,X_r)=h(v_1,ldots,v_r).
]
Thus an (r)-ary coordinate label (h) belongs to the translation-invariant sector of (N_{r+1}), not (N_r).

Under antipodal reversal this coordinate label satisfies
[
h(v_r,ldots,v_1)=1-h(v_1,ldots,v_r).
]

This (r=k-1) distinction is mandatory throughout NOR: (k) indexes the arity of the colored cube-vertex tuple; (r) may be used for the number of steps or the arity of a reduced coordinate label.
