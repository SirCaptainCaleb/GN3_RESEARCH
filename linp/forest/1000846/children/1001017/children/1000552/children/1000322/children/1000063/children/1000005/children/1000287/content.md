# Punctured-Steiner boundary all-special conjecture

## Statement

For every d>=3, every d-regular linear 3-uniform hypergraph H on 2d+2 vertices with global maximum linear-path length d is all-special. Equivalently, every one-point puncture of an STS(2d+3) whose longest linear path has d edges has every edge special.

## Body

This conjecture is the direct infinite generalization of the 12-vertex Class-III theorem ffa00b5a307c.

The current human reductions are already uniform in d:

1. efe44a01f2dc: every such H is a punctured Steiner system with perfect-matching leave. A hypothetical maximum-rank nonspecial edge e gives a residual hypergraph R on 2d-1 vertices with degree profile
(d-2)^3,(d-3)^(2d-4),
two terminal perfect matchings with mutual forbidden (d-2)-edge endpoint paths, and a path-relative double-blocker union with only one or two open alternating components.

2. e6c8f5225c3f: the complement of the residual 2-shadow is exactly the disjoint union of the three deleted-star matchings and the surviving leave matching. Thus the residual obstruction is a canonically four-colored leave problem, not an arbitrary partial Steiner system.

3. ffbd337476d6: the alternating defects are exactly saturated. There is one single blocker and one unused precursor vertex per open alternating component, with no slack.

4. ba1f1d706d77: there are only two global defect topologies: one open alternating chain, or two open chains plus a canonical terminal 3-cycle.

5. 6cefae015b36: every terminal single-blocker defect is either genuinely early on the longest path or is pinned to the private vertex of the penultimate precursor edge.

For d=5, the residual low vertices have degree two, allowing ffa00b5a307c to finish by explicit residual matching classification. The general problem is to replace that degree-two classification by an expansion/uncrossing argument on the saturated chain endpoint(s).

A proof of this conjecture would generalize the strongest part of the order-12 humanization and would verify the global nonspecial-edge inequality 3delta<=2L+2 on the entire critical family delta=L=d, n=2d+2.