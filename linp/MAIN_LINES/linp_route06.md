# Main Line 6 — Algebraic and Steiner constructions

# Algebraic and Steiner constructions

This rehearsal concerns lower bounds. A finite \(P_\ell^{(3)}\)-free linear \(3\)-graph \(G\) with \(v\) vertices and \(m\) edges gives, by taking disjoint copies,
\[
\operatorname{ex}_L(n,P_\ell^{(3)})
\ge
\frac{m}{v}n-O(v). \tag{1}
\]
The aim is therefore to construct finite components whose ratio \(m/v\) is as large as possible relative to their longest linear path.

## 1. The general one-third-scale construction

### Proposition 1
For every \(\ell\ge2\),
\[
\operatorname{ex}_L(n,P_\ell^{(3)})
\ge
\frac{\ell-1}{3}n-O(\ell^2). \tag{2}
\]

#### Proof
A linear \(3\)-uniform path with \(\ell\) edges has \(2\ell+1\) vertices. Hence every linear triple system on at most \(2\ell\) vertices is \(P_\ell^{(3)}\)-free.

If \(\ell\equiv1\) or \(2\pmod 3\), then
\[
2\ell-1\equiv1\text{ or }3\pmod6.
\]
Take a Steiner triple system on
\[
t=2\ell-1
\]
vertices. It has
\[
\frac{t(t-1)}6
\]
edges, so
\[
\frac{|E|}{t}
=
\frac{t-1}{6}
=
\frac{\ell-1}{3}.
\]

If \(\ell\equiv0\pmod3\), take a maximum partial triple system on
\[
t=2\ell\equiv0\pmod6
\]
vertices. Such a system has
\[
\frac{t(t-2)}6
\]
edges, and again
\[
\frac{|E|}{t}
=
\frac{t-2}{6}
=
\frac{\ell-1}{3}.
\]

Take \(\lfloor n/t\rfloor\) disjoint copies and leave the remaining vertices isolated. The omitted final component costs \(O(\ell^2)\) edges. ∎

To improve the leading coefficient, one needs components with density near or above \(\ell/3\) whose longest path is still shorter than \(\ell\).

## 2. Binary projective systems

Let
\[
V=\mathbb F_2^d\setminus\{0\},
\]
and let \(H_d\) have as edges the triples
\[
\{x,y,x+y\}
\]
with \(x,y\) distinct. This is the projective Steiner triple system on \(2^d-1\) points.

A spanning path in \(H_d\) has a useful parity constraint.

### Lemma 2
Suppose a spanning linear path in \(H_d\) has joint set \(J\). Then
\[
\sum_{x\in J}x=0. \tag{3}
\]

#### Proof
Every hyperedge has vector sum zero. Sum the edge equations along the path. Every joint is counted twice and every other vertex once. Since the path is spanning, the total of the vertices counted once is the sum of all nonzero vectors of \(\mathbb F_2^d\), which is zero. In characteristic two, the doubled joints disappear from the sum of the edge equations, leaving (3). ∎

For \(d=4\), this obstruction is strong enough to forbid a spanning path.

### Theorem 3
The projective system on \(\mathbb F_2^4\setminus\{0\}\) contains no \(7\)-edge linear path. Consequently
\[
\operatorname{ex}_L(n,P_7^{(3)})
\ge
\frac73 n-O(1). \tag{4}
\]

#### Proof
The system has \(15\) vertices and
\[
\binom{15}{2}/3=35
\]
edges. A \(7\)-edge linear \(3\)-uniform path has \(15\) vertices, so any such path would be spanning.

Let \(j_1,\ldots,j_6\) be the joints of a hypothetical spanning path. By Lemma 2,
\[
j_1+\cdots+j_6=0. \tag{5}
\]
The six vectors lie in a \(4\)-dimensional vector space, so their relation space has dimension at least two. Besides (5), choose a nonzero proper relation and replace its support by its complement if necessary. Its support has size at most three. A zero-sum set of distinct nonzero vectors cannot have size one or two, so it has size three. Hence the joints split as
\[
J=U^*\sqcup W^*,
\]
where \(U^*=U\setminus\{0\}\) and \(W^*=W\setminus\{0\}\) for complementary \(2\)-dimensional subspaces
\[
\mathbb F_2^4=U\oplus W.
\]

Two consecutive joints cannot both lie in \(U^*\). If \(u,u'\in U^*\) were consecutive, their path edge would also contain \(u+u'\), the third point of \(U^*\), which is another joint, contrary to the intersection pattern of a linear path. The same holds for \(W^*\). Thus
\[
j_1,\ldots,j_6
\]
alternates between \(U^*\) and \(W^*\).

Identify the nine vectors outside \(U^*\cup W^*\) with the edges of \(K_{3,3}\): the vector \(u+w\) corresponds to the edge \(uw\), where \(u\in U^*\) and \(w\in W^*\). The joint sequence is a Hamilton path \(T\) of \(K_{3,3}\), and the five internal nonjoint vertices of the hypergraph path correspond exactly to the five edges of \(T\).

The four remaining nonjoint vertices therefore correspond to
\[
E(K_{3,3})\setminus E(T).
\]
Assume \(j_1\in U^*\), so \(j_6\in W^*\). The first hyperedge contains \(j_1\) and two of these four remaining vertices. Writing them as
\[
u+w,\qquad u'+w',
\]
their sum is \(j_1\in U\), so \(w=w'\). Hence the two corresponding edges of \(K_{3,3}\setminus T\) share the vertex \(w\).

In the complement of a Hamilton path of the cubic graph \(K_{3,3}\), the only vertices of degree two are the endpoints \(j_1,j_6\). Since \(w\in W^*\), we must have \(w=j_6\). The two \(U\)-neighbors required by the first hyperedge include \(j_5\), so the complement would contain \(j_5j_6\). But \(j_5j_6\) is the last edge of the Hamilton path \(T\), a contradiction.

Thus the projective system is \(P_7^{(3)}\)-free. Taking disjoint copies gives (4). ∎

This exceptional obstruction does not persist in higher dimensions. For all sufficiently large projective dimensions, the projective system has a spanning linear path. Likewise, deleting two prescribed nonzero points from a sufficiently large projective system still leaves a spanning linear path. Thus the projective construction yields isolated exceptional lengths rather than an infinite improvement.

## 3. Ternary affine systems

Let \(A_d\) be the affine Steiner triple system on \(\mathbb F_3^d\), whose edges are affine lines.

### Lemma 4
If \(A_d\) has a spanning linear path with joint set \(J\), then
\[
\sum_{x\in J}x=0. \tag{6}
\]

#### Proof
Every affine line has the form
\[
\{x-a,x,x+a\},
\]
whose sum is zero in \(\mathbb F_3^d\). Sum the edge equations along a spanning path. Every nonjoint vertex is counted once and every joint twice. The sum of all vectors of \(\mathbb F_3^d\) is zero, so the resulting equality is exactly (6). ∎

### Proposition 5
The affine plane \(A_2\) contains no spanning \(4\)-edge linear path.

#### Proof
A spanning \(4\)-edge path on nine vertices has three joints. By Lemma 4, their sum is zero. Three distinct points of \(\mathbb F_3^2\) sum to zero exactly when they form an affine line. But then the edge determined by two consecutive joints contains the third joint as well, contradicting the intersection pattern of a linear path. ∎

This obstruction is not stable with dimension. In \(A_3\), the following thirteen affine lines form a spanning \(13\)-edge path:
\[
\begin{aligned}
&\{000,100,200\},\ \{000,001,002\},\ \{001,010,022\},\\
&\{010,110,210\},\ \{011,110,212\},\ \{012,112,212\},\\
&\{012,102,222\},\ \{021,120,222\},\ \{120,121,122\},\\
&\{101,111,121\},\ \{020,111,202\},\ \{202,211,220\},\\
&\{201,211,221\}.
\end{aligned}
\]
Consecutive lines meet once, nonconsecutive lines are disjoint, and their union is all \(27\) points. Thus the joint-sum condition alone cannot yield an infinite affine family.

## 4. Dense Boolean systems near the projective case

Let \(A\subseteq\mathbb F_2^r\setminus\{0\}\), and put an edge on every triple
\[
\{x,y,x+y\}\subseteq A.
\]
Dense examples of this form are strongly constrained.

### Theorem 6
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

## 5. Incidence-code obstruction and its limitation

Let \(M_H\) be the vertex-edge incidence matrix of a linear \(3\)-graph over \(\mathbb F_2\).

### Lemma 7
If \(H\) contains a linear path with \(\ell\) edges, then the binary column span of \(M_H\) contains a vector of Hamming weight \(\ell+2\).

#### Proof
Sum the incidence vectors of the \(\ell\) path edges. Every joint occurs twice and cancels. The remaining vertices are the two endpoints and the \(\ell\) private vertices, altogether \(\ell+2\) coordinates. ∎

Thus absence of weight \(\ell+2\) is a sufficient condition for \(P_\ell^{(3)}\)-freeness. It cannot, however, prove a density above \(\ell/3\).

### Theorem 8
If
\[
\frac{|E(H)|}{|V(H)|}>\frac{\ell}{3},
\]
then the binary incidence code of \(H\) contains a word of weight \(\ell+2\).

#### Proof
Pass to the \(>\ell/3\)-core. It is nonempty, has the same or larger density, and has minimum degree greater than \(\ell/3\). Its average degree exceeds \(\ell\), so some vertex \(v\) has degree at least \(\ell+1\). The edges through \(v\) form a linear star, whose \(2d\) vertices outside \(v\) are all distinct.

The sum of \(k\) star edges has weight \(2k\) when \(k\) is even and \(2k+1\) when \(k\) is odd.

If \(\ell\equiv2\pmod4\), take \(k=(\ell+2)/2\). If \(\ell\equiv1\pmod4\), take \(k=(\ell+1)/2\). These give the required weight directly.

If \(\ell\equiv0\pmod4\), choose an edge \(f\) not containing \(v\). It meets at most three star edges. Choose
\[
k=\frac{\ell-2}{2}
\]
star edges disjoint from \(f\); their sum has weight \(\ell-1\), and adding \(f\) gives weight \(\ell+2\).

If \(\ell\equiv3\pmod4\), choose a star edge \(e=\{v,a,b\}\) and another edge \(f\ne e\) through \(a\). Choose
\[
k-1=\frac{\ell-1}{2}
\]
further star edges disjoint from \(f\). The sum of these \(k\) star edges has weight \(\ell+1\), and adding \(f\), which meets the support exactly in \(a\), changes the weight to \(\ell+2\). ∎

Therefore a code construction must use more information than the absence of one support size.

## 6. General obstructions to amplification

Several natural ways to enlarge the exceptional small systems do not improve the asymptotic coefficient.

### Proposition 9
A fixed number of full two-bit Boolean fibre extensions cannot increase the limiting normalized density
\[
\frac{|E(H)|}{|V(H)|(L(H)+1)},
\]
where \(L(H)\) is the maximum linear-path length.

#### Proof
If a Boolean domain has \(v\) vertices and \(m\) additive triples, a full two-bit extension has
\[
4v+3
\]
vertices and
\[
16m+6v+1
\]
edges. If the original maximum path length is \(L\), the extended system contains a path of length at least
\[
4L-1,
\]
and when \(L\) is even, at least \(4L+3\). Thus vertex count, edge density, and maximum path length all scale by the same factor \(4\), up to bounded additive terms. Repeating a fixed number of times cannot increase the limiting ratio. ∎

### Proposition 10
Let \(S\) be an edge-transitive Steiner triple system on \(v=2\ell+1\) vertices. If \(S\) has a spanning \(\ell\)-edge path, then every set of blocks meeting every spanning \(\ell\)-edge path has size at least
\[
v/3. \tag{10}
\]

#### Proof
Fix one spanning path \(P\), and choose a uniformly random automorphism from an edge-transitive automorphism group. For any fixed block \(e\),
\[
\Pr(e\in \gamma(P))
=
\frac{\ell}{|E(S)|}
=
\frac{3}{v}.
\]
If \(D\) meets every spanning path, then
\[
1
\le
\mathbb E|D\cap E(\gamma(P))|
=
\frac{3|D|}{v}.
\]
Hence \(|D|\ge v/3\). ∎

Deleting enough blocks to destroy all spanning paths therefore already loses the amount of density needed to return to the general \((\ell-1)/3\) benchmark.

Large full Steiner triple systems also contain linear paths on \((1-o(1))v\) vertices. Consequently, if such systems themselves are used as components, their normalized density at the first forbidden path length is at most
\[
\frac13+o(1). \tag{11}
\]

Ordinary Steiner-system doubling has the same limitation. Its mixed triples are obtained from a proper edge-coloring of a complete graph, and long rainbow graph paths lift to long linear hypergraph paths. Hence the doubled system already contains paths of length comparable with half its order, preventing a coefficient above one third.

Binary-projective diagonal tensor squares also fail. For \(d\ge3\), put
\[
M=2^d-1,\qquad N=2^{d-1}-1.
\]
Choose multiplicative generators \(\alpha,\beta\) of orders \(M,N\). Since \(\gcd(M,N)=1\), the sequence
\[
q_i=(\alpha^i x,(1,\beta^i z)),
\qquad 0\le i<MN,
\]
has period \(MN\). Put
\[
d_i=q_{i-1}+q_i.
\]
The \(q_i\) are distinct, the \(d_i\) are distinct, and the two sets are disjoint because their distinguished second-coordinate bits differ. Hence
\[
\{q_{i-1},q_i,d_i\},\qquad 1\le i<MN,
\]
form a linear path of length \(MN-1\). The tensor square has normalized density strictly below \(1/3\) at its first forbidden length.

These observations rule out the direct higher-dimensional projective, affine, single-weight-code, repeated fibre-extension, symmetric-deletion, ordinary-doubling, and diagonal-tensor enlargements of the preceding small examples.

## 7. The two-point-fibre problem

The most economical remaining Boolean model has one distinguished point \(\infty\) and, over each point \(x\) of a binary projective quotient, a pair
\[
G_x=\{(x,0),(x,1)\}.
\]
For each \(x\), include
\[
\{\infty,(x,0),(x,1)\}.
\]
For each projective line \(\{x,y,z\}\), choose a bit
\[
\sigma(x,y,z)\in\mathbb F_2
\]
and include the four triples satisfying
\[
b_x+b_y+b_z=\sigma(x,y,z). \tag{12}
\]
Flipping the two labels in one fibre \(G_x\) changes the bits on all quotient lines through \(x\), so only the equivalence class of the line-sign function under such fibre flips affects the isomorphism type.

### Open problem
Determine whether there is an infinite family of line-sign functions in (12) for which the resulting Steiner triple systems have no spanning linear path.

A positive answer would produce an infinite family of dense algebraic components outside the projective and affine obstructions above. A negative answer would close the principal remaining low-rank Boolean construction family.

Any further construction based on dense Steiner or additive systems must use a global obstruction not already removed by the preceding arguments.
