# Interior separability forces two crossings without minimality

## Statement

Let H be a boundary tournament with a two-cover A|B, where A=(a_1,...,a_m), and let s=a_i, t=a_j with i<j be inseparable in H, meaning every two-cover of H places s and t together. Fix h with i<h<j, put v=a_h, L=A[1,h-1], and R=A[h+1,m]. If H-v has a two-cover T separating s and t, then T has at least two ordinary path edges whose endpoints lie in different members of the partition V(L)|V(R)|V(B).

## Body

By the parent cut-obstruction theorem, both H[V(L) union V(B)] and H[V(R) union V(B)] are non-Hamiltonian.

Let T be a two-cover of H-v separating s and t. Since L,R,B are nonempty and partition V(H)-{v}, at least one ordinary edge of T crosses between these three classes; otherwise the two components of T could meet at most two nonempty classes.

Assume for contradiction that there is exactly one crossing edge. Cutting it from the two-path forest T yields exactly three nonempty path blocks. Because there are exactly three nonempty old classes and no further crossing, each of L,R,B is itself one of those blocks. Therefore T is obtained by joining exactly two whole classes into one path and leaving the third class as the other path.

The joined pair cannot be L and R, because then s and t lie in the same component of T. It cannot be L and B, because that would be a Hamilton path on H[V(L) union V(B)], contradicting the cut obstruction. Likewise it cannot be R and B.

All possibilities for a unique crossing are impossible. Hence every separating two-cover of H-v has at least two crossings of V(L)|V(R)|V(B).

Again, no minimum-order hypothesis is used: minimality is needed only in applications to guarantee that H-v actually has a separating two-cover.