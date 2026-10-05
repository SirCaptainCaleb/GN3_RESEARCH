# Two deletion covers with a direct mixed edge force path disturbance, endpoint reversal, descent, or an omission swap

**Summary:** Two deletion covers with a direct mixed edge force path disturbance, endpoint reversal, descent, or an omission swap.

## Statement

Let H be any boundary tournament. Let H-y=R|Q be a two-cover with R=(r_0,...,r_m), m>=2, and let z be a displayed endpoint of R. Put A=V(R)-{z}, and let T be a two-cover of H-z. Suppose T contains an ordinary edge joining A to V(Q), and every T-component contains its surviving R-vertices in their inherited relative order. Then at least one of the following holds: (1) an inherited edge of R-z has endpoints in two different path supports of T; (2) one T-component leaves R-z through a nonempty exterior segment and later returns; (3) a tight triple reverses the displayed endpoint edge of R incident with z; (4) H has a two-cover; (5) the spanning three-cover T|{z} admits a strict quadratic-potential decrease by one pairwise repartition; or (6) the endpoint restoration is Phi-neutral and produces a deletion cover compatible with T on their common domain.

## Body

Apply e2ffb6f50728 to R, the omitted endpoint z, the comparison cover T, and exterior class V(Q). If the surviving R-vertices occupy more than one T-block, that theorem gives either an inherited edge of R-z whose endpoints lie in different T path supports or a leave-and-return subpath through a nonempty exterior segment. These are outcomes (1) and (2).

It remains that the surviving R-vertices form one contiguous inherited-order block B of one T-component C and every mixed edge is incident with an endpoint of B. By symmetry assume z=r_0, so B=(r_1,...,r_m), and write the other T-component as D.

Write C=L,B,K, where L,K contain no R-vertices. If K is nonempty, then (z,B,K) is tight: the first triple and all triples inside B are inherited from R, while the transition from B into K and the remaining triples are inherited from C. Repartitioning C together with the singleton z as
L | (z,B,K)
is therefore legal. Put c=|C| and l=|L|. Relative to T|{z}, the change in quadratic potential is
l^2+(c-l+1)^2-c^2-1 = -2(l-1)(c-l).
If L is empty, the new state is a two-cover of H, giving (4). If l>=2, then K nonempty implies c-l>0 and the change is strictly negative, giving (5). If l=1, let w be the unique vertex of L. Omitting w from the restored cover gives a deletion cover whose two displayed paths restrict on H-{z,w} to exactly (B,K)|D, the same restriction as T; hence the two deletion covers are compatible, giving (6).

It remains that K is empty, so a mixed attachment occurs immediately before B. Write L=L',w with w the last exterior vertex before r_1. If (w,z,r_1) is non-tight, boundary antisymmetry gives (r_1,z,w) tight, which reverses the displayed endpoint edge zr_1 and gives (3). If (w,z,r_1) is tight, then (w,z,B) is tight and the legal repartition
L' | (w,z,B)
has potential change -2(t-1)(c-t), where t=|L'|. If L' is empty we obtain a two-cover; if t>=2 the change is strict; and if t=1 the unique split-off vertex yields, after omission, a deletion cover compatible with T on the common domain exactly as above.

The case in which z is the terminal endpoint of R is symmetric. No minimum-counterexample or minimality hypothesis is used.

## Metadata

- ID: path_disturbance_endpoint_reversal_descent_or_an_omission_swap
- Kind: toolkit
- Version: 2
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
