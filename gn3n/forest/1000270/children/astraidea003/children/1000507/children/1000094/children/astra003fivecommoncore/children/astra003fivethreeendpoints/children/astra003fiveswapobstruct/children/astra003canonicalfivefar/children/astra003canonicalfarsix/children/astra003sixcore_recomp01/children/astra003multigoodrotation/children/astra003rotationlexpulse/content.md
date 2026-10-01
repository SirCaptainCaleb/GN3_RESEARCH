# Every 4-to-(m+1) excursion is strictly upward in the sorted component-size order

## Statement

Let a spanning three-cover have component orders r,5,m with r>=1 and m>=5. Repartitioning the 5-side together with the m-side into components of orders 4 and m+1 strictly increases the decreasingly sorted component-order triple lexicographically. Consequently the quadratic-neutral rotations arising in astra003multigoodrotation and astra003twogoodrotation are never neutral for both standard extremal measures: the outward 5|m -> 4|(m+1) step is strictly lexicographically upward and strictly increases Phi, while the certified return 4|(m+1) -> 5|m step exactly restores Phi and the original size triple.

## Body

Compare the multisets {r,5,m} and {r,4,m+1}. If r<=m, the largest entry of the old multiset is m (or tied with r) while the new multiset has largest entry m+1, so the sorted triple strictly increases at its first coordinate. If r>m, then r>=m+1 because the orders are integers. The largest coordinate remains r, while the second-largest coordinate increases from m to m+1, so the sorted triple again increases lexicographically. Thus the 4|(m+1) excursion is always strictly lexicographically upward. Its Phi increase is [4^2+(m+1)^2]-[5^2+m^2]=2m-8>0. By the exact calculation in the rotation lemmas, a foursidedescentobstruction return lowers Phi by the same amount and restores component orders 5,m, hence restores the original sorted size triple. Therefore any genuinely cyclic neutral transport must use the internal support/order data of the minimum-Phi 5|m states; it cannot be flat in the size data throughout the cycle.
