# Feasible-support antimatroids and minimal non-union certificates

## Metadata

- ID: feasible_support_antimatroids_and_minimal_non_union_certificates
- Parent Section: higher_memory_norine_geodesics
- Position: 41
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Feasible-support antimatroids and minimal failures of union closure

Fix coordinate arity \(r\ge2\), a color \(\sigma\), and an ordered terminal \((r-1)\)-tuple
\[
S=(s_1,\ldots,s_{r-1}).
\]
Define
\[
\mathcal F_{\sigma,S}
=
\{A\subseteq V\setminus S:
\text{some ordering of }A,S\text{ is }\sigma\text{-tight}\}.
\]

### Lemma 1: accessibility

The family \(\mathcal F_{\sigma,S}\) contains \(\varnothing\) and is accessible. If
\[
(a_1,\ldots,a_t,S)
\]
witnesses \(A\in\mathcal F_{\sigma,S}\) with \(A\ne\varnothing\), then
\[
A\setminus\{a_1\}\in\mathcal F_{\sigma,S}.
\]

Thus the only missing axiom for \(\mathcal F_{\sigma,S}\) to be an antimatroid is union closure.

### Lemma 2: minimal failure of union closure gives two deletion certificates

Let \(\mathcal F\) be any finite accessible family containing \(\varnothing\), and suppose it is not union-closed. Choose
\[
A,B\in\mathcal F,\qquad U=A\cup B\notin\mathcal F
\]
so that \(|U|\) is minimum, and subject to this \(|A|+|B|\) is minimum.

Let
\[
\operatorname{ex}(A)=\{a\in A:A\setminus\{a\}\in\mathcal F\}
\]
be the removable elements of \(A\). Then
\[
\operatorname{ex}(A)\subseteq A\setminus B,
\qquad
\operatorname{ex}(B)\subseteq B\setminus A.
\]
Moreover, for every
\[
a\in\operatorname{ex}(A),\qquad b\in\operatorname{ex}(B),
\]
we have
\[
U\setminus\{a\}\in\mathcal F,
\qquad
U\setminus\{b\}\in\mathcal F.
\]

#### Proof

If \(a\in\operatorname{ex}(A)\cap B\), then
\[
(A\setminus\{a\})\cup B=U,
\]
so the smaller pair \(A\setminus\{a\},B\) is still a non-union pair with the same union, contradicting the secondary minimality of \(|A|+|B|\). Hence every removable element of \(A\) lies outside \(B\), and symmetrically for \(B\).

For such an \(a\),
\[
(A\setminus\{a\})\cup B=U\setminus\{a\}.
\]
If this set were infeasible, it would be a non-union pair with strictly smaller union, contradicting the primary minimality of \(|U|\). The statement for \(b\) is symmetric. \(\square\)

Applied to \(\mathcal F_{\sigma,S}\), accessibility guarantees nonempty removable sets, so a minimal failure of union closure always produces distinct vertices
\[
a\in A\setminus B,\qquad b\in B\setminus A
\]
such that both
\[
U\setminus\{a\},\qquad U\setminus\{b\}
\]
admit \(\sigma\)-tight spanning orders ending at the same terminal state \(S\).

If \(P_a\) is a witness for \(U\setminus\{a\}\), infeasibility of \(U\) forces \(a\) to be blocked at the exposed front:
\[
h(a,F_{P_a})=1-\sigma.
\]
Likewise
\[
h(b,F_{P_b})=1-\sigma.
\]
Thus minimal failure of antimatroidality lands exactly in the blocked-front exchange geometry.

### Lemma 3: a near-spanning monochromatic tight path already closes NOR

Suppose
\[
P=(v_1,\ldots,v_{n-1})
\]
is a \(\sigma\)-tight path on \(V\setminus\{x\}\).

If
\[
h(x,v_1,\ldots,v_{r-1})=\sigma,
\]
then \((x,P)\) is a monochromatic spanning tight path.

Otherwise
\[
h(x,v_1,\ldots,v_{r-1})=1-\sigma.
\]
Let
\[
F=(v_1,\ldots,v_{r-1}).
\]
The path \(P^{\rm rev}\) is \((1-\sigma)\)-tight by reversal antisymmetry, and the short branch
\[
(x,F)
\]
is also \((1-\sigma)\)-tight. These two paths form a spanning converging tight fork with common center \(F\) and \(F^{\rm rev}\). By the fork equivalence, there is a spanning coordinate order whose status word changes at most once.

Therefore any counterexample has no monochromatic tight path on \(n-1\) vertices.

Equivalently, for every \(\sigma,S\),
\[
A\in\mathcal F_{\sigma,S}
\quad\Longrightarrow\quad
|A|\le n-r-1
\]
in a counterexample.

### Proposition 4: coordinate arity two gives an antimatroid

When \(r=2\), \(\mathcal F_{\sigma,s}\) is union-closed for every terminal vertex \(s\).

Interpret color-\(\sigma\) ordered pairs as the arcs of a tournament. Let \(A,B\in\mathcal F_{\sigma,s}\), witnessed by directed paths ending at \(s\). Start with a directed Hamilton path on \(A\cup\{s\}\). Take the vertices of a witnessing path for \(B\cup\{s\}\) in reverse order from \(s\) outward and insert the new vertices one at a time.

When a new vertex \(x\) is inserted, its successor on the \(B\)-path is already present and satisfies
\[
x\to y.
\]
Hence \(x\) has an outgoing arc to the current directed path. The standard tournament insertion rule inserts \(x\) immediately before the first current path vertex dominated by \(x\), preserving both directedness and the terminal vertex \(s\).

After all insertions, the resulting directed path spans
\[
A\cup B\cup\{s\}
\]
and ends at \(s\). Thus
\[
A\cup B\in\mathcal F_{\sigma,s}.
\]

Hence \(\mathcal F_{\sigma,s}\) is accessible and union-closed, i.e. an antimatroid.

### Significance

The tournament base case has exact antimatroid structure. Higher coordinate arity preserves accessibility but can lose union closure. A minimal loss of union closure produces two same-terminal deletion certificates together with blocked-front identities, precisely the local geometry already appearing in minimum-counterexample NOR.

This suggests viewing higher NOR as a controlled failure of the antimatroid/tournament insertion mechanism rather than as an unrelated generalization.

## Frontier

- Development version when composed: None
- Development version now: 1
