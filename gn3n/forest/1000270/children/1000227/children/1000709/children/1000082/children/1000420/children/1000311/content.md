# Every root Hamiltonizes at least three fifths of the four-subsets of any large core

## Statement

Let H be a boundary tournament, let X be a vertex set of order m>=6, and let r be a vertex outside X. Then at least (3/5) binom(m,4) four-subsets D of X have H[D union {r}] Hamiltonian.

## Body

For every six-subset B of X, apply the rooted seven-set shell theorem 84ac56baf953 to B union {r}. At least nine of the fifteen four-subsets D of B satisfy that D union {r} is Hamiltonian. Count incidences (B,D) with |B|=6, |D|=4, D subset B, and D union {r} Hamiltonian. The lower bound is 9 binom(m,6). Each fixed good four-set D is contained in exactly binom(m-4,2) six-subsets B. Therefore the number N_r of good four-sets satisfies N_r binom(m-4,2)>=9 binom(m,6). Since binom(m,6)/binom(m-4,2)=binom(m,4)/15, we obtain N_r >= (3/5) binom(m,4).
