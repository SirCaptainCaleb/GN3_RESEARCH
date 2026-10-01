# The hard endpoint branch retains four Hamiltonian five-supports and four synchronized non-Hamiltonian residuals

## Statement

Let H be a boundary tournament and X|P|Q a spanning three-cover, with |X|=4 and P=(p1,...,pm), m>=6. Put a=p1, b=pm and M=(p2,...,p(m-1)). Either one pairwise repartition of X|P strictly decreases quadratic potential, or both X+{a}, X+{b} are non-Hamiltonian and, for every t in X, F_t=(X-{t}) union {a,b} is Hamiltonian while L_t=V(M) union {t} is non-Hamiltonian. In the latter case there are distinct x,y,z in X for which W={a,b,x,y} and W'={a,b,x,z} are Hamiltonian; their five-vertex union is Hamiltonian. If H is a minimum counterexample, every Hamiltonian support displayed has a non-Hamiltonian complement of path-cover number two, and every L_t has path-cover number two. In particular this alternative applies to the double-wrap three-cover from any deletion cover in a minimum counterexample of order at least fifteen, choosing a complementary path of order at least six.

## Body

Write |P|=m. If X+{a} or X+{b} is Hamiltonian, replace X and P by that Hamiltonian five-set and the inherited endpoint truncation of P. The orders change from (4,m) to (5,m-1), and the change in quadratic potential is 25+(m-1)^2-16-m^2=10-2m<0.

Otherwise both endpoint five-extensions are non-Hamiltonian. Apply two_bad_five_extensions_all_opposite01 to X,a,b. It makes all four sets F_t Hamiltonian, not just a selected union of overlap witnesses. For every t, F_t and L_t are disjoint and partition X union V(P). If any L_t is Hamiltonian, they give the same strict descent of component orders (5,m-1). Consequently absence of these descents forces all four L_t to be non-Hamiltonian simultaneously, with the same displayed tight middle path M.

Apply two_bad_five_extensions_adjacent_four01 to obtain W,W'. Their union is F_t for the fourth vertex t of X, so it is Hamiltonian already. A non-Hamiltonian-five-set alternative is impossible in this producer configuration.

For a minimum counterexample, mincex01 gives path-cover number two for every proper non-Hamiltonian L_t and a non-Hamiltonian path-cover-two complement for every proper Hamiltonian support. The supports here have at most five vertices and the ambient order exceeds ten, so they are proper. Finally d26d8171978f gives a double-wrap three-cover S|R|T with |S|=4 and |R|+|T|=n-4. For n>=15 one of R,T has order at least six, and the first assertion applies. All descents are actual pairwise repartitions of the displayed pair; no independent cover on another support is asserted reachable.

This theorem preserves the whole common middle path. The residuals L_t are not Hamiltonian merely because M is a path; their simultaneous non-Hamiltonicity is the unresolved attachment constraint. The analogous residual obstruction at global quadratic minima is already present in 8ea5d1ada257. The new use is earlier, without global minimality, and excludes the non-Hamiltonian-overlap branch of endpoint_overlap_pc2_star01 when that consumer is reached through the bad-endpoint producer.