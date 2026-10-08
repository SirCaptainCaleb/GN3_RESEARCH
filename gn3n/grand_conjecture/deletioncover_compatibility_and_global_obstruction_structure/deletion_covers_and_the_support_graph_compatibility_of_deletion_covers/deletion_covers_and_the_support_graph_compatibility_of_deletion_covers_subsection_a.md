# 

Two path covers of the same vertex set are support-compatible if they induce the same partition into path supports. They are compatible if they are support-compatible and every two vertices lying in one common support occur in the same relative order in the two path orders. When two deletion covers omit different vertices, these definitions are applied after restricting both covers to their common vertex set.

**Lemma 2 (compatibility gluing).** Let \(D\subseteq V(H)\), \(|D|\ge4\), and for every \(d\in D\) let \(F_d\) be a cover of \(H-d\) by at most two tight paths. If the covers are pairwise compatible on their common domains, then \(H\) has a two-cover.

**Proof.** For distinct \(u,v\), choose \(d\in D-\{u,v\}\). The relation saying that \(u,v\) lie in the same path of \(F_d\), together with their relative order when they do, is independent of \(d\) by compatibility. Any three vertices survive in some \(F_d\), so the same-path relation is transitive. It therefore partitions \(V(H)\) into at most two classes; otherwise three representatives from distinct classes survive in one cover.

Each class inherits a total order. Take three consecutive vertices in one class. A deletion label can be chosen outside them, and in the corresponding \(F_d\) these three vertices occur consecutively in the inherited order. Their ordered triple is tight. Hence every class is a tight path. These one or two paths cover \(H\). \(\square\)

The next lemma gives the local form of a compatible pair.

**Lemma 3 (insertion slots).** Let \(F_a\) and \(F_b\) be compatible deletion covers. Then the omitted vertices \(a\) and \(b\) are inserted into the same common support. Their insertion slots in the common order are equal or adjacent. If the slots are adjacent, there is a tight triple reversing the two inserted labels across the unique common vertex between the slots.

**Proof.** On \(V(H)-\{a,b\}\), compatibility gives two ordered supports, say \(P,Q\). In \(F_a\), the vertex \(b\) is inserted into one of them; in \(F_b\), the vertex \(a\) is inserted into one of them. If they are inserted into different supports, augmenting both supports simultaneously gives a two-cover of \(H\), a contradiction. Thus both are inserted into the same support, say
\[
P=(p_1,\ldots ,p_m).
\]

If the two slots are separated by at least one entire slot, insert both vertices into \(P\) at their respective positions. No new consecutive triple contains both inserted vertices; each consecutive triple is inherited from \(P\), \(F_a\), or \(F_b\). This again gives a two-cover with \(Q\). Hence the slots are equal or adjacent.

In the adjacent case write the common order as \(L,z,R\), with
\[
F_b=(L,a,z,R)\mid Q,\qquad F_a=(L,z,b,R)\mid Q.
\]
Every consecutive triple of \((L,a,z,b,R)\) is known to be tight except possibly \((a,z,b)\). If this triple were tight, the displayed path together with \(Q\) would cover \(H\) by two paths. Hence \((a,z,b)\) is non-tight, so its boundary flip
\[
(b,z,a)
\]
is tight. \(\square\)
