# GN3 Research Tree

This file is the mutable hierarchical model of the live search. It is **not canonical mathematics**, not an archive of discoveries, and not an audit ledger. Researchers normally do not edit it directly. The Director or delegated Vice Director updates it continuously when the abstraction changes and performs additional compression after guidance waves.

The tree is deliberately top-down. Its purpose is to counterbalance the natural tendency of research to become local and constructive by keeping visible the chain

`theorem -> earliest unresolved bridge -> candidate mechanism -> concrete subproblem`.

Current guidance should have an identifiable location in this hierarchy. Audited live facts may carry a compact audit label at the node they support; detailed audit history belongs elsewhere. Nodes may be renamed, merged, moved, rewritten, or deleted aggressively. Git history is sufficient recovery for discarded branches.

## Two-tight-paths conjecture

### Close the augmentation gap for a lexicographically maximal spanning three-path cover

Fix a lexicographically maximal spanning three-path cover

`F=A|B|C`, with `|A|>=|B|>=|C|`.

The earliest unresolved bridge is to construct either a spanning two-path cover or a spanning three-path cover with lexicographically larger component-order triple.

The organizing object is the complete cover `F`. Every useful local construction must eventually specify how all vertices are retained in a new spanning cover.

#### Rule out false descent through continuation

Under the continuation relation of Section 4, once a two-vertex support is reduced to a singleton, the permitted operations never enlarge a support. In particular, that source support cannot later reappear on the same two-vertex set. At the singleton stage, prescribed singleton replacements can also cycle. Thus the present continuation machinery does not by itself supply a progressing recurrence on spanning covers.

Section 4 remains available as a source of explicit extended paths, reductions, singleton supports, and tight triples. It becomes part of the augmentation argument only when one of those constructions is embedded in a literal spanning replacement.

#### Reduce and close small complements

**Current guidance `[G01]` attacks this node first.**

A proposed reduction, presently requiring independent audit, is

`|B|<=4  ==>  |C|=1`.

Together with Proposition 6.1, this would leave only

`(|B|,|C|)=(3,1)` or `(4,1)`

when `|B|<=4`.

These are the first concrete cases to attack. In the `(3,1)` case, `|A|=n-4`, so the first component is already as long as any tight path can be; a contradiction must therefore come from a spanning two-path cover. In the `(4,1)` case, `|A|=n-5`; producing a tight path on `n-4` vertices would already improve the first coordinate after completing its complement by Lemma 1.1, while a spanning two-path cover closes the case directly.

Recent local facts about endpoint orientations and Hamiltonian small subsets belong under this node only insofar as they help build one of those complete spanning replacements. For each such finding, the Vice Director should test the statement itself, useful strengthenings, and sufficient weakenings at the earliest proof-spine location where they can apply before treating them as merely small-complement machinery.

#### Construct a spanning cut-and-join augmentation for larger complements

**Current guidance `[G01]` also attacks this node as the larger-complement branch.**

Seek an explicit augmentation obtained by cutting ordinary edges of `F` and rejoining the resulting tight subpaths.

A particularly concrete first template is one cut followed by two joins. One cut creates four tight path components. Two lawful joins can yield a spanning two-path cover provided the joins preserve vertex-disjointness, create no cycle or branching, and every new consecutive triple is tight. A one-cut/one-join construction may instead preserve three components and improve the sorted component orders.

The Section 5 crossing mechanism can certify one comparison between ordinary edges of actual deleted covers; Section 6 supplies extremal end restrictions; Appendix A supplies intersection alternatives. The missing step is to turn such local information into all joins required by a complete spanning replacement.

Any proposed construction should state explicitly:

- which ordinary edge or edges are cut;
- the resulting ordered tight subpaths;
- the new joins and the exact tight triples certifying them;
- why the resulting ordinary graph is a disjoint union of paths rather than a cycle or branching graph;
- how every vertex of `H` is accounted for;
- why the resulting cover has two components or has lexicographically larger component orders.

If the available crossing supplies only one join, isolate the exact obstruction to obtaining the next join rather than treating the local crossing as an augmentation.

#### Seek a cleaner parent theorem

A bounded alternative remains welcome if it genuinely replaces the cut-and-join construction by a simpler global theorem or invariant. It must still imply a literal spanning two-cover or a lexicographic improvement of `F`.

A result developed inside either constructive branch should be tested upward against this node and then against the augmentation bridge itself. If a strengthened or weakened form supplies a cleaner parent theorem, the tree should be reorganized around that higher abstraction rather than preserving the local route that discovered it.