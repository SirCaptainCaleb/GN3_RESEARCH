# Lemma 3 — preserved pre-item development

Let \(e\) have edge rank \(q\).

1. If \(q>t\), then every vertex of \(e\) lies in \(V_t\).
2. If \(q=t\), then \(e\) meets \(V(H)\setminus V_t\) if and only if \(e\) is ascending. In that case its unique entrance lies outside \(V_t\), and both terminal vertices lie in \(V_t\).

#### Proof
If \(e\) is special, every vertex is terminal at \(e\), hence has vertex rank at least \(q\).

If \(e\) is nonspecial with unique entrance \(x\), then the two terminal vertices have rank at least \(q\), while \(\phi(x)\ge q-1\). Therefore \(q>t\) implies all three ranks are at least \(t\). When \(q=t\), the unique entrance lies outside \(V_t\) exactly when \(\phi(x)=t-1\), which is exactly the ascending condition. ∎

Accordingly, ascending edges are precisely the boundary edges of the rank superlevels at their own edge rank.
