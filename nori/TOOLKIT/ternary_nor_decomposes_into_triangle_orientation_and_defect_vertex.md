# Ternary NOR decomposes into a simplex-face orientation plus a defect vertex

**Summary:** A ternary NOR coloring is an honest orientation of every triangle of the coordinate simplex, plus at most one marked defect vertex per triangle. The color of a-b-c is the triangle orientation, flipped exactly when b is the marked vertex.

## Statement

Every reversal-odd ternary binary label h is uniquely encoded by an alternating orientation alpha on every unordered coordinate triangle together with an optional distinguished defect vertex d(T) on that triangle. Writing epsilon=(-1)^h, one has epsilon(a,b,c)=alpha(a,b,c) unless the middle vertex b is d({a,b,c}), in which case the sign is reversed.

## Body


## Alternating projection of a reversal-odd ternary label

Let epsilon(a,b,c)=(-1)^{h(a,b,c)}. Reversal oddness is

epsilon(c,b,a)=-epsilon(a,b,c).

Fix an oriented triple (a,b,c) and set

A(a,b,c)=epsilon(a,b,c)+epsilon(b,c,a)+epsilon(c,a,b).

The three summands are each +/-1, so A is one of -3,-1,1,3 and is never zero.

Define

alpha(a,b,c)=sign A(a,b,c).

### Lemma: alpha is alternating

Cyclic permutation preserves A. Reversing two vertices turns the three cyclic orientations into their reversals, negating every epsilon term. Hence every odd permutation negates A. Therefore alpha is a genuine alternating orientation of each unordered triangle.

Thus alpha is an honest simplicial 2-face orientation on the coordinate simplex.

### The defect vertex

If |A|=3, all three cyclic epsilon values agree with alpha. Call the triangle coherent and set d(T)=none.

If |A|=1, exactly one of the three cyclic epsilon values disagrees with alpha. Each cyclic ordering has a unique middle vertex:

epsilon(a,b,c) has center b,
epsilon(b,c,a) has center c,
epsilon(c,a,b) has center a.

Define d(T) to be the center of the unique minority term.

This vertex is independent of the chosen cyclic presentation of T. Reversal negates both the majority and every term, so it also leaves d(T) unchanged.

### Reconstruction formula

For every ordering (a,b,c) of a triangle T,

epsilon(a,b,c)
=
alpha(a,b,c) if d(T) is not b,

and

epsilon(a,b,c)
=
-alpha(a,b,c) if d(T)=b.

Equivalently,

epsilon(a,b,c)=alpha(a,b,c)(-1)^{1_{d(T)=b}}.

Thus the pair (alpha,d) determines h completely, and every reversal-odd h produces such a pair uniquely.

### Geometric meaning

The arbitrary directed data split into two simplex-native objects:

1. alpha is a true orientation/sign on every 2-face of the coordinate simplex;
2. d is a partial Sperner-style labeling of 2-faces by one of their own vertices.

Coherent triangles d=none are exactly those for which the three cyclic center readings have one common sign. Noncoherent triangles carry one distinguished center at which the directed label differs from the alternating triangle orientation.

For an edge-ordered coloring h(a,b,c)=1_{lambda(ab)>lambda(bc)}, a strict ordering of the three edge weights prevents all three cyclic comparisons from agreeing, so every triangle has a defect vertex; it is the vertex opposite the median edge.

### Closure relevance

This decomposition converts the ternary NOR problem from a family of unrelated center tournaments into an oriented 2-skeleton plus a vertex-valued defect field on the simplex. It is therefore directly compatible with simplicial cochains, Sperner/KKM-style face labelings, and the exact cube-to-simplex completion.

A one-change Hamilton order asks for a chamber in which the oriented triangle signs, after the middle-vertex defect flips, change at most once.


## Metadata

- ID: ternary_nor_decomposes_into_triangle_orientation_and_defect_vertex
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
