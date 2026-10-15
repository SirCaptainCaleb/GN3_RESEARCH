# Parabolic character obstruction and the first Coxeter one-switch theorem

# Parabolic character obstruction and the first Coxeter one-switch theorem

Let \(G\) be a finite group, \(K\le G\), and \(t\in G\), and let \(f:G\to\mathbb F_2\) be right-\(K\)-invariant. Its orbit word of length \(m\) is \((f(g),f(gt),\ldots,f(gt^{m-1}))\).

**Lemma 1 (the alternating-character obstruction).** Assume \(G=\langle K,t\rangle\) and that there is no homomorphism \(\chi:G\to\mathbb F_2\) with \(\chi(K)=0\) and \(\chi(t)=1\). Then
\[
\boxed{\text{Some }g\in G\text{ satisfies }f(g)=f(gt).}
\tag{1}
\]
In particular, for \(m=3\), some orbit word has at most one switch, regardless of any antipodal constraint on \(f\).

*Proof.* Suppose \(f(gt)=1-f(g)\) for every \(g\). Right-\(K\)-invariance says \(f(gk)=f(g)\) for \(k\in K\). In a word in the generators \(K\cup\{t,t^{-1}\}\), multiplication on the right by \(t\) or \(t^{-1}\) complements \(f\), while multiplication by an element of \(K\) leaves it unchanged. Since \(G=\langle K,t\rangle\), the function \(\chi(g)=f(g)+f(1)\) counts the parity of occurrences of \(t^{\pm1}\) in any such word. It follows that \(\chi(gh)=\chi(g)+\chi(h)\), \(\chi(K)=0\), and \(\chi(t)=1\), a contradiction. Hence (1). A three-letter binary word without two switches has at most one switch; if every three-letter word had two switches, its first two letters would disagree for every \(g\), contradicting (1). \(\square\)

The relevant canonical Coxeter-coset instances are as follows.

**Theorem 2 (common parabolic character vanishing).** In the type-\(A_{n-1}\) instance
\[
G=S_n,\quad K=\{\sigma:\sigma(1)=1,\ \sigma(2)=2,\ \sigma(3)=3\},\quad t=(1\,2\,\cdots\,n),
\tag{2}
\]
the hypotheses of Lemma 1 hold for \(n\ge5\). In the type-\(B_n\) instance
\[
G=\mathbb F_2^n\rtimes S_n,\quad
K=\{(a,\sigma):a\in\{0,e_1\},\ \sigma(1)=1\},\quad
t=(e_1,(1\,2\,\cdots\,n)),
\tag{3}
\]
they hold for \(n\ge3\).

*Proof.* In (2), \(K\) contains the transposition \((4\,5)\); conjugating it by powers of the \(n\)-cycle \(t\) supplies the adjacent transpositions and hence generates \(S_n\). Thus \(G=\langle K,t\rangle\). Every homomorphism \(S_n\to\mathbb F_2\) is a multiple of permutation parity. Because \((4\,5)\in K\), a character vanishing on \(K\) is trivial.

In (3), the projection of \(\langle K,t\rangle\) to \(S_n\) contains the point stabilizer \(S_{\{2,\ldots,n\}}\) and an \(n\)-cycle, hence is all of \(S_n\). The subgroup contains the elementary sign flip \((e_1,\mathrm{id})\in K\); conjugating this flip by lifts of permutations moves it to every dimension. Thus it contains all translations and therefore equals \(\mathbb F_2^n\rtimes S_n\). A homomorphism from \(B_n\) to \(\mathbb F_2\) has the form
\[
\chi(a,\sigma)=A\sum_i a_i+B\,\operatorname{sgn}(\sigma)
\quad(A,B\in\mathbb F_2):
\tag{4}
\]
its restriction to the normal group \(\mathbb F_2^n\) is linear and invariant under permutations, while its restriction to \(S_n\) is a parity character. The subgroup \(K\) contains both \((e_1,\mathrm{id})\) and \((0,(2\,3))\) when \(n\ge3\). Consequently \(\chi(K)=0\) forces \(A=B=0\). \(\square\)

**Corollary 3 (a common proof in the first three-slot ranks).** The classical Coxeter parabolic-coset one-switch conjecture holds for type \(A_4\), namely ordinary reversal-odd boundary 3-tournaments on five vertices, and for type \(B_3\), namely antipodally odd cube-edge colorings of \(Q_3\). In both cases the proposed word has length three and some complete flag has at most one switch.

*Proof.* Apply Lemma 1 and Theorem 2 with \(m=n-2=3\) in (2), or \(m=n=3\) in (3). The coset-word reconstructions identify the resulting words respectively with the triple bits of a Hamilton ordering on all five vertices and the edge bits of a full three-dimension antipodal geodesic. In type \(B_3\), rotating at its possible unique switch yields a monochromatic full geodesic. \(\square\)

The same character argument proves the weaker conclusion (1) at every rank. It rules out a global alternating two-color character on the Coxeter-element arrows while respecting local-incidence descent. For orbit words of length at least four, the presence of one equal neighboring pair does not bound the total number of switches. A full-rank one-switch proof therefore needs a stronger use of the parabolic coset identifications.
