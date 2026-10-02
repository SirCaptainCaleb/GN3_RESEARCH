# Route 8 — Global/symmetric 2-shadow and strong-rainbow translation

## Statement

Comprehensive synthesis of the representation-level upper route through the properly edge-colored 2-shadow, source-oriented directed/rainbow coupling, and the full symmetric strong-rainbow formulation.

## Body

# Route 8. The symmetric 2-shadow and strong-rainbow paths

## Goal and setup

This route translates the upper-bound problem into a properly edge-colored graph problem on the original vertex set.

Let H be a linear 3-uniform hypergraph with n vertices and m hyperedges. Construct its full 2-shadow G as follows. For every hyperedge

{x,y,z},

place all three graph edges xy,xz,yz and color them respectively by z,y,x.

Linearity implies that this coloring is proper. Every hyperedge contributes exactly three shadow edges, so

e(G)=3m,      (1)

and at every vertex v,

d_G(v)=2d_H(v).      (2)

The central question is: what graph-path condition corresponds exactly to a linear hypergraph path?

## 1. Exact strong-rainbow encoding

Consider a graph path

x_0x_1…x_k

in G, and let c_i be the color of x_{i−1}x_i. The corresponding hyperedges are

E_i={x_{i−1},x_i,c_i}.

The sequence E_1,…,E_k is a linear hypergraph path exactly when the following 2k+1 objects are all distinct:

x_0,x_1,…,x_k,c_1,…,c_k.      (3)

Indeed, adjacent hyperedges already share the intended path vertex x_i. Condition (3) prevents them from sharing any second vertex, prevents nonconsecutive hyperedges from meeting through a repeated color, and prevents a color from colliding with a nonincident path vertex. Conversely, if the hyperedges form a linear path, all these extra coincidences are forbidden.

Call a graph path satisfying (3) **strong-rainbow**.

The exact translation is therefore

H is P_ℓ-free  ⇔  G has no ℓ-edge strong-rainbow path.      (4)

This statement is proved but currently pending audit.

Combining (1) and (4), the one-third upper target

m≤(ℓ/3)n

becomes the purely colored-graph statement

e(G)≤ℓ n      (5)

for every symmetric triangle-colored shadow G with no ℓ-edge strong-rainbow path.

This is the cleanest formulation of the route.

## 2. Why the coloring is more structured than an arbitrary proper coloring

Every hyperedge xyz creates a colored triangle

xy colored z,
xz colored y,
yz colored x.

Thus colors and vertices belong to the same ground set, and every colored edge sits inside a triangle where the three colors are exactly the opposite vertices.

This symmetry is much stronger than ordinary proper edge-coloring. It is also precisely what makes the strong-rainbow condition difficult: the color of one edge may equal a far-away vertex of the graph path even when no color repeats.

A theorem that treats G as merely an arbitrary properly colored graph throws away this triangle symmetry and therefore cannot be expected to reach the one-third target.

## 3. The A/B separation and its intrinsic loss

There is a safe way to convert strong-rainbow paths into ordinary rainbow paths.

Partition the vertex set into A∪B. Keep only shadow edges whose two endpoints lie in A and whose color lies in B. In this retained graph, every ordinary rainbow path automatically satisfies (3): its path vertices lie in A, its distinct colors lie in B, so colors cannot collide with path vertices.

Hence every rainbow path in the retained graph lifts to a linear hypergraph path.

Suppose a generic theorem for properly edge-colored graphs guaranteed a rainbow path of length at least

αd−O(1)

from minimum degree d. Optimizing the partition and core extraction then yields the hypergraph estimate

m ≤ (2/(3α))ℓ n + O(n).      (6)

Even the ideal black-box value α=1 gives leading coefficient 2/3.

Thus the A/B separation is useful but has an unavoidable factor-two cost. Any proof aiming below two thirds must use more than generic proper coloring; it must exploit either the full symmetric shadow or additional rank information.

## 4. Degree normalization

Two minimum-degree reductions are available, but they apply to different objects and must not be conflated.

First, from any hypergraph of density ρ one may pass to an induced subhypergraph of density at least ρ and minimum hypergraph degree at least ρ.

Second, after the A/B shadow construction one may pass to a retained colored graph with minimum graph degree at least approximately

3ρ/4.      (7)

The quantities δ(H) and δ(G) are not interchangeable. Equation (2) applies to the full shadow, not automatically to an arbitrary A/B subgraph.

This distinction matters whenever a rainbow-path theorem assumes graph minimum degree.

## 5. Source-oriented hybrid model

There is an intermediate representation between the lossy A/B model and the fully symmetric shadow.

Choose one source σ(T) in every hyperedge T={x,y,z}. Add directed arcs from the source to the other two vertices, and join the two nonsource vertices by a graph edge colored by the source.

If s(v) is the number of triples for which v is the source and h(v) the number for which v is a nonsource vertex, then

d_H(v)=s(v)+h(v),

while in the directed graph D,

d_D^+(v)=2s(v),
d_D^−(v)=h(v).

Therefore

(1/2)d_D^+(v)+d_D^−(v)=d_H(v).      (8)

Now let v_0…v_p be a longest directed path. At its initial and terminal vertices, maximality forces complementary bounds on source and nonsource incidence. Roughly, if the directed path is short, a large part of the degree must appear in the properly colored terminal graph; if that colored part is sufficiently rich, one seeks a rainbow path there.

This tradeoff yields an unconditional directed-or-rainbow path guarantee of order 7ρ/27, where ρ=m/n, up to an absolute additive constant. It is useful infrastructure but far from the one-third target.

The important point is conceptual: the source-oriented model makes the repeated-source obstruction visible rather than discarding it.

## 6. The repeated-hub obstruction

A long ordinary path in the full 2-shadow need not contain any long hypergraph path.

Take distinct vertices x_0,…,x_t and two hubs z,w. For odd i let

E_i={x_{i−1},x_i,z},

and for even i let

E_i={x_{i−1},x_i,w}.

The resulting 3-graph is linear: two odd edges meet only at z, two even edges meet only at w, and consecutive edges additionally use successive x-vertices in the intended way.

Its 2-shadow contains the arbitrarily long ordinary graph path

x_0x_1…x_t,

but the colors on that path alternate z,w. Any attempt to use many corresponding hyperedges creates repeated nonconsecutive intersections at z or w. In fact every linear hypergraph path has bounded length, at most four in the constructed family.

Thus there is no theorem of the form

“take an arbitrary long shadow path and extract a fixed positive fraction as a hypergraph path.”

The obstruction is concentrated reuse of a few colors or hubs. This theorem is proved but still pending audit.

## 7. What the symmetric route must exploit

The repeated-hub example identifies the missing structure.

If colors are mostly fresh, then a long ordinary or rainbow path is already close to strong-rainbow and can be lifted.

If a few colors are reused heavily, then the triangle symmetry says those colors are actual hypergraph vertices incident with many shadow edges. Such reuse creates large star-like families of hyperedges and potentially alternative routes through the other two shadow sides of their triangles.

Therefore the hoped-for proof has a dichotomy:

1. low color reuse gives a long strong-rainbow path directly;
2. high color reuse creates enough structured density around the repeated hubs to reroute through fresh vertices and colors.

No theorem currently executes this dichotomy at the required scale.

## 8. Interface with rank flow

There is one established way to repair many color-vertex collisions: retain the ascending-edge rank structure.

For a rank layer of ascending nonspecial edges, terminal pairs colored by their entrances form a proper-colored graph with strong rank restrictions. Directed paths through the entrance-to-terminal orientation force strictly increasing vertex rank. In that setting, many collisions that are possible in the unrestricted full shadow become impossible or point only backward.

Those are theorems of the dense-core rank-flow route, not of the representation route itself. They may be imported if a shadow proof needs an ordering device.

The conceptual distinction should remain clear:

- Route 2 asks whether ascending nonspecial mass can survive across rank layers;
- Route 8 asks for a path theorem in the full symmetric shadow after most rank information has been discarded.

## 9. Known dead ends

Three shortcuts are closed.

First, generic properly colored graph theorems have the factor-two A/B ceiling (6), so they cannot by themselves reach one third.

Second, an ordinary long full-shadow path is insufficient because of the repeated-hub construction.

Third, even an ordinary rainbow path in the full shadow is not enough: an edge color may equal a nonincident path vertex. The correct condition is the mutual distinctness in (3), unless one uses an A/B separation.

Finally, hypergraph and shadow minimum degrees must be kept distinct after any subgraph extraction.

## 10. First unsupported implication

The proof stops at the following exact colored-graph theorem.

**Symmetric strong-rainbow target.** Let G be the full 2-shadow of a linear 3-uniform hypergraph, with every edge colored by the third vertex of its unique parent hyperedge. If G has no ℓ-edge path whose path vertices and edge colors are all mutually distinct, prove

e(G)≤ℓ n.      (9)

By (1), this is exactly the one-third upper bound.

Any successful proof must survive concentrated repeated-color/hub configurations of the type above. The A/B theorem cannot cross the two-thirds ceiling, and no present full-shadow theorem controls hub reuse at the necessary density.

The exact strong-rainbow encoding and repeated-hub obstruction are proved but pending audit; the full-shadow degree identity and A/B/source-oriented machinery are certified.

## Research handoff

The strongest next target is a density-to-strong-rainbow-path theorem exploiting the symmetric colored triangles, with an explicit structural branch for repeated hub colors. A useful intermediate theorem would show that high color multiplicity forces a decomposition or rerouting mechanism that creates fresh colors elsewhere.

Do not retry generic rainbow black boxes, arbitrary ordinary-shadow path extraction, or ordinary rainbow lifting without controlling color-vertex collisions.

If the argument begins using rank superlevels or monotone edge ranks essentially, import the rank-flow machinery rather than rebuilding it here; at that point the proof is deliberately using the interface with Route 2.