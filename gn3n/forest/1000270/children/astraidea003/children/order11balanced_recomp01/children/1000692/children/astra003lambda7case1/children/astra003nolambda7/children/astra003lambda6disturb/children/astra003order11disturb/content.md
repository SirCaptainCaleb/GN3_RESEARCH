# Every hypothetical order-eleven counterexample exposes crossing or order disturbance

## Statement

Let H be a hypothetical order-eleven minimum counterexample. Then its maximum tight-path order is five or six. If it is five, every equitable 5|5|1 state exposes an internal mixed-support crossing or relative-order disagreement. If it is six, some endpoint-deletion exact two-cover of a longest six-path has at least two crossings across the longest-path/complement cut or exposes explicit relative-order disagreement. Thus no order-eleven branch remains without concrete transport disturbance.

## Body

Let (H) be a hypothetical minimum counterexample of order eleven, and let
[
lambda
]
be its maximum tight-path order.

The order-eleven longest-path reduction d324f9a5a0e2 gives
[
lambdain{5,6,7}.
]
The theorem astra003nolambda7 excludes
[
lambda=7.
]
Hence
[
lambdain{5,6}.
]

If
[
lambda=5,
]
then (H) has no tight path of order six. The certified internal non-clean deletion theorem in the order-eleven stress test 2ac31d8f3bb6 applies to every exact equitable deletion state
[
H-x=P|Q.
]
It gives an internal good deletion that is not the same-slot clean replacement, and the certified internal-deletion localization theorem therefore yields either:
- an ordinary path edge crossing between inherited support pieces; or
- relative-order disagreement with the inherited five-path order.

Thus the (lambda=5) branch always exposes explicit crossing/order disturbance.

Now suppose
[
lambda=6.
]
By astra003lambda6disturb, the neutral two-end exchange outcome of the codimension-five endpoint normalization is impossible: it would create a common-middle square whose endpoint barrier extends a longest six-path to order seven, contradicting astra003nolambda7.

Therefore the certified final endpoint normalization codim5_01 leaves only its first two outcomes:
- some endpoint-deletion exact two-cover has at least two ordinary edges crossing between the surviving longest-path vertices and the five-vertex complement; or
- an endpoint comparison exposes explicit relative-order disagreement.

Hence the (lambda=6) branch also always exposes concrete crossing/order disturbance.

Therefore every hypothetical order-eleven minimum counterexample lies directly on the endpoint-transport / defect-compression interface: there is no remaining neutral longest-path or disconnected-reconfiguration residue.
