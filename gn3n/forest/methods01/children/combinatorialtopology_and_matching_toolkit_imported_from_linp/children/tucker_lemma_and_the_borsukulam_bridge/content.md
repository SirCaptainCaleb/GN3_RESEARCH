# Tucker lemma and the Borsuk--Ulam bridge

## Statement

Tucker's combinatorial lemma is the antipodal analogue of Sperner: an antipodally labeled triangulated ball must contain a complementary edge. It is equivalent to the no-antipodal-extension form of Borsuk--Ulam and supplies a finite sign-label obstruction well suited to combinatorial state spaces.

## Body


Classical form. Let K triangulate B^d, with its boundary triangulation invariant under x->-x. Label vertices by {+/-1,...,+/-d}, with lambda(-v)=-lambda(v) on boundary vertices. Then some edge uv is complementary:
  lambda(u)=-lambda(v).

Source for a constructive proof: Robert M. Freund and Michael J. Todd, "A constructive proof of Tucker''s combinatorial lemma", J. Combinatorial Theory A 30 (1981), 321--325, DOI 10.1016/0097-3165(81)90027-3.
Publisher: https://www.sciencedirect.com/science/article/pii/0097316581900273

Clean equivalence with Borsuk--Ulam.

Borsuk--Ulam/no-antipodal-extension => Tucker. Suppose a Tucker labeling has no complementary edge. Send a vertex labeled +i to e_i and one labeled -i to -e_i, and extend linearly on each simplex. Because vertices of a simplex are pairwise adjacent, no simplex contains both +i and -i. Hence 0 is not in the convex hull of its label vectors: coordinatewise cancellation to 0 would require both signs of some coordinate. Normalize the piecewise-linear map to obtain
  g:B^d -> S^{d-1}.
On the boundary the labeling is antipodal, hence g(-x)=-g(x), contradicting the no-antipodal-extension form of Borsuk--Ulam.

Tucker => no-antipodal-extension. Suppose instead that a continuous g:B^d->S^{d-1} is antipodal on the boundary. Choose a sufficiently fine antipodally symmetric triangulation. At each vertex v choose an index i where |g_i(v)| is maximal and label v by sign(g_i(v))*i, with an antipodally consistent tie rule on the boundary. Tucker gives an edge uv labeled +i,-i. Since max_j|g_j(w)|>=1/sqrt(d), we have g_i(u)>=1/sqrt(d) and g_i(v)<=-1/sqrt(d). For a sufficiently fine mesh, uniform continuity makes such a jump across one edge impossible. Contradiction.

Constructive proof note. Freund--Todd do more than derive Tucker topologically: they give a finite path-following/pivoting proof based on Reiser''s algorithm. The exact pivot bookkeeping is useful algorithmically but not currently LINP-specific, so it is linked rather than reproduced line by line.

Useful poset/octahedral variant. A common equivalent formulation labels nonzero sign vectors x in {-,0,+}^d antipodally. Under a monotonicity/no-complementary-pair condition along comparable sign vectors, at least d label magnitudes are required. This is often the easiest form to match to a discrete state poset.

LINP relevance. If a path-state can be encoded by a sign vector recording which side of d local cuts/choices is active, path reversal or complementary construction may provide the antipodal involution. Tucker then says that avoiding a local complementary pair is impossible once the labeling dimension is too small. This is a natural finite certificate to seek before importing any chain-level topology.
 