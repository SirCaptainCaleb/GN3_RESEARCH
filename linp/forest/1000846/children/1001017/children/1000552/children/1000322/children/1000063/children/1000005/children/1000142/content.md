# Minimum-degree rank floor and layer recurrence have disjoint support

## Statement

Let H be a finite linear 3-graph of minimum degree delta. If an ascending nonspecial edge lies in layer J_k, then k>=ceil((delta+1)/2). Therefore the positive-coefficient range delta>2k-1 of the ascending-layer recurrence contains no nonempty ascending layer.

## Body

The certified minimum-degree ascending-rank bound gives phi(e)>=ceil((delta+3)/2). In layer J_k one has phi(e)=k+1, so k>=ceil((delta+1)/2). But the recurrence coefficient delta-2k+1 is positive only when delta>2k-1, equivalently k<(delta+1)/2. No integer k satisfies both. Thus the current rank floor and current layer recurrence cannot bootstrap each other in a dense core; a new ingredient is required.
