# Ascending terminal density would reduce equality to the single critical residue

## Statement

Let H be a P_ell-free linear 3-graph on n vertices with m=d n edges, where d=floor(2ell/3), and let A be the number of ascending nonspecial edges. Then the certified ascending-edge accounting inequality forces
A >= (3d-2ell+3)n.
Equivalently:
if ell≡0 mod3, A>=3n;
if ell≡1 mod3, A>=n;
if ell≡2 mod3, A>=2n.

Consequently, if the ascending terminal-pair graph T_up satisfies mad(T_up)<=3, hence A<=3n/2, then no exact-density equality-layer counterexample can exist for ell≡0 or 2 mod3. Under that terminal-graph bound, the grand equality-layer induction is reduced entirely to ell≡1 mod3.

## Body

The certified ascending-edge formulation 419519f0efa5 gives
  3m-A <= (2ell-3)n.
At exact density m=dn,
  A >= (3d-2ell+3)n.

Now compute by residue class.

If ell=3r, then d=2r and
  3d-2ell+3=6r-6r+3=3.

If ell=3r+1, then d=2r and
  3d-2ell+3=6r-(6r+2)+3=1.

If ell=3r+2, then d=2r+1 and
  3d-2ell+3=(6r+3)-(6r+4)+3=2.

Thus A is at least 3n,n,2n in the three residues respectively.

The terminal-pair graph T_up has one graph edge for every ascending nonspecial hyperedge, so |E(T_up)|=A. If mad(T_up)<=3, then in particular
  2A/n <=3,
hence A<=3n/2.
This contradicts A>=3n in residue 0 and A>=2n in residue 2. Only residue 1 is compatible.

This dovetails with the independent mod-three deletion induction b60e28d26d52: the only residue where deleting one vertex loses the strict minimum-degree threshold is ell≡1 mod3.
