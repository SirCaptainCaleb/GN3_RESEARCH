# Deletion-family averaging for fractional path covers

## Statement

Let H be a finite boundary tournament, let A be a vertex set of order m>=2, and for each v in A choose a cover C_v of H-v with k_v components. Then
tau*(H) <= (sum_{v in A} k_v)/(m-1).
If in addition H[A] has a cover with r components, then
tau*(H) <= (sum_{v in A} k_v + r)/m.
Consequently, if every C_v has at most q components, then tau*(H)<=q m/(m-1), and with an r-component cover of H[A] one also has tau*(H)<=q+r/m.

## Body

For the first bound, assign fractional weight 1/(m-1) to every path occurrence in every chosen cover C_v, combining repeated supports if desired. A vertex u in A is absent only from C_u and belongs to exactly one component of each C_v with v in A-{u}; hence its total coverage is exactly (m-1)/(m-1)=1. A vertex u outside A belongs to exactly one component of every C_v, so its coverage is m/(m-1)>1. Thus the assignment is a feasible fractional path cover, of total mass (sum_v k_v)/(m-1).

For the second bound, assign weight 1/m to every component of every C_v and also weight 1/m to every component of a fixed r-component cover of H[A]. A vertex outside A receives coverage m/m=1 from the deletion covers. A vertex u in A receives (m-1)/m from the deletion covers and exactly 1/m from the cover of H[A], again totaling one. The total mass is (sum_v k_v+r)/m.

The uniform-q consequences are immediate.

This removes the minimum-counterexample hypothesis from the averaging mechanism behind fractionaldeletionavg01 and fractionalpathavg01. Taking A=V(H) and q=2 gives the former bound 2|V(H)|/(|V(H)|-1) whenever every one-vertex deletion has a two-cover. Taking A to be any tight path, q=2 and r=1 gives tau*(H)<=2+1/|A| whenever H-v has a two-cover for each v in A. The original Astra nodes remain useful applications because minimum-counterexample calculus supplies precisely those deletion covers.
