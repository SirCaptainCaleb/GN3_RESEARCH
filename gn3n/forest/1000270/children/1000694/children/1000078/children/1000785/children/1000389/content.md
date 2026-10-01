# Above order fourteen every Hamiltonian four-side escapes by descent, a Hamiltonian six-window, or order disagreement

## Statement

Let H be a minimum counterexample of order n>=15. Let W be any Hamiltonian four-vertex support and let H-W=P|Q be any two-cover. Then at least one of the following occurs:

(1) W|P|Q admits an explicit spanning three-cover with strictly smaller quadratic potential Phi;

(2) H contains a proper Hamiltonian six-vertex support U whose complement is non-Hamiltonian of path-cover number two;

(3) the local Hamiltonian-support comparison data expose explicit order disagreement.

Thus, above order fourteen, a Hamiltonian four-window with two-cover complement cannot be a structureless terminal frontier.

## Body

Apply the certified cross-endpoint exchange dichotomy 27a05b61e8c3.

In its shared-endpoint branch, apply 064902822993. This gives either a Hamiltonian six-set with path-cover-two complement, outcome (2), or order disagreement, outcome (3).

In its checkerboard branch, because |P|+|Q|=n-4>=11, at least one of P,Q has order at least six. Apply 92c86d754e08: all four displayed endpoints individually Hamiltonize W, and transferring an endpoint from a complementary path of order at least six into W changes Phi by 10-2m<=-2. This is outcome (1).

The two branches exhaust 27a05b61e8c3.
