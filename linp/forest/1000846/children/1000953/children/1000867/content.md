# Residue-free (ell-1)/3 lower construction

## Statement

For every integer ell>=2, there is a P_ell^(3)-free linear triple system component T on t in {2ell-1,2ell} vertices with |E(T)|=((ell-1)/3)t. Hence ex_L(n,P_ell^(3)) >= ((ell-1)/3)n-O(ell^2) for every n; when n is divisible by the chosen t, ex_L(n,P_ell^(3)) >= ((ell-1)/3)n exactly.

## Body

Proof. A 3-uniform linear path with ell edges has 2ell+1 vertices, so every linear triple system on at most 2ell vertices is P_ell^(3)-free. If ell≡1 or 2 (mod 3), then 2ell-1≡1 or 3 (mod 6), respectively; take a Steiner triple system on t=2ell-1 vertices. It has t(t-1)/6 edges, so |E|/t=(t-1)/6=(ell-1)/3. If ell≡0 (mod 3), take a maximum partial triple system on t=2ell≡0 (mod 6) vertices. The exact MPTS formula gives t(t-2)/6 edges, so again |E|/t=(t-2)/6=(ell-1)/3. Disjoint unions preserve P_ell-freeness. Taking floor(n/t) copies and isolated leftover vertices gives the stated general-n bound, with loss less than one component, hence O(ell^2). This is a residue-free exact-density cleanup, not a leading-coefficient improvement.