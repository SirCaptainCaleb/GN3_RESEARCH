# Logarithmic common-last-vertex bound for ascending edges

## Statement

There is an absolute constant C such that, for every finite linear 3-graph H and every vertex v, the number a(v) of ascending edges for which v is a last vertex satisfies a(v)<=C log(φ(v)+2).

## Body

The construction d5e0ab668a51 shows that logarithmic growth would be best possible up to the constant: it has a(v)=r+1 and φ(v) of order 2^r. If this conjecture holds, then 2A=sum_v a(v)=O(n log ell) in every P_ell^(3)-free linear 3-graph. Combining with 3m-A<=sum_v(2φ(v)-1)<=(2ell-3)n gives m<=(2ell/3+O(log ell))n. Thus the conjecture alone would improve the leading coefficient from 1 to 2/3, while remaining compatible with the failure of every absolute pointwise bound.
