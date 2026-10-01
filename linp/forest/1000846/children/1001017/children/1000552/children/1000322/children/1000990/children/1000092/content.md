# The sharp Turan equality layer forces residue-dependent ascending mass

## Statement

Let d=floor(2ell/3). If a P_ell-free linear 3-graph satisfies |E(H)|=d|V(H)| and A is its number of ascending nonspecial edges, then A>=3n, n, or 2n according as ell is congruent to 0,1, or 2 mod3. Thus the equality layer itself forces a large structured ascending defect, especially in residues 0 and 2.

## Body

Let H be an n-vertex P_ell-free linear 3-graph with
  m=d n,  d=floor(2ell/3),
and let A be the number of ascending nonspecial edges.

By the certified ascending-edge inequality 419519f0efa5,
  3m-A <= (2ell-3)n.
Substituting m=dn gives
  A >= (3d-2ell+3)n.

Evaluate the coefficient by residues.

If ell=3r, then d=2r, so
  3d-2ell+3=6r-6r+3=3,
hence A>=3n.

If ell=3r+1, then d=2r, so
  3d-2ell+3=6r-(6r+2)+3=1,
hence A>=n.

If ell=3r+2, then d=2r+1, so
  3d-2ell+3=(6r+3)-(6r+4)+3=2,
hence A>=2n.

Thus every equality-layer counterexample to S_ell must carry a residue-dependent linear mass of ascending nonspecial edges. In particular the ell≡0 and ell≡2 layers demand more ascending edges than the conjectural universal bound A<=3n/2; even substantially weaker equality-layer versions of that bound would suffice there. Only the ell≡1 residue is compatible with A at the n scale.

This separates the equality-layer task by residue:
- ell≡0: prove A<3n under the equality-layer minimum-degree hypothesis;
- ell≡2: prove A<2n;
- ell≡1: requires genuinely sharper structure, since A>=n is modest.
