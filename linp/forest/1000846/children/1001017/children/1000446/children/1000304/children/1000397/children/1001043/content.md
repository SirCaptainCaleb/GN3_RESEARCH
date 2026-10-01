# Ascending edges at one last vertex can have unbounded φ-gap

## Statement

For every integer q>=5 there is a linear 3-graph containing two ascending nonspecial edges e and f that share a last vertex v and satisfy φ(e)=2q-3 and φ(f)=q. In particular, the difference φ(e)-φ(f)=q-3 is unbounded.

## Body

Construction. Let Q=(E_1,...,E_p) be a 3-uniform linear path of length p=2q-3. Choose the last vertex v of Q to be private in E_p, let w be a private vertex of E_{q-1}, and add a new edge f={w,v,u} with u new. Put e=E_p. The intersection graph consists of the path E_1...E_p together with the extra vertex f adjacent exactly to E_{q-1} and E_p; thus it is a q-cycle E_{q-1},E_q,...,E_p,f with the path E_1,...,E_{q-2} attached at E_{q-1}. The longest induced path ending at E_p has length p, namely E_1,...,E_p. Any induced path ending at E_p through f must omit E_{q-1} and has length at most q+1<p for q>=5. Hence φ(e)=p and the unique entrance of e is E_{p-1}∩E_p. The corresponding entrance vertex has φ-value p-1, witnessed by E_1,...,E_{p-1}; the alternative route through f has length at most q+1<=p-1. Therefore e is ascending and nonspecial. For f, the path E_1,...,E_{q-1},f has length q and enters f through w. Any induced path ending at f through E_p can use at most E_q,...,E_p,f and has length q-1. Hence φ(f)=q and w is its unique entrance. The longest path with last vertex w has length q-1, witnessed by E_1,...,E_{q-1}; therefore f is also ascending. Both e and f have v as a last vertex of a longest path. This proves the claim.