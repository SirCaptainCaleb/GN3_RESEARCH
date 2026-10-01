# High compatibility degree forces many support switches or many same-path relocations

## Statement

Let d have compatibility degree k, and let F_d=P|Q. Then there exist a neighbor a of d and a set B of at least ceil((k-3)/2) further neighbors b of d, all incompatible with a, such that one of the following holds uniformly for all b in B: (i) a and b lie in different paths of F_d, so every pair F_a,F_b is support-incompatible solely because d switches between the two anchor support classes; or (ii) a and b lie in the same path of F_d, so every pair F_a,F_b is support-compatible and their incompatibility is solely a relative-order relocation of d, with d restored in F_a near a and in F_b near b in the anchor order.

## Body

# Proof

By compatanchedburst04 there is a neighbor a of d and a set B_0 of at least k-3 other neighbors b of d such that a and b are incompatible for every b in B_0, and every such incompatibility is localized at d.

Partition B_0 according to whether b lies in the same path of the fixed anchor cover F_d as a or in the other path. One class has size at least ceil((k-3)/2); call it B.

For every b in B, apply compatanchorclass05.

If B is the opposite-path class, then a and b lie in different anchor paths for every b in B. Thus F_a and F_b are support-incompatible, and the only support disagreement is that d belongs to different anchor support classes in the two covers.

If B is the same-path class, then a and b lie in one fixed anchor path for every b in B. Thus F_a and F_b are support-compatible. Since they are incompatible, their disagreement is purely relative order involving d. The compatible-pair normal form localizes the position of d in F_a to the equal-or-adjacent slot neighborhood of a and its position in F_b to the equal-or-adjacent slot neighborhood of b.

Hence high compatibility degree cannot remain amorphous: after choosing one compatible partner a, a linear subfamily has one uniform mechanism, either repeated support switching of d across the two anchor paths or repeated transport of d along one fixed anchor path.