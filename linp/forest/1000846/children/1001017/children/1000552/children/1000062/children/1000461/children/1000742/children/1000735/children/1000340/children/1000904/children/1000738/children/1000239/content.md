# Ordered common-terminal edges force quadratic total entrance rank in every uniformity

## Statement


Let H be a finite linear r-graph with r>=3. Let v be a vertex of rank p, and let e_1,...,e_k be distinct ascending nonspecial edges terminal at v. Assume that, for every e_i, the vertex v has minimum vertex rank among the r-1 terminal vertices of e_i. Write q_i=phi(e_i), let x_i be the unique entrance of e_i, and relabel so that q_1<=...<=q_k.

Then the sets e_i\{v} are pairwise disjoint and, for every i,
  q_i >= ceil((8i+4r-14)/(6r-7)).
Consequently
  sum_{i=1}^k phi(x_i)
  >= sum_{i=1}^k [ceil((8i+4r-14)/(6r-7))-1]
  >= [4k^2-(2r+3)k]/(6r-7).

Moreover, besides x_i each edge e_i contains r-2 terminal vertices, all of rank at least p. These (r-2)k vertices are mutually distinct and disjoint from the entrances. Hence
  sum_{z in union_i(e_i\{v})} phi(z)
  >= (r-2)pk
     + sum_{i=1}^k [ceil((8i+4r-14)/(6r-7))-1].

In particular, a common-terminal family of size k=Theta(p) forces total vertex rank Theta(p^2) on pairwise distinct vertices outside v.


## Body


For each i put
  J_{q_i}(v)={f containing v: phi(f)<=q_i}.
Because q_1<=...<=q_i, the i distinct edges e_1,...,e_i all belong to J_{q_i}(v).

Apply the certified fixed-entrance capacity bound from a570a11f0001 with h=e_i. Its hypotheses hold because e_i is ascending of rank q_i and v is terminal at e_i. Thus
  i <= |J_{q_i}(v)|
    <= ((6r-7)/8)q_i + (7-2r)/4.
Rearranging gives
  q_i >= (8i+4r-14)/(6r-7),
and integrality of q_i gives the asserted ceiling.

Since e_i is ascending with unique entrance x_i,
  phi(x_i)=q_i-1.
Summing the ceiling bound proves the first displayed inequality. Dropping the ceilings gives
  sum_i phi(x_i)
  >= sum_i [(8i+4r-14)/(6r-7)-1]
  = [4k^2-(2r+3)k]/(6r-7).

Any two distinct e_i,e_j already share v. Linearity therefore implies
  (e_i\{v}) cap (e_j\{v}) = emptyset.
Thus all entrances and all other off-v vertices in the displayed family are distinct. A nonspecial r-edge has exactly one unique entrance and r-1 terminal vertices, so e_i has r-2 terminal vertices besides v. By the minimum-rank hypothesis on v, every one of those vertices has rank at least phi(v)=p. Adding their ranks to the entrance-rank estimate proves the total off-v bound.
