# Inductive path-hull ears are threshold-supported in an edge-minimal counterexample

## Statement

Let ell>=4 and k=floor(2ell/3)+1. Assume the dense-core all-special conjecture for all smaller forbidden lengths, and let H be an edge-minimal P_ell-free counterexample with minimum degree k. Let D={v:d_H(v)=k}. Let e be a nonspecial edge of rank q<=ell-2 and P a q-edge witness path ending in e. Put G=H[V(P)].

Then there exists v∈V(P) with
  d_H(v)-d_G(v) >= k-floor(2(q+1)/3).
Every edge through v counted on the left meets D.

If v∉D, these external edges meet pairwise distinct vertices of D. Hence v has at least
  k-floor(2(q+1)/3)
distinct neighbors in D, each lying with v in a different external hyperedge.

## Body

By the inductive path-hull lemma 62ebb49a0efa, some v∈V(P) satisfies
d_G(v)<=floor(2(q+1)/3).
Since d_H(v)>=k,
d_H(v)-d_G(v)>=k-floor(2(q+1)/3).

An edge through v counted in this difference is not wholly contained in V(P), hence cannot be one of the path edges of P. By the threshold-cover lemma 1e01357bf9c3, every edge outside P meets D. Therefore every such external edge meets D.

If v∉D, choose from each external edge one D-vertex lying on it. Two distinct external edges through v cannot use the same d∈D, since then they would share the pair {v,d}, contradicting linearity. Thus the chosen D-vertices are distinct, giving the claimed packet size.
