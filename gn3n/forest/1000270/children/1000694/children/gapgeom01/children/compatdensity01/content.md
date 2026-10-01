# Compatibility-graph geometry and density

## Statement

For any chosen family of exact deletion two-covers, the pair-state compatibility graph is K4-free, each edge lies in at most two triangles, cyclic triangles are edge-isolated, transitive diamonds are confined to the two physical gap-neighbor directions and force order reversal; quantitatively, e <= floor((m^2+2m)/4), so some cover is incompatible with at least ceil((m-4)/2) others.

## Body

# Compatibility-graph geometry and density

Let H be a boundary tournament with pc(H)>2. For some set of deletion labels choose one exact two-cover F_v of H-v for each label v.

Form the compatibility graph Gamma whose vertices are these chosen deletion covers, with F_uF_v an edge when the two covers are compatible on V(H)-{u,v} in the pair-state sense of the compatibility/gluing theorem.

Then the following hold.

## Theorem

1. Gamma contains no K4.
2. Every edge of Gamma lies in at most two triangles.
3. If a compatible triangle has cyclic precedence, each of its three edges lies in no other triangle.
4. If a compatible triangle has transitive precedence source -> middle -> sink, then:
   - the source-sink edge lies in no other triangle;
   - only the source-middle edge can acquire a second triangle through the left neighbor of the common insertion gap;
   - only the middle-sink edge can acquire a second triangle through the right neighbor of the common insertion gap.
   Whenever such a second triangle exists, the diamond-reversal theorem gives an explicit pair-order reversal across the two nonadjacent tips of the resulting diamond.
5. If the common insertion gap of a compatible triangle is an endpoint gap of its common path, then its precedence tournament is necessarily cyclic. Consequently every edge of such an endpoint triangle lies in exactly that triangle and no other.

## Proof

### No K4

This is the q=2, four-deletion consequence of the compatibility/gluing theorem. Four pairwise-compatible deletion two-covers would glue to a spanning two-cover of H.

### At most two triangles through an edge

Fix a triangle

F_a,F_b,F_c.

By the common-gap theorem it has one common insertion gap and a precedence tournament T on {a,b,c}.

Suppose another vertex F_d is adjacent to both F_a and F_b, so the edge F_aF_b lies in the second triangle F_aF_bF_d.

The fourth-cover theorem the fourth-cover localization theorem says that d must be one of the two physical vertices of the common path adjacent to the triangle gap. More precisely, because the third label for the edge F_aF_b is c:

- if c is a sink of T, d must be the left gap-neighbor;
- if c is a source of T, d must be the right gap-neighbor;
- if c is neither, no such d exists.

For the fixed edge F_aF_b and fixed third label c, at most one of the two source/sink alternatives can occur: a vertex of a tournament cannot be both source and sink when the other two vertices are distinct.

Hence there is at most one additional common neighbor d besides c. Therefore every compatibility edge lies in at most two triangles.

### Cyclic triangles are edge-isolated

If T is cyclic, it has no source and no sink. The final clause of the fourth-cover localization theorem says every outside deletion cover is compatible with at most one member of the triangle.

Thus no edge of a cyclic triangle lies in a second triangle.

### Transitive triangles

Let the precedence tournament be

a -> b -> c,
a -> c.

Then a is the unique source, b the unique middle vertex, and c the unique sink.

For edge F_aF_b the third label is c, a sink. Hence the fourth-cover localization theorem allows a second triangle only through the left gap-neighbor.

For edge F_bF_c the third label is a, a source. Hence a second triangle is possible only through the right gap-neighbor.

For edge F_aF_c the third label is b, neither source nor sink. Hence no second triangle can use that edge.

The order-reversal statement for any realized diamond is exactly the diamond-reversal theorem.

### Endpoint gaps force cyclic precedence

Assume first that the common insertion gap is the left endpoint of the common path P. Thus the common-gap theorem writes the fixed common path class as

(a,b,c labels inserted before) R,

with the second path Q fixed.

Suppose for contradiction that the precedence tournament T is transitive. Let s be its source, and let u,v be the other two labels.

Among the reversal pair of triples with middle s, exactly one of

(u,s,v),
(v,s,u)

is tight.

Suppose without loss of generality that

(u,s,v)

is tight.

Because s is the source of T, the pair s,v is oriented s before v in the unique deletion cover containing that pair, namely F_u. Since the common gap is the left endpoint, F_u has its first component beginning

(s,v,R)

in that order.

Therefore the sequence

(u,s,v,R)

is tight: its first triple is the displayed tight triple, and every later consecutive triple is inherited from F_u.

Together with the unchanged common path Q, this gives a spanning two-cover of H, contradiction.

Thus T cannot be transitive. A tournament on three vertices is either transitive or cyclic, so T is cyclic.

The right-endpoint case is symmetric. If T were transitive, take its sink s. For the tight triple in the reversal pair with middle s, its first adjacent pair points into s and hence agrees with T; append that triple to the common left block L and use the appropriate deletion cover for all preceding consecutive triples. This again gives one tight path containing the whole common class and all three labels, plus Q, contradicting pc(H)>2.

Hence endpoint-gap triangles are cyclic. By the cyclic case already proved, none of their edges lies in another triangle. ∎

## Geometric interpretation

The compatibility graph of deletion covers is not an arbitrary K4-free graph. Its triangles are rigid geometric objects attached to one insertion gap:

- cyclic triangles are completely edge-isolated;
- transitive triangles can form diamonds only in the two physical gap-neighbor directions;
- every such diamond exports a concrete order reversal in H.

This structure is independent of the ambient path lengths and therefore survives at arbitrary order. ∎

# Quantitative incompatibility density

Let `H` be a boundary tournament with `pc(H)>2`. Let `D` be a set of `m` vertices, and for each `d in D` choose one exact two-path cover `F_d` of `H-d`. Form the graph `G` on `D` in which `d,e` are adjacent exactly when `F_d,F_e` are compatible on `H-{d,e}` in the pair-state sense.

Then `e(G) <= floor((m^2+2m)/4)`.

Consequently at least `binom(m,2)-floor((m^2+2m)/4)` pairs of chosen deletion covers are incompatible. In particular some `F_d` is incompatible with at least `ceil((m-4)/2)` of the other chosen covers.

## Proof

By the compatibility-graph local-structure lemma `the local compatibility-graph theorem above`, every edge of `G` lies in at most two triangles. Let `e=e(G)`, let `t` be the number of triangles, and write `d(v)` for vertex degrees. Counting incidences of edges with triangles gives `3t<=2e`.

For each edge `uv`, its number of common neighbors is at least `d(u)+d(v)-m`. Summing over edges, `3t = sum_{uv in E(G)} |N(u) intersection N(v)| >= sum_v d(v)^2-me`. By Cauchy-Schwarz, `sum_v d(v)^2 >= 4e^2/m`. Hence `3t >= 4e^2/m-me`.

Combining with `3t<=2e` gives, for `e>0`, `4e<=m^2+2m`. The same conclusion is trivial for `e=0`, proving the edge bound after taking the integer floor.

The incompatible-pair count is `binom(m,2)-e(G)`. Its average incompatible degree is at least `(m-4)/2`, so some chosen deletion cover has incompatible degree at least `ceil((m-4)/2)`. ∎

This arbitrary-order consequence does not itself turn disagreement into augmentation, but it shows that incompatibility cannot be sparse: one deletion state disagrees with linearly many others.
