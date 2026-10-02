# From order twenty-seven the quiet reversal branch forces quadratic deletion-cover disturbance

## Statement

Let H be a minimum counterexample of order n>=27, and suppose the quiet outcome (4) of reversal_halfstable_manydeletion01 holds: there are a reversed label d and a set C of deletion labels with m=|C|>=ceil((n-2)/4) such that d is internal in every two-cover of H-t for every t in C. Choose arbitrarily one two-cover F_t of H-t for each t in C. Then among the binom(m,2) chosen pairs, at least floor((m-1)^2/4) are incompatible. Hence at least ceil(floor((m-1)^2/4)/2) incompatible pairs have one common broad type: either support-incompatible or support-compatible but order-incompatible. Moreover some anchor a in C is incompatible with at least floor((m-1)/2) of the other chosen covers, and at least ceil(floor((m-1)/2)/2) of those anchor incompatibilities have one common broad type.

## Body

Since n>=27 and m>=ceil((n-2)/4), we have m>=7. Apply the certified exact Mantel theorem compatibility_satisfies_the_exact_mantel_density_bound to the chosen deletion-cover family {F_t:t in C}. Its compatibility graph has at most floor(m^2/4) edges. Therefore the number I of incompatible pairs is at least binom(m,2)-floor(m^2/4)=floor((m-1)^2/4).

Every incompatible pair has exactly one of the two broad types in the compatibility hierarchy: support-incompatible, or support-compatible but order-incompatible. A two-color pigeonhole argument therefore gives at least ceil(I/2) incompatible pairs of one common broad type.

The same theorem compatibility_satisfies_the_exact_mantel_density_bound also gives an anchor a whose cover F_a is incompatible with at least k=floor((m-1)/2) others. Coloring those k anchor incompatibilities by the same two broad types yields a uniform anchor subfamily of size at least ceil(k/2).

The universal internality of d is not needed for the extremal graph count itself; it identifies this quadratic incompatibility pattern as occurring inside the quiet reversed-pair branch, where every chosen deletion state simultaneously forbids the same reversed label d as a displayed endpoint.