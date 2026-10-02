# Critical-core slack fixes forest-joint count modulo three

## Statement

In the extremal |D|=k critical core, with private slack sigma=2k-(m+2c) and joint count j=m-c, one has 3c+j=2k-sigma and hence j congruent to 2k-sigma mod 3. For sigma<=k-2, also 0<=j<=sigma. Thus every fixed small-slack layer has only finitely many forest templates; in particular sigma=0 requires 3|k and j=0, while sigma=1 is impossible for k=0 mod3 and otherwise forces j=1 or 0 according as k=1 or 2 mod3.

## Body


In the |D|=k critical-core normal form let F=H-D have m edges and c nonempty path components, and write
  j=m-c
for the total number of forest joints. Let
  sigma=2k-(m+2c)
be the private-vertex slack.

Since m=c+j,
  m+2c = 3c+j,
and therefore
  3c+j = 2k-sigma.                        (1)
In particular
  j ≡ 2k-sigma (mod 3).                    (2)

Combine this with e46ac48fe118: whenever 0<=sigma<=k-2,
  0<=j<=sigma.
Thus for each fixed small sigma, j belongs to the finite set
  {0,1,...,sigma} ∩ (2k-sigma mod 3),
and then c=(2k-sigma-j)/3 is forced.

The first layers are especially rigid.

sigma=0:
  j=0 and 3c=2k.
Hence zero slack is possible only when 3|k, and F is a matching.

sigma=1:
  j<=1 and j≡2k-1 mod3.
Thus:
- if k≡0 mod3, no one-slack core exists;
- if k≡1 mod3, j=1, so F is a matching plus exactly one two-edge path component;
- if k≡2 mod3, j=0, so F is a matching.

sigma=2:
  j<=2 and j≡2k-2 mod3.
Thus:
- k≡0 mod3 -> j=1;
- k≡1 mod3 -> j=0;
- k≡2 mod3 -> j=2.

sigma=3:
  j<=3 and j≡2k mod3.
Thus:
- k≡0 mod3 -> j∈{0,3};
- k≡1 mod3 -> j=2;
- k≡2 mod3 -> j=1.

More generally, fixed sigma leaves at most ceil((sigma+1)/3) possible joint counts, and each determines the number of components exactly. Therefore the small-slack branch of the grand induction is a finite-defect template problem depending only on sigma and k mod3, not on the ambient number of vertices.
