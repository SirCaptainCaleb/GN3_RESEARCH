# Equivariant domination compresses reachability labels and preserves the full topological obstruction

Let c be an antipodally odd binary edge coloring of Q_n. Define the uncolored symmetric reflexive relation x~z iff z belongs to R(x), meaning that a monochromatic geodesic of either color joins x,z. Antipodal complementation tau is an automorphism of this relation. Let G be its reflexive graph.

For a tau-invariant set W of actual cube vertices, let G_W be the INDUCED graph and N_W(x)=R(x) intersect W. Edges of G_W always retain their original monochromatic geodesic witnesses in Q_n; a witness may pass through cube vertices outside W. Define
K_W={sigma subseteq W : sigma subseteq N_W(x) for some x in W}.
Thus K_W is the abstract complex whose simplices have a common monochromatically reachable root, allowing different colors for different targets.

THEOREM 1 (paired domination fold). Suppose u,v belong to W, v is outside {u,tau u}, and N_W(u) is contained in N_W(v). Set W'=W\{u,tau u}. Define f(u)=v, f(tau u)=tau v, and f(x)=x otherwise. Then:
(a) f:G_W -> G_W' is an equivariant graph retraction.
(b) There exists x in W with N_W(x) intersect N_W(tau x) nonempty if and only if the analogous condition holds in W'.
(c) K_W' is the induced subcomplex K_W[W'], and its realization is an equivariant strong deformation retract of |K_W|.

Proof. Equivariance gives N_W(tau u) subseteq N_W(tau v). For every s in W we have N_W(s) subseteq N_W(f(s)). If a~b, symmetry and these two inclusions imply f(a)~b and then f(a)~f(b), proving (a). A common neighbor z of x,tau x maps to the common neighbor f(z) of f(x),tau f(x). Conversely all vertices and edges retained in the induced graph are original ones; this proves (b).

For (c), if sigma subseteq N_W(x), each s in sigma satisfies x~s, hence x~f(s). Therefore sigma union f(sigma) is a simplex of K_W. The identity and f are contiguous simplicial maps. A simplex sigma of K_W whose vertices lie in W' has some root x; if x was removed, N_W(x) subseteq N_W(f(x)), so the same sigma has a root in W'. This proves K_W'=K_W[W']. In the standard geometric realization, H_t(p)=(1-t)p+t|f|(p) stays in a simplex containing sigma union f(sigma). It is equivariant, fixes |K_W'| pointwise, and at t=1 is the retraction. QED.

If instead N_W(u) subseteq N_W(tau u), reflexivity immediately gives u~tau u, an actual monochromatic antipodal geodesic. Thus an iterative procedure either exposes closure or can delete an antipodal pair of dominated vertices. It terminates after finitely many deletions at an equivariant core with no further permitted domination. Every stage preserves the antipodal-overlap criterion, hence the existence of a monochromatic antipodal geodesic after the standard one-switch rotation.

Under hypothetical failure of closure, no simplex of K_W contains an antipodal pair: such a simplex would put z,tau z in N_W(x) for some root x, giving closure. Consequently the tau-action on K_W is free. The paired folds preserve its complete equivariant homotopy type, including any equivariant index used in a topological argument.

THEOREM 2 (single-stage maximal-neighborhood compression). In the original graph choose one representative of each distinct inclusion-maximal neighborhood R(z), pairing choices under tau. If a neighborhood class is tau-fixed, R(z)=R(tau z) already yields closure. Otherwise representatives can be chosen equivariantly. Map each target z to a representative m(z) with R(z) subseteq R(m(z)), taking m to fix representatives and to commute with tau. Such choices exist by finiteness. Then for every root x, m(R(x)) is contained in R(x). For every finite family of roots X,
intersection_(x in X) R(x) is nonempty
iff
intersection_(x in X) (R(x) intersect D) is nonempty,
where D is the representative set.

Indeed, a common target z can be replaced by m(z): symmetry gives x in R(z) subseteq R(m(z)) for every x in X, hence m(z) in every R(x). Thus this first compression preserves ALL intersections of the reachability family, not only antipodal ones. The same contiguity argument identifies the reduced reachability complex with an equivariant strong deformation retract.

After this first stage, additional domination may emerge in induced graphs and permit further paired folds. At these later stages one retains the global overlap equivalence of Theorem 1; root and target witnesses may move to remaining physical vertices. No artificial reachability edges are introduced.

COMPRESSION FRONTIER. If the final core has 2m vertices and closure has not occurred, its complex is an invariant subcomplex of the boundary of the m-dimensional crosspolytope, one signed coordinate per remaining antipodal vertex pair. This is an honest reduced label space, and every forced antipodal overlap still extracts actual geodesics. What remains open is a dimension-independent bound or structural obstruction on cores arising from cube geodesic reachability, sufficient for a topological forcing theorem. No bound in terms of n is established here.

Finite verification checked all 512 antipodally invariant reflexive graphs on three antipodal pairs, including all 1728 permitted paired folds, confirming overlap equivalence, induced-complex equality, and simplicial contiguity. The proofs above apply to every finite reflexive symmetric relation with a free involution.
