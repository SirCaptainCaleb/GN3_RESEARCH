# Article V — longest paths and reversal structure

---

## Section — Introduction

<!-- section_id: longest_paths_and_reversal_structure_introduction -->

Let \(H\) be a minimum counterexample to \(\operatorname{pc}(H)\le2\). A tight triple \((x,v,u)\) reverses the ordered edge \((u,v)\) of a tight path.

---

## Section — Reversals are unavoidable

<!-- section_id: longest_paths_and_reversal_structure_reversals_are_unavoidable -->

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


### Neutral internalization of a double reversal

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

### Global marked-reversal minimization

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



### Marked minima are global minima



### Endpoint polarities on a three-cover force an anchored four-support

The pairwise concatenation failures of three displayed paths have a parity obstruction.

**Lemma 18 (endpoint-polarity triangle).** Let
\[
A=(a_1,\ldots,a_r),\qquad
B=(b_1,\ldots,b_s),\qquad
C=(c_1,\ldots,c_t)
\]
be a spanning three-cover of a minimum counterexample, with all three paths nontrivial. Then the six displayed endpoint edges contain a Hamiltonian four-support.

More precisely, for each unordered pair of displayed paths, either a Hamiltonian four-set already occurs among their four endpoint edges, or the pair has one of exactly two coherent polarities:

- **initial polarity:** the initial endpoint of each path reverses the terminal edge of the other;
- **terminal polarity:** the terminal endpoint of each path reverses the initial edge of the other.

These pair-polarities cannot be assigned consistently on the triangle \(AB,BC,CA\) without forcing a Hamiltonian four-support.

**Proof.** Consider two paths \(A,B\). Since \(A\cup B\) cannot be Hamiltonian, the concatenation
\[
A,B
\]
has at least one failed junction triple among
\[
(a_{r-1},a_r,b_1),
\qquad
(a_r,b_1,b_2).
\]
If both fail, boundary reversal gives
\[
(b_1,a_r,a_{r-1}),
\qquad
(b_2,b_1,a_r)
\]
tight, so
\[
(b_2,b_1,a_r,a_{r-1})
\]
is a Hamiltonian four-path. Hence, outside the desired conclusion, exactly one of the two junction triples fails.

The same applies to the reverse concatenation
\[
B,A,
\]
whose possible failed junction triples are
\[
(b_{s-1},b_s,a_1),
\qquad
(b_s,a_1,a_2).
\]

Suppose the failure in \(AB\) is the first triple and the failure in \(BA\) is the second. Then
\[
(b_1,a_r,a_{r-1}),
\qquad
(a_2,a_1,b_s)
\]
are tight: both failures mark \(A\), while neither marks \(B\). Lemma 15 above shows that this already forces a Hamiltonian four-support. The symmetric mixed pattern similarly forces one.

Therefore, outside the Hamiltonian-four-support conclusion, the only two possibilities are:

1. the first junction triple fails in both \(AB\) and \(BA\), giving
   \[
   (b_1,a_r,a_{r-1}),
   \qquad
   (a_1,b_s,b_{s-1})
   \]
   tight. This is the initial polarity;

2. the second junction triple fails in both \(AB\) and \(BA\), giving
   \[
   (b_2,b_1,a_r),
   \qquad
   (a_2,a_1,b_s)
   \]
   tight. This is the terminal polarity.

Thus each pair \(AB,BC,CA\) receives one of two polarities unless a Hamiltonian four-support already exists.

Now inspect one component, say \(A\). If the two incident pairs \(AB\) and \(AC\) have the same polarity, then two distinct exterior endpoint labels—one from \(B\), one from \(C\)—reverse the same exposed end edge of \(A\). Lemma 38 then yields a Hamiltonian four-support.

Hence, outside the desired conclusion, the two pair-polarities incident with \(A\) must be different. The same must hold at \(B\) and at \(C\). But a triangle cannot have its edges colored with two colors so that the two incident edges at every vertex have different colors. This contradiction proves the lemma. \(\square\)

The significance is not the mere existence of a small Hamiltonian set. The support is forced directly by the endpoint-reversal network of an arbitrary spanning three-cover. Thus every globally minimal marked-reversal state contains an endpoint-anchored Hamiltonian four-support generated by the same reversal geometry, with no bounded-order hypothesis.


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


---

## Section — A longest path

<!-- section_id: longest_paths_and_reversal_structure_a_longest_path -->

Choose a longest tight path
\[
A=(a_0,\ldots ,a_{\lambda-1})
\]
and put
\[
U=V(H)-V(A).
\]

**Lemma 3.**
1. \(H[U]\) is non-Hamiltonian and has path-cover number two.
2. For every \(y\in U\),
\[
(a_1,a_0,y),\qquad
(y,a_{\lambda-1},a_{\lambda-2})
\]
are tight.
3. The complement of every nonempty proper contiguous subpath of \(A\) is non-Hamiltonian and has path-cover number two.

**Proof.** If \(H[U]\) were Hamiltonian, Hamilton paths on \(A\) and \(U\) would two-cover \(H\). Minimality gives a two-cover of every proper induced subtournament, proving (1).

If \((y,a_0,a_1)\) were tight, prepending \(y\) would give a longer tight path. Hence \((y,a_0,a_1)\) is non-tight and boundary reversal gives \((a_1,a_0,y)\) tight. The other end is symmetric.

Let \(I\) be a nonempty proper contiguous subpath of \(A\). If \(H-I\) were Hamiltonian, Hamilton paths on \(I\) and \(H-I\) would two-cover \(H\). Minimality again gives path-cover number two. \(\square\)

No two-cover of \(U\cup\{a_0,a_1\}\) can have a component ending with \((a_0,a_1)\), since the inherited suffix of \(A\) could then be appended. The symmetric statement holds at the other end. Thus the two reversed endpoint families coexist but cannot be joined directly.

### Lexicographic longest-path normal form

The global longest-path reduction can be sharpened by extremizing the complementary two-cover as well.

**Lemma 4 (lexicographic three-cover normal form).** Let \(H\) be a minimum counterexample. Choose a globally longest tight path
\[
A=(a_1,\ldots,a_r).
\]
By Lemma 3, \(H-A\) is non-Hamiltonian with path-cover number two. Among all two-covers
\[
H-A=P\mid Q,
\]
choose one for which \(\max\{|P|,|Q|\}\) is maximum, and relabel so that
\[
|P|\ge |Q|.
\]
Write
\[
P=(p_1,\ldots,p_m),\qquad Q=(q_1,\ldots,q_t).
\]

Then every displayed endpoint \(q\in\{q_1,q_t\}\) simultaneously reverses both end edges of both \(A\) and \(P\):
\[
(a_2,a_1,q),\qquad (q,a_r,a_{r-1}),
\]
and
\[
(p_2,p_1,q),\qquad (q,p_m,p_{m-1})
\]
are tight whenever the corresponding paths have order at least two.

Equivalently, \(q\) is noninsertable at every position of the displayed orders of both \(A\) and \(P\).

**Proof.** Since \(A\) is globally longest, \(A\cup\{q\}\) is non-Hamiltonian for every \(q\notin A\). Applying [[endpoint_replacement_truncation_dichotomy01]] to the displayed order of \(A\) shows that \(q\) is noninsertable at every gap of \(A\). In particular the two endpoint insertions fail, and boundary antisymmetry gives
\[
(a_2,a_1,q),\qquad(q,a_r,a_{r-1})
\]
tight.

Now let \(q\) be an endpoint of \(Q\). If \(P\cup\{q\}\) were Hamiltonian, then deleting \(q\) from the displayed endpoint of \(Q\) would leave a tight path \(Q-q\), and
\[
(P\cup\{q\})\mid(Q-q)
\]
would be a two-cover of \(H-A\) whose larger component has order \(|P|+1\). This contradicts the extremal choice of \(P\mid Q\). Thus \(P\cup\{q\}\) is non-Hamiltonian. Applying [[endpoint_replacement_truncation_dichotomy01]] again, now to \(P\), shows that \(q\) is noninsertable at every gap of the displayed order of \(P\). Hence its two endpoint insertion triples are non-tight, and their boundary reversals give
\[
(p_2,p_1,q),\qquad(q,p_m,p_{m-1})
\]
tight. \(\square\)

Thus the smallest component of a lexicographically extremal three-cover is not merely hard to absorb into one neighboring path. Each of its endpoints is simultaneously blocked from both larger paths and reverses both exposed end edges of each.

This converts the general two-cover problem into a two-path merger problem with a common obstruction certificate:

> **Four-ended merger problem.** Let \(A\mid P\mid Q\) be in the lexicographic normal form above. Use one endpoint of \(Q\), or both when \(|Q|\ge2\), together with the simultaneous reversal constraints on \(A\) and \(P\) to construct either a path on \(A\cup P\cup\{q\}\), a lexicographically larger three-cover, or a spanning two-cover.

Unlike the order-eleven reductions, this formulation is valid for arbitrary order and directly targets elimination of one whole path component.


### Endpoint transfer or mutual reversal inside the complement

The lexicographic normal form admits an explicit two-vertex augmentation step.

**Lemma 5 (two-vertex transfer dichotomy).** Work in the setting of Lemma 4, with
\[
P=(p_1,\ldots,p_m),\qquad Q=(q_1,\ldots,q_t),\qquad m\ge t.
\]
Assume \(m\ge3\) and \(t\ge2\).

At the left ends, exactly one of the following holds:

1. the path
   \[
   (p_2,p_1,q_1,q_2,\ldots,q_t)
   \]
   is tight, and therefore
   \[
   (p_2,p_1,q_1,\ldots,q_t)\mid(p_3,\ldots,p_m)
   \]
   is a two-cover of \(H-A\) with component orders
   \[
   t+2,\qquad m-2;
   \]
2. the triple
   \[
   (q_2,q_1,p_1)
   \]
   is tight, so \(p_1\) reverses the initial edge \(q_1q_2\) of \(Q\).

Symmetrically, at the right ends, exactly one of the following holds:

1. the path
   \[
   (q_1,\ldots,q_t,p_m,p_{m-1})
   \]
   is tight, and therefore
   \[
   (p_1,\ldots,p_{m-2})\mid(q_1,\ldots,q_t,p_m,p_{m-1})
   \]
   is a two-cover of \(H-A\) with component orders
   \[
   m-2,\qquad t+2;
   \]
2. the triple
   \[
   (p_m,q_t,q_{t-1})
   \]
   is tight, so \(p_m\) reverses the terminal edge \(q_{t-1}q_t\) of \(Q\).

If \\(m\\ge4\\) and both transfer alternatives hold simultaneously, then
\[
(p_2,p_1,q_1,\ldots,q_t,p_m,p_{m-1})
\]
is a tight path and, together with
\[
(p_3,\ldots,p_{m-2}),
\]
gives a two-cover of \(H-A\) with component orders
\[
t+4,\qquad m-4
\]
when the middle path is nonempty.

**Proof.** By Lemma 4, the left endpoint \(q_1\) is noninsertable at the left end of \(P\), so
\[
(p_2,p_1,q_1)
\]
is tight.

Test the next junction triple
\[
(p_1,q_1,q_2).
\]
If it is tight, then the displayed path
\[
(p_2,p_1,q_1,q_2,\ldots,q_t)
\]
is tight, because all later triples are inherited from \(Q\). The remaining vertices of \(P\) form the inherited path
\[
(p_3,\ldots,p_m).
\]
This proves the left transfer alternative.

If \((p_1,q_1,q_2)\) is non-tight, boundary antisymmetry gives
\[
(q_2,q_1,p_1)
\]
tight, which is the mutual-reversal alternative.

The right-hand statement is symmetric. If both transfer junctions are tight, their two constructions concatenate through the whole displayed order of \(Q\), giving the final path and the inherited middle segment of \(P\). \(\square\)

**Corollary 6 (near-balanced complements force mutual reversal).** Under the same hypotheses:

- if \(m-t\le1\), both ends are in the mutual-reversal alternative;
- if \(m-t\le3\), at least one end is in the mutual-reversal alternative.

**Proof.** A single transfer creates a component of order \(t+2\). If \(m-t\le1\), then \(t+2>m\), contradicting the maximal choice of the larger component \(P\) in Lemma 4. Hence neither transfer is possible.

If both transfers occur, the resulting two-cover has a component of order \(t+4\). When \(m-t\le3\), this exceeds \(m\), again contradicting maximality. Hence at least one transfer must fail, and the corresponding mutual reversal occurs. \(\square\)

Thus, when the complementary two-cover is close to balanced, an endpoint of \(Q\) and the corresponding endpoint of \(P\) reverse one another's exposed end edges, while both endpoints already reverse the two ends of the globally longest path \(A\). This is a genuinely global terminal pattern, independent of the total order of \(H\).


### A longest path forces bounded support at arbitrary order

**Corollary 7 (universal bounded-support reduction).** Let (H) be a minimum counterexample. Then (H) has a proper Hamiltonian support (K) of order at most four such that
[
operatorname{pc}(H-K)=2
]
and (H-K) is non-Hamiltonian.

More precisely, in the lexicographic normal form of Lemma 4,
[
Amid Pmid Q,
qquad |P|ge |Q|,
]
either (|Q|=1), in which case (Q) itself is such a support, or (|Q|ge2), in which case there is a Hamiltonian four-support meeting an endpoint edge of the globally longest path (A).

**Proof.** If (|Q|=1), the singleton (Q) is a proper Hamiltonian support. Its complement is two-covered by (Amid P). It cannot be Hamiltonian, since a Hamilton path on (H-Q) together with the singleton path (Q) would two-cover (H). Hence
[
operatorname{pc}(H-Q)=2.
]

Assume now that
[
Q=(q_1,ldots,q_t),qquad tge2.
]
By Lemma 4, both distinct endpoints (q_1,q_t) reverse the same terminal edge of the globally longest path
[
A=(a_1,ldots,a_r):
]
[
(q_1,a_r,a_{r-1}),
qquad
(q_t,a_r,a_{r-1})
]
are tight.

Choose any vertex
[
y
otin{a_{r-1},a_r,q_1,q_t}.
]
Such a vertex exists because a minimum counterexample has more than ten vertices.

If
[
(y,q_1,a_r)
]
is tight, then
[
(y,q_1,a_r,a_{r-1})
]
is a Hamiltonian four-path. The same conclusion holds with (q_t) in place of (q_1).

Assume therefore that both
[
(y,q_1,a_r),qquad(y,q_t,a_r)
]
are non-tight. Boundary antisymmetry gives
[
(a_r,q_1,y),qquad(a_r,q_t,y)
]
tight. The parallel-middle lemma in [[localextend01]] then makes
[
{a_r,q_1,q_t,y}
]
Hamiltonian.

Thus in every case (H) has a Hamiltonian four-support (K). Since (K) is proper, minimum-counterexample calculus gives
[
operatorname{pc}(H-K)le2.
]
The complement cannot be Hamiltonian, because then (K) together with a Hamilton path on (H-K) would two-cover (H). Therefore
[
operatorname{pc}(H-K)=2.
]
(square)

This is an arbitrary-order reduction: bounded Hamiltonian support is forced directly from a globally longest path and an extremal two-cover of its complement. No bounded-order analysis or numerical case classification is used.

The remaining issue is therefore not whether the general problem reaches bounded support. It does. The relevant question is which additional anchor data on (K) is needed to convert its path-cover-two complement into the one-defect bridge or a two-cover.



### The universal four-support can be chosen mixed across all three components

**Corollary 8 (mixed-anchor refinement).** Work in the lexicographic normal form
[
Amid Pmid Q,
qquad
A=(a_1,ldots,a_r),quad
P=(p_1,ldots,p_m),quad
Q=(q_1,ldots,q_t),
]
with (tge2).

Then (H) has a Hamiltonian four-support (K) with non-Hamiltonian path-cover-two complement such that (K) meets all three displayed components and one of the following holds.

1. For some (qin{q_1,q_t}),
   [
   K={p_1,q,a_{r-1},a_r}.
   ]
   Thus (K) contains the full terminal edge of the globally longest path together with vertices from both complementary paths.

2. 
   [
   K={p_1,q_1,q_t,a_r},
   ]
   and (K) has a Hamilton order whose one endpoint is (a_r) and whose other endpoint lies in ({q_1,q_t}).

**Proof.** Repeat the proof of Corollary 7 with the auxiliary vertex chosen to be
[
y=p_1.
]
Lemma 4 gives
[
(q_1,a_r,a_{r-1}),
qquad
(q_t,a_r,a_{r-1})
]
tight.

If one of
[
(p_1,q_1,a_r),qquad(p_1,q_t,a_r)
]
is tight, say the former, then
[
(p_1,q_1,a_r,a_{r-1})
]
is a Hamilton four-path, giving outcome 1.

Assume both triples are non-tight. Boundary antisymmetry gives
[
(a_r,q_1,p_1),
qquad
(a_r,q_t,p_1)
]
tight. The parallel-middle lemma then gives one of the two Hamilton paths
[
(a_r,q_1,p_1,q_t),
qquad
(a_r,q_t,p_1,q_1).
]
This is outcome 2.

In either case (K) is proper. Minimum-counterexample calculus gives
[
operatorname{pc}(H-K)le2,
]
and the complement cannot be Hamiltonian without two-covering (H). Hence
[
operatorname{pc}(H-K)=2.
]
(square)

Thus the longest-path reduction does not merely force an unspecified small support. It forces a **mixed** four-support tied simultaneously to the longest path and to both paths of an extremal complementary two-cover.

This is the natural bounded interface for the global problem: endpoint deletion from (K) can now be compared against inherited path geometry on all three sides, rather than restarting from an unanchored four-set.



### Opposite extremal covers force a crossing or bidirectional reversal

The transfer dichotomy is more effective when one compares opposite extremal two-covers of the same complement rather than iterating an allowed transfer.

Let
\[
U=H-A,
\]
where \(A\) is globally longest. Choose:

- a **maximally imbalanced** two-cover
  \[
  U=P\mid Q,\qquad |P|\ge |Q|,
  \]
  maximizing \(|P|\); and
- a **maximally balanced** two-cover
  \[
  U=R\mid S,\qquad |R|\ge |S|,
  \]
  minimizing \(|R|-|S|\).

The first cover is the one used in Lemma 4.

**Lemma 7 (dual extremal normal form).** If
\[
|R|-|S|\ge2,
\]
then every displayed endpoint \(r\) of \(R\) is noninsertable at every position of the displayed Hamilton order of \(S\). In particular \(r\) reverses both end edges of \(S\).

**Proof.** Let \(r\) be an endpoint of \(R\). If \(S\cup\{r\}\) were Hamiltonian, deleting \(r\) from the displayed endpoint of \(R\) would leave a tight path \(R-r\), giving the two-cover
\[
(R-r)\mid(S\cup\{r\})
\]
of \(U\). Its component-size difference is
\[
(|R|-1)-(|S|+1)=|R|-|S|-2,
\]
strictly smaller than the chosen minimum. Hence \(S\cup\{r\}\) is non-Hamiltonian. By [[endpoint_replacement_truncation_dichotomy01]], \(r\) is noninsertable at every gap of the displayed order of \(S\); in particular both endpoint insertions fail, so boundary antisymmetry gives the two end-edge reversals. \(\square\)

Thus the complement of a longest path carries reversal certificates in opposite directions: endpoints of the small side of a maximally imbalanced cover reverse the large side, while endpoints of the large side of a maximally balanced cover reverse the small side.

**Lemma 8 (extremal-cover comparison).** With the two covers above, at least one of the following holds.

1. The support partitions coincide:
   \[
   \{V(P),V(Q)\}=\{V(R),V(S)\}.
   \]
   If their common size difference is at least two, then the endpoints on both sides reverse both end edges of the opposite side.
2. Some ordinary edge of one of \(R,S\) joins a vertex of \(P\) to a vertex of \(Q\).

**Proof.** Suppose no ordinary edge of either \(R\) or \(S\) joins \(V(P)\) to \(V(Q)\). Since each of \(R,S\) is connected as an ordinary path, each lies wholly inside one of \(V(P),V(Q)\). Because \(R,S\) partition \(U=V(P)\sqcup V(Q)\) and both old supports are nonempty, one of \(R,S\) equals \(V(P)\) and the other equals \(V(Q)\). Thus the support partitions coincide.

If they coincide and the common size difference is at least two, Lemma 4 applied to the maximally imbalanced realization gives reversal from the smaller side into the larger, while Lemma 7 applied to the maximally balanced realization gives reversal from the larger side into the smaller. \(\square\)

Consequently the general problem on \(H-A\) has only two global geometries:

\[
\boxed{\text{bidirectional end reversal on one fixed partition}}
\]
or
\[
\boxed{\text{a comparison path crossing the two supports}}.
\]

The second case is precisely the kind of cut-interaction disturbance controlled by [[coversurg01]]: a crossing comparison edge, together with an inherited neighbor on one old support, immediately yields a local reversal/cut interaction. The first case is still more rigid: both component endpoints attack the opposite component at both ends.

This is a genuinely global reduction. It uses no bounded-order hypothesis and no assumption that an allowed transfer must be monotone. The next step is to show that either global geometry merges \(P,Q\), or can be spliced through the globally longest path \(A\) to create a path longer than \(A\).


### Longestness forces the same transfer dichotomy across \(A\) and \(P\)

**Lemma 9.** In the lexicographic normal form
\[
A=(a_1,\ldots,a_r),\qquad P=(p_1,\ldots,p_m),\qquad r\ge m\ge2,
\]
exactly one of the following holds at the left end:

1. \((a_2,a_1,p_1,\ldots,p_m)\) is a tight path of order \(m+2\);
2. \((p_2,p_1,a_1)\) is tight.

Exactly one of the following holds at the right end:

1. \((p_1,\ldots,p_m,a_r,a_{r-1})\) is a tight path of order \(m+2\);
2. \((a_r,p_m,p_{m-1})\) is tight.

If both transfer alternatives hold, then
\[
(a_2,a_1,p_1,\ldots,p_m,a_r,a_{r-1})
\]
is a tight path of order \(m+4\).

**Proof.** Longestness of \(A\) gives
\[
(a_2,a_1,p_1),\qquad (p_m,a_r,a_{r-1})
\]
tight. Test \((a_1,p_1,p_2)\). If tight, it completes the left displayed path; otherwise boundary antisymmetry gives \((p_2,p_1,a_1)\). The right side is symmetric, testing \((p_{m-1},p_m,a_r)\). If both tested triples are tight, the two constructions concatenate through \(P\). \(\square\)

**Corollary 10.**
If \(r-m\le1\), both ends of \(A\) and \(P\) are mutually reversing. If \(r-m\le3\), at least one end is mutually reversing.

Indeed, a successful one-sided transfer gives a path of order \(m+2\), while two successful transfers give a path of order \(m+4\); either would exceed the longest-path order \(r\) under the stated inequalities.

Together with Corollary 6, if both
\[
r-m\le1,\qquad m-|Q|\le1,
\]
then each end carries a reversal ladder
\[
A\longleftrightarrow P\longleftrightarrow Q,
\]
and the endpoints of \(Q\) also reverse the corresponding end edges of \(A\).

Thus the arbitrary-order problem now couples component-size gaps to explicit reversal density rather than to any fixed total order.


### A single crossing is a genuine segment transfer from the large side

Continue with the maximally imbalanced cover
\[
U=P\mid Q,\qquad |P|=m\ge t=|Q|,
\]
and a maximally balanced cover
\[
U=R\mid S.
\]
Let \(c\) be the number of ordinary edges of \(R\mid S\) joining \(V(P)\) to \(V(Q)\).

**Lemma 11 (single-crossing augmentation).** If \(c=1\), then the balanced cover does not keep all of \(P\) in one component. Equivalently, it is \(P\), not \(Q\), that is split into two nonempty monochromatic blocks.

More precisely, cutting the unique crossing edge produces three nonempty monochromatic blocks. One is all of \(Q\), while the other two partition \(P\). One path of \(R\mid S\) consists of \(Q\) concatenated with one \(P\)-block, and the other path is the remaining \(P\)-block.

**Proof.** Cutting the unique crossing edge of the two-path forest \(R\mid S\) produces exactly three monochromatic blocks. Since both old classes \(P,Q\) are nonempty, one old class occurs in two blocks and the other in one.

Suppose \(Q\) were the split class. Then \(P\) would occur as one whole block. The unique crossing edge joins that whole \(P\)-block to one nonempty \(Q\)-block, so one component of \(R\mid S\) would have order strictly greater than
\[
|P|=m.
\]
But \(P\mid Q\) was chosen so that \(m\) is the maximum possible component order among all two-covers of \(U\). Contradiction.

Hence \(P\) is split and \(Q\) is one whole block. The unique crossing edge joins \(Q\) to one of the two \(P\)-blocks; the remaining \(P\)-block is the second component. \(\square\)

If, in addition, the two \(P\)-blocks occur as inherited intervals of the displayed order
\[
P=(p_1,\ldots,p_m),
\]
then Lemma 11 is literally a segment transfer:
\[
P=P^{\mathrm{left}}\,P^{\mathrm{right}}
\]
at one inherited cut, and the balanced cover is
\[
(P^{\mathrm{left}}\cup Q)\mid P^{\mathrm{right}}
\]
or its symmetric version, with the first union realized by one tight path.

If the \(P\)-blocks are not inherited intervals, then some inherited edge of \(P\) is split between comparison blocks or one comparison path leaves \(P\) and later returns. Thus:

**Corollary 12 (global augment-or-disturb dichotomy).** Comparing maximally imbalanced and maximally balanced two-covers of \(H-A\) yields one of:

1. the same support partition, with bidirectional endpoint reversal when the size gap is at least two;
2. a genuine transfer of an inherited end segment of the large path \(P\) onto the whole small path \(Q\);
3. a split inherited edge or leave-and-return disturbance in \(P\) or \(Q\).

When there are at least two crossing edges, outcome 3 follows from the block count. When there is exactly one, Lemma 11 gives outcome 2 unless the comparison blocks already disturb the inherited order.

This is the global augmenting-path formulation: the move from maximal imbalance toward maximal balance is either an honest segment transfer or it leaves a concrete path disturbance. No bounded total order is involved.


---

## Section — A five-set or an end-edge reversal

<!-- section_id: longest_paths_and_reversal_structure_a_five_set_or_an_end_edge_reversal -->

For \(y\in U\), the first and third triples of
\[
(a_1,a_0,y,a_{\lambda-1},a_{\lambda-2})
\]
are tight by Lemma 3. If
\[
(a_0,y,a_{\lambda-1})
\]
is tight, these five vertices form a Hamilton path.

Suppose instead that this middle triple is non-tight for every \(y\in U\). Then
\[
(a_{\lambda-1},y,a_0)
\]
is tight for every \(y\in U\). Define a tournament on \(U\) by
\[
p\to q
\quad\Longleftrightarrow\quad
(p,a_{\lambda-1},q)\text{ is tight}.
\]
Since \(|U|\ge4\), some \(y\) has an in-neighbor \(w\) and an out-neighbor \(z\). Then
\[
(y,a_{\lambda-1},z,a_0)
\]
is a tight four-path, while
\[
(w,a_{\lambda-1},y)
\]
reverses its first edge \((y,a_{\lambda-1})\). Indeed, the first triple comes from \(y\to z\), the second consecutive triple is the difficult-orientation relation \((a_{\lambda-1},z,a_0)\), and \(w\to y\) gives the displayed reversing triple.

Thus:

**Lemma 4.** Either some
\[
(a_1,a_0,y,a_{\lambda-1},a_{\lambda-2})
\]
is a Hamilton path, or a four-vertex tight path has an explicitly reversed end edge.

In the second case the four-set supporting the displayed tight path is Hamiltonian, and the reversing triple uses one additional exterior vertex. In a minimum counterexample its complement is therefore non-Hamiltonian and has path-cover number two.

---

## Section — A common four-vertex core

<!-- section_id: longest_paths_and_reversal_structure_a_common_four_vertex_core -->

Put
\[
D=\{a_1,a_0,a_{\lambda-1},a_{\lambda-2}\}.
\]
Call \(y\in U\) good when \(D\cup\{y\}\) is Hamiltonian in the displayed order. If three vertices of \(U\) are not good, the tournament argument above produces the end-edge reversal of Lemma 4. Therefore:

**Lemma 5.** Unless the end-edge-reversal four-path occurs, all but at most two vertices of \(U\) are good.

When \(|U|\ge6\), at least four such labels exist.

**Lemma 6.** If \(|U|\ge6\) and the end-edge-reversal four-path does not occur, then either
1. \(H\) contains a Hamiltonian six-set with two-coverable complement; or
2. there is a four-set \(C\) and three distinct vertices \(r_1,r_2,r_3\notin C\) such that each \(C\cup\{r_i\}\) is Hamiltonian and has two-coverable complement.

**Proof.** By Lemma 5, at least \(|U|-2\ge4\) vertices of \(U\) are good. Choose three distinct such vertices \(r_1,r_2,r_3\), and set \(C=D\). For each \(i\), the order
\[
(a_1,a_0,r_i,a_{\lambda-1},a_{\lambda-2})
\]
is a Hamilton path on \(C\cup\{r_i\}\).

Put \(S_i=C\cup\{r_i\}\). The set \(V(H)-S_i\) is nonempty, since it contains \(U-\{r_i\}\), and is a proper subset of \(V(H)\). Minimality gives \(\operatorname{pc}(H-S_i)\le2\). If \(H-S_i\) were Hamiltonian, its Hamilton path together with the displayed path on \(S_i\) would give a two-cover of \(H\), a contradiction. Hence \(\operatorname{pc}(H-S_i)=2\) for each \(i\). Alternative (2) follows with the original core \(C=D\). \(\square\)

Choose Hamilton orders on the three five-sets. If two induce different orders on \(C\), there is an order disagreement. Otherwise each root is inserted into one gap of a common order on \(C\). Separated gaps give a Hamiltonian six-set; adjacent gaps give either a Hamiltonian six-set or a reverse tight triple through the intervening core vertex; a common internal gap gives a Hamiltonian four-set. If all three roots use one endpoint gap, boundary reversal among the roots gives a Hamiltonian four-set. Thus the common-core case always carries additional ordered information.

---

## Section — The endpoint-pair family

<!-- section_id: longest_paths_and_reversal_structure_the_endpoint_pair_family -->

Assume a displayed end-edge reversal has been chosen maximal with respect to the order of its path and no preceding small Hamiltonian support occurs. Then every other exterior vertex satisfies the reverse relations at both ends. In the difficult orientation one also has
\[
(a_{\lambda-1},y,a_0)
\]
tight for every exterior \(y\).

For distinct \(y,z\), exactly one of
\[
(y,a_{\lambda-1},z),\qquad
(z,a_{\lambda-1},y)
\]
is tight. In the first case
\[
(y,a_{\lambda-1},z,a_0)
\]
is Hamiltonian; in the second, the reversed order is. Therefore every four-set
\[
\{a_0,a_{\lambda-1},y,z\}
\]
is Hamiltonian, and its complement is non-Hamiltonian with path-cover number two.

Among any three exterior vertices, orient \(p\to q\) when \((p,a_{\lambda-1},q)\) is tight. Some vertex has both an in-neighbor and an out-neighbor, yielding two Hamiltonian four-paths whose common pair is ordered oppositely. Thus this endpoint case gives a family of overlapping Hamiltonian four-sets with explicit order disagreement.

---

## Section — Opposite endpoint replacements

<!-- section_id: longest_paths_and_reversal_structure_opposite_endpoint_replacements -->

Let \(x,y\notin V(A)\). Suppose \(L\) is a Hamilton path on
\[
(V(A)-\{a_0\})\cup\{x\}
\]
and \(R\) is a Hamilton path on
\[
(V(A)-\{a_{\lambda-1}\})\cup\{y\},
\]
and both preserve the order inherited from \(A\). Assume \(\lambda\ge6\).

**Lemma 7.** The support
\[
(V(A)-\{a_0,a_{\lambda-1}\})\cup\{x,y\}
\]
is Hamiltonian.

**Proof.** Since \(A\cup\{x\}\) is not Hamiltonian, \(x\) can occupy only one of the first two positions relative to \(a_1,\ldots ,a_{\lambda-1}\); otherwise prepending \(a_0\) extends \(A\). Thus
\[
L=(x,a_1,\ldots ,a_{\lambda-1})
\]
or
\[
L=(a_1,x,a_2,\ldots ,a_{\lambda-1}).
\]
Similarly,
\[
R=(a_0,\ldots ,a_{\lambda-2},y)
\]
or
\[
R=(a_0,\ldots ,a_{\lambda-3},y,a_{\lambda-2}).
\]
Delete the old endpoints and combine the corresponding left and right forms. Every consecutive triple is inherited from \(L\), \(R\), or the middle of \(A\), so the resulting order is Hamiltonian. \(\square\)

Thus a difficult pair of opposite endpoint replacements must change the inherited order. Comparing deletion covers at \(a_0\) and \(a_{\lambda-1}\), one obtains either a reversed surviving edge of \(A\), different support partitions on the common double deletion, or an order disagreement on a common support.

---

## Section — Amplification from an arbitrary reversing triple

<!-- section_id: longest_paths_and_reversal_structure_amplification_from_an_arbitrary_reversing_triple -->

Let \(T\) be the vertex set of a reversing tight triple, and let \(J_T\) be the graph on \(V(H)-T\) in which \(yz\) is an edge exactly when \(T\cup\{y,z\}\) is Hamiltonian.

**Lemma 8.**
\[
\alpha(J_T)\le2.
\]

**Proof.** A reversing tight triple is itself a tight three-vertex path. Apply the bad-extension-pair theorem from [[localextend01]] to this path and the exterior set \(V(H)-T\). The nonedges of \(J_T\) are exactly the bad extension pairs, and those form a triangle-free graph. Hence \(\alpha(J_T)\le2\). \(\square\)

Thus the complement of \(J_T\) is triangle-free, so Mantel's theorem gives
\[
|E(J_T)|
\ge
\binom{m}{2}-\left\lfloor\frac{m^2}{4}\right\rfloor,
\qquad m=|V(H)-T|.
\]
Every edge gives a Hamiltonian five-set containing the same reversal and having two-coverable complement. Hence some exterior vertex lies in several such edges, producing Hamiltonian five-sets with a common four-vertex core. The insertion-position analysis following Lemma 6 then gives a Hamiltonian four- or six-set, an order disagreement, or another positioned reversal.

---

## Section — The remaining lemma

<!-- section_id: longest_paths_and_reversal_structure_the_remaining_lemma -->

The preceding lemmas produce one of the following:
- a Hamiltonian support of order four, five, or six with two-coverable complement and displayed endpoint information;
- three Hamiltonian five-sets with a common four-set;
- the endpoint-pair family of Section 5;
- an order disagreement attached to the two endpoint deletions of a longest path;
- a tight triple reversing an edge in one of these displayed configurations.

**Remaining Lemma.** In a minimum counterexample, any one of these configurations yields a reversal of an end edge of a displayed path occurring in a deletion-cover or three-cover state, or directly yields a two-cover, or yields a spanning ordering of defect span at most \(2\).

A proof completes the longest-path argument.

---

## Section — Appendix. Two invalid shortcuts

<!-- section_id: longest_paths_and_reversal_structure_appendix_two_invalid_shortcuts -->

For an ordered triple \((u,v,z)\), the boundary-reversed triple is
\[
(z,v,u),
\]
not \((v,u,z)\). A repeated-cut argument that substitutes the latter therefore uses an unsupported cyclic rotation.

Likewise, a deletion-cover path may contain a small exceptional set without those vertices forming a contiguous interval in the displayed longest-path order. A bound on the size of the exceptional set cannot by itself justify deleting one interval from the longest path.

These observations invalidate the corresponding shortcut arguments but do not affect Lemmas 1–8.
