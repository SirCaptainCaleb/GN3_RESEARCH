# Equality obstructions have Steiner deficiency at least two

## Statement

Let d=floor(2ell/3). An exact-density P_ell-free linear triple system with |E(H)|=d|V(H)| cannot have order 6d+1 or 6d+2. Equivalently the leave-deficiency parameter s=n-(6d+1) is at least 2. At s=0 the system is an STS and is 3d-regular; at s=1 parity forces the leave to be a perfect matching, again making H 3d-regular. In both cases the minimum-degree endpoint-potential bound forces a P_ell.

## Body


Let ell>=4 and put d=floor(2ell/3). Let H be an n-vertex linear triple system with
  |E(H)|=dn
and no P_ell.

Write
  n=6d+1+s,
so by f3bd131eaaa2 the uncovered-pair leave graph U has average degree s. For every vertex v,
  d_U(v)=n-1-2d_H(v),
so
  d_U(v) ≡ n-1 (mod 2).                              (1)

CASE s=0.
Then n=6d+1 and U is empty, so H is the Steiner triple system case and every vertex has
  d_H(v)=3d.
By the certified minimum-degree endpoint-potential floor 6a4d9b21f0c3,
  H contains a path of length at least
  ceil((3d+1)/2).

This is at least ell in every residue:
- ell=3r, d=2r: ceil((3d+1)/2)=3r+1>ell;
- ell=3r+1, d=2r: value=3r+1=ell;
- ell=3r+2, d=2r+1: value=3r+2=ell.
Contradiction.

CASE s=1.
Then n=6d+2 is even, so n-1 is odd. By (1), every leave degree is odd and nonnegative. Its average is 1. Therefore every leave degree equals 1; U is a perfect matching.

Hence
  d_H(v)=(n-1-1)/2=(n-2)/2=3d
for every v. The same minimum-degree path bound gives a P_ell, contradiction.

Therefore any exact-density P_ell-free linear triple system must satisfy
  n>=6d+3,
or equivalently its leave-deficiency parameter satisfies
  s>=2.
