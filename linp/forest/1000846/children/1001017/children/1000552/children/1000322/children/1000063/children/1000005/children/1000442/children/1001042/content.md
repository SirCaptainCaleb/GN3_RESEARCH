# Minimal-counterexample induction reduces every bad path hull to ears or a spanning top-rank core

## Statement

Assume the dense-core all-special conjecture is true for every forbidden length r<ell. Let H be a counterexample for ell with minimum degree delta>2ell/3, chosen with |V(H)| minimum. Let e be any nonspecial edge of rank q and let P be any q-edge path ending in e. Put U=V(P) and G=H[U].

Then exactly one of the following holds:

(A) G has a vertex v with
    d_G(v)<=floor(2(q+1)/3),
so v is incident in H with at least
    delta-floor(2(q+1)/3)
edges not contained in U; every such edge is a clean ear or one-contact chord relative to U.

(B) q=ell-1 and U=V(H). In particular P is a spanning top-rank path and |V(H)|=2ell-1.

Thus every nonspecial edge in a minimal counterexample either exposes a quantitatively ear-rich vertex on each maximum witness path, or is top-rank and has a spanning witness. 

## Body

If q<=ell-2, conclusion (A) is exactly 62ebb49a0efa, using the induction hypothesis at forbidden length q+1.

Now suppose q=ell-1. Then |U|=2ell-1. If U is a proper subset of V(H), G is a strictly smaller induced subhypergraph. It is P_ell-free because H is, and e remains rank q=ell-1 and nonspecial in G: P survives, no longer e-ending path can appear under deletion, and every longest e-ending path in G is also one in H and hence has the same unique entrance.

By minimality of |V(H)|, G cannot itself satisfy delta(G)>2ell/3, for otherwise G would be a smaller counterexample. Hence
delta(G)<=floor(2ell/3)=floor(2(q+1)/3),
which gives (A), with the same external-ear interpretation as in 62ebb49a0efa.

The only remaining possibility is U=V(H), yielding (B). 