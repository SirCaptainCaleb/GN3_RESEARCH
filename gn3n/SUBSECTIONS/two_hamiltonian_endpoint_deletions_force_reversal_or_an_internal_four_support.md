# Two Hamiltonian endpoint deletions reduce to reversal or an order-four rail

## Metadata

- ID: two_hamiltonian_endpoint_deletions_force_reversal_or_an_internal_four_support
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 189
- Row version: 2
- Development version: 2
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Let H be a minimum-order counterexample. Let S be a fixed Hamiltonian support and put G=H-S. Let a,b be distinct vertices of G such that G-a and G-b are Hamiltonian.

Choose deletion covers H-a=S|R_a and H-b=S|R_b using the same displayed Hamilton order on S.

After restricting to H-{a,b}, both covers have support partition S | (G-{a,b}).

If their induced orders on G-{a,b} disagree, this is the order-disagreement/reversal interface.

Assume they agree, with common Hamilton order C.

By the insertion-slot theorem, a and b insert into equal or adjacent slots of C.

Adjacent slots force a reversing tight triple.

An equal endpoint slot gives a spanning two-cover of H, impossible.

Suppose the equal slot is internal, between consecutive vertices u,v of C. Then (u,a,v) and (u,b,v) are tight, so {u,v,a,b} is a Hamiltonian four-support K.

By minimum-counterexample minimality, pc(H-K)=2.

Moreover K is localized in the common Hamilton path: deleting the consecutive pair u,v from C leaves at most two contiguous residual intervals C_1,C_2. Hence
H-K = S | C_1 | C_2
is an inherited three-cover.

Apply [[every_seam_reseed_is_support_preserving_or_exposes_a_cross_residual_reversal]] to K. Either C_1,C_2 concatenate, yielding H-K=S|R and therefore H-S=K|R with an order-four complementary rail, or an endpoint of one residual interval reverses an exposed end edge of the other.

Therefore two Hamiltonian endpoint deletions of the same maximal-support complement reduce entirely to:
- a positioned reversal/order disagreement; or
- a complementary two-cover of S with one component of order four.

There is no independent internal-four-support residue.
