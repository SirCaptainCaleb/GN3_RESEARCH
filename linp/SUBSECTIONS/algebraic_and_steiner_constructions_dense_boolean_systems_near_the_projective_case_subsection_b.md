# Theorem 6

## Metadata

- ID: algebraic_and_steiner_constructions_dense_boolean_systems_near_the_projective_case_subsection_b
- Parent Section: algebraic_and_steiner_constructions_dense_boolean_systems_near_the_projective_case
- Position: 2
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Let \(A\) have odd cardinality \(n\), and let \(M\) be the number of unordered pairs \(\{x,y\}\subseteq A\) for which \(x+y\notin A\). If
\[
M<n,
\]
then exactly one of the following holds:

1. \(A=W\setminus\{0\}\) for a subspace \(W\);
2. \(A=W\setminus\{0,a,b\}\) for a subspace \(W\) and distinct nonzero \(a,b\in W\).

#### Proof
Put
\[
S=A\cup\{0\}.
\]
For \(x\in S\), let
\[
b_S(x)=|\{y\in S:x+y\notin S\}|.
\]
Each missing unordered sum contributes two ordered failures, so
\[
\sum_{x\in S}b_S(x)=2M. \tag{7}
\]

For nonzero \(x\), translation by \(x\) partitions the ambient group into pairs \(\{y,y+x\}\). Thus \(b_S(x)\) counts the pairs with one point in S and the other outside S, and since \(|S|\) is even,
\[
b_S(x)\equiv0\pmod2.
\]
Because \(2M<2n\), some nonzero \(k\in S\) has \(b_S(k)=0\). Hence
\[
S+k=S.
\]

Let \(K\) be the full translation stabilizer of \(S\). Then \(K\) is a nontrivial subgroup and
\[
S=\pi^{-1}(T)
\]
for a subset \(T\) of the quotient group \(G/K\) with trivial translation stabilizer. Put \(q=|K|\) and \(s=|T|\). If
\[
F_T=\sum_{t\in T}|\{u\in T:t+u\notin T\}|,
\]
then
\[
2M=q^2F_T. \tag{8}
\]
Trivial stabilizer gives \(F_T\ge s-1\), while \(M<n=qs-1\) gives
\[
q^2F_T<2(qs-1). \tag{9}
\]

If \(q\ge4\) and \(s>1\), (8)–(9) contradict \(F_T\ge s-1\). Hence either \(s=1\), which gives \(S=K\), or \(q=2\).

Assume \(q=2\) and \(s>1\). Then (8)–(9) force
\[
F_T=s-1.
\]
Consequently every nonzero \(t\in T\) has exactly one partner \(u\in T\) for which \(t+u\notin T\). The graph of these exceptional pairs is therefore a matching. If \(\{a,b\}\) and \(\{c,d\}\) are two exceptional pairs, every cross pair between them is ordinary, and comparing the unique exceptional partners shows
\[
a+b=c+d.
\]
Thus all exceptional pairs have one common sum \(h\notin T\). It follows that
\[
T\cup\{h\}
\]
is a subgroup of \(G/K\). Its preimage \(W\) is a subgroup of \(G\), and the missing coset over \(h\) has exactly two points \(a,b\). Hence
\[
A=W\setminus\{0,a,b\}.
\]
∎

Thus every sufficiently dense Boolean candidate lies in the projective family or a two-point deletion of it. Both families have spanning paths in all sufficiently large dimensions. Therefore this dense Boolean branch has no infinite improvement beyond the small projective exceptions.

A more general density-beating Boolean example can also be reduced to a two-point fibre extension of a smaller quotient: after deleting at most the naturally occurring translation-boundary points, the remaining domain is invariant under a nonzero translation and hence is a full two-point fibre over a quotient. Therefore it is enough to consider such two-point fibre extensions.

## Frontier

- Development version when composed: None
- Development version now: 1
