# Near-dangerous gap-one states force a macroscopic lens-free overlap of near-top maximum paths

## Statement

First, let R be a maximum endpoint path ending at y. Among all maximum endpoint paths Q ending at x, choose Q to maximize |V(Q) intersect V(R)|. Then Q and R contain no genuine clean internal lens with distinct Q- and R-sides.

Consequently, in the near-dangerous gap-one setting of 58659c428983 with delta=o(q), there exist two vertices x,y with
phi(x)=q-o(q),  phi(y)=q-o(q),
and maximum endpoint paths Q_x,Q_y ending at x,y such that
|V(Q_x) intersect V(Q_y)| >= (11/16-o(1))q,
while Q_x,Q_y contain no genuine clean internal lens.

Thus every asymptotically dangerous gap-one state contains a canonical residual object: two almost-q-long maximum paths with macroscopic intersection but no switchable internal lens.

## Body

For the normalization statement, suppose Q and R contain a genuine clean internal lens bounded by common vertices a,b. Let L_Q,L_R be its two distinct sides. Since both Q and R are maximum endpoint paths, 390e818020e1 gives
|L_Q|=|L_R|.
Replace L_Q inside Q by L_R. Cleanliness guarantees a linear path Q' ending at the same endpoint x, and the equality of side lengths gives |Q'|=|Q|=phi(x), so Q' is again maximum.

Every internal vertex of L_R belongs to R. By cleanliness, the interior of L_Q contains no vertex of R; otherwise there would be an additional common vertex inside the lens. Since the lens is genuine and the sides are distinct, replacing L_Q by L_R strictly increases the number of vertices shared with R (equivalently, after suppressing any shared boundary edge, at least one R-side vertex or edge is newly gained). This contradicts the choice of Q. Hence no such lens exists.

Now apply 58659c428983. It supplies two canonical maximum source rails R_1,R_2, of endpoint potentials q-o(q), sharing at least (11/16-o(1))q vertices. Fix R_2. Among all maximum paths ending at the endpoint of R_1, choose Q_x maximizing vertex overlap with R_2. Since R_1 itself is an admissible candidate,
|V(Q_x) intersect V(R_2)| >= |V(R_1) intersect V(R_2)|
>= (11/16-o(1))q.
Set Q_y=R_2. The normalization statement makes the pair lens-free, while their endpoint potentials remain the original rail lengths q-o(q).
