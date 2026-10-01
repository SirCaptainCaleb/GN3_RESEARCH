# Good-residue spanning cores have two-hole alternate entrance witnesses

## Statement

Let H have 2ell-1 vertices and a spanning (ell-1)-edge path ending in a nonspecial edge e. If deleting either free vertex a of the first path edge yields an all-special graph H-a, then H-a contains an alternate (ell-2)-edge longest path Q_a ending in e through an entrance different from the unique entrance in H. The path Q_a misses exactly two vertices of H, and every edge at either opposite endpoint of Q_a is a single or double blocker on Q_a, with at most two single blockers. Consequently, under induction, this applies to both free first-edge vertices when ell is 0 or 2 mod 3.

## Body


Let P=(g_1,...,g_{\ell-2},e) be the spanning path, where e is nonspecial and is entered through x. Let a,b be the two vertices of g_1\g_2.

Fix a. Since a lies only in g_1 among the path edges, deleting a removes g_1 but leaves
  P_a=(g_2,...,g_{\ell-2},e),
an (\ell-2)-edge path ending in e through x.

The graph H-a has 2\ell-2 vertices, so every linear path in H-a has at most \ell-2 edges. Hence P_a is a longest path in H-a ending in e and phi_{H-a}(e)=\ell-2.

By hypothesis H-a is all-special, so e is special in H-a. Since phi_{H-a}(e)>=2, the unique-longest-entrance characterization implies that there is another longest (\ell-2)-edge path Q_a ending in e whose entrance label x_a differs from x.

Because an (\ell-2)-edge linear 3-uniform path uses exactly 2\ell-3 vertices, Q_a omits exactly one vertex r_a of H-a. Thus
  V(H)\V(Q_a)={a,r_a}.

Now consider either free last vertex u of the first edge of Q_a. If an edge f through u distinct from that first edge met V(Q_a) only at u, then f,Q_a (with Q_a oriented from u toward e) would be an (\ell-1)-edge path in H ending in e with entrance x_a != x. This contradicts nonspeciality of e in H, since phi_H(e)=\ell-1.

Therefore every edge through either opposite endpoint u of Q_a, other than the first edge of Q_a, has at least one additional contact with V(Q_a). Since only a and r_a lie outside Q_a, every such incident edge is either:
- a single-blocker edge: one additional Q_a-contact and one vertex in {a,r_a}; or
- a double-blocker edge: two additional Q_a-contacts.
By linearity, the single blockers at a fixed endpoint use distinct outside vertices, so there are at most two of them.

The same argument with b deleted gives an (\ell-2)-edge alternate witness Q_b with entrance x_b != x, omitting exactly one additional vertex r_b, and the identical two-hole endpoint blocker normal form.

If the dense-core conjecture is known for \ell-1 and \ell is congruent to 0 or 2 modulo 3, then 39ff078cd8f1 supplies the hypothesis that both H-a and H-b are all-special. Thus every hypothetical spanning top-rank counterexample in those residue classes carries two alternate near-spanning witnesses Q_a,Q_b with distinct-from-x entrance labels and only two outside vertices each.
