# Linear height barrier for global ordered-pair transition ranks

- Stable ID: note_boundary_pair_rank_linear_height_barrier
- Author: unspecified; session provenance retained
- Primary home: section:nori_seven_coordinate_structure
- Labels: obstruction, rank_potential, boundary_tournament
- Lifecycle: resolved
- Epistemic status: proved
- Current version: 3
- Retention: current and at most one previous snapshot
- Created session: session_nori_r4981_3
- Updated session: session_nori_r4593_2
- Disposition: Mathematical result preserved as completed background; future use is as evidence or test of a common NORI1/boundary-tournament unification.
- Successor: none

## Related references

- subsection:layered_boundary_snakes_and_a_dense_rank_sensitivity_barrier
- subsection:coupled_chronological_saddle_potentials_and_checkerboard_obstructions

## Research note

# Linear height barrier for strict transition-rank certificates

## Theorem (finite graph version)

Let G=(V,E) be a finite simple graph with at least one edge. For every vertex v and distinct neighbors a,c of v, designate exactly one of the oriented length-two walks (a,v,c) and (c,v,a) as positive. Let rho(u,v) be an integer rank in {1,...,m} on every oriented edge uv. Assume that every positive triple (a,v,c) satisfies

rho(a,v) < rho(v,c).                                      (1)

Then

m >= 2|E|/|V|.                                            (2)

In particular, for every ordinary reversal-odd boundary 3-tournament on n vertices, ANY strictly increasing rank certificate on ordered terminal pairs uses at least n-1 distinct available levels.

## Proof

Fix v. Define D_v={a in N(v): rho(v,a)<=rho(a,v)}. For each a in D_v introduce the nonempty integer interval

I(v,a)=[rho(v,a),rho(a,v)] intersection {1,...,m}.

The intervals I(v,a), a in D_v, are pairwise disjoint. Indeed, if distinct a,c have a common integer t, then rho(v,a)<=t<=rho(a,v) and rho(v,c)<=t<=rho(c,v). Thus both candidate inequalities rho(a,v)<rho(v,c) and rho(c,v)<rho(v,a) fail. Yet exactly one of (a,v,c),(c,v,a) is positive, contradicting (1).

Consequently sum_{a in D_v}|I(v,a)| <= m for each v. Summing over v gives at most m|V|.

Consider one undirected edge {u,v}, and write x=rho(u,v), y=rho(v,u). If x<y, its only contribution to the preceding interval sum is the interval [x,y] at u, of length y-x+1>=2. If x>y, it contributes the analogous interval at v, again length >=2. If x=y, it contributes the singleton [x,x] at both endpoints, total length 2. Thus every undirected edge contributes at least two, and

2|E| <= sum_v sum_{a in D_v}|I(v,a)| <= m|V|.

This proves (2). No transitivity of the local comparison tournaments is assumed.

## Sharpness

For n even, take a proper (n-1)-edge-coloring of K_n (a 1-factorization). Put rho(u,v)=rho(v,u)=the edge color of {u,v}, regarded as a rank from 1 to n-1. At each center v, compare the distinct ranks of incident edges and designate the strictly increasing orientation positive. This is an ordinary boundary tournament and satisfies (1) with m=n-1, attaining equality.

More generally, a d-regular class-I graph with a proper d-edge-coloring attains m=d, so the graph bound is sharp across a broad family.

## Scope and research consequence

This is an exact obstruction to attempts to construct ordinary boundary tournaments with O(sqrt(n))-length positive paths by assigning O(sqrt(n)) global integer levels to ordered pairs and forcing every positive transition to increase its level. Such a construction is impossible even before imposing vertex simplicity or restricting to paths. The theorem does NOT prove long vertex-simple tight paths: an increasing walk of ordered-pair states can repeat original vertices. Moreover, many ordinary boundary tournaments have directed cycles in their ordered-pair transition digraph and hence admit no strict integer rank at all. The result gives no full-class improvement beyond the Devine-Milans square-root theorem, and makes no claim about unrestricted NORI1 edge colorings.

A useful next step is to formulate an obstruction/construction with ranks that may fall on a quantitatively controlled exceptional family of transitions, preserving explicit predecessor-path witnesses; any stronger universal long-path deduction must exploit the joint realizability of those witness paths rather than only scalar pair ranks.

## Editorial disposition: single unified goal

Proved rank-height obstruction preserved. This closes the isolated transition-rank investigation as a NORI research direction; the rank theorem provides a diagnostic for candidate common rank/selection mechanisms. Explore its consequences within a concrete shared object and compare its honest path-witness specializations in NORI1 and ordinary boundary tournaments.
