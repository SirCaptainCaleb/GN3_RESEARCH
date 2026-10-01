# Three second-type insertion obstructions yield a Hamiltonian four-set or an interval path

## Statement

Let B=(b_1,...,b_m) be a tight path in a boundary tournament, and let x,y,z be three distinct exterior vertices. Suppose alternative 2 of the failed-insertion normal form in insert01 holds for x,y,z at gaps b_i|b_{i+1}, b_j|b_{j+1}, b_k|b_{k+1}, respectively. Then either two of i,j,k are equal, in which case the corresponding two exterior labels together with that displayed edge form a Hamiltonian four-set, or two of the obstruction gaps differ by at least two, say r<s with s>=r+2, in which case the corresponding exterior labels are joined by a tight connector through the displayed interval (u,b_{r+1},...,b_s,v). Thus three second-type locks cannot all remain in the adjacent-gap cross-only residue.

## Body

Relabel x,y,z so that i<=j<=k. If two of i,j,k are equal, apply the same-gap case of 36fccff06d48 to those two labels. It gives a Hamiltonian four-set on the two labels and the two vertices of the common displayed gap.

Assume now that i,j,k are pairwise distinct. Then i<j<k, hence k>=i+2. Apply the separated-gap case of 36fccff06d48 to the labels at gaps i and k. It gives the tight connector consisting of the first exterior label, the displayed interval b_{i+1},...,b_k, and the second exterior label. These two cases are exhaustive. In particular the adjacent-gap cross alternative of the two-label spacing trichotomy cannot be the only structure across all three labels.
