# NOR reversal is antipodality on the simplex-boundary Coxeter sphere

**Summary:** The completed cube places all coordinate orders on a standard antipodal sphere: permutations are chambers of sd(boundary simplex), and reversing a permutation is exactly subset complementation on that sphere.

## Statement

In the Freudenthal cube-to-simplex completion, the macroface opposite the distinguished vertex e_0 is sd(Delta^{n-1}); the link of its full-face barycenter is sd(boundary Delta^{n-1}), an (n-2)-sphere. Coordinate permutations are its chambers, and subset complementation sends the chamber of pi to the chamber of pi^rev. Thus reversal-odd NOR window data live canonically on an antipodal Coxeter sphere.

## Body


## The Coxeter sphere inside the completed simplex

Use the exact simplex realization of the completed Freudenthal cube.

The macroface B_0 opposite e_0 has vertices a_i for singleton faces {i}, together with cube vertices S of size at least two, which are barycenters of faces S. Hence B_0 is exactly sd(Delta^{n-1}).

Let b_[n] be the vertex corresponding to the full coordinate set. Every top simplex of B_0 contains b_[n], and

L_n = lk(b_[n],B_0) = sd(boundary Delta^{n-1}),

an (n-2)-sphere.

A maximal simplex of L_n is a chain
{pi_1} subset {pi_1,pi_2} subset ... subset {pi_1,...,pi_{n-1}},
so chambers are exactly coordinate permutations pi=(pi_1,...,pi_n).

Subset complementation c(S)=[n] minus S reverses inclusion. Applied to the displayed chain and reordered increasingly, it gives the chamber of pi^rev=(pi_n,...,pi_1). Thus c is the free simplicial reversal involution on L_n; it is PL-conjugate to the ordinary antipodal map on S^{n-2}.

A coordinate window (pi_i,...,pi_{i+r-1}) appears as a consecutive-rank chain of prefixes inside the permutation chamber. Complementation sends it to the corresponding reversed window. Therefore a reversal-odd coordinate label h is precisely an odd binary labeling of these distinguished consecutive-rank faces.

Directed NOR is consequently the following sphere problem: find a chamber of this antipodal Coxeter sphere whose ordered sequence of distinguished window faces changes color at most once. A counterexample would give an odd coloring in which every chamber contains both change directions.

This places the exact NOR obstruction in a standard setting for Tucker/Ky Fan, equivariant chains, and simplex connector arguments. The remaining issue is to exploit that the colored faces occur at consecutive ranks rather than as an arbitrary face coloring.


## Metadata

- ID: nor_reversal_is_antipodality_on_the_simplex_boundary_coxeter_sphere
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
