# Port-cogirth-preserving contractions and binary-generator Cayley lift matroids

Let (M,p) be a finite pointed binary matroid. Its port cogirth gamma_p(M) is the minimum cardinality of a cocircuit containing p. Let P4(M,p) mean: for every binary cycle X containing p, a port cocircuit Y of cardinality gamma_p(M) satisfies |X intersect Y| at most four. Theorem (contraction inheritance). Suppose T excludes p, M0=M/T, and gamma_p(M)=gamma_p(M0). If M0 satisfies P4, then M satisfies P4. Proof: project X to X0=X intersect (E(M) minus T), which is a binary cycle of M0. Choose a shortest port cocircuit Y of M0 intersecting X0 in at most four elements. Cocircuits of M0 are cocircuits of M disjoint from T, and cogirth equality makes Y shortest in M. Thus |X intersect Y|=|X0 intersect Y| at most four. The same argument works for the bound two. Consequently any pointed binary matroid with a port-cogirth-preserving contraction to the cube matroid D_n inherits the corresponding intersection conjecture, including the monochromatic strengthening.

### Pointed binary generator construction

Let \((N,t)\) be a simple binary matroid on \(S\cup\{t\}\), where \(S\) spans \(t\). Let \(q\ge4\) be the smallest size of a circuit of \(N\) containing \(t\), and put \(\ell=q-1\). Represent the elements by distinct nonzero vectors \(s\in V=\mathbb F_2^r\) and \(t\in V\). Let \(K=\operatorname{Cay}(V,S)\), joining \(x\) to \(x+s\). Translation \(\tau(x)=x+t\) acts freely on vertices and edges, and \(G=K/\tau\) is simple because \(t\) is neither a generator nor a sum of two generators. Put \(H=L(G)\), with incidence matrix \(B_H\) over \(\mathbb F_2\) and a cochain \(a\) recording the covering monodromy of \(L(K)\to H\). Define the pointed binary matroid
\[
\mathfrak D(N,t)=M\left(\begin{array}{c|c}B_H&0\\a&1\end{array}\right)^*,
\]
where the new final column is the port \(p\). This construction is determined by the pointed matroid \((N,t)\), independently of choices of its binary representation or of the cochain \(a\).

**Theorem (cubical core and port cogirth).** Every such \(\mathfrak D(N,t)\) has port cogirth \(q=\ell+1\) and a contraction onto \(D_\ell\), preserving that port cogirth.


*Proof of the cubical-core theorem.* Choose a shortest circuit \(C\ni t\) of \(N\), and write \(A=C\setminus\{t\}\). Binary circuit dependence yields \(\sum_{s\in A}s=t\), while the \(\ell\) members of \(A\) are independent. For every root \(x\in V\), the induced directions \(A\) on \(x+\operatorname{span}(A)\) form a \(\tau\)-invariant \(Q_\ell\). This cube is induced in \(K\): if \(s\in S\setminus A\) belonged to the span of \(A\), then \(s\) would equal the sum of \(w\ge2\) members of \(A\), giving an expression of \(t\) using only \(\ell-w+1<\ell\) generators. Such an expression contradicts the choice of \(C\).

Therefore the folded cube \(Q_\ell/\tau\) embeds in \(G\), and its line graph \(H_\ell\) is induced in \(H\). Let \(F\) be its set of turns. Restricting the pointed matrix before dualization to \(F\cup\{p\}\), and deleting zero rows, gives the pointed matrix for \(D_\ell^*\): its incidence part is that of \(H_\ell\) and its monodromy row is the canonical cube covering class, up to a cut. Hence
\[
\mathfrak D(N,t)/(E(H)\setminus F)\cong D_\ell.
\]

Every port cocircuit of \(\mathfrak D(N,t)\) has the form \(C_H\cup\{p\}\) with \(C_H\) a simple turn cycle of \(H\) with odd covering monodromy. Lifting its cyclic sequence to \(L(K)\), the consecutive edge-contact vertices yield a walk of at most \(|C_H|\) generator steps from \(u\) to \(u+t\). Any such walk has at least \(\ell\) steps, because \(\ell\) is the shortest generator representation of \(t\). Thus \(|C_H|\ge\ell\). A geodesic inside the invariant \(Q_\ell\) gives an odd-monodromy turn cycle of length \(\ell\). Therefore the port cogirth is \(\ell+1=q\). \(\square\)
