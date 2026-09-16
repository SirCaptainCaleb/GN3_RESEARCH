# Fixed-pair reduction and the remaining recurrence obstruction

**Status: supervised GN3 reconstruction. The argument below incorporates the independent audit corrections but is not yet a final GN3 certification.**

## 1. Minimal-counterexample setup

Assume the two-path-cover theorem is false and let `H` be a smallest counterexample. The certified small-order argument gives

`|V(H)|>10`.

Fix distinct vertices `a,c`. For every `x∈V(H)-{a,c}`, boundary antisymmetry makes exactly one of

`(a,x,c)` and `(c,x,a)`

tight. Hence the remaining vertices split into the two classes

`X={x:(a,x,c) is tight}`,  
`Y={x:(c,x,a) is tight}`.

The argument below repeatedly uses two vertices from one class while keeping the same pair `{a,c}` fixed.

## 2. Fixed-pair reduction lemma

The following previously proved lemma is the only nontrivial transformation needed in this section.

### Lemma 2.1

Let `a,c,s,t` be distinct and suppose

`(a,s,c)` and `(a,t,c)`

are tight. Then there is a finite valid continuation that either produces a spanning cover of `H` by two tight paths or returns to the two singleton paths

`(a)|(c)`

and, in the latter case, also records strict reductions of the two original ordered pairs

`(a,s) -> (s)`,  
`(t,c) -> (t)`.

Applying the same lemma with `s,t` interchanged records

`(a,t) -> (t)`,  
`(s,c) -> (s)`.

The directional dual holds when `(c,s,a)` and `(c,t,a)` are tight.

### Why this lemma is safe to use

The accepted proof first chooses which endpoint of each of the two disjoint ordered pairs is to survive and then uses the proved endpoint-contact theorem to obtain the strict reductions above. It does not infer a new current path configuration merely from deleting vertices, and it does not use either invalidated E9007 composition or the flagged E9006 composition.

For the present proof, Lemma 2.1 is best treated as one established graph-theoretic transformation with explicit input and output. Its internal legacy decomposition is provenance, not part of the mathematical spine.

## 3. Reduction at all but at most one remaining vertex

Fix one of the two classes, say `X`.

If `|X|>=2`, choose `t∈X`. For each `s∈X-{t}`, apply Lemma 2.1 first to the ordered roles `(s,t)` and then to `(t,s)`. Each application either finishes the theorem or returns to the same singleton pair `(a)|(c)`. If the theorem does not finish, then after the two applications the construction has recorded both strict reductions associated with `s` in the tight ordered triple `(a,s,c)`,

`(a,s)->(s)` and `(s,c)->(s)`,

and likewise both reductions associated with `t`.

Repeating this with the same pivot `t` records both reductions for every vertex of `X`. The same argument applies to `Y`, using the reversed tight ordered triples `(c,x,a)`.

A class of size `0` or `1` may therefore leave at most one vertex without both recorded reductions. The order bound is what turns this into a global statement. Since

`|V(H)-{a,c}| >= 9`,

the two classes cannot both have size at most one. Thus at most one of the two classes can contribute an untreated singleton. Consequently:

### Fixed-pair reduction conclusion

Unless a spanning two-path cover has already appeared, for all but at most one vertex `x∈V(H)-{a,c}` the construction has recorded strict reductions of both ordered pairs incident with `x` in its tight ordered triple through `a,c`.

This is the correct content of the earlier fixed-pair iteration argument.

An immediate consequence is purely about physical support. Any later configuration consisting of two disjoint ordered pairs on four distinct vertices must contain at least one such recorded vertex. Indeed, the set consisting of `a,c` together with the at most one untreated remaining vertex has size at most three.

Nothing stronger follows merely from this counting argument. In particular, a later four-vertex configuration may use an old vertex with new witnesses or in a new arrangement.

## 4. What a later intersection with recorded history actually gives

Fix a vertex `s∈X` for which both reductions

`(a,s)->(s)` and `(s,c)->(s)`

have been recorded. The original tight ordered triple `(a,s,c)` is also retained.

Two different facts are relevant.

### 4.1 A later singleton at `s` need not force progress

If a later construction again contains the singleton path `(s)`, the old ordered triple `(a,s,c)` allows contact with the two recorded reductions to recover the two original two-vertex supports `{a,s}` and `{s,c}`. This can happen using only the old three vertices.

Therefore the mere fact that a later construction meets a vertex with both recorded reductions does not by itself create a new vertex or a longer path.

### 4.2 A genuinely new second endpoint cannot be hidden

Suppose instead that a later nontrivial ordered pair contains `s` and another vertex

`u∉{a,c}`.

The proved path-contact theorem then forces either a strict extension or the corresponding reversed-contact configuration, and in either outcome the vertex `u` remains present. Thus the interaction cannot be confined entirely to the old ordered triple `(a,s,c)`.

Accordingly, the only two-vertex supports through `s` that are not excluded from recurrence using only the old ordered triple are exactly

`{a,s}` and `{s,c}`.

This is deliberately weaker than saying that every later occurrence on one of those supports is stationary. The remaining problem is precisely to understand a complete later four-vertex configuration when one of its two ordered pairs has one of these old supports.

## 5. Additional five-vertex geometry

The order bound also supplies a useful configuration after the fixed-pair reductions.

There are at least nine vertices outside `{a,c}`, so one of `X,Y` has at least five vertices. Since at most one remaining vertex lacks both recorded reductions, that larger class contains at least four vertices for which both reductions have been recorded.

Among any four vertices `S` satisfying `(a,x,c)` tight for every `x∈S`, the previously proved four-vertex comparison gives distinct `x,y,z∈S` such that

`(x,a,y,c,z)`

is a tight five-vertex path.

Hence one may retain, in addition to the pairwise reduction data, a tight path through `a,c` containing three vertices whose two incident ordered pairs have both been reduced to their middle vertex.

This extra path is available for the final argument, but no accepted theorem yet shows that it resolves the remaining recurrence.

## 6. Exact unresolved statement

The open step can now be stated without the old process terminology.

Take any later four-vertex configuration consisting of two disjoint ordered pairs of the kind required by the endpoint-selection lemma. By Section 3, at least one of its four vertices, say `s`, has both recorded reductions through the fixed pair `{a,c}`.

If the ordered pair containing `s` uses another vertex outside `{a,c}`, Section 4.2 gives a strict extension or reversed-contact configuration containing that new vertex.

The unresolved case is therefore concentrated on the situation in which that ordered pair has one of the two old supports

`{a,s}` or `{s,c}`.

One must use the **entire** later four-vertex configuration—especially its second ordered pair and its opposite-end witness—together with the two recorded reductions at `s` (and, if useful, the five-vertex path of Section 5) to prove one of the following:

1. `H` has a spanning two-path cover; or
2. the construction reaches a configuration that cannot be confined to the same old two-vertex supports.

No currently accepted theorem proves this implication.

## 7. Provenance and integrity

The exact legacy results supporting the argument are:

- the small-order theorem: E8997 / R2152;
- the fixed-pair reduction lemma: R2222;
- its endpoint-selection input: R2185, using R224 and R433;
- the fixed-pair iteration: R2224;
- the singleton recurrence warning: R2226;
- the new-endpoint contact theorem: R2229;
- the five-vertex path: R2230 and R2231;
- the path-contact theorem used in the strict reductions: S9010.

S9014 is not used as an independent transformation theorem here. The invalidated R2225 and R2228 compositions are not used, and neither is the flagged E9006 composition.
