# The order-six endpoint-hard branch gives order disagreement or a neutral four-side migration

## Statement

Let H be a boundary tournament and let X|P|Q be a spanning three-cover, where |X|=4 and P=(p_1,p_2,p_3,p_4,p_5,p_6) is a tight path. Suppose H[X union {p_1}] and H[X union {p_6}] are both non-Hamiltonian. Put U=X union {p_1,p_6} and M=(p_2,p_3,p_4,p_5). Then either (1) H[U] is non-Hamiltonian, in which case the four Hamiltonian five-sets U-{x}, x in X, force relative-order disagreement between Hamilton paths on two distinct such deletions; or (2) H[U] is Hamiltonian, in which case replacing X|P by U|M is a legal pairwise repartition with the same quadratic potential. Thus in outcome (2) the four-side migrates from X to the inherited interior M of P while the component-order multiset {4,6} is preserved.

## Body

By the four-of-six theorem in smallset01 applied to U, at least four one-vertex deletions of U are Hamiltonian. The deletions U-{p_1}=X union {p_6} and U-{p_6}=X union {p_1} are non-Hamiltonian by hypothesis, so every deletion U-{x}, x in X, is Hamiltonian. If H[U] is non-Hamiltonian, astra004fourgooddisagree applied to these four good deletion labels gives relative-order disagreement between Hamilton paths on two distinct sets U-{x}. If H[U] is Hamiltonian, M is an inherited tight path and U is a Hamiltonian support, so U|M is a legal pairwise repartition of X|P. The old pair contribution to quadratic potential is 4^2+6^2=52 and the new contribution is 6^2+4^2=52. Hence the move is Phi-neutral and replaces the old four-side X by the interior four-path M.