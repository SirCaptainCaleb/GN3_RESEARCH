# The universal four-support is immediate

## Metadata

- ID: defect_lines_and_spanning_order_compression_the_remaining_lemma_subsection_b
- Parent Section: defect_lines_and_spanning_order_compression_the_remaining_lemma
- Position: 2
- Row version: 10
- Development version: 10
- Composition version: 1
- Composition stale: False

## Composition

### The first descent can preserve the universal reversal

The strict descent from Lemma 19 can be chosen so that the exposed endpoint reversal survives.

**Lemma 20 (reversal-preserving first descent).** Let
\[
A\mid (u,v)\mid C
\]
be one of the universal reversal states supplied by Corollary 18. Then there is a strict pairwise \(\Phi\)-decrease to a spanning three-cover
\[
A'\mid X\mid C'
\]
with
\[
|X|=3,
\]
such that an external tight triple through one of \(u,v\) still reverses an end edge of \(A'\) or \(C'\).

**Proof.** Write
\[
A=(a_1,\ldots,a_r),\qquad C=(c_1,\ldots,c_s).
\]
Since \(r+s\ge9\), one of \(r,s\) is at least five.

By Lemma 3 of [[longest_paths_and_reversal_structure_reversals_are_unavoidable]], the two-vertex-middle state has one of three endpoint patterns.

In the first pattern, one or both of \(u,v\) reverse the terminal edge
\[
a_{r-1}a_r
\]
of \(A\). If \(r\ge5\), move the opposite endpoint \(a_1\) from \(A\) into the two-set \(\{u,v\}\). The residual path
\[
A'=(a_2,\ldots,a_r)
\]
retains the reversed terminal edge, while \(\{u,v,a_1\}\) has a Hamilton tight order. Thus the reversal survives. If instead \(s\ge5\), transfer the endpoint \(c_s\) from \(C\); \(A\) is unchanged, so its reversal survives.

The second endpoint pattern is symmetric.

In the third pattern, after naming the middle vertices \(z,w\), the vertex \(w\) reverses both exposed end edges,
\[
a_{r-1}a_r
\qquad\text{and}\qquad
c_1c_2.
\]
Choose a side of order at least five and transfer the endpoint opposite its reversed edge: \(a_1\) from \(A\), or \(c_s\) from \(C\). The other reversal is untouched, and the reversal on the shortened side is also untouched.

In every case the transferred endpoint together with \(u,v\) forms a Hamiltonian three-set, so the pairwise repartition is legal. If the donor side has order \(m\ge5\), the two affected component orders change from
\[
(m,2)\quad\text{to}\quad(m-1,3),
\]
and hence
\[
\Delta\Phi=(m-1)^2+3^2-m^2-2^2
=6-2m<0.
\]
Thus the descent is strict and the external endpoint reversal persists. \(\square\)

Lemma 20 repairs the first step of the persistence route: the universal reversal is not merely present before descent; it can be carried into the order-three regime. From there [[three_cover_repartitions_and_recurrence_moving_away_from_a_three_vertex_side]] becomes the natural next interface. The remaining persistence question is therefore narrower:

> starting from a three-cover with a three-vertex component and a certified external endpoint reversal on another component, can every further strict descent be chosen to preserve a certified reversal or else produce direct one-cut compression?


### The order-three persistence obstruction is one-sided

The reversal-preserving route can be pushed one step further.

**Lemma 21 (one-sided obstruction after the first descent).** Let
\[
X\mid P\mid Q
\]
be a spanning three-cover of a minimum counterexample, where \(|X|=3\), and suppose an external tight triple through a vertex of \(X\) reverses the terminal edge
\[
p_{m-1}p_m
\]
of
\[
P=(p_1,\ldots,p_m).
\]
Then at least one of the following holds.

1. There is a strict pairwise \(\Phi\)-decrease after which a certified external endpoint reversal still survives.
2. The same pairwise-repartition component reaches a Hamiltonian support of order four or five carrying endpoint information, hence the bounded-support comparison regime.
3. All three component orders are at most four.
4. The following one-sided residue occurs:
   \[
   |Q|\le4,\qquad m\ge5,
   \]
   the four-set \(X\cup\{p_m\}\) is Hamiltonian, but \(X\cup\{p_1\}\) is non-Hamiltonian.

The symmetric statement holds for a reversal of the initial edge of \(P\).

**Proof.** First suppose \(|Q|\ge5\). Apply Lemma 3 of [[three_cover_repartitions_and_recurrence_moving_away_from_a_three_vertex_side]] to the pair \(X\mid Q\). If it yields strict descent, only \(X\) and \(Q\) are repartitioned, so the path \(P\) and its reversed terminal edge remain untouched; outcome 1 holds. Otherwise that lemma produces a Hamiltonian four- or five-support with endpoint information, giving outcome 2.

Hence assume \(|Q|\le4\). If also \(m\le4\), outcome 3 holds. Thus we may assume \(m\ge5\).

Apply the same three-vertex-side analysis to \(X\mid P\). If \(X\cup\{p_1\}\) is Hamiltonian, transfer the endpoint \(p_1\) into \(X\). The residual path
\[
(p_2,\ldots,p_m)
\]
retains the reversed terminal edge \(p_{m-1}p_m\), and the move changes the affected orders from \((3,m)\) to \((4,m-1)\), with
\[
\Delta\Phi=8-2m<0.
\]
Thus outcome 1 holds.

If neither \(X\cup\{p_1\}\) nor \(X\cup\{p_m\}\) is Hamiltonian, Lemma 3 produces a bounded Hamiltonian four- or five-support, giving outcome 2.

The only remaining possibility is therefore that \(X\cup\{p_m\}\) is Hamiltonian while \(X\cup\{p_1\}\) is not. This is outcome 4. \(\square\)

Thus, after the universal reversal has been carried into the order-three regime, reversal-preserving descent fails only at a sharply asymmetric local configuration: the opposite complementary path has order at most four, and the reversed side admits extension only at the very endpoint whose incident edge is being reversed. Any proof of persistence need now address only this one-sided residue (plus the bounded \(3|4|4\) profile).


### The one-sided obstruction also preserves a reversal

The asymmetric residue in Lemma 21 is not a genuine failure of the reversal invariant. Although the old reversed edge disappears under the only available endpoint transfer, the resulting four-component forces a new endpoint reversal.

**Lemma 22 (reversal regeneration after the one-sided transfer).** In outcome 4 of Lemma 21, write
[
Xmid Pmid Q,qquad
P=(p_1,ldots,p_m),
]
where (|X|=3), (mge5), (Xcup{p_m}) is Hamiltonian, and (Xcup{p_1}) is non-Hamiltonian. Then there is a strict pairwise (Phi)-decrease to a spanning three-cover that still contains a certified external endpoint reversal.

**Proof.** Choose a Hamilton path (Y) on
[
V(Y)=Xcup{p_m}.
]
The inherited prefix
[
R=(p_1,ldots,p_{m-1})
]
is a tight path. Hence
[
Xmid Pmid Q
longrightarrow
Ymid Rmid Q
]
is a legal pairwise repartition. The affected component orders change from
[
(3,m)quad	ext{to}quad(4,m-1),
]
so
[
DeltaPhi
=
4^2+(m-1)^2-3^2-m^2
=
8-2m<0
]
because (mge5).

Now apply the theorem *A displayed four-path is reversed or reverses both ends of its partner* from [[line_rooted_small_support_descent_from_deletion_cover_lifts]] to the displayed pair (Ymid R). Since (H) is a minimum counterexample, one of the following holds:

- a tight triple through a vertex of (R) reverses an end edge of the displayed four-path (Y); or
- both displayed end edges of (R) are reversed through endpoints of (Y).

In either case the descended three-cover (Ymid Rmid Q) contains a certified external endpoint reversal. Thus the strict descent preserves the reversal invariant, although generally with a different reversing triple from the one present before the move. (square)

Combining Lemmas 20–22, every strict descent encountered from the universal two-vertex-middle reversal state through the order-three regime can be chosen so that a certified external endpoint reversal survives, except possibly when the process reaches the bounded profile
[
3mid4mid4.
]

Thus the persistence frontier has collapsed to a single bounded size profile. The remaining question is no longer whether a reversal can survive arbitrary long-path descent; it is whether a (3|4|4) state carrying a certified external endpoint reversal already compresses directly, or can be moved neutrally to a state where strict reversal-preserving descent resumes.


### Neutral endpoint swaps preserve the reversal invariant in (3|4|4)

The remaining (3|4|4) profile is an absolute minimum of the quadratic potential, so its natural dynamics are neutral rather than descending. The reversal invariant nevertheless survives the basic neutral move.

**Lemma 23 (neutral reversal persistence in (3|4|4)).** Let
[
Tmid Amid B
]
be a spanning three-cover of a minimum counterexample with
[
|T|=3,qquad |A|=|B|=4,
]
and suppose a tight triple through a vertex (win T) reverses an end edge of one of the displayed four-paths, say
[
A=(a_1,a_2,a_3,a_4),
qquad
(w,a_4,a_3) 	ext{tight}.
]
Suppose a displayed (3|4) pair admits a neutral endpoint swap
[
3|4longrightarrow4|3.
]
Then the resulting (3|4|4) state also contains a certified external endpoint reversal.

**Proof.** There are two cases according to which four-side participates in the swap.

First suppose the neutral swap repartitions (Tmid B). The component (A) is unchanged. Every vertex of the old (T), including (w), belongs to the new four-component produced from (T) together with one endpoint of (B). Hence (w) remains external to (A), and the same tight triple
[
(w,a_4,a_3)
]
still reverses the terminal edge of (A).

Now suppose the swap repartitions (Tmid A). If the endpoint (a_1) is transferred into (T), the residual three-path
[
(a_2,a_3,a_4)
]
still contains the reversed terminal edge (a_3a_4), while (w) belongs to the new four-component. Thus the same reversing triple survives.

It remains that the endpoint (a_4) is transferred into (T). Let (Y) be a Hamiltonian four-path on
[
V(T)cup{a_4},
]
and let
[
A'=(a_1,a_2,a_3)
]
be the residual three-path. The old reversed edge (a_3a_4) is no longer contained in one displayed component. However the third component (B) is still a displayed Hamiltonian four-path. Apply the theorem *Two displayed four-paths force an end-edge reversal* from [[line_rooted_small_support_descent_from_deletion_cover_lifts]] to the pair (Ymid B). It supplies a tight triple through one of these components reversing an end edge of the other. Hence the new three-cover again carries a certified external endpoint reversal. (square)

Therefore every neutral endpoint-swap edge in the (3|4|4) state graph preserves the property
[
	ext{“some displayed component has an externally reversed end edge.”}
]
Combined with Lemmas 20–22, the reversal invariant now survives both all strict descents identified by the order-three analysis and all neutral (3|4leftrightarrow4|3) endpoint swaps at the terminal balanced profile.

The remaining (3|4|4) difficulty is consequently not loss of the reversal under reconfiguration. It is the genuinely terminal question: use a reversal that persists throughout the absolute-minimum neutral component to obtain a two-cover or a one-cut defect ordering.


### Every prescribed root has a canonical order-eleven reversal state

The terminal (3|4|4) profile has a stronger normal form than neutral persistence alone suggests. At order eleven, the three-component may be required to contain any prescribed vertex, while the two four-components simultaneously admit Hamiltonian extensions through that vertex.

**Lemma 24 (prescribed-root terminal normal form).** Let (H) be a minimum counterexample of order eleven, and prescribe any vertex (xin V(H)). Then there exist distinct vertices (p,q
e x) and disjoint Hamiltonian four-sets (C,D) such that
[
V(H)=Cmathbin{dotcup}Dmathbin{dotcup}{p,q,x},
]
with all of
[
C,qquad D,qquad Ccup{x},qquad Dcup{x}
]
Hamiltonian. Consequently
[
Cmid Dmid{p,q,x}
]
is a spanning (4|4|3) three-cover containing a certified external endpoint reversal.

**Proof.** By the order-eleven consequence in [[extremal01]], the deletion (H-x) has an equitable Hamiltonian two-cover
[
H-x=Pmid Q,
qquad |P|=|Q|=5.
]
Both six-sets
[
V(P)cup{x},
qquad
V(Q)cup{x}
]
are non-Hamiltonian, since Hamiltonicity of either would give a spanning (6|5) two-cover of (H).

Apply the prescribed Hamiltonian (K_4)-overlap theorem from [[extremal01]] to the non-Hamiltonian six-set (V(P)cup{x}), prescribing the good deletion (x). It yields (pin V(P)) such that both
[
C=V(P)-{p}
]
and
[
Ccup{x}
]
are Hamiltonian. Applying the same theorem to (V(Q)cup{x}) gives (qin V(Q)) such that
[
D=V(Q)-{q}
]
and
[
Dcup{x}
]
are Hamiltonian.

The remaining three vertices are exactly ({p,q,x}), and every three-vertex boundary tournament has a Hamiltonian tight path. Hence
[
Cmid Dmid{p,q,x}
]
is a spanning (4|4|3) cover.

Finally choose displayed Hamiltonian four-paths on (C) and (D). The theorem *Two displayed four-paths force an end-edge reversal* from [[line_rooted_small_support_descent_from_deletion_cover_lifts]] applies to the pair (Cmid D): a tight triple through one four-component reverses an end edge of the other. Thus the canonical state carries a certified external endpoint reversal. (square)

This normal form is stronger than merely knowing that some (3|4|4) minimum state carries a reversal. The root (x) is arbitrary, and it simultaneously Hamiltonian-extends **both** four-components:
[
C+x,qquad D+x.
]
Therefore the terminal order-eleven problem may be studied under this synchronized extension hypothesis without loss of generality.

In particular, the persistence route and the equitable-deletion route meet at the same terminal object. The remaining obstruction can be stated purely at order eleven:

> rule out a minimum counterexample admitting, for every prescribed root (x), a (4|4|3) cover (C|D|{p,q,x}) such that (C+x) and (D+x) are Hamiltonian and the two four-components carry an external endpoint reversal.

The extra simultaneous extensions through (x) are the new structure available for attacking the final one-cut compression step.


### The quiet order-eleven residue is a double same-slot square

The prescribed-root normal form has three naturally linked deletion covers. Their compatibility already forces a much more rigid terminal configuration.

**Lemma 25 (double same-slot reduction).** In the setting of Lemma 24, write
[
P=Ccup{p},qquad Q=Dcup{q},
]
and choose Hamilton orders witnessing
[
F_x=Pmid Q,qquad
F_p=(Ccup{x})mid Q,qquad
F_q=Pmid(Dcup{x}).
]
Then, on each of the two four-cores (C,D), one of the following occurs:

1. the corresponding pair of deletion covers has an order disagreement on the common four-core;
2. the omitted labels occupy adjacent insertion slots, in which case the insertion-slot lemma produces a tight reversing triple through the unique common vertex between the two slots;
3. the omitted labels occupy exactly the same insertion slot.

Consequently, if neither spoke produces order disagreement nor an adjacent-slot reversing triple, there are Hamilton orders
[
C=(c_1,c_2,c_3,c_4),qquad
D=(d_1,d_2,d_3,d_4)
]
such that (p) and (x) occupy the same insertion slot in (C), while (q) and (x) occupy the same insertion slot in (D).

**Proof.** Restrict (F_x) and (F_p) to the common vertex set (H-{x,p}). Both induce the support partition
[
Cmid Q.
]
If their common-support orders disagree, outcome 1 holds. Otherwise the covers are compatible. Lemma 3 of [[deletion_covers_and_the_support_graph_compatibility_of_deletion_covers]] applies: the omitted labels (x,p) are inserted into the same common support, namely (C), and their insertion slots are equal or adjacent. If adjacent, that lemma gives a tight triple reversing the two inserted labels across the intervening core vertex, which is outcome 2. Otherwise the slots are equal, giving outcome 3.

The same argument applied to (F_x,F_q), after restricting to (H-{x,q}), uses the common support partition
[
Pmid D
]
and yields the identical trichotomy for (x,q) on (D). (square)

Thus the terminal order-eleven obstruction has a precise quiet form. After excluding the already-developed order-disagreement and reversing-triple branches, the prescribed root (x) is synchronized with both displaced labels:
[
p 	ext{and} x 	ext{share one slot of }C,
qquad
q 	ext{and} x 	ext{share one slot of }D.
]

This is stronger than the mere simultaneous Hamiltonicity
[
C+p, C+x, D+q, D+x.
]
The four five-sets are now aligned by common core orders and insertion positions. The remaining order-eleven problem can therefore be attacked as a finite slot-synchronization problem: show that a double same-slot square either creates a cross-extension, a two-cover, or a one-cut defect ordering.


### Near-end same slots force a two-cover

The double same-slot residue has only three viable slot positions on each four-core.

**Lemma 26 (near-end slots are impossible).** In the quiet case of Lemma 25, let
[
C=(c_1,c_2,c_3,c_4)
]
be the common core order for (p,x). Then their common insertion slot cannot be between (c_1,c_2) or between (c_3,c_4). Hence the only possible common slots on (C) are:

- before (c_1);
- between (c_2,c_3);
- after (c_4).

The same conclusion holds for the common insertion slot of (q,x) in
[
D=(d_1,d_2,d_3,d_4).
]

**Proof.** Suppose first that (p,x) are both inserted between (c_1,c_2). Then
[
(c_1,p,c_2,c_3,c_4)
qquad	ext{and}qquad
(c_1,x,c_2,c_3,c_4)
]
are tight Hamilton paths.

Boundary antisymmetry on the triple ({p,c_1,x}) says exactly one of
[
(x,c_1,p),qquad (p,c_1,x)
]
is tight. In the first case
[
(x,c_1,p,c_2,c_3,c_4)
]
is a Hamilton tight path on (Ccup{p,x}); in the second case
[
(p,c_1,x,c_2,c_3,c_4)
]
is such a path. Thus (Ccup{p,x}) is Hamiltonian.

But its complementary five-set is
[
Dcup{q}=Q,
]
which is Hamiltonian by construction. These two disjoint Hamilton paths give a spanning two-cover of (H), contradiction.

Now suppose (p,x) are both inserted between (c_3,c_4). Then
[
(c_1,c_2,c_3,p,c_4)
qquad	ext{and}qquad
(c_1,c_2,c_3,x,c_4)
]
are tight. Exactly one of
[
(p,c_4,x),qquad (x,c_4,p)
]
is tight. Accordingly one of
[
(c_1,c_2,c_3,p,c_4,x),
qquad
(c_1,c_2,c_3,x,c_4,p)
]
is a Hamilton tight path on (Ccup{p,x}). Again (Q=Dcup{q}) supplies the complementary Hamilton five-path, giving a two-cover of (H), contradiction.

Thus neither near-end internal slot is possible. The argument for (D) is identical, with complementary Hamilton five-set (P=Ccup{p}). (square)

Hence the exact-slot synchronization problem has only three local states per core:
[
	ext{left endpoint},qquad
	ext{central gap},qquad
	ext{right endpoint}.
]
The quiet order-eleven residue is therefore reduced from twenty-five slot pairs to nine.


## Development

### The first descent can preserve the universal reversal

The strict descent from Lemma 19 can be chosen so that the exposed endpoint reversal survives.

**Lemma 20 (reversal-preserving first descent).** Let
\[
A\mid (u,v)\mid C
\]
be one of the universal reversal states supplied by Corollary 18. Then there is a strict pairwise \(\Phi\)-decrease to a spanning three-cover
\[
A'\mid X\mid C'
\]
with
\[
|X|=3,
\]
such that an external tight triple through one of \(u,v\) still reverses an end edge of \(A'\) or \(C'\).

**Proof.** Write
\[
A=(a_1,\ldots,a_r),\qquad C=(c_1,\ldots,c_s).
\]
Since \(r+s\ge9\), one of \(r,s\) is at least five.

By Lemma 3 of [[longest_paths_and_reversal_structure_reversals_are_unavoidable]], the two-vertex-middle state has one of three endpoint patterns.

In the first pattern, one or both of \(u,v\) reverse the terminal edge
\[
a_{r-1}a_r
\]
of \(A\). If \(r\ge5\), move the opposite endpoint \(a_1\) from \(A\) into the two-set \(\{u,v\}\). The residual path
\[
A'=(a_2,\ldots,a_r)
\]
retains the reversed terminal edge, while \(\{u,v,a_1\}\) has a Hamilton tight order. Thus the reversal survives. If instead \(s\ge5\), transfer the endpoint \(c_s\) from \(C\); \(A\) is unchanged, so its reversal survives.

The second endpoint pattern is symmetric.

In the third pattern, after naming the middle vertices \(z,w\), the vertex \(w\) reverses both exposed end edges,
\[
a_{r-1}a_r
\qquad\text{and}\qquad
c_1c_2.
\]
Choose a side of order at least five and transfer the endpoint opposite its reversed edge: \(a_1\) from \(A\), or \(c_s\) from \(C\). The other reversal is untouched, and the reversal on the shortened side is also untouched.

In every case the transferred endpoint together with \(u,v\) forms a Hamiltonian three-set, so the pairwise repartition is legal. If the donor side has order \(m\ge5\), the two affected component orders change from
\[
(m,2)\quad\text{to}\quad(m-1,3),
\]
and hence
\[
\Delta\Phi=(m-1)^2+3^2-m^2-2^2
=6-2m<0.
\]
Thus the descent is strict and the external endpoint reversal persists. \(\square\)

Lemma 20 repairs the first step of the persistence route: the universal reversal is not merely present before descent; it can be carried into the order-three regime. From there [[three_cover_repartitions_and_recurrence_moving_away_from_a_three_vertex_side]] becomes the natural next interface. The remaining persistence question is therefore narrower:

> starting from a three-cover with a three-vertex component and a certified external endpoint reversal on another component, can every further strict descent be chosen to preserve a certified reversal or else produce direct one-cut compression?


### The order-three persistence obstruction is one-sided

The reversal-preserving route can be pushed one step further.

**Lemma 21 (one-sided obstruction after the first descent).** Let
\[
X\mid P\mid Q
\]
be a spanning three-cover of a minimum counterexample, where \(|X|=3\), and suppose an external tight triple through a vertex of \(X\) reverses the terminal edge
\[
p_{m-1}p_m
\]
of
\[
P=(p_1,\ldots,p_m).
\]
Then at least one of the following holds.

1. There is a strict pairwise \(\Phi\)-decrease after which a certified external endpoint reversal still survives.
2. The same pairwise-repartition component reaches a Hamiltonian support of order four or five carrying endpoint information, hence the bounded-support comparison regime.
3. All three component orders are at most four.
4. The following one-sided residue occurs:
   \[
   |Q|\le4,\qquad m\ge5,
   \]
   the four-set \(X\cup\{p_m\}\) is Hamiltonian, but \(X\cup\{p_1\}\) is non-Hamiltonian.

The symmetric statement holds for a reversal of the initial edge of \(P\).

**Proof.** First suppose \(|Q|\ge5\). Apply Lemma 3 of [[three_cover_repartitions_and_recurrence_moving_away_from_a_three_vertex_side]] to the pair \(X\mid Q\). If it yields strict descent, only \(X\) and \(Q\) are repartitioned, so the path \(P\) and its reversed terminal edge remain untouched; outcome 1 holds. Otherwise that lemma produces a Hamiltonian four- or five-support with endpoint information, giving outcome 2.

Hence assume \(|Q|\le4\). If also \(m\le4\), outcome 3 holds. Thus we may assume \(m\ge5\).

Apply the same three-vertex-side analysis to \(X\mid P\). If \(X\cup\{p_1\}\) is Hamiltonian, transfer the endpoint \(p_1\) into \(X\). The residual path
\[
(p_2,\ldots,p_m)
\]
retains the reversed terminal edge \(p_{m-1}p_m\), and the move changes the affected orders from \((3,m)\) to \((4,m-1)\), with
\[
\Delta\Phi=8-2m<0.
\]
Thus outcome 1 holds.

If neither \(X\cup\{p_1\}\) nor \(X\cup\{p_m\}\) is Hamiltonian, Lemma 3 produces a bounded Hamiltonian four- or five-support, giving outcome 2.

The only remaining possibility is therefore that \(X\cup\{p_m\}\) is Hamiltonian while \(X\cup\{p_1\}\) is not. This is outcome 4. \(\square\)

Thus, after the universal reversal has been carried into the order-three regime, reversal-preserving descent fails only at a sharply asymmetric local configuration: the opposite complementary path has order at most four, and the reversed side admits extension only at the very endpoint whose incident edge is being reversed. Any proof of persistence need now address only this one-sided residue (plus the bounded \(3|4|4\) profile).


### The one-sided obstruction also preserves a reversal

The asymmetric residue in Lemma 21 is not a genuine failure of the reversal invariant. Although the old reversed edge disappears under the only available endpoint transfer, the resulting four-component forces a new endpoint reversal.

**Lemma 22 (reversal regeneration after the one-sided transfer).** In outcome 4 of Lemma 21, write
[
Xmid Pmid Q,qquad
P=(p_1,ldots,p_m),
]
where (|X|=3), (mge5), (Xcup{p_m}) is Hamiltonian, and (Xcup{p_1}) is non-Hamiltonian. Then there is a strict pairwise (Phi)-decrease to a spanning three-cover that still contains a certified external endpoint reversal.

**Proof.** Choose a Hamilton path (Y) on
[
V(Y)=Xcup{p_m}.
]
The inherited prefix
[
R=(p_1,ldots,p_{m-1})
]
is a tight path. Hence
[
Xmid Pmid Q
longrightarrow
Ymid Rmid Q
]
is a legal pairwise repartition. The affected component orders change from
[
(3,m)quad	ext{to}quad(4,m-1),
]
so
[
DeltaPhi
=
4^2+(m-1)^2-3^2-m^2
=
8-2m<0
]
because (mge5).

Now apply the theorem *A displayed four-path is reversed or reverses both ends of its partner* from [[line_rooted_small_support_descent_from_deletion_cover_lifts]] to the displayed pair (Ymid R). Since (H) is a minimum counterexample, one of the following holds:

- a tight triple through a vertex of (R) reverses an end edge of the displayed four-path (Y); or
- both displayed end edges of (R) are reversed through endpoints of (Y).

In either case the descended three-cover (Ymid Rmid Q) contains a certified external endpoint reversal. Thus the strict descent preserves the reversal invariant, although generally with a different reversing triple from the one present before the move. (square)

Combining Lemmas 20–22, every strict descent encountered from the universal two-vertex-middle reversal state through the order-three regime can be chosen so that a certified external endpoint reversal survives, except possibly when the process reaches the bounded profile
[
3mid4mid4.
]

Thus the persistence frontier has collapsed to a single bounded size profile. The remaining question is no longer whether a reversal can survive arbitrary long-path descent; it is whether a (3|4|4) state carrying a certified external endpoint reversal already compresses directly, or can be moved neutrally to a state where strict reversal-preserving descent resumes.


### Neutral endpoint swaps preserve the reversal invariant in (3|4|4)

The remaining (3|4|4) profile is an absolute minimum of the quadratic potential, so its natural dynamics are neutral rather than descending. The reversal invariant nevertheless survives the basic neutral move.

**Lemma 23 (neutral reversal persistence in (3|4|4)).** Let
[
Tmid Amid B
]
be a spanning three-cover of a minimum counterexample with
[
|T|=3,qquad |A|=|B|=4,
]
and suppose a tight triple through a vertex (win T) reverses an end edge of one of the displayed four-paths, say
[
A=(a_1,a_2,a_3,a_4),
qquad
(w,a_4,a_3) 	ext{tight}.
]
Suppose a displayed (3|4) pair admits a neutral endpoint swap
[
3|4longrightarrow4|3.
]
Then the resulting (3|4|4) state also contains a certified external endpoint reversal.

**Proof.** There are two cases according to which four-side participates in the swap.

First suppose the neutral swap repartitions (Tmid B). The component (A) is unchanged. Every vertex of the old (T), including (w), belongs to the new four-component produced from (T) together with one endpoint of (B). Hence (w) remains external to (A), and the same tight triple
[
(w,a_4,a_3)
]
still reverses the terminal edge of (A).

Now suppose the swap repartitions (Tmid A). If the endpoint (a_1) is transferred into (T), the residual three-path
[
(a_2,a_3,a_4)
]
still contains the reversed terminal edge (a_3a_4), while (w) belongs to the new four-component. Thus the same reversing triple survives.

It remains that the endpoint (a_4) is transferred into (T). Let (Y) be a Hamiltonian four-path on
[
V(T)cup{a_4},
]
and let
[
A'=(a_1,a_2,a_3)
]
be the residual three-path. The old reversed edge (a_3a_4) is no longer contained in one displayed component. However the third component (B) is still a displayed Hamiltonian four-path. Apply the theorem *Two displayed four-paths force an end-edge reversal* from [[line_rooted_small_support_descent_from_deletion_cover_lifts]] to the pair (Ymid B). It supplies a tight triple through one of these components reversing an end edge of the other. Hence the new three-cover again carries a certified external endpoint reversal. (square)

Therefore every neutral endpoint-swap edge in the (3|4|4) state graph preserves the property
[
	ext{“some displayed component has an externally reversed end edge.”}
]
Combined with Lemmas 20–22, the reversal invariant now survives both all strict descents identified by the order-three analysis and all neutral (3|4leftrightarrow4|3) endpoint swaps at the terminal balanced profile.

The remaining (3|4|4) difficulty is consequently not loss of the reversal under reconfiguration. It is the genuinely terminal question: use a reversal that persists throughout the absolute-minimum neutral component to obtain a two-cover or a one-cut defect ordering.


### Every prescribed root has a canonical order-eleven reversal state

The terminal (3|4|4) profile has a stronger normal form than neutral persistence alone suggests. At order eleven, the three-component may be required to contain any prescribed vertex, while the two four-components simultaneously admit Hamiltonian extensions through that vertex.

**Lemma 24 (prescribed-root terminal normal form).** Let (H) be a minimum counterexample of order eleven, and prescribe any vertex (xin V(H)). Then there exist distinct vertices (p,q
e x) and disjoint Hamiltonian four-sets (C,D) such that
[
V(H)=Cmathbin{dotcup}Dmathbin{dotcup}{p,q,x},
]
with all of
[
C,qquad D,qquad Ccup{x},qquad Dcup{x}
]
Hamiltonian. Consequently
[
Cmid Dmid{p,q,x}
]
is a spanning (4|4|3) three-cover containing a certified external endpoint reversal.

**Proof.** By the order-eleven consequence in [[extremal01]], the deletion (H-x) has an equitable Hamiltonian two-cover
[
H-x=Pmid Q,
qquad |P|=|Q|=5.
]
Both six-sets
[
V(P)cup{x},
qquad
V(Q)cup{x}
]
are non-Hamiltonian, since Hamiltonicity of either would give a spanning (6|5) two-cover of (H).

Apply the prescribed Hamiltonian (K_4)-overlap theorem from [[extremal01]] to the non-Hamiltonian six-set (V(P)cup{x}), prescribing the good deletion (x). It yields (pin V(P)) such that both
[
C=V(P)-{p}
]
and
[
Ccup{x}
]
are Hamiltonian. Applying the same theorem to (V(Q)cup{x}) gives (qin V(Q)) such that
[
D=V(Q)-{q}
]
and
[
Dcup{x}
]
are Hamiltonian.

The remaining three vertices are exactly ({p,q,x}), and every three-vertex boundary tournament has a Hamiltonian tight path. Hence
[
Cmid Dmid{p,q,x}
]
is a spanning (4|4|3) cover.

Finally choose displayed Hamiltonian four-paths on (C) and (D). The theorem *Two displayed four-paths force an end-edge reversal* from [[line_rooted_small_support_descent_from_deletion_cover_lifts]] applies to the pair (Cmid D): a tight triple through one four-component reverses an end edge of the other. Thus the canonical state carries a certified external endpoint reversal. (square)

This normal form is stronger than merely knowing that some (3|4|4) minimum state carries a reversal. The root (x) is arbitrary, and it simultaneously Hamiltonian-extends **both** four-components:
[
C+x,qquad D+x.
]
Therefore the terminal order-eleven problem may be studied under this synchronized extension hypothesis without loss of generality.

In particular, the persistence route and the equitable-deletion route meet at the same terminal object. The remaining obstruction can be stated purely at order eleven:

> rule out a minimum counterexample admitting, for every prescribed root (x), a (4|4|3) cover (C|D|{p,q,x}) such that (C+x) and (D+x) are Hamiltonian and the two four-components carry an external endpoint reversal.

The extra simultaneous extensions through (x) are the new structure available for attacking the final one-cut compression step.


### The quiet order-eleven residue is a double same-slot square

The prescribed-root normal form has three naturally linked deletion covers. Their compatibility already forces a much more rigid terminal configuration.

**Lemma 25 (double same-slot reduction).** In the setting of Lemma 24, write
[
P=Ccup{p},qquad Q=Dcup{q},
]
and choose Hamilton orders witnessing
[
F_x=Pmid Q,qquad
F_p=(Ccup{x})mid Q,qquad
F_q=Pmid(Dcup{x}).
]
Then, on each of the two four-cores (C,D), one of the following occurs:

1. the corresponding pair of deletion covers has an order disagreement on the common four-core;
2. the omitted labels occupy adjacent insertion slots, in which case the insertion-slot lemma produces a tight reversing triple through the unique common vertex between the two slots;
3. the omitted labels occupy exactly the same insertion slot.

Consequently, if neither spoke produces order disagreement nor an adjacent-slot reversing triple, there are Hamilton orders
[
C=(c_1,c_2,c_3,c_4),qquad
D=(d_1,d_2,d_3,d_4)
]
such that (p) and (x) occupy the same insertion slot in (C), while (q) and (x) occupy the same insertion slot in (D).

**Proof.** Restrict (F_x) and (F_p) to the common vertex set (H-{x,p}). Both induce the support partition
[
Cmid Q.
]
If their common-support orders disagree, outcome 1 holds. Otherwise the covers are compatible. Lemma 3 of [[deletion_covers_and_the_support_graph_compatibility_of_deletion_covers]] applies: the omitted labels (x,p) are inserted into the same common support, namely (C), and their insertion slots are equal or adjacent. If adjacent, that lemma gives a tight triple reversing the two inserted labels across the intervening core vertex, which is outcome 2. Otherwise the slots are equal, giving outcome 3.

The same argument applied to (F_x,F_q), after restricting to (H-{x,q}), uses the common support partition
[
Pmid D
]
and yields the identical trichotomy for (x,q) on (D). (square)

Thus the terminal order-eleven obstruction has a precise quiet form. After excluding the already-developed order-disagreement and reversing-triple branches, the prescribed root (x) is synchronized with both displaced labels:
[
p 	ext{and} x 	ext{share one slot of }C,
qquad
q 	ext{and} x 	ext{share one slot of }D.
]

This is stronger than the mere simultaneous Hamiltonicity
[
C+p, C+x, D+q, D+x.
]
The four five-sets are now aligned by common core orders and insertion positions. The remaining order-eleven problem can therefore be attacked as a finite slot-synchronization problem: show that a double same-slot square either creates a cross-extension, a two-cover, or a one-cut defect ordering.


### Near-end same slots force a two-cover

The double same-slot residue has only three viable slot positions on each four-core.

**Lemma 26 (near-end slots are impossible).** In the quiet case of Lemma 25, let
[
C=(c_1,c_2,c_3,c_4)
]
be the common core order for (p,x). Then their common insertion slot cannot be between (c_1,c_2) or between (c_3,c_4). Hence the only possible common slots on (C) are:

- before (c_1);
- between (c_2,c_3);
- after (c_4).

The same conclusion holds for the common insertion slot of (q,x) in
[
D=(d_1,d_2,d_3,d_4).
]

**Proof.** Suppose first that (p,x) are both inserted between (c_1,c_2). Then
[
(c_1,p,c_2,c_3,c_4)
qquad	ext{and}qquad
(c_1,x,c_2,c_3,c_4)
]
are tight Hamilton paths.

Boundary antisymmetry on the triple ({p,c_1,x}) says exactly one of
[
(x,c_1,p),qquad (p,c_1,x)
]
is tight. In the first case
[
(x,c_1,p,c_2,c_3,c_4)
]
is a Hamilton tight path on (Ccup{p,x}); in the second case
[
(p,c_1,x,c_2,c_3,c_4)
]
is such a path. Thus (Ccup{p,x}) is Hamiltonian.

But its complementary five-set is
[
Dcup{q}=Q,
]
which is Hamiltonian by construction. These two disjoint Hamilton paths give a spanning two-cover of (H), contradiction.

Now suppose (p,x) are both inserted between (c_3,c_4). Then
[
(c_1,c_2,c_3,p,c_4)
qquad	ext{and}qquad
(c_1,c_2,c_3,x,c_4)
]
are tight. Exactly one of
[
(p,c_4,x),qquad (x,c_4,p)
]
is tight. Accordingly one of
[
(c_1,c_2,c_3,p,c_4,x),
qquad
(c_1,c_2,c_3,x,c_4,p)
]
is a Hamilton tight path on (Ccup{p,x}). Again (Q=Dcup{q}) supplies the complementary Hamilton five-path, giving a two-cover of (H), contradiction.

Thus neither near-end internal slot is possible. The argument for (D) is identical, with complementary Hamilton five-set (P=Ccup{p}). (square)

Hence the exact-slot synchronization problem has only three local states per core:
[
	ext{left endpoint},qquad
	ext{central gap},qquad
	ext{right endpoint}.
]
The quiet order-eleven residue is therefore reduced from twenty-five slot pairs to nine.
