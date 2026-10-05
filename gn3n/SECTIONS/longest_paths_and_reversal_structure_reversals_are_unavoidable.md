# Reversals are unavoidable

## Composition

**Lemma 1.** If two tight paths of order at least three have an order disagreement on their common vertices, then \(H\) contains a tight triple reversing an edge of one of the paths.

**Proof.** Choose a disagreeing pair with minimum union and then minimum total order. If a common edge is traversed in opposite directions, a consecutive tight triple containing that edge reverses the corresponding edge of the other path.

Otherwise the first change of relative order yields a reversing triple unless the two paths close into a vertex-simple tight cycle. Open such a cycle at any edge. Its complement is non-Hamiltonian and has a two-cover \(A\mid B\). Let \((a_{m-1},a_m)\) be an end edge of a nontrivial component \(A\). If both triples needed to concatenate \(A\) to the opened cycle were tight, the concatenation together with \(B\) would two-cover \(H\). Hence one of those triples is non-tight. Boundary reversal then gives a tight triple reversing either \((a_{m-1},a_m)\) or an edge of the opened cycle. \(\square\)

Deletion covers at different vertices cannot all induce one common support partition and one common relative order, since those orders would glue to a two-cover. Hence:

**Corollary 2.** Every minimum counterexample contains a tight triple reversing an edge of a tight path.

The remaining question is where such a reversal can be placed.

### Every prescribed pair forces an endpoint-reversal pattern

The preceding existence statement has a pairwise strengthening.

**Lemma 3.** Let \(H\) be a minimum counterexample and let \(u,v\in V(H)\) be distinct. Then
\[
\operatorname{pc}(H-\{u,v\})=2.
\]
Moreover, in every two-cover
\[
H-\{u,v\}=A\mid C,
\]
both \(A\) and \(C\) have order at least two. Writing
\[
A=(a_1,\ldots ,a_r),\qquad C=(c_1,\ldots ,c_s),
\]
one of the following holds:

1. both
\[
(u,a_r,a_{r-1}),\qquad (v,a_r,a_{r-1})
\]
are tight;

2. both
\[
(c_2,c_1,u),\qquad (c_2,c_1,v)
\]
are tight;

3. after naming one of \(u,v\) as \(z\) and the other as \(w\),
\[
(a_{r-1},a_r,z),\qquad (z,c_1,c_2)
\]
are tight, while
\[
(w,a_r,a_{r-1}),\qquad (c_2,c_1,w)
\]
are tight.

In particular, every prescribed pair \(\{u,v\}\) participates in a spanning three-cover in which an exposed end edge of one of the other two paths is reversed by a tight triple through \(u\) or \(v\).

**Proof.** Every two-vertex set is a tight path. Since \(\{u,v\}\) is a proper Hamiltonian support, minimum-counterexample calculus gives
\[
\operatorname{pc}(H-\{u,v\})\le2.
\]
If \(H-\{u,v\}\) were Hamiltonian, its Hamilton path together with the two-vertex path on \(\{u,v\}\) would give a two-cover of \(H\). Hence the path-cover number is exactly two.

Let \(A\mid C\) be any two-cover of the complement. Neither component can be a singleton. Indeed, if \(A=\{a\}\), then the three-set \(\{u,v,a\}\) has a tight Hamilton path: fixing \(v\) as the middle vertex, exactly one of
\[
(u,v,a),\qquad(a,v,u)
\]
is tight. That three-vertex path together with \(C\) would two-cover \(H\), a contradiction. Thus \(r,s\ge2\).

Now
\[
A\mid(u,v)\mid C
\]
is a spanning three-cover. Apply the two-vertex-middle endpoint classification from the rooted small-support analysis. Its three alternatives are exactly the three displayed patterns above. \(\square\)

Thus reversals in a minimum counterexample are not isolated artifacts of a particular deletion cover or longest path: every chosen vertex pair can be placed into a two-vertex middle component whose complementary two-cover exposes an endpoint reversal. The remaining issue is positional compression, not production of reversals.

### The universal two-vertex-middle reversal descends while preserving itself

The two-vertex-middle construction above has a useful monotonicity property.

**Lemma 4.** Let
\[
A\mid (u,v)\mid C
\]
be a spanning three-cover of a minimum counterexample \(H\). Suppose a tight triple through one of \(u,v\) reverses an end edge of \(A\). Then the same pairwise-repartition component contains a three-cover of strictly smaller quadratic potential in which the same tight triple still reverses the same displayed end edge.

**Proof.** Write
\[
A=(a_1,\ldots,a_r),\qquad C=(c_1,\ldots,c_s),
\]
and suppose, after reversing the displayed order of \(A\) if necessary, that the reversed edge is the terminal edge \(a_{r-1}a_r\). Say
\[
(u,a_r,a_{r-1})
\]
is tight.

If \(s\ge4\), remove an endpoint \(c\) of \(C\). Every three-vertex boundary tournament is Hamiltonian, so \(\{u,v,c\}\) has a Hamilton path, while \(C-c\) inherits a tight path. Thus
\[
(u,v)\mid C
\longrightarrow
\{u,v,c\}\mid(C-c)
\]
is a legal pairwise repartition. Its potential change is
\[
3^2+(s-1)^2-\bigl(2^2+s^2\bigr)=6-2s<0.
\]
The displayed path \(A\), its terminal edge, and the reversing triple are untouched.

It remains that \(s\le3\). Since \(|V(H)|>10\),
\[
r+s+2=|V(H)|\ge11,
\]
so \(r\ge6\). Remove from \(A\) the endpoint opposite the reversed edge, namely \(a_1\). The set \(\{a_1,u,v\}\) has a Hamilton path, while
\[
A-a_1=(a_2,\ldots,a_r)
\]
still displays the same terminal edge \(a_{r-1}a_r\). Hence
\[
A\mid(u,v)
\longrightarrow
(A-a_1)\mid\{a_1,u,v\}
\]
is legal, with
\[
(r-1)^2+3^2-\bigl(r^2+2^2\bigr)=6-2r<0.
\]
Again the same reversal survives.

The initial-edge and \(C\)-side cases are symmetric. \(\square\)

Therefore the universal reversal supplied by Lemma 3 can be pushed at least one strict step downward without losing its exact reversal certificate. This is stronger than the bare observation that every two-vertex-middle state descends: the local obstruction survives the descent and can be used as an invariant in a constrained-minimality argument.


### Frozen-path reversal normal form

The preceding persistence can be globalized by freezing the path that carries the reversed edge.

**Lemma 5 (frozen reversal normal form).** Let \(H\) be a minimum counterexample, let
\[
A=(a_1,\ldots,a_r)
\]
be a proper Hamiltonian path, and suppose \(w\notin A\) satisfies
\[
(w,a_r,a_{r-1})
\]
tight. Then \(H-A\) is non-Hamiltonian with path-cover number two. Choose, among all two-covers
\[
H-A=B\mid C,
\]
one minimizing
\[
\Psi(B,C)=|B|^2+|C|^2.
\]
Then:

1. \(A\mid B\mid C\) is a spanning three-cover carrying the same external reversal \((w,a_r,a_{r-1})\);
2. every two-cover \(B'\mid C'\) of \(H-A\) satisfies
   \[
   \bigl||B'|-|C'|\bigr|
   \ge
   \bigl||B|-|C|\bigr|;
   \]
3. both \(B\) and \(C\) have order at least two;
4. if one of \(B,C\) has order two, then the other has order at most three.

Consequently, if \(|H-A|\ge6\), both components of the frozen minimum have order at least three.

**Proof.** Since \(A\) is a proper Hamiltonian support, minimum-counterexample calculus gives
\[
\operatorname{pc}(H-A)\le2.
\]
The complement cannot be Hamiltonian, since a Hamilton path on \(H-A\) together with \(A\) would two-cover \(H\). Hence
\[
\operatorname{pc}(H-A)=2.
\]

Choose a two-cover \(B\mid C\) minimizing \(\Psi\). The reversal certificate is unaffected: the path \(A\) is fixed, and the vertex \(w\) remains in \(H-A=B\cup C\). This proves (1).

For fixed total order \(|B|+|C|\),
\[
|B|^2+|C|^2
=
\frac{(|B|+|C|)^2+(|B|-|C|)^2}{2}.
\]
Thus minimizing \(\Psi\) is equivalent to minimizing the size difference, proving (2).

Suppose \(B=\{b\}\) is a singleton and put \(|C|=s\). Every tight path in a minimum counterexample has complement of order at least four, so
\[
|H-A|\ge4
\]
and hence \(s\ge3\). Remove an endpoint \(c\) of \(C\). The two-vertex set \(\{b,c\}\) is a tight path and \(C-c\) is an inherited tight path. Thus
\[
\{b\}\mid C
\longrightarrow
(b,c)\mid(C-c)
\]
is a two-cover of \(H-A\) with potential change
\[
2^2+(s-1)^2-\bigl(1+s^2\bigr)=4-2s<0,
\]
contradicting minimality. Hence neither component is a singleton.

Finally suppose \(|B|=2\) and \(|C|=s\ge4\). Remove an endpoint \(c\) of \(C\). Every three-set is Hamiltonian, so \(B\cup\{c\}\) has a Hamilton path, while \(C-c\) remains tight. The repartition
\[
B\mid C
\longrightarrow
(B\cup\{c\})\mid(C-c)
\]
has potential change
\[
3^2+(s-1)^2-\bigl(2^2+s^2\bigr)=6-2s<0,
\]
again contradicting minimality. This proves (3) and (4). \(\square\)

Every external endpoint reversal therefore admits a canonical representative in which the reversed path is fixed and the complementary two-cover is as balanced as Hamiltonicity permits. Any further strict repartition of the complementary union is impossible, while the reversal certificate is still present. This is the natural constrained-minimum state for the reversal branch.


### Terminal normalization around a fixed reversed four-path

The terminal \(3|4|4\) profile admits a sharper normalization than neutral persistence alone.

**Lemma 6 (double reversal or three reciprocal hooks).** Let
\[
T\mid A\mid B
\]
be a spanning \(3|4|4\) three-cover of a minimum counterexample, and write
\[
A=(a_1,a_2,a_3,a_4).
\]
Suppose \(w\in T\) satisfies
\[
(w,a_4,a_3)
\]
tight. Then, after neutral repartitioning only the seven-set
\[
U=V(T)\cup V(B)
\]
and leaving \(A\) fixed, at least one of the following holds.

1. The same vertex \(w\) reverses both displayed end edges of \(A\):
   \[
   (a_2,a_1,w),
   \qquad
   (w,a_4,a_3)
   \]
   are tight.

2. There are three distinct vertices
   \[
   t_1,t_2,t_3\in U-\{w\}
   \]
   such that
   \[
   (a_1,w,t_i)
   \]
   is tight for each \(i\). Consequently either some four-set
   \[
   \{a_1,w,t_i,t_j\}
   \]
   is Hamiltonian, or the five-set
   \[
   \{a_1,w,t_1,t_2,t_3\}
   \]
   is Hamiltonian.

In every state used above the original reversal \((w,a_4,a_3)\) remains unchanged.

**Proof.** By the seven-set prescribed-endpoint theorem in [[localextend01]], the seven-set \(U\), with prescribed vertex \(w\), has a \(4|3\) cover
\[
S\mid R
\]
in which \(S\) has a Hamilton order ending at \(w\). Write
\[
S=(s_1,s_2,t,w),
\]
so \(t\) is the path-neighbor of \(w\). Replacing \(T|B\) by \(S|R\) is a neutral pairwise repartition of the terminal \(3|4|4\) state, while \(A\) is untouched.

Apply the theorem *Two displayed four-paths force an end-edge reversal* from [[line_rooted_small_support_descent_from_deletion_cover_lifts]] to the pair
\[
S\mid A.
\]
With the displayed orders above, it gives
\[
(a_1,w,t)
\qquad\text{or}\qquad
(a_2,a_1,w)
\]
tight.

If \((a_2,a_1,w)\) is tight, outcome 1 holds together with the standing reversal \((w,a_4,a_3)\).

Assume therefore that
\[
(a_2,a_1,w)
\]
is non-tight. The seven-set theorem gives endpoint-rooted \(4|3\) covers with at least three distinct possible neighbors \(t_1,t_2,t_3\) of \(w\). Apply the preceding argument to each such cover. The second alternative is globally excluded, so
\[
(a_1,w,t_i)
\]
is tight for all three \(i\). The three-hook consequence of [[localextend01]] now gives the final Hamiltonian-support dichotomy. \(\square\)

Thus the terminal reversal regime splits into two highly structured local patterns: a single vertex reversing both ends of one four-path, or a three-hook fan from the opposite endpoint into the neutral seven-set. In the latter case the hooks already force a bounded Hamiltonian support through the ordered anchor pair \((a_1,w)\).


### Double reversal forces an anchored bounded support

The difficult branch of Lemma 6 still carries more bounded structure than a generic external reversal.

**Lemma 7 (anchored support from a double reversal).** Let
\[
A=(a_1,a_2,a_3,a_4)
\]
be a tight four-path and let \(w\notin V(A)\) satisfy
\[
(a_2,a_1,w),
\qquad
(w,a_4,a_3)
\]
tight. Put
\[
T=\{a_1,a_4,w\}.
\]
Then at least one of the following holds.

1. One of the four-sets
   \[
   T\cup\{a_2\},
   \qquad
   T\cup\{a_3\}
   \]
   is Hamiltonian.

2. The five-set
   \[
   V(A)\cup\{w\}
   \]
   is Hamiltonian and has a Hamilton path whose two endpoints both lie in \(T\).

In a minimum counterexample, every Hamiltonian support supplied above is proper and has non-Hamiltonian complement of path-cover number two.

**Proof.** If either displayed four-set is Hamiltonian, outcome 1 holds. Assume both are non-Hamiltonian. They have the common three-set
\[
T=\{a_1,a_4,w\}
\]
and distinct exterior vertices \(a_2,a_3\). The two-bad-four-extension lemma in [[localextend01]] applies directly and gives a Hamilton path on
\[
T\cup\{a_2,a_3\}=V(A)\cup\{w\}
\]
whose two endpoints both belong to \(T\). This is outcome 2.

For the final assertion, minimum-counterexample calculus applies to every proper Hamiltonian support: its complement has path-cover number at most two and cannot be Hamiltonian, since otherwise the two Hamilton paths would two-cover \(H\). \(\square\)

Thus the double-reversal branch retains the ordered anchor triple consisting of the reversing vertex and both endpoints of the reversed four-path. Either that anchor already lies in a Hamiltonian four-support, or the surrounding five-support has a Hamilton order with both endpoints inside the anchor. This is the natural form in which to feed the double reversal back into endpoint-rooted comparison.


**Corollary 8 (double reversal returns to a rooted four-support).** Under the hypotheses of Lemma 7, \(H\) has a Hamiltonian four-support \(K\) such that
\[
w\in K,
\qquad
K\cap\{a_1,a_4\}\ne\varnothing,
\qquad
\operatorname{pc}(H-K)=2.
\]

More precisely, either \(K\) contains the whole anchor triple
\[
\{a_1,a_4,w\},
\]
or \(K\) is obtained from the Hamiltonian five-support of Lemma 7 by deleting one of \(a_1,a_4\), and therefore retains \(w\) together with the opposite displayed endpoint of \(A\).

**Proof.** In outcome 1 of Lemma 7 there is already a Hamiltonian four-set containing
\[
T=\{a_1,a_4,w\},
\]
so take it for \(K\).

In outcome 2, let \(F=V(A)\cup\{w\}\) and choose the Hamilton path on \(F\) whose two endpoints both lie in
\[
T=\{a_1,a_4,w\}.
\]
Among those two endpoints, at least one belongs to \(\{a_1,a_4\}\); call it \(z\). Delete \(z\). The remaining four vertices inherit a Hamilton path, so
\[
K=F-\{z\}
\]
is Hamiltonian. It contains \(w\), and it contains the other displayed endpoint of \(A\).

Minimum-counterexample calculus gives
\[
\operatorname{pc}(H-K)\le2.
\]
The complement cannot be Hamiltonian, since otherwise a Hamilton path on \(K\) together with one on \(H-K\) would two-cover \(H\). Hence
\[
\operatorname{pc}(H-K)=2.
\]
\(\square\)

Thus the double-reversal branch does not merely create some bounded support: it returns to the four-support comparison regime while preserving the reversing vertex and at least one endpoint of the original reversed path. This retained incidence is the extra datum available for the next comparison step.


## Neutral internalization of a double reversal

### Every terminal witness has two neutral swaps into either four-component

**Lemma 9 (two neutral witness swaps).** Let
[
Tmid Amid B
]
be a spanning (3|4|4) three-cover, and let (win T). Then there are at least two distinct vertices
[
a,a'in A
]
such that
[
(A-a)+w
qquad	ext{and}qquad
(A-a')+w
]
are Hamiltonian four-sets.

For every such (a), the three-set
[
(T-w)+a
]
is Hamiltonian. Hence
[
Tmid Amid B
longrightarrow
igl((T-w)+aigr)midigl((A-a)+wigr)mid B
]
is a neutral (3|4|4) pairwise repartition.

The same conclusion holds with (A,B) interchanged.

**Proof.** Consider the five-set
[
F=Acup{w}.
]
Every five-vertex boundary tournament has at least three Hamiltonian four-subsets. One of them is (A=F-{w}). Therefore at least two of the remaining four deletions
[
F-{a}=(A-a)+w,qquad ain A,
]
are Hamiltonian.

For every such (a), the set ((T-w)+a) has order three, and every three-vertex boundary tournament has a Hamilton tight path. Thus the displayed repartition is legal. Both sides have profile (3|4), so the quadratic potential is unchanged. (square)

This neutral mobility is independent of the reversal certificate: every distinguished vertex of the three-component has at least two ways to enter either four-component.

**Corollary 10 (double reversal internalization).** Suppose additionally that
[
A=(a_1,a_2,a_3,a_4)
]
and that (w) reverses both displayed end edges:
[
(a_2,a_1,w),
qquad
(w,a_4,a_3)
]
are tight. Then there is a neutral witness swap as in Lemma 9 whose new four-component contains (w) together with an entire reversed end edge and its reversing tight triple.

More precisely, for every swappable (ain A):

- if (ain{a_1,a_2}), the new four-component contains
  [
  {w,a_3,a_4}
  ]
  and retains the tight reversal
  [
  (w,a_4,a_3);
  ]

- if (ain{a_3,a_4}), the new four-component contains
  [
  {a_1,a_2,w}
  ]
  and retains the tight reversal
  [
  (a_2,a_1,w).
  ]

Since Lemma 9 supplies at least two swappable vertices, at least one such neutral internalization always exists. (square)

Thus the difficult double-reversal branch can be moved, without changing the terminal (3|4|4) profile, to a state in which the reversing vertex and a complete reversed edge lie inside one Hamiltonian four-component. This is stronger than preserving only the witness and one old endpoint: the full local reversal certificate survives the neutral move.

## Global marked-reversal minimization

### Imbalance in a frozen complement forces a new reversal carrier

Call a spanning three-cover
[
Amid Bmid C
]
a **marked reversal state** if some vertex outside (A) forms a tight triple reversing an end edge of the displayed path (A).

Choose a marked reversal state minimizing
[
Phi=|A|^2+|B|^2+|C|^2
]
over all marked reversal states of (H).

**Lemma 11 (frozen imbalance forces a carrier switch).** Suppose (A) is marked and, among all two-covers of (H-A), the displayed cover
[
B=(b_1,ldots,b_s)mid C=(c_1,ldots,c_t)
]
minimizes
[
Psi=|B|^2+|C|^2.
]
Assume (2le sle t) and
[
tge s+2.
]
Then each endpoint (cin{c_1,c_t}) of (C) reverses both displayed end edges of (B):
[
(b_2,b_1,c)
qquad	ext{and}qquad
(c,b_s,b_{s-1})
]
are tight.

In particular (B) is itself a valid reversal carrier, with either endpoint of (C) as an external reversing vertex.

**Proof.** Fix an endpoint (c) of (C). Suppose (Bcup{c}) were Hamiltonian. Since deleting an endpoint from the displayed path (C) leaves a tight path, we would obtain a two-cover
[
(Bcup{c})mid(C-c)
]
of (H-A). Its potential differs from that of (Bmid C) by
[
(s+1)^2+(t-1)^2-(s^2+t^2)
=2(s-t+1)le -2,
]
contradicting the choice of (Bmid C).

Thus (Bcup{c}) is non-Hamiltonian. In particular (c) cannot be prepended to the displayed order of (B), so
[
(c,b_1,b_2)
]
is non-tight and boundary antisymmetry gives
[
(b_2,b_1,c)
]
tight. Likewise (c) cannot be appended to (B), so
[
(b_{s-1},b_s,c)
]
is non-tight and therefore
[
(c,b_s,b_{s-1})
]
is tight. (square)

This is a genuine reduction mechanism: imbalance does not merely create a bounded configuration; it moves the reversal certificate from one component to another without changing the spanning cover.

### Consequence at a global marked minimum

**Corollary 12 (largest-component endpoints reverse both smaller components).** Let
[
Amid Bmid C
]
be a marked reversal state minimizing (Phi) globally, and order the component sizes as
[
|A|le |B|le |C|.
]
Suppose
[
|C|ge |B|+2.
]
Then both endpoints of (C) reverse both displayed end edges of (B).

Moreover (B) may now be taken as the marked carrier in the same (Phi)-minimal state. Consequently the displayed two-cover
[
Amid C
]
of (H-B) is also minimum-potential among all two-covers of (H-B). Since
[
|C|ge |B|+2ge |A|+2,
]
Lemma 11 applied with (B) as the marked carrier shows that the same two endpoints of (C) reverse both displayed end edges of (A) as well.

Thus, whenever the largest component is separated from the middle component by at least two vertices, each endpoint (c) of the largest component satisfies all four tight reversals
[
(a_2,a_1,c),qquad(c,a_{|A|},a_{|A|-1}),
]
[
(b_2,b_1,c),qquad(c,b_{|B|},b_{|B|-1}).
]

**Proof.** The first assertion is Lemma 11.

Because (B) now carries an external endpoint reversal, the same three-cover is a marked reversal state with carrier (B). If some two-cover
[
H-B=A'mid C'
]
had
[
|A'|^2+|C'|^2<|A|^2+|C|^2,
]
then
[
Bmid A'mid C'
]
would be a marked reversal state of smaller total (Phi), contradicting global minimality. Hence (Amid C) is frozen-minimal for the carrier (B). Applying Lemma 11 to that frozen complement gives the asserted reversals on (A). (square)

The unresolved global case has therefore narrowed to two regimes:

1. the marked-minimum size profile is nearly balanced at the top,
   [
   |C|le |B|+1;
   ]
2. the two endpoints of the largest component simultaneously reverse both end edges of each smaller component.

This dichotomy is valid for arbitrary order. It is the appropriate starting point for a general reduction to the complementary-splice framework rather than for further bounded-order case analysis.

### Imbalance at a global marked minimum forces bounded support

**Corollary 13.** Let
[
Amid Bmid C
]
be a marked reversal state minimizing (Phi) globally among all marked reversal states, with
[
|A|le |B|le |C|.
]
If
[
|C|ge |B|+2,
]
then (H) contains a Hamiltonian component of order at most five whose complement has path-cover number two. More precisely, either (|A|le3), or there is a Hamiltonian four- or five-support containing an endpoint of (C) and both displayed endpoints of (A).

**Proof.** By Corollary 12, each endpoint (c) of (C) reverses both displayed end edges of (A). Write
[
A=(a_1,ldots,a_r).
]

If (rle3), the displayed component (A) is already a bounded Hamiltonian support, and its complement is two-covered by (Bmid C).

Assume (rge4). Put
[
T={a_1,a_r,c}.
]
Consider the two four-sets
[
Tcup{a_2},
qquad
Tcup{a_{r-1}}.
]
If either is Hamiltonian, we have the required Hamiltonian four-support.

Assume both are non-Hamiltonian. The two-bad-four-extension lemma from [[localextend01]], applied to the common three-set (T) and the two distinct exterior vertices (a_2,a_{r-1}), gives a Hamiltonian path on
[
Tcup{a_2,a_{r-1}},
]
a five-set containing (c) and both displayed endpoints (a_1,a_r).

Thus in all cases there is a Hamiltonian support (K) of order four or five containing the asserted anchor vertices, unless (A) itself already has order at most three.

Since (K) is a proper Hamiltonian support in a minimum counterexample, minimum-counterexample calculus gives
[
operatorname{pc}(H-K)le2.
]
The complement cannot be Hamiltonian, because then (K) together with a Hamilton path on (H-K) would two-cover (H). Hence
[
operatorname{pc}(H-K)=2.
]
(square)

Therefore the imbalanced branch of the global marked-reversal minimum is already reduced, at arbitrary order, to bounded support. The only marked-minimum regime not yet reduced in this way is
[
|C|le |B|+1.
]

This isolates the genuinely global remaining case: a nearly balanced pair of largest components in a marked-reversal state. No bounded-order hypothesis is involved.



### A global marked minimum is almost equitable unless bounded support appears

**Corollary 14.** Let
[
Amid Bmid C
]
be a marked reversal state minimizing (Phi) globally, with
[
|A|le |B|le |C|.
]
If (H) has no Hamiltonian support of order four or five arising from the marked-minimum analysis, then
[
|B|le |A|+1
qquad	ext{and}qquad
|C|le |B|+1.
]
In particular
[
|C|-|A|le2.
]

**Proof.** Corollary 13 already shows that
[
|C|ge |B|+2
]
forces bounded Hamiltonian support. Hence, in the unresolved branch,
[
|C|le |B|+1.
]

It remains to compare (A) and (B). Write
[
A=(a_1,ldots,a_r),
]
and suppose the marked reversal is on the terminal edge (a_{r-1}a_r). Assume for contradiction that
[
|B|ge r+2.
]

Let (z) be any endpoint of (B). If
[
(z,a_1,a_2)
]
were tight, then
[
(z,a_1,ldots,a_r)
]
would be a Hamilton path on (Acup{z}), while deleting the endpoint (z) from (B) leaves a tight path. Repartitioning (Amid B) therefore changes their sizes from
[
(r,|B|)
]
to
[
(r+1,|B|-1).
]
The potential change is
[
(r+1)^2+(|B|-1)^2-r^2-|B|^2
=
2(r-|B|+1)<0.
]
The displayed terminal edge of (A) and its standing external reversal are untouched. Hence the new state is still marked, contradicting global minimality.

Therefore
[
(z,a_1,a_2)
]
is non-tight, and boundary antisymmetry gives
[
(a_2,a_1,z)
]
tight.

The same argument applies to both endpoints of (B). It also applies to both endpoints of (C), since
[
|C|ge|B|ge r+2.
]
Thus there are at least four distinct vertices (zin V(B)cup V(C)) satisfying
[
(a_2,a_1,z)
]
tight.

Choose any three of them. The three-hook consequence of [[localextend01]] produces a Hamiltonian support of order four or five containing the ordered anchor pair
[
(a_2,a_1),
]
contrary to the unresolved assumption.

Hence
[
|B|le |A|+1.
]
Together with
[
|C|le |B|+1,
]
this proves the result. (square)

Thus every unresolved global marked-reversal minimum has an almost equitable size profile:
[
(r,r,r),qquad (r,r,r+1),qquad (r,r+1,r+1),
qquad	ext{or}qquad (r,r+1,r+2)
]
up to the displayed ordering of component sizes.

The remaining global problem is therefore no longer arbitrary imbalance. It is to exploit the marked reversal inside these four near-balanced profile families.



### Carrier switching removes the remaining size gap

**Lemma 15 (carrier switch between displayed components).** Let
[
A=(a_1,ldots,a_r),qquad B=(b_1,ldots,b_s)
]
be two nontrivial components of a spanning three-cover of a minimum counterexample. Then either (B) is a marked reversal carrier in the same three-cover, or (H) contains a Hamiltonian four-support.

**Proof.** The concatenation (AB) cannot be tight, since together with the third displayed component it would give a two-cover. By Lemma 1 of [[global_augmentation_by_complementary_path_splices]], either
[
(b_1,a_r,a_{r-1})
]
is tight, marking (A), or
[
(b_2,b_1,a_r)
]
is tight, marking (B).

Likewise (BA) cannot be tight. Hence either
[
(a_1,b_s,b_{s-1})
]
is tight, marking (B), or
[
(a_2,a_1,b_s)
]
is tight, marking (A).

Suppose (B) is not marked by either comparison. Then
[
(b_1,a_r,a_{r-1}),qquad(a_2,a_1,b_s)
]
are tight.

If
[
(a_1,b_s,b_1)
]
is tight, then
[
(a_2,a_1,b_s,b_1)
]
is a Hamiltonian four-path. If
[
(b_s,b_1,a_r)
]
is tight, then
[
(b_s,b_1,a_r,a_{r-1})
]
is a Hamiltonian four-path. If both displayed middle triples are non-tight, their boundary flips
[
(b_1,b_s,a_1),qquad(a_r,b_1,b_s)
]
are tight, and
[
(a_r,b_1,b_s,a_1)
]
is a Hamiltonian four-path. (square)

**Corollary 16 (full balance or bounded support).** Let
[
Amid Bmid C
]
be a globally (Phi)-minimal marked reversal state with
[
|A|le |B|le |C|.
]
Then either (H) contains a Hamiltonian support of order at most five with two-coverable complement, or
[
|B|le |A|+1,qquad |C|le |B|+1,
]
and in fact
[
|C|-|A|le1.
]

Equivalently the unresolved size profiles are exactly
[
(r,r,r),qquad(r,r,r+1),qquad(r,r+1,r+1).
]

**Proof.** Corollary 14 already gives
[
|B|le |A|+1,qquad |C|le |B|+1.
]
Only the profile ((r,r+1,r+2)) remains to exclude.

Assume
[
|A|=r,qquad |B|=r+1,qquad |C|=r+2.
]
If (rle5), then the displayed Hamiltonian component (A) itself is bounded support with two-coverable complement (Bmid C). Hence assume (rge6).

By Lemma 15, unless a Hamiltonian four-support already exists, (C) can be taken as the marked carrier in this same state. Global marked minimality then implies that
[
Amid B
]
is minimum-potential among all two-covers of (H-C): a lower-potential replacement would give a marked three-cover of smaller total (Phi).

But
[
|B|=|A|+1,
]
so no contradiction yet. Now instead take (B) as marked carrier, again using Lemma 15. Its frozen complement is
[
Amid C,
]
whose component orders differ by two. Lemma 11 therefore applies and says that each endpoint of (C) reverses both displayed end edges of (A). Corollary 13's local double-reversal argument then produces a Hamiltonian support of order at most five with two-coverable complement, contradiction.

Thus the profile ((r,r+1,r+2)) is impossible in the unresolved branch. (square)

Therefore the global marked-reversal problem lands exactly in the three near-equitable size families treated separately in Article II, with no bounded-order hypothesis.



### Global marked minima reduce to two disturbance geometries

**Corollary 17.** Let
[
Amid Bmid C
]
be a globally (Phi)-minimal marked reversal state of a minimum counterexample. Unless a Hamiltonian support of order at most five with two-coverable complement has already appeared, the state has one of the three absolute-minimum profiles
[
(r,r,r),qquad (r,r,r+1),qquad (r,r+1,r+1).
]
Consequently the Article II profile theorems produce, after the standard reductions, either

1. an external tight triple reversing an edge of a relevant displayed or comparison path; or
2. an inherited displayed edge split between two comparison paths, or a leave-and-return disturbance through a nonempty exterior segment.

**Proof.** Corollary 16 leaves exactly the three displayed size profiles. For totals (3r,3r+1,3r+2), respectively, these are the absolute minimizers of
[
x^2+y^2+z^2
]
among positive integer triples of the same sum. Hence the state is a genuine (Phi)-minimum in its whole pairwise-repartition component, not merely among marked states.

Apply the corresponding profile theorem from Article II:
[[quadratic_potential_and_pairwise_repartition_the_size_profile_rrr]],
[[quadratic_potential_and_pairwise_repartition_the_size_profile_r1rr]],
or
[[quadratic_potential_and_pairwise_repartition_the_size_profile_r1r1r]].

Their outputs are order disagreement, direct mixing between displayed supports, split inherited edges, leave-and-return block patterns, reversing tight triples, or the additional same-side recurrence structures in the ((r,r+1,r+1)) profile.

Order disagreement gives an external reversing triple by Lemma 1 of this Section. Direct mixing enters the disturbance theorem
[[path_disturbance_endpoint_reversal_descent_or_an_omission_swap]], which yields split/leave-and-return, external reversal, a two-cover, strict descent, or a compatible omission swap. Strict descent contradicts the global marked minimum whenever the marked certificate survives; the compatible neutral residue is precisely the bridge-manufacture interface now isolated in Article III. The same-side recurrence alternatives either give bounded common-core structure or return to these comparison disturbances by the Article II/IV recurrence analysis.

Thus, outside bounded support and the coherent neutral omission-swap residue, the only genuinely geometric outputs are external reversal and split/leave-and-return. (square)

This gives an arbitrary-order chain
[
	ext{external reversal}
Longrightarrow
	ext{global marked minimum}
Longrightarrow
	ext{absolute equitable profile}
Longrightarrow
	ext{reversal or split disturbance}.
]

Hence the remaining new global mathematics is not a small-order classification. It is the conversion of a split/leave-and-return comparison—or its compatible neutral omission-swap residue—into the abstract one-defect bridge of Article III.



## Marked minima are global minima


### Endpoint polarities on a three-cover force an anchored four-support

The endpoint-polarity triangle theorem remains valid, with the final carrier chosen from the common component rather than from the two exterior twin labels.

**Lemma 18 (endpoint-polarity triangle).** Let
\[
A=(a_1,\ldots,a_r),\qquad
B=(b_1,\ldots,b_s),\qquad
C=(c_1,\ldots,c_t)
\]
be a spanning three-cover of a minimum counterexample, with all three paths nontrivial. Then the six displayed endpoint edges contain a Hamiltonian four-support.

For each unordered pair of displayed paths, either a Hamiltonian four-set already occurs among their endpoint data, or the pair has one of exactly two coherent polarities:

- **initial polarity:** the initial endpoint of each path reverses the terminal edge of the other;
- **terminal polarity:** the terminal endpoint of each path reverses the initial edge of the other.

**Proof.** The pairwise concatenation analysis is unchanged. For a pair \(A,B\), if both junction triples in one displayed concatenation fail, their boundary reversals concatenate to a Hamiltonian four-path. If exactly one junction triple fails in each concatenation order, the mixed failure patterns are absorbed by the carrier-switch comparison. Hence, outside bounded support, only the two coherent polarities remain.

Color the three pair-edges
\[
AB,\ BC,\ CA
\]
by their polarities. A triangle with two colors has a vertex at which the two incident pair-edges have the same color. Suppose this vertex is \(A\).

If both \(AB\) and \(AC\) have initial polarity, then the initial endpoint \(a_1\) reverses the terminal edge of \(B\) and the terminal edge of \(C\). These are vertex-disjoint displayed edges. By the valid common-reverser lemma, one carrier reversing two disjoint terminal edges forces a Hamiltonian four-support.

If both \(AB\) and \(AC\) have terminal polarity, then the terminal endpoint \(a_r\) reverses the initial edge of \(B\) and the initial edge of \(C\). Again these are vertex-disjoint displayed edges, and the symmetric initial-initial common-reverser lemma gives a Hamiltonian four-support.

Thus every two-coloring of the polarity triangle forces the desired support. \(\square\)

The previous proof error was to use the two exterior labels that both reverse one common edge of \(A\). Same-edge twins do not force bounded support. The correct carrier is the corresponding endpoint of \(A\), which reverses two **different** exposed edges, one in each of the other two paths.

Hence the endpoint-polarity network really does force an anchored Hamiltonian four-support in every nontrivial spanning three-cover.


### Every spanning three-cover is already marked

The distinction between a global (Phi)-minimum and a global marked-reversal minimum disappears.

**Lemma 19.** Let (H) be a boundary (3)-tournament with
[
operatorname{pc}(H)ge3,
]
and let
[
Amid Bmid C
]
be any spanning three-cover. Then some displayed end edge of one component is reversed by a tight triple through a vertex of another component. In particular, every spanning three-cover is a marked reversal state.

**Proof.** At most one component can be a singleton. Indeed, if two components were singletons, their two vertices form a tight two-vertex path, and together with the third displayed component this would give a spanning two-cover.

Hence at least two displayed components are nontrivial; relabel them (A) and (B), with
[
A=(a_1,ldots,a_r),qquad B=(b_1,ldots,b_s),
qquad r,sge2.
]
Their union is non-Hamiltonian, since a Hamilton path on (V(A)cup V(B)), together with (C), would two-cover (H).

Consider the displayed concatenation
[
(a_1,ldots,a_r,b_1,ldots,b_s).
]
Every consecutive triple except the two junction triples
[
(a_{r-1},a_r,b_1),qquad
(a_r,b_1,b_2)
]
is inherited and tight. Since the union is non-Hamiltonian, at least one junction triple is non-tight. Boundary reversal therefore gives respectively
[
(b_1,a_r,a_{r-1})
qquad	ext{or}qquad
(b_2,b_1,a_r)
]
tight. The first reverses the terminal edge of (A) through (b_1); the second reverses the initial edge of (B) through (a_r). (square)

**Corollary 20.** In a minimum counterexample, minimizing
[
Phi=|A|^2+|B|^2+|C|^2
]
over all spanning three-covers is exactly the same optimization problem as minimizing (Phi) over marked reversal states.

Hence all conclusions previously proved for a globally (Phi)-minimal marked reversal state apply to an ordinary global (Phi)-minimum of the three-cover repartition graph. In particular, outside the bounded-support conclusions already obtained, the global minimum has one of the equitable profiles
[
(r,r,r),qquad
(r,r,r+1),qquad
(r,r+1,r+1).
]

This removes any need to preserve a particular reversal certificate while descending in (Phi): every intermediate spanning three-cover automatically carries some displayed end-edge reversal.


## Metadata

- ID: longest_paths_and_reversal_structure_reversals_are_unavoidable
- Kind: section
- Version: 20
- Math version: 17
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False

## Development tree

- [Subsection 1 — (untitled)](../SUBSECTIONS/longest_paths_and_reversal_structure_reversals_are_unavoidable_subsection_a.md) (`longest_paths_and_reversal_structure_reversals_are_unavoidable_subsection_a`; development v8; composition v1; stale=False)
- [Subsection 2 — Neutral internalization of a double reversal](../SUBSECTIONS/longest_paths_and_reversal_structure_reversals_are_unavoidable_subsection_b.md) (`longest_paths_and_reversal_structure_reversals_are_unavoidable_subsection_b`; development v3; composition v1; stale=False)
- [Subsection 3 — Global marked-reversal minimization](../SUBSECTIONS/longest_paths_and_reversal_structure_reversals_are_unavoidable_subsection_c.md) (`longest_paths_and_reversal_structure_reversals_are_unavoidable_subsection_c`; development v7; composition v1; stale=False)
- [Subsection 4 — Marked minima are global minima](../SUBSECTIONS/longest_paths_and_reversal_structure_reversals_are_unavoidable_subsection_d.md) (`longest_paths_and_reversal_structure_reversals_are_unavoidable_subsection_d`; development v5; composition vNone; stale=False)
