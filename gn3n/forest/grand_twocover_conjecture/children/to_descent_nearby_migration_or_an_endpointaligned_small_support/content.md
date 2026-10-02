# Four-window transport compresses to descent, nearby migration, or an endpoint-aligned small support

## Statement

Let H be a minimum counterexample, let W be a Hamiltonian four-set, and let H-W=P|Q be a two-cover. Then at least one of the following holds.

(1) |V(H)|<=14.

(2) The anchored three-cover W|P|Q admits an endpoint-transfer repartition of strictly smaller quadratic potential.

(3) The bounded transport alternative of four_window_transport15 occurs: there are a three-set D, one displayed endpoint e of one complementary path, and both displayed endpoints f,g of the other such that D union {e,f} and D union {e,g} are Hamiltonian five-sets, with the associated six-set carrying the one- and two-label path-cover-two transport data of four_window_transport_allorders01. Moreover this branch can always be sharpened further to one of:
  (3a) a Hamiltonian four-set W1 with non-Hamiltonian path-cover-two complement and |W intersect W1|=3; or
  (3b) an endpoint-aligned small support: either a Hamiltonian four-set Z containing e,f,g with non-Hamiltonian path-cover-two complement, or a Hamiltonian five-set S with non-Hamiltonian path-cover-two complement and a Hamilton path whose two endpoints both lie in {e,f,g}.

Thus above order fourteen an anchored Hamiltonian four-window cannot terminate in an unstructured order-disagreement residue: it either descends, moves to a distance-one four-window, or produces an explicitly endpoint-aligned Hamiltonian support of order four or five.

## Body

Apply four_window_transport15. Its small-order and strict endpoint-transfer outcomes give (1) and (2), while its remaining outcome is exactly the bounded six-vertex transport package recorded in four_window_transport_allorders01.

In that bounded branch, apply the shared-endpoint fork compression used in migration_is_distanceone_or_a_paired_oppositeend_fork. If one of the three one-endpoint replacements is Hamiltonian, minimum-counterexample calculus gives a Hamiltonian four-set W1 at Johnson distance one from W whose complement is non-Hamiltonian with path-cover number two, giving (3a). Otherwise two Hamiltonian four-windows W_f and W_g share a three-core and contain e together with the opposite displayed endpoints f,g.

Write A for their common two-vertex part inside D and C=A union {e}. Then W_f=C union {f} and W_g=C union {g}. Apply the adjacent-four-window lemma fourwindows_force_a_pc2_square_or_a_twolabel_core_fan. If the five-set C union {f,g} is non-Hamiltonian, that lemma gives at least two Hamiltonian four-deletions with path-cover-two complements; at most one deletes e, so one deletion keeps e,f,g, producing the four-set Z in (3b). If the five-set is Hamiltonian, its complement is non-Hamiltonian with path-cover number two. Unless deleting one of the two vertices of A is already Hamiltonian (again producing such a Z), both of those deletions are non-Hamiltonian. Therefore no Hamilton path of the five-set can have an endpoint in A, because deleting a displayed endpoint of a Hamilton path leaves a Hamilton path. Hence both displayed endpoints lie in {e,f,g}, producing the five-set alternative of (3b).

This combines the original bounded transport information with its endpoint-positioned consequence, so no sequential migration residue remains.