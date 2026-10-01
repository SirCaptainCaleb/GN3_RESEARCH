# At deficiency two, P_l-freeness forces many leave branches and universal vertices

## Statement

In the s=2 equality layer let B be the leave vertices of degree at least 4, b=|B|, and z the number of leave-isolated/pair-universal vertices. Then P_ell-freeness forces b>=3d-2ell+3, and the defect identity gives z>=b. Thus b,z are at least 3,1,2 according as ell is 0,1,2 mod3.

## Body

Assume the exact-density equality layer has Steiner deficiency s=2, with leave U. Let
  B={v:d_U(v)>=4}
be the set of leave branch vertices and put b=|B|.

Every vertex outside B has leave degree 0 or 2, because all leave degrees are even. Hence for u outside B,
  d_H(u)=3d+1   if d_U(u)=0,
  d_H(u)=3d     if d_U(u)=2.
Thus every surviving vertex has degree at least 3d in H.

Delete B. By linearity, for a fixed surviving vertex u, each deleted vertex can lie with u in at most one hyperedge, so deleting B removes at most b edges incident with u. Therefore
  delta(H-B)>=3d-b.                                  (1)

The induced subhypergraph H-B is still P_ell-free. By the certified endpoint-potential floor, any linear 3-graph of minimum degree at least 2ell-2 contains P_ell, because
  ceil(((2ell-2)+1)/2)=ell.
Therefore (1) cannot satisfy 3d-b>=2ell-2. Hence
  b>=3d-2ell+3.                                      (2)

By the exact s=2 defect identity 4884d121035b,
  z=sum_{j>=2}(j-1)n_{2j},
where z is the number of leave-isolated (pair-universal) vertices. Every branch vertex contributes at least one unit to the right side, so
  z>=b.
Combining with (2),
  z>=b>=3d-2ell+3.

By residues:
- ell=3r, d=2r: b,z>=3;
- ell=3r+1, d=2r: b,z>=1;
- ell=3r+2, d=2r+1: b,z>=2.

Thus in residue zero the minimally irregular configuration with two universal vertices and one degree-six leave branch is impossible; at least three branch vertices and three universal vertices are required. In residue two at least two of each are required.
