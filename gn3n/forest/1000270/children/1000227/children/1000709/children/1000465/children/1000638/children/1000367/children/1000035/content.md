# Absent a three-label crossing producer, the coupled graph has minimum degree six

## Statement

In the order-thirteen mu=6 shell, assume every Hamiltonian six-set has odd-graph degree at most two, equivalently assume the three-label synchronized-crossing producer from 1fd7f3a83b04 is absent. Let J be the Johnson-radius-three graph on nonisolated Hamiltonian six-sets. Then delta(J)>=6; equivalently the complementary deficient-support graph Gamma has minimum degree at least six.

## Body

Fix P in V(J), choose an odd-graph neighbor Q, and write p=deg_G(P), q=deg_G(Q), a=deg_J(P), b=deg_J(Q). By hypothesis 1<=p,q<=2.

The certified bridge theorem f79e0116afc6 gives at least
E >= 14-p-q
distinct odd-graph edges between the proper J-neighborhoods N_J(P) and N_J(Q).

We sharpen the left-side capacity bound. Every odd-graph neighbor A of Q other than P is a proper J-neighbor of P: indeed, if the edge Q-A has omitted label y in P, then A=(P-{y}) union {x}, where x is the omitted label of P-Q, so A shares five vertices with P. There are exactly q-1 such vertices A in N_J(P), and each already has the odd edge A-Q. Since Q is not a proper J-neighbor of itself, none of these q-1 edges is counted among the E bridge edges.

Every vertex of N_J(P) has odd-graph degree at most two. Summing odd degrees over the a vertices of N_J(P), the E bridge edges consume E incidences and the q-1 edges from N_J(P) to Q consume q-1 further incidences. Therefore
E+(q-1) <= 2a.
Combining with the bridge lower bound gives
14-p-q+q-1 <= 2a,
so
13-p <= 2a.
Since p<=2, 2a>=11 and hence a>=6.

As P was arbitrary, delta(J)>=6. Complementation is an isomorphism from J to the radius-three deficient-support graph Gamma, giving the equivalent conclusion there. ∎
