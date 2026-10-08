# 

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


## Development

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
