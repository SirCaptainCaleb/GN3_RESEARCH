# Freudenthal gallery interpretation of prefix-tail reachability — preserved pre-item development

## Prefix-tail states are Freudenthal faces

Fix coordinate-label arity (rge2) on (V). Identify cube vertices with subsets of (V), and use the standard Freudenthal triangulation of ([0,1]^V).

A prefix-tail state
[
s=(P;a_1,ldots,a_{r-1})
]
corresponds to the oriented ((r-1))-simplex
[
Delta(s)=
[P,,
Pcup{a_1},,
Pcup{a_1,a_2},,
ldots,,
Pcup{a_1,ldots,a_{r-1}}].
]

If
[
s=(P;a_1,ldots,a_{r-1})
longrightarrow
t=(Pcup{a_1};a_2,ldots,a_{r-1},x),
]
then (s) and (t) are the bottom and top ((r-1))-facets of the Freudenthal (r)-simplex
[
[P,,
P+a_1,,
P+a_1+a_2,,
ldots,,
P+a_1+cdots+a_{r-1},,
P+a_1+cdots+a_{r-1}+x].
]
Its color is
[
h(a_1,ldots,a_{r-1},x).
]

Thus the prefix-tail state DAG is the directed gallery graph obtained by crossing a Freudenthal (r)-simplex from its bottom facet to its top facet. A coordinate permutation is a maximal monotone gallery.

### Antipodality

Cube complementation sends the simplex of
[
(P;a_1,ldots,a_{r-1})
]
to the simplex represented by
[
J(P;a_1,ldots,a_{r-1})
=
(Vsetminus(Pcup{a_1,ldots,a_{r-1}});
a_{r-1},ldots,a_1).
]
It reverses the directed gallery step and complements its color.

Hence the previously defined reachability sets (R_0,R_1) have the following geometric meaning:

- (R_sigma) is the set of oriented ((r-1))-faces reachable from the lower Freudenthal boundary by a monotone gallery of (sigma)-colored (r)-simplices;
- (J(R_sigma)) is the antipodal upper region obtained from the corresponding lower region.

The directed NOR target is
[
(R_0cup R_1)cap J(R_0cup R_1)
earnothing.
]

### Interface forcing

Assume a counterexample, so the lower and upper regions are disjoint.

Let (sin R_sigma), and let
[
s	o t
]
be a gallery step with (t
otin R_sigma). Then that (r)-simplex has color (1-sigma). Otherwise the (sigma)-gallery reaching (s) would extend to (t).

Dually, suppose
[
s	o t,
qquad
tin J(R_	au),
qquad
s
otin J(R_	au).
]
Then the crossing (r)-simplex has color (	au). Indeed the antipodal step
[
J(t)	o J(s)
]
has complementary color; if the original color were (1-	au), the antipodal step would have color (	au) and would extend the lower (	au)-gallery from (J(t)), placing (s) in (J(R_	au)).

Therefore every monotone gallery from the lower region to the upper region encounters two forced interface colors: it leaves a lower (sigma)-region through color (1-sigma), and it enters an upper (J(R_	au))-region through color (	au). When the two interfaces coincide in one gallery step, necessarily
[
	au=1-sigma,
]
and that step is an isolated opposite-color crossing between monochromatic lower and upper arms.

### Significance

This puts the one-change problem into the same ambient Freudenthal geometry used by the chain-level antipodal toolkit, but with a different local object: colors live on (r)-simplices and reachability lives on their directed bottom/top facets.

The remaining closure problem can now be stated geometrically:

> two antipodal monochromatic monotone-gallery regions in the Freudenthal (r)-skeleton cannot remain disjoint under the reversal-complement coloring rule.

Any chain or separator argument should act on these directed (r)-simplex interfaces rather than only on the permutation chamber sphere. This retains the full cube geometry that is lost after fixing one coordinate-order sphere.
