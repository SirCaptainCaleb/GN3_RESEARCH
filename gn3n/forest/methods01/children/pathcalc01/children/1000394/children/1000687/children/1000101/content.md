# A neutral common-middle square has a synchronized square of exact-pc2 complements

## Statement

Assume additionally that H is the all-equal minimum-counterexample setting |V(H)|=3r and the common-middle square has core M of order r-2 with corners a,ell,c,r. Put Omega=V(H)-(V(M) union {a,ell,c,r}). Then |Omega|=2r-2, and the complements of the four Hamiltonian r-supports are respectively Omega union {ell,r}, Omega union {a,r}, Omega union {ell,c}, and Omega union {a,c}. Each of these four induced 2r-vertex subtournaments is non-Hamiltonian with path-cover number exactly two.

## Body

The four Hamiltonian supports are S_ac=M+{a,c}, S_lc=M+{ell,c}, S_ar=M+{a,r}, and S_lr=M+{ell,r}. Since |M|=r-2, each has order r. Define Omega by deleting M and all four corner labels from V(H). Because |V(H)|=3r, |Omega|=3r-(r-2)-4=2r-2. Direct complementation gives V(H)-S_ac=Omega+{ell,r}, V(H)-S_lc=Omega+{a,r}, V(H)-S_ar=Omega+{ell,c}, and V(H)-S_lr=Omega+{a,c}. Each S is a nonempty proper Hamiltonian support. By the certified minimum-counterexample complement principle mincex01, its complement has path-cover number exactly two and is non-Hamiltonian. Thus the neutral endpoint square synchronizes four exact-pc2 residues over one fixed Omega core, adjacent residues differing by a single corner-label exchange.