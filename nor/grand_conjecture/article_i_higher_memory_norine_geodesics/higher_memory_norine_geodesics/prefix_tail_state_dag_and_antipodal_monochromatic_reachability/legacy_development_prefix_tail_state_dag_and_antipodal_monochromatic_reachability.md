# Prefix-tail state DAG and antipodal monochromatic reachability — preserved pre-item development

## Development

## Prefix-tail state DAG and the antipodal reachability criterion

Fix coordinate-label arity \(r\ge 2\) in the directed translation-invariant sector,
\[
h(v_1,\ldots,v_r)\in\{0,1\},
\qquad
h(v_r,\ldots,v_1)=1-h(v_1,\ldots,v_r).
\]
Let
\[
m=n-r+1.
\]

A **prefix-tail state** of rank \(i\), \(0\le i\le m\), is a pair
\[
s=(P;a_1,\ldots,a_{r-1}),
\]
where \(|P|=i\), the displayed tail is an ordered \((r-1)\)-tuple of distinct vertices, and it is disjoint from \(P\).

There is an upward transition
\[
(P;a_1,\ldots,a_{r-1})
\longrightarrow
(P\cup\{a_1\};a_2,\ldots,a_{r-1},x)
\]
for every
\[
x\notin P\cup\{a_1,\ldots,a_{r-1}\}.
\]
Give this transition the color
\[
h(a_1,\ldots,a_{r-1},x).
\]

Every maximal directed path from rank \(0\) to rank \(m\) is uniquely a coordinate permutation
\[
(v_1,\ldots,v_n),
\]
and its transition colors are the sliding \(r\)-tuple status word
\[
h(v_1,\ldots,v_r),\ldots,h(v_{n-r+1},\ldots,v_n).
\]

### Antipodal involution

For
\[
s=(P;S),
\qquad
S=(a_1,\ldots,a_{r-1}),
\]
put
\[
T=V\setminus(P\cup\{a_1,\ldots,a_{r-1}\})
\]
and define
\[
J(s)=(T;S^{\rm rev}).
\]
Then \(J\) sends rank \(i\) to rank \(m-i\) and is fixed-point-free whenever the state DAG has a nonzero rank interval.

If \(s\to t\) is an upward transition of color \(c\), then
\[
J(t)\to J(s)
\]
is the corresponding upward transition after reversal, and its color is \(1-c\). Thus \(J\) reverses the graded direction and complements edge color.

### Monochromatic reachability

For \(\sigma\in\{0,1\}\), let \(R_\sigma\) be the set of states reachable from some rank-zero state by an upward directed path all of whose edges have color \(\sigma\). Rank-zero states belong to both \(R_0\) and \(R_1\) by the empty-path convention. Put
\[
R=R_0\cup R_1.
\]

### Theorem: one change is equivalent to an antipodal reachability intersection

The directed NOR conclusion holds if and only if
\[
R\cap J(R)\ne\varnothing.
\]

#### Proof

Suppose first that a coordinate permutation has a status word with at most one change. Choose a rank \(i\) state \(s\) at the switch, so the prefix transitions from rank \(0\) to \(s\) are monochromatic, say color \(\alpha\), and the suffix transitions from \(s\) to rank \(m\) are monochromatic, say color \(\beta\). Hence \(s\in R_\alpha\).

Reverse the suffix and apply \(J\). Because \(J\) reverses transition direction and complements color, this becomes a monochromatic upward path of color \(1-\beta\) from rank \(0\) to \(J(s)\). Thus \(J(s)\in R_{1-\beta}\), and therefore \(s\in R\cap J(R)\).

Conversely, suppose
\[
s\in R_\sigma,
\qquad
J(s)\in R_\tau.
\]
Take a color-\(\sigma\) upward path from rank \(0\) to \(s\). Take also a color-\(\tau\) upward path from rank \(0\) to \(J(s)\), reverse it, and apply \(J\). This gives an upward path from \(s\) to rank \(m\) whose edges all have color \(1-\tau\).

Concatenating the two paths gives a maximal directed path, hence a coordinate permutation, with status word
\[
\sigma^*(1-\tau)^*.
\]
It changes at most once. \(\square\)

### Counterexample form

A directed-sector counterexample is therefore equivalent to
\[
R\cap J(R)=\varnothing.
\]
This is stronger than working only in the quotient overlap graph: the prefix set records which coordinates have already been used, so every directed path in the state DAG is globally injective.

The reachability sets also satisfy a useful closure rule: if \(s\in R_\sigma\) and an upward edge \(s\to t\) has color \(\sigma\), then \(t\in R_\sigma\). Thus a counterexample would produce two disjoint antipodal reachability regions separated inside a graded state complex, with the edge coloring constraining how their boundaries may be crossed.

### Ternary specialization

For \(r=3\), write a state as
\[
(P;a,b).
\]
For \(\sigma\in\{0,1\}\), let \(F_\sigma(P;a,b)\) denote membership in \(R_\sigma\). Then
\[
F_\sigma(\varnothing;a,b)=\text{true},
\]
and for nonempty \(P\),
\[
F_\sigma(P;a,b)
\iff
\exists x\in P:
F_\sigma(P\setminus\{x\};x,a)
\text{ and }
h(x,a,b)=\sigma.
\]
The involution is
\[
J(P;a,b)=\bigl(V\setminus(P\cup\{a,b\});b,a\bigr).
\]

Hence directed \(N_4\) reduces to the following complement-partition statement:

> There exist distinct \(a,b\), a partition
> \[
> V\setminus\{a,b\}=P\,\dot\cup\,T,
> \]
> and colors \(\sigma,\tau\) such that
> \[
> F_\sigma(P;a,b)
> \quad\text{and}\quad
> F_\tau(T;b,a).
> \]

This is the spanning-fork target with the internal branch orders existentially compressed. It exposes a possible closure route through complementary-set intersection or a Hex/Tucker-type separation argument on the graded state complex.
