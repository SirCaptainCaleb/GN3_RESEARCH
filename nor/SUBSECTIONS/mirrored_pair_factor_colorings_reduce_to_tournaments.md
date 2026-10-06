# Mirrored-pair factor colorings reduce to tournaments

## Metadata

- ID: mirrored_pair_factor_colorings_reduce_to_tournaments
- Parent Section: higher_memory_norine_geodesics
- Position: 8
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Mirrored-pair factor colorings are completely soluble

A substantial subclass of the directed tuple conjecture reduces to ordinary tournament Hamilton paths.

Fix (kge2), and choose mirrored positions
[
1le i<k+1-ile k.
]
Set
[
d=k+1-2i>0.
]
Suppose the coloring factors through those two mirrored positions:
[
h(a_1,ldots,a_k)=t(a_i,a_{k+1-i}),
]
where (t) is a tournament coloring,
[
t(y,x)=1-t(x,y).
]
Then the reversal law for (h) is automatic.

**Proposition.** Every such (h) admits a permutation whose entire sliding (k)-tuple word is constant. Hence (N_k) holds in zero-change form for all mirrored-pair factor colorings.

**Proof.** It is enough to construct a permutation
[
v_1,ldots,v_n
]
such that
[
t(v_p,v_{p+d})=0
qquad
(1le ple n-d).
]
Indeed, a window beginning at position (j) has color
[
h(v_j,ldots,v_{j+k-1})
=
t(v_{j+i-1},v_{j+k-i}),
]
and the two indices differ by (d).

Partition the position set ({1,ldots,n}) into its residue classes modulo (d). The graph joining (p) to (p+d) is therefore a disjoint union of ordinary paths, one on each residue class.

Now partition the ground vertices arbitrarily into subsets having the corresponding residue-class sizes. On each subset, the tournament (t) has a directed Hamilton path. Place the vertices of that Hamilton path, in order, into the positions of the corresponding residue class. Then every step (p	o p+d) follows a (t)-directed edge, so
[
t(v_p,v_{p+d})=0
]
for every relevant (p). Thus every sliding (k)-window has color (0). ∎

### Structural consequence for (k=3)

For (k=3), every directed tuple coloring can be written as a family of tournaments
[
T_bquad (bin V),
]
where
[
a	o_{T_b} c
quadLongleftrightarrowquad
h(a,b,c)=0.
]
The proposition says that if these center-indexed tournaments are all the same tournament, then the conjecture is trivial: split the permutation positions into the two parity classes and place a directed Hamilton path of that tournament in each class.

Thus the genuine difficulty of (N_3) is not reversal antisymmetry itself and not even tournament structure at each center. It is the **variation of the tournament with the middle vertex**. Any closure mechanism for (N_3) can therefore focus on synchronizing the family ({T_b}), rather than treating (h) as an undifferentiated ternary coloring.
