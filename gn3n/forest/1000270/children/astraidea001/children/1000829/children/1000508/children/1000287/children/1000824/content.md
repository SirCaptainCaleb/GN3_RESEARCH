# Four pairwise support-incompatible deletion covers force a common-core support disagreement

## Statement

Let H be a boundary tournament and let F_a,F_b,F_c,F_d be two-covers of H-a,H-b,H-c,H-d. Assume the covers are pairwise support-incompatible and U=V(H)-{a,b,c,d} is nonempty. Then some triple among {F_a,F_b,F_c,F_d} has two members inducing different support partitions on its common three-deletion core. In particular, in the sharp half-order shell with lambda>=3, four pairwise support-incompatible lambda|lambda deletion covers necessarily contain such a triple.

## Body

Suppose for contradiction that every three-cover subfamily takes the common-core switch alternative of compattriplesupport14.

Apply that alternative to F_a,F_b,F_c. On W_c=V(H)-{a,b,c}, the restrictions of F_a and F_b induce the same support partition. Since d and every vertex of U belong to W_c, the same-path relation between d and every u in U is identical in F_a and F_b.

Now apply the same alternative to F_a,F_b,F_d. Its common core is W_d=V(H)-{a,b,d}. The special label d is present in F_a and F_b, and the support-switch conclusion says that d lies in opposite classes relative to the common partition of W_d between those two covers. Therefore, for every u in the nonempty set U subset W_d, the truth value of 'd and u lie in the same support class' is reversed between F_a and F_b.

This contradicts the conclusion from the triple F_a,F_b,F_c. Hence at least one triple cannot take the common-core switch branch; by compattriplesupport14 it must instead exhibit different support partitions on its common three-deletion core.

In the sharp half-order shell n=2lambda+1 with lambda>=3, n>=7, so after removing four distinct labels the residual set U has order 2lambda-3>=3 and is automatically nonempty. ∎