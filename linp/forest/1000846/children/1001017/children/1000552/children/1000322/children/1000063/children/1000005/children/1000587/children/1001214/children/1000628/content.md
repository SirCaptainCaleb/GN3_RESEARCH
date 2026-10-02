# Good-residue witnesses contain linearly many genuine two-hole collisions

## Statement

In the two-hole wrong-entrance setting, the two hole-centered matchings N_a,N_b have at least 4delta-2ell-10 common covered vertices. At the dense-core threshold this is at least 2m-6 for ell=3m and also for ell=3m+2. Every such vertex w supports distinct hyperedges {a,w,r} and {b,w,t} with r!=t, i.e. exactly a genuine two-hole collision of the splice type.

## Body


Work in the two-hole wrong-entrance setting of 7383e241bcce. Let N_a,N_b be the two hole-centered matchings on
  W=V(Q)\setminus h_1,
so
  |N_a|,|N_b| >= delta-4
and
  |W|=2ell-6.

Let A=V(N_a), B=V(N_b) be the sets of W-vertices covered by the two matchings. Since a matching of size t covers 2t vertices,
  |A|,|B| >= 2(delta-4).
Hence
  |A∩B| >= |A|+|B|-|W|
          >= 4(delta-4)-(2ell-6)
          = 4delta-2ell-10.

At the dense-core threshold delta>=floor(2ell/3)+1, this becomes:
- ell=3m:
    |A∩B| >= 4(2m+1)-6m-10 = 2m-6;
- ell=3m+2:
    |A∩B| >= 4(2m+2)-(6m+4)-10 = 2m-6.

For every w in A∩B there are unique matching edges
  {w,r} in N_a,
  {w,t} in N_b,
corresponding to hyperedges
  {a,w,r}, {b,w,t}.
The mates r,t are distinct. Otherwise N_a and N_b would contain the same pair {w,r}, contradicting their edge-disjointness.

Thus every common covered vertex is a genuine two-hole collision vertex of exactly the form used in the gap-two/gap-three splice lemmas.
