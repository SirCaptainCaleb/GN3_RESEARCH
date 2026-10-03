# Exceptional leaf transfer equals the support-order gap

**Summary:** In a connected selected support tree, any leaf comparison of the exceptional containment form transfers exactly the difference between the two support orders. The exceptional selected cover and the natural support-compatible replacement have the same component-size multiset.

## Statement

Let J be a connected selected support tree. Let P be a leaf support with neighbor Q, let x label PQ, and let y in Q. Suppose the selected cover of H-y has one component S properly contained in P and its other component has block order (R,x,Q-{y}) or (Q-{y},x,R), where R=P-S. Then |S|=|Q| and |R|=|P|-|Q|. In particular Q-{y} union {x} is Hamiltonian and P | ((Q-{y}) union {x}) is a deletion cover of H-y with exactly the same component-order multiset as the selected exceptional cover.

## Body

Let \(J\) be a connected selected support tree, with bipartition \(A\dot\cup B\). For each support-vertex \(u\in V(J)\), write \(S_u\) for its represented support. Every edge of \(J\) has a distinct deletion label, and connectedness gives \(|E(J)|=|V(H)|\), hence \(|V(J)|=|V(H)|+1\).

Root \(J\) at a support-vertex \(w\). For an edge labeled \(d\), the usual membership alternation across deletion-partition edges shows that \(d\in S_w\) exactly when the farther endpoint of that edge has positive even depth from \(w\). Edges are in bijection with non-root vertices, so \(|S_w|\) equals the number of vertices in the bipartition class of \(w\) other than \(w\) itself. Consequently every support represented in \(A\) has order \(|A|-1\), and every support represented in \(B\) has order \(|B|-1\).

Now let \(P=S_p\) be a leaf support with neighbor \(Q=S_q\), and let \(x\) label \(pq\). Fix \(y\in Q\), put \(C=Q-\{y\}\), and suppose the selected deletion cover \(F_y\) has one component with support \(S=S_r\subsetneq P\), while its other component has one of the block orders
\[
(R,x,C),\qquad(C,x,R),
\]
where \(R=P-S\neq\varnothing\).

Since \(S_r\subsetneq S_p\), the deletion-partition containment parity forces the \(p\)-\(r\) path in \(J\) to have odd length. Hence \(r\) lies in the bipartition class opposite \(p\), which is also the class containing the neighbor \(q\). The census above therefore gives
\[
|S|=|Q|.
\]
Thus
\[
|R|=|P|-|S|=|P|-|Q|.
\]
Moreover \(C\cup\{x\}\) is a contiguous subpath of the second component of \(F_y\), so it is Hamiltonian. Therefore
\[
P\mid(C\cup\{x\})
\]
is another deletion cover of \(H-y\). The selected exceptional cover has component orders
\[
|S|,\quad |R|+1+|C|
 =|Q|,\quad |P|,
\]
while the displayed replacement has component orders \(|P|,|Q|\). Hence the two covers have exactly the same component-order multiset and the same quadratic contribution.

In particular, if the selected covers are chosen to minimize component imbalance, the replacement is also minimum-imbalance. On the common domain \(H-\{x,y\}\), its support partition is \(P\mid C\), the same support partition inherited from \(F_x=P\mid Q\). Thus every exceptional leaf comparison in a connected support tree admits an equally balanced support-compatible replacement at the same omitted label. \(\square\)

## Metadata

- ID: exceptional_leaf_transfer_equals_support_order_gap
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
