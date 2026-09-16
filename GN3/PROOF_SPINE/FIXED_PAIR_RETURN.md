# Fixed-pair reduction and the remaining recurrence obstruction

**Status: supervised GN3 reconstruction. The argument below incorporates the independent audit corrections but is not yet a final GN3 certification.**

## 1. Common input

Work throughout under the conclusions of [`PRELIMINARIES.md`](PRELIMINARIES.md). Thus `H` is a smallest counterexample with

`pc(H)=3`, `|V(H)|>10`,

and deleting any two vertices leaves an exact two-path-coverable graph in which neither path is a singleton.

Fix distinct vertices `a,c`, and use the orientation classes

`X={x:(a,x,c) is tight}`,  
`Y={x:(c,x,a) is tight}`

from the preliminary document. They partition `V(H)-{a,c}` and together contain at least nine vertices.

The argument below repeatedly uses two vertices from one class while keeping the same pair `{a,c}` fixed.

## 2. What historical information is retained

The fixed-pair argument uses earlier paths after the current local configuration has changed, so the distinction between **current paths** and **retained proof data** must be explicit.

Suppose an earlier step contained the tight ordered pair `(u,v)` as part of a specified tight ordered triple, and a later application of the proved path-contact theorem showed that contact with a current singleton at the other endpoint leaves the singleton `(v)` as a strict subpath of that earlier pair. What is retained thereafter is the following finite certificate:

1. the concrete earlier tight path `(u,v)`;
2. the tight ordered triple that supplies the endpoint witness required by the path-contact theorem;
3. the concrete singleton `(v)` produced by that theorem; and
4. the finite chain of already proved local transformations establishing this strict-subpath conclusion.

This certificate is a statement about the proof history. It does **not** assert that `(u,v)` remains a path in the current configuration, nor that `(u,v)` and `(v)` occur simultaneously in any path cover. Later arguments may use the earlier pair only through a theorem whose hypotheses explicitly allow such retained earlier-path data.

This is the precise meaning below whenever we say that the proof retains the fact that an earlier ordered pair has been reduced to its second vertex.

## 3. Fixed-pair reduction lemma

The following previously proved theorem is the only nontrivial transformation needed in this section.

### Lemma 3.1

Let `a,c,s,t` be distinct and suppose

`(a,s,c)` and `(a,t,c)`

are tight.

Starting from the two disjoint ordered pairs `(a,s)` and `(t,c)` with the endpoint witnesses supplied by those two tight ordered triples, the established endpoint-selection theorem gives a finite certified sequence with one of two outcomes:

1. a spanning cover of `H` by two tight paths; or
2. the current distinguished paths are the singletons `(a)` and `(c)`, while the proof retains the following two path-contact certificates:
   - from the earlier pair `(a,s)` and the tight triple `(a,s,c)`, contact at `a` produces the strict singleton subpath `(s)`;
   - from the earlier pair `(t,c)` and the tight triple `(a,t,c)`, contact at `c` produces the strict singleton subpath `(t)`.

Applying the same theorem with `s,t` interchanged retains the analogous certificates from `(a,t)` to `(t)` and from `(s,c)` to `(s)`.

The directional dual holds when `(c,s,a)` and `(c,t,a)` are tight.

### Why this lemma is safe to use

The accepted proof first chooses which endpoint of each of the two disjoint ordered pairs is to keep and then applies the proved path-contact theorem at the resulting singleton pair. It does not infer a new current path merely from deleting vertices, and it does not use either invalidated E9007 composition or the flagged E9006 composition.

For the present spine, Lemma 3.1 is therefore treated as one established theorem with explicit graph-theoretic input, current output, and retained earlier-path certificates. Its internal legacy decomposition belongs only in provenance.

## 4. The fixed-pair iteration

Fix one of the two classes, say `X`.

If `|X|>=2`, choose `t∈X`. For each `s∈X-{t}`, apply Lemma 3.1 first with roles `(s,t)` and then with the roles reversed. Each application either proves the theorem or returns to the same current singleton pair `(a),(c)`.

If no spanning two-path cover appears, then after these two applications the proof retains, for `s`, both earlier-path certificates associated with the tight ordered triple `(a,s,c)`:

- contact with the earlier pair `(a,s)` produced the singleton `(s)`;
- contact with the earlier pair `(s,c)` produced the singleton `(s)`.

The same two facts are retained for `t`. Repeating the argument with the same pivot `t` gives both certificates for every vertex of `X`. The same argument applies to `Y`, using the reversed tight ordered triples `(c,x,a)`.

A class of size `0` or `1` may therefore leave at most one vertex without both certificates. The order bound is what turns this into a global statement. Since

`|V(H)-{a,c}| >= 9`,

the two classes cannot both have size at most one. Thus at most one of the two classes can contribute an untreated singleton.

Consequently, unless a spanning two-path cover has already appeared, for all but at most one vertex `x∈V(H)-{a,c}` the proof retains both strict path-contact certificates arising from the two ordered pairs incident with `x` in its tight ordered triple through `a,c`.

An immediate consequence is purely about vertex support. Any later configuration consisting of two disjoint ordered pairs on four distinct vertices must contain at least one vertex carrying both certificates. Indeed, the set consisting of `a,c` together with the at most one untreated remaining vertex has size at most three.

Nothing stronger follows merely from this counting argument. In particular, a later four-vertex configuration may use an old vertex with new witnesses or in a new arrangement.

## 5. What a later intersection with the retained certificates gives

Fix `s∈X` and suppose both certificates from the tight ordered triple `(a,s,c)` have been retained.

Two different facts are relevant.

### 5.1 A later singleton at `s` need not force progress

If a later current configuration again contains the singleton path `(s)`, the original tight ordered triple `(a,s,c)`, together with the two retained path-contact certificates, allows the two old supports `{a,s}` and `{s,c}` to occur again. This can happen using only the old three vertices.

Therefore the mere fact that a later configuration meets a vertex carrying both certificates does not by itself create a new vertex or a longer path.

### 5.2 A genuinely new second endpoint cannot be hidden

Suppose instead that a later nontrivial ordered pair contains `s` and another vertex

`u∉{a,c}`.

The proved path-contact theorem then forces either a strict extension or the corresponding reversed-contact configuration, and in either outcome the vertex `u` remains present. Thus the interaction cannot be confined entirely to the old ordered triple `(a,s,c)`.

Accordingly, the only two-vertex supports through `s` that are not excluded from recurrence using only the old ordered triple are exactly

`{a,s}` and `{s,c}`.

This is deliberately weaker than saying that every later occurrence on one of those supports is stationary. The remaining problem is precisely to understand a complete later four-vertex configuration when one of its two ordered pairs has one of these old supports.

## 6. Additional five-vertex geometry

The order bound also supplies a useful configuration after the fixed-pair iteration.

There are at least nine vertices outside `{a,c}`, so one of `X,Y` has at least five vertices. Since at most one remaining vertex lacks both certificates, that larger class contains at least four vertices carrying both.

Among any four vertices `S` satisfying `(a,x,c)` tight for every `x∈S`, the previously proved four-vertex comparison gives distinct `x,y,z∈S` such that

`(x,a,y,c,z)`

is a tight five-vertex path.

Hence one may retain, in addition to the pairwise path-contact certificates, a tight path through `a,c` containing three vertices for which both incident earlier pairs have certified singleton subpaths at the middle vertex.

This extra path is available for the final argument, but no accepted theorem yet shows that it resolves the remaining recurrence.

## 7. Exact unresolved statement

Take any later four-vertex configuration consisting of two disjoint ordered pairs of the kind required by the endpoint-selection theorem. By Section 4, at least one of its four vertices, say `s`, carries both fixed-pair path-contact certificates.

If the ordered pair containing `s` uses another vertex outside `{a,c}`, Section 5.2 gives a strict extension or reversed-contact configuration containing that new vertex.

The unresolved case is therefore concentrated on the situation in which that ordered pair has one of the two old supports

`{a,s}` or `{s,c}`.

One must use the **entire** later four-vertex configuration—especially its second ordered pair and the tight ordered triples certifying the opposite endpoint orientation—together with the two retained certificates at `s` (and, if useful, the five-vertex path of Section 6) to prove one of the following:

1. `H` has a spanning two-path cover; or
2. the construction reaches a configuration that cannot be confined to the same old two-vertex supports.

No currently accepted theorem proves this implication.

## 8. Provenance and integrity

The exact legacy results supporting the argument are:

- the fixed-pair reduction lemma: R2222;
- its endpoint-selection input: R2185, using R224 and R433;
- the fixed-pair iteration: R2224;
- the singleton recurrence warning: R2226;
- the new-endpoint contact theorem: R2229;
- the five-vertex path: R2230 and R2231;
- the path-contact theorem used in the strict reductions: S9010.

The common small-order theorem and pair-deletion argument now live in [`PRELIMINARIES.md`](PRELIMINARIES.md).

S9014 is not used as an independent transformation theorem here. The invalidated R2225 and R2228 compositions are not used, and neither is the flagged E9006 composition.
