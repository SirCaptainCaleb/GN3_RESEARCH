# The neutral four-to-six branch is exactly a sharpened pc2-square state

## Statement

In the componentwise Phi-minimal four-side setup with |X|=4 and P=(p_1,...,p_m), m>=6, the endpoint six-set U=X union {p_1,p_m} has the following dichotomy. If U is non-Hamiltonian, all four X-label deletions are Hamiltonian and two such five-deletions exhibit order disagreement. Otherwise m=6, U is Hamiltonian, X|P -> U|(p_2,p_3,p_4,p_5) is Phi-neutral, H-U is non-Hamiltonian with path-cover number two, and U contains labels d,e whose complementary four-set D=U-{d,e} is Hamiltonian while H-U, H-U+d, H-U+e, and H-D are all non-Hamiltonian pc2. For every top two-cover of H-D, either one of d,e is universally internal, support partitions disagree, common-support Hamilton orders disagree, or simultaneous endpoint exposure yields strict pairwise Phi descent, ambient order at most fourteen, or a same-component endpoint pair on a component of order at most six. In the latter case order six is exactly the neutral 4-to-6 swap. In particular n>=17 forces order disagreement.

## Body

Endpoint insertion into X changes pair sizes (4,m) to (5,m-1), with Phi change 10-2m<0, so both one-endpoint extensions are non-Hamiltonian. If U is non-Hamiltonian, four-of-six leaves only the four X-label deletions as the required Hamiltonian five-deletions, and the four-good-six interface gives order disagreement.

If U is Hamiltonian, replacing X|P by U|R changes (4,m) to (6,m-2), with Phi change 24-4m. Local minimality therefore forces m=6 and equality. Since R|Q covers H-U and H-U cannot be Hamiltonian, H-U is non-Hamiltonian pc2.

Apply the Hamiltonian-six square theorem: choose d,e in U so D=U-{d,e} is Hamiltonian and the four lower/top states K=H-U, K+d, K+e, K+d+e=H-D are all non-Hamiltonian pc2. The square top-cover normal form gives endpoint exposure, universal internality, support disagreement, or order disagreement.

If d,e are endpoints of different top components A,B, moving one endpoint into D changes (4,s) to (5,s-1), with Phi change 10-2s. Failure of strict descent on both sides forces |A|,|B|<=5 and n<=14. If d,e are the two endpoints of one component A of order s, moving both into D changes (4,s) to (6,s-2), with Phi change 24-4s; failure of strict descent gives s<=6, with equality at s=6. Finally n>=17 ensures one path beside the original four-side has order at least seven, excluding the neutral m=6 case on that pair.