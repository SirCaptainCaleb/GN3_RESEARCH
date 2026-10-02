# Good-residue two-hole witnesses force linearly many three-center collisions

## Statement

In the setting of 7383e241bcce, let F be the union of the four pairwise edge-disjoint blocker matchings on W, and let T be the number of vertices w in W with d_F(w)>=3. Then
  T >= |E(F)|-|W|.

Consequently, at the dense-core threshold:
- if ell=3m, then T>=2m-4;
- if ell=3m+2, then T>=2m-4.

Thus outside the small equality cases ell=6,8, every good-residue alternate witness contains not merely one but linearly many interior vertices incident with blocker pairs from at least three distinct centers among the two holes and two opposite endpoints.

## Body

Since F is the union of four matchings, Delta(F)<=4. Write N=|W| and E=|E(F)|. Then
  2E-2N = sum_{w in W}(d_F(w)-2).
Vertices of degree at most two contribute at most zero. A vertex counted by T has degree three or four and hence contributes at most two. Therefore
  2E-2N <= 2T,
which gives T>=E-N.

Now apply 7383e241bcce. For ell=3m,
  E-N >= (8m-10)-(6m-6)=2m-4.
For ell=3m+2,
  E-N >= (8m-6)-(6m-2)=2m-4.
This proves the stated bounds.