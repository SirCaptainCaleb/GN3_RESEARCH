# Directed NOR as an antipodal cut problem on overlap words

## Metadata

- ID: directed_nor_as_an_antipodal_cut_problem_on_overlap_words
- Parent Section: higher_memory_norine_geodesics
- Position: 10
- Row version: 2
- Development version: 2
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Directed NOR as an antipodal cut problem on the injective-word overlap graph

Fix (n) and (rge2). Let (mathcal O_{n,r}) be the directed overlap graph whose vertices are injective ordered (r)-tuples
[
(a_1,ldots,a_k),
]
with an arc
[
(a_1,ldots,a_k)longrightarrow(a_2,ldots,a_k,b)
]
whenever (b
otin{a_1,ldots,a_k}).

A directed NOR coloring (h) is simply a binary vertex coloring of (mathcal O_{n,r}) satisfying
[
h(Rw)=1-h(w),
qquad
R(a_1,ldots,a_k)=(a_k,ldots,a_1).
]

Define the change cochain on arcs by
[
delta(w,w')=h(w)oplus h(w').
]
Then:

1. (delta=1) exactly on the cut between the two color classes;
2. (delta) is a coboundary, so its mod-two sum around every directed cycle is zero;
3. reversal sends every arc to the oppositely directed reversed arc and
[
delta(Rw',Rw)=delta(w,w'),
]
so the change cochain is reversal-even even though (h) is reversal-odd.

Every permutation
[
(v_1,ldots,v_n)
]
induces the special overlap path
[
(v_1,ldots,v_k)	o(v_2,ldots,v_{r+1})	ocdots	o(v_{n-r+1},ldots,v_n).
]
It is not an arbitrary path of (mathcal O_{n,r}): globally, the underlying coordinate sequence uses every ground element exactly once.

Therefore (N_k) is equivalent to the following cut-crossing statement:

> Every reversal-odd 2-coloring of the vertices of (mathcal O_{n,r}) has a ground-set Hamiltonian overlap path crossing the color cut at most once.

This separates two issues that are easy to conflate. Component arguments in the monochromatic subgraphs of (mathcal O_{n,r}) control arbitrary overlap walks, but NOR requires a globally injective ground-coordinate walk. Equality of monochromatic components is therefore not by itself a closure statement; one still needs a simple-word extraction mechanism.

For (r=3), writing
[
a	o_{T_b}c Longleftrightarrow h(a,b,c)=0
]
identifies the color-zero vertices with transitions certified by the center-indexed tournaments (T_b). The mirrored-pair lemma is exactly the case in which all (T_b) coincide. In general, the cut formulation shows that the hard part is synchronizing these local tournaments while preserving global injectivity of the coordinate word.

This formulation also explains a topological caution: the raw change indicator (delta) is reversal-even, so an antipodal Borsuk--Ulam argument cannot simply use (delta) as its odd label. Any topological proof must retain an odd lift such as (h), a violation vector, or a component-pair/root label whose zero or balance forces a low-cut Hamiltonian overlap path.
