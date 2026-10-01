# Every retained whole chord spans another common vertex in the lens-free braid

## Statement

In the setup of 3ef8a7c2d941, let Q,R be the two lens-free near-top maximum endpoint paths and let e_i={x_i,v,u_i} be one of the retained early distinguished edges whose whole pair {x_i,u_i} lies in V(Q)∩V(R). Then x_i and u_i are not consecutive common vertices on both rails simultaneously. Equivalently, at least one of the two Q- or R-segments between x_i and u_i contains a third vertex of V(Q)∩V(R) in its interior. Hence all (25/88-o(1))q retained whole distinguished pairs span nontrivial common-vertex structure in the normalized braid.

## Body

Fix one retained whole pair {x,u} from an early distinguished edge e={x,v,u}. In 3ef8a7c2d941 the host paths Q,R are obtained from final source rails, while e belongs to the earlier distinguished family; thus x,u are internal vertices of both Q and R, and v is absent from both rails. Since H is linear, x and u cannot lie together on one path edge of Q or R: otherwise that path edge and e would share the two vertices x,u while being distinct (e contains v, which is absent from the rail). Suppose for contradiction that the open Q-segment between x and u contains no R-vertex and the open R-segment between x and u contains no Q-vertex. Then the two x-u segments have internally disjoint vertex sets. They are distinct, because if they shared a path edge then every vertex of that edge would be common and one would lie in the interior. Therefore x,u bound a genuine clean internal lens with distinct Q- and R-sides. This contradicts the lens-free conclusion of 3ef8a7c2d941. Hence at least one open segment contains a third common vertex. Applying this to every retained whole distinguished pair gives the final packet statement.
