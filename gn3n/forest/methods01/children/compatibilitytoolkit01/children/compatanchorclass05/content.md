# Anchored incompatibility splits into support switches and near-label transport

## Statement

Let F_d=P|Q be a chosen deletion cover of H-d, and let a,b be distinct neighbors of d in the compatibility graph. For each neighbor y in {a,b}, compatibility of F_y with F_d implies that in F_y the restored label d lies in the same support class in which y lies in F_d, and its insertion slot is equal or adjacent to the reinsertion slot of y in the corresponding anchor path with y deleted. Consequently, if a and b lie in different paths of F_d, then F_a and F_b are support-incompatible on V(H)-{a,b}, with d switching between the two anchor support classes. If a and b lie in the same path of F_d, then F_a and F_b are support-compatible; if they are incompatible, their disagreement is purely relative order involving d, and the two positions of d are each localized to the equal-or-adjacent slot neighborhood of a and b respectively.

## Body

# Proof

Fix y in {a,b}. Since F_y and F_d are compatible, apply the certified compatible-pair normal form from d43a7c9e2f61 to the pair of deletion labels d,y.

On their common domain V(H)-{d,y}, the two covers have two common ordered support classes. The omitted labels d and y restore into the same one of those classes, and their restoration slots are equal or adjacent. Viewed from the fixed anchor cover F_d, the restored vertex y simply occupies its displayed location in whichever anchor path P or Q contains y. Therefore in F_y the restored label d lies in that same anchor support class, and its insertion slot in the path with y deleted is equal or adjacent to the slot into which y is restored in F_d.

Now compare a and b.

If a and b lie in different paths of F_d, then the preceding paragraph puts d in the P-class in one of F_a,F_b and in the Q-class in the other. All pair data not involving d agree after deleting d, by compatanchorlocal03. Thus F_a and F_b are support-incompatible, and the support disagreement is exactly the switch of d between the two anchor classes.

If a and b lie in the same path of F_d, then in both F_a and F_b the restored label d lies in that same anchor support class. Every vertex other than d retains the anchor support relation, so the two covers are support-compatible. If a,b is a nonedge of the compatibility graph, compatanchorlocal03 says the remaining disagreement must involve d. Since the support relation agrees, the disagreement is in relative order. The compatible-pair normal form already localizes the position of d in F_a to an equal-or-adjacent slot around the position of a, and similarly localizes its position in F_b around b.

Hence every anchored incompatibility has one of two canonical descriptions relative to F_d: d switches anchor support classes, or d stays on one anchor path but appears near two different deleted-label positions.
