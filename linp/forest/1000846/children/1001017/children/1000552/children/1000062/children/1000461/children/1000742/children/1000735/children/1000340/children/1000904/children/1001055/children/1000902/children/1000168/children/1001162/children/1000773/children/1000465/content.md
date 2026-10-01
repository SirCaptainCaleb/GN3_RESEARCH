# Crossing balanced endpoint lenses on one maximum path must intersect off the host

## Statement

Let P be a maximum endpoint path ending at v. Let L_1 and L_2 be two clean balanced endpoint lenses attached to P, with host-side endpoint pairs (a,c) and (b,d) appearing in the order a<b<c<d along P. Let A_1,A_2 denote the corresponding off-P lens sides. Then A_1 and A_2 cannot be internally vertex-disjoint. Equivalently, any family of balanced endpoint lenses whose off-host sides are pairwise internally disjoint has a noncrossing (laminar/disjoint) family of host intervals.

## Body

Assume the off-P sides A_1,A_2 are internally vertex-disjoint. Cleanliness says each A_i meets P only at its two lens endpoints. Traverse P from its initial end to a, then traverse A_1 from a to c, then traverse the host segment P[c,b] backwards, then A_2 from b to d, and finally the host suffix P[d,v]. These five pieces are internally vertex-disjoint except at consecutive joining endpoints: the used P-pieces are disjoint because a<b<c<d, each A_i is clean relative to P, and A_1,A_2 are disjoint by assumption. Hence they form a linear path ending at v. Since each lens is balanced, |A_1|=|P[a,c]| and |A_2|=|P[b,d]|. Relative to P, the new path traverses the overlap segment P[b,c] twice in length accounting, once through each balanced detour, while omitting it as a forward host segment. Its total length is |P|+2|P[b,c]|>|P|, contradicting maximality of P at v. Therefore A_1,A_2 must intersect.