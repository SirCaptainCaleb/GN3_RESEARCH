# Proof-rehearsal frontier: five surviving global quadratic-minimum regimes

## Statement

Let H be a minimum counterexample and let A|B|C be a spanning three-cover minimizing Phi=sum |P_i|^2 among all spanning three-covers, with a=|A|>=b=|B|>=c=|C|. Then c>=3, and at least one of the following holds. (1) For every displayed endpoint e of A and f of B, H[V(C) union {e,f}] is non-Hamiltonian with path-cover number two. (2) H has a proper Hamiltonian induced set W of order four or five whose complement is non-Hamiltonian with path-cover number two. (3) For one displayed endpoint e of A there are y in V(B) and z in V(C) such that both (z,y,e) and (y,z,e) are tight. (4) The component-size profile is equitable: a-c<=1, and the maximin parameter among spanning three-covers is floor(|V(H)|/3). (5) The profile is the maximin-tight staircase (c+2,c+1,c), so |V(H)|=3(c+1) and the maximin parameter is c=floor(|V(H)|/3)-1.

## Body

Choose a spanning three-cover minimizing Phi globally. Since H is a minimum counterexample, no spanning three-cover lies in a pairwise-repartition component containing a two-cover, so this globally minimizing cover is Phi-minimal in a trapped component. The certified small-side theorem therefore gives c>=3, and in particular the two larger components satisfy the hypotheses of the certified global quadratic-minimum reduction.

Apply the global quadratic-minimum reduction. If one of its first three alternatives occurs, we obtain regimes (1), (2), or (3). Otherwise a-b<=1 and b-c<=1. Apply the certified adjacent-gap arithmetic lemma to the family of component-order triples of all spanning three-covers. Its two alternatives are exactly: an equitable profile with maximin floor(n/3), or the staircase (c+2,c+1,c) with maximin c=floor(n/3)-1. These are regimes (4) and (5).

Thus the present end-to-end proof frontier is not an unstructured collection of local obstructions: every hypothetical minimum counterexample enters one of these five explicit global regimes. Closing the grand theorem now requires eliminating or consuming these regimes into a two-cover or defect-span compression.
