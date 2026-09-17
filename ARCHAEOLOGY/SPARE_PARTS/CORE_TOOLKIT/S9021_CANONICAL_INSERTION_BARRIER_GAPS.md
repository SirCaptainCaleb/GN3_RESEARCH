# S9021 — Canonical Barrier Gaps for Noninsertable Vertices in an Edge-Ordered Path

## Theorem

Let G be an edge-ordered graph and let Q=(q_0,...,q_m), m>=1, be an increasing path. Let x be a vertex outside Q adjacent to every q_i. For 0<=i<=m-1, call the gap i right-feasible if either i=m-1 or the edge xq_{i+1} precedes q_{i+1}q_{i+2}; call it left-feasible if either i=0 or q_{i-1}q_i precedes q_i x. Assume that inserting x between q_i and q_{i+1} never gives an increasing path, for any i. Then some gap is simultaneously left- and right-feasible, and at every such gap the middle spoke pair is reversed: xq_{i+1} precedes xq_i. In particular, if beta(x) is the least right-feasible gap, then beta(x) is also left-feasible and xq_{beta(x)+1}<xq_{beta(x)}. Moreover, for two such noninsertable vertices x,y, if beta(x)<beta(y), then at the rail vertex q_{beta(x)+1} one has xq_{beta(x)+1}<q_{beta(x)+1}q_{beta(x)+2}<yq_{beta(x)+1}; consequently the ordered turn (x,q_{beta(x)+1},y) is tight in the boundary tournament induced by the edge order. Thus any family of noninsertable exterior vertices carries a canonical barrier preorder, with strict barrier separation witnessed by a graph-intrinsic cross turn.

## Proof

Write e_i=q_iq_{i+1} for the Q-edges, so e_0<e_1<...<e_{m-1}. For a fixed exterior x define L_0=true and, for i>=1, L_i to mean e_{i-1}<q_i x. Define R_{m-1}=true and, for i<=m-2, R_i to mean xq_{i+1}<e_{i+1}. Suppose for contradiction that no i has both L_i and R_i. Since L_0 holds, R_0 fails. If i<m-1 and L_i holds while R_i fails, then e_{i+1}<xq_{i+1}; because e_i<e_{i+1}, we get e_i<xq_{i+1}, which is exactly L_{i+1}. Inductively L_{m-1} holds, but R_{m-1} is true by definition, contradiction. Hence some gap i has both outer seam inequalities. At such a gap, inserting x between q_i and q_{i+1} would be increasing unless the middle comparison q_i x < xq_{i+1} fails: the preceding turn is certified by L_i when present and the following turn by R_i when present. By hypothesis the insertion is not increasing, so totality of the edge order gives xq_{i+1}<q_i x. Now let beta(x) be the least right-feasible gap. For every j<beta(x), R_j fails. Starting from L_0 and using the same propagation shows L_{beta(x)}; the preceding argument then gives xq_{beta(x)+1}<q_{beta(x)}x. Finally suppose beta(x)<beta(y). Then beta(x)<=m-2. At i=beta(x), R_i(x) gives xq_{i+1}<e_{i+1}, while minimality of beta(y) makes R_i(y) false and hence e_{i+1}<yq_{i+1}. Therefore xq_{i+1}<e_{i+1}<yq_{i+1}, so in the edge-order boundary relation (x,q_{i+1},y) is tight. This proves all claims.

## Why this is reusable

Failed literal insertion is compressed to one canonical barrier index per exterior vertex, and strict separation of barrier indices produces an intrinsic cross turn. This replaces a diffuse insertion-failure array by a scalar obstruction.

## Scope and nonclaims

The result requires an edge order and literal noninsertability into the displayed path order. It does not apply to arbitrary non-edge-orderable boundary tournaments and does not itself produce a path cover.

## Provenance

Rescued from accepted archived result `R895`.
