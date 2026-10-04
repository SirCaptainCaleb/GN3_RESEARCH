# From topological recurrence to local GN3 structure

**Summary:** Recurrent carrier faces compress to bounded GN3 structure; in a minimum counterexample exact deficiency one sharpens the terminal handoff to a canonical Hamiltonian four-support with non-Hamiltonian path-cover-two complement.

## Statement

Positive carrier-face balance makes every nonzero chamber root recurrent. In the no-two-cover branch, minimum switch span removes every unbounded permutahedral residue, yielding a small-middle three-cover or a Hamiltonian four- or five-support. In a minimum counterexample, the exact inversion deficiency is one: its unique omitted vertex reverses the terminal edges of both deletion paths and therefore forces a canonical Hamiltonian four-support whose complement is non-Hamiltonian with path-cover number two.

## Body

## From balanced recurrence to local reversal structure

### Determining positions and positive face balance

Let \(F=B_1|\cdots|B_k\) be a proper permutahedral face, with its blocks occupying consecutive positions. Assume its chamber roots admit a circulation strictly positive on every occurring root, as provided by [[convex_root_balance_and_bourgin_yang]]. Then every coordinate occurring as a first switch also occurs as a reflected last switch in the same face. Every chamber belongs to a directed root cycle, unless it has a zero root and is already an exact diagonal.

This is stronger than choosing just one cycle. The following deductions explain what can be extracted without assuming that convex balance is already a two-cover.

### Block separation with explicit determining windows

A first switch at \(x\) is determined by the first \(x+1\) statuses and hence by vertex positions
\[
1,\ldots,x+3.
\]
A reflected last switch at \(x\) is determined by the last \(x+1\) statuses and hence by positions
\[
n-x-2,\ldots,n.
\]

**Lemma 7.1.** Suppose \(F\) has a chamber with first switch \(x\), a chamber with reflected last switch \(x\), and a block boundary after position \(j\) such that
\[
x+3\leq j\leq n-x-3.
\]
Then \(F\) contains a chamber with root zero.

**Proof.** Use the block orders from the first witness in every block up to the boundary, and those from the second witness after it. Both determining windows remain unchanged. The resulting chamber has \(a=\bar b=x\). \(\square\)

Consequently, if \(F\) contains no diagonal and the displayed interval of possible boundaries is nonempty, all positions
\[
x+3,\ldots,n-x-2
\]
lie in a single block. Its size is at least \(n-2x-4\).

**Corollary 7.2.** Under strictly positive face balance and absence of a diagonal, let \(r\) be the least switch coordinate occurring in any chamber root of \(F\). If \(n\geq2r+6\), one block contains positions \(r+3,\ldots,n-r-2\). It also contains every nonempty corridor of this form for any larger occurring coordinate.

**Proof.** Positive balance supplies both kinds of witness for \(r\), so Lemma 7.1 excludes all boundaries in its corridor. Corridors for larger coordinates are nested inside it. \(\square\)

This gives a single block for all occurring root coordinates, not only those of a selected cycle. If \(n<2r+6\), this separation lemma gives no block conclusion. Near-central coordinates must be treated by a separate argument; their numerical location alone does not prove a bounded-support descent.

### Cross-intersecting determining families

Fix the orders of all blocks other than a chosen block \(B\), and fix a coordinate \(x\) whose two determining windows are disjoint. Let \(\mathcal L_x\) consist of the sets of labels of \(B\) occupying its positions in the left window in some chamber with first switch \(x\). Define \(\mathcal R_x\) analogously for reflected last switch \(x\). Witness orders of these sets inside the corresponding positions are retained when combining them.

**Lemma 7.3.** If no chamber with these fixed outside orders has root zero, then every \(L\in\mathcal L_x\) intersects every \(R\in\mathcal R_x\).

**Proof.** If the sets were disjoint, place each in its own determining positions using its witness order, and fill the remaining positions of \(B\) arbitrarily. The disjoint windows and the fixed outside orders preserve both witnesses. This produces a diagonal. \(\square\)

The qualification about outside orders is essential: face balance supplies witnesses somewhere in \(F\), not automatically witnesses with every prescribed choice of outside block orders.

If both families are nonempty, any member of \(\mathcal L_x\) is a transversal of \(\mathcal R_x\). An inclusion-minimal transversal \(T\) contained in it has, for each \(v\in T\), a member of \(\mathcal R_x\) meeting \(T\) exactly at \(v\); otherwise \(v\) could be removed. This preserves the private-witness mechanism without asserting an absolute bound on \(|T|\). Such a bound would require a bound on the number of determining positions inside \(B\).

### Front motion with the witness hypotheses retained

**Lemma 7.4.** Fix all outside block orders. Suppose a permutation of \(B\) realizes first switch \(x\), another realizes reflected last switch \(x\), and no permutation of \(B\) realizes a diagonal. Then an adjacent transposition within \(B\) changes the first switch coordinate.

**Proof.** In the second witness, the first switch cannot equal \(x\). The adjacent-transposition graph of the permutations of \(B\) is connected. Along a path between the two witnesses, at least one swap changes the first switch. \(\square\)

If positions \(j,j+1\) are swapped, only triple positions \(j-2,\ldots,j+1\) can change, clipped to \(1,\ldots,m\). Consequently only switch positions \(j-3,\ldots,j+1\) can change. If two resulting first-switch coordinates \(a<a'\) differ, the earlier coordinate \(a\) lies in this five-position interval; the word with first switch \(a'\) is constant through position \(a'\). Thus a long displacement has a monochromatic interval, while the cause of the displacement is local. The same statement holds for last switches by reversal.

### The conversion problem after face recurrence

Boundary antisymmetry turns each specified non-tight triple into its reversed tight triple. By itself, however, the preceding face geometry does not yet synchronize arbitrary left and right witnesses: a moved front need not already be one exterior vertex reversing two required end edges, and witnesses with different outside block orders need not have disjoint exposed edges.

The next subsection resolves precisely this issue without trying to synchronize two arbitrary chambers. Instead one minimizes switch span inside the carrier face and transports the **same physical carrier** to the two extreme fronts of a single chamber. The common-block conclusion above keeps both tests inside the face, while minimality prevents inward front motion. This produces the required local reversal structure and removes the formerly global synchronization problem.

The local path-cover mechanisms used after that compression are recorded in [[path_disturbance_endpoint_reversal_descent_or_an_omission_swap]], [[endpoint_transport_and_small_support_gluing_the_remaining_lemma]], and [[defect_lines_and_spanning_order_compression_the_remaining_lemma]].


## Recurrent-face and minimum-span compression


### Compact switch span

For a spanning order
\[
\pi=(v_1,\ldots,v_n)
\]
whose status word has first switch \(a\) and last switch \(b\), put
\[
d(\pi)=b-a.
\]

**Lemma 7.5 (compact switch span).** If \(d(\pi)\le 2\), then \(H\) has a spanning two-cover.

**Proof.** Cut the order after \(v_{a+2}\). Every status internal to the left block has index at most \(a\), hence has the first-run color. Every status internal to the right block has index at least \(a+3>b\), hence has the last-run color. A monochromatic block is a tight path in its displayed orientation when its color is tight, and in the reverse orientation when its color is non-tight. Thus the two blocks can be oriented as tight paths. \(\square\)

The same cut calculation gives a useful next range.

**Lemma 7.6 (small middle from span at most five).** If
\[
3\le d(\pi)\le5,
\]
then \(H\) has a spanning three-cover
\[
L\mid M\mid R
\]
in which
\[
|M|=d(\pi)-2\le3.
\]

**Proof.** Put
\[
L=(v_1,\ldots,v_{a+2}),\qquad
M=\{v_{a+3},\ldots,v_b\},\qquad
R=(v_{b+1},\ldots,v_n).
\]
All internal statuses of \(L\) have the first-run color and all internal statuses of \(R\) have the last-run color, so each outer block has a tight orientation. The middle has order at most three and is therefore Hamiltonian: orders one and two are vacuous, and on three vertices one of the two reverse orders is tight by boundary antisymmetry. \(\square\)

### A recurrent carrier face has no large global residue

Let
\[
F=B_1|\cdots|B_k
\]
be a carrier face supplied by Theorem 6.1, so every chamber root occurring in \(F\) lies on a directed root cycle unless it is zero. Assume first that \(F\) contains no zero root.

Choose a chamber
\[
\pi=(v_1,\ldots,v_n)\in\mathcal V(F)
\]
for which \(d=b-a\) is minimum among the chambers of \(F\). Put
\[
m=n-2,\qquad c=m-b,
\]
so the root of \(\pi\) is the arc
\[
a\longrightarrow c.
\]

Because this arc lies on a directed root cycle, choose a simple such cycle and let \(r\) be its least coordinate. Every arc \(x\to y\) on the cycle comes from a chamber with
\[
x+y=m-d(\text{that chamber})\le m-1.
\]

If
\[
n<2r+6,
\]
then \(m\le2r+3\). For a neighbor \(s\) of \(r\) on the cycle,
\[
2r\le r+s\le m-1\le2r+2.
\]
There are no loops because \(F\) has no zero root, so \(s-r\in\{1,2\}\). The chamber realizing \(r\to s\) has switch span
\[
m-r-s\le2,
\]
and Lemma 7.5 gives a two-cover.

Hence, in a counterexample,
\[
n\ge2r+6.
\]
Corollary 7.2 then gives one block \(B\) of \(F\) containing the whole corridor
\[
r+3,\ldots,n-r-2=r+3,\ldots,m-r.
\]
Since \(a,c\ge r\), whenever \(d=b-a\ge6\) the position interval
\[
a+4,\ldots,b-1
\]
lies inside this same block.

This allows one physical vertex to be tested at both extreme fronts without leaving the face.

**Theorem 7.7 (one-carrier compression in a recurrent face).** Suppose \(H\) has no spanning two-cover. Suppose \(F\) has positive balance on every chamber and contains no zero root. Let \(\pi\in\mathcal V(F)\) minimize switch span in \(F\). If \(d(\pi)\ge6\), then \(H\) contains a Hamiltonian support of order four or five.

**Proof.** Let
\[
W=\{v_{a+4},\ldots,v_{b-1}\}.
\]
Then \(|W|=d-4\ge2\), and all these positions lie in the single face block \(B\).

Fix \(w\in W\). First permute only positions \(a+4,\ldots,b-1\) inside \(B\) so that \(w\) occupies position \(a+4\). This preserves both extreme switches: the first switch is determined through position \(a+3\), while the last switch \(b\) is determined by positions \(b,\ldots,n\). Now swap positions \(a+3,a+4\). No switch before \(a\) can be created, and \(b\) is outside the affected window. If the first switch moved to the right, the new chamber of \(F\) would have smaller switch span, contrary to the choice of \(\pi\). Therefore the first switch remains \(a\).

Let \(\alpha\) be the first-run color. If \(\alpha=1\), the preceding statement says that \(w\) reverses the terminal edge of the tight-oriented left outer block. If \(\alpha=0\), the left outer block is tight after reversal and the same statement says that \(w\) reverses its initial edge.

Independently restart from \(\pi\), place the same \(w\) at position \(b-1\), and swap positions \(b-1,b\). The first switch is now outside the affected window. If the last switch moved left, the switch span would decrease. Hence the last switch remains \(b\). Writing \(\omega\) for the last-run color, \(w\) reverses the terminal edge of the tight-oriented right outer block when \(\omega=0\), and its initial edge when \(\omega=1\).

The two exposed edges are vertex-disjoint because \(d\ge6\).

If \(\alpha\ne\omega\), the two reversals have the same endpoint type: terminal-terminal for \((\alpha,\omega)=(1,0)\), and initial-initial for \((0,1)\). A common reverser of two disjoint same-type end edges gives a Hamiltonian four-support. For completeness, in the terminal-terminal case, if the two tight paths end in \(x_0,x_1\) and \(y_0,y_1\), then
\[
(w,x_1,x_0),\qquad(w,y_1,y_0)
\]
are tight. Exactly one of
\[
(x_1,w,y_1),\qquad(y_1,w,x_1)
\]
is tight. In the first case
\[
(x_1,w,y_1,y_0)
\]
is a tight four-path; in the second
\[
(y_1,w,x_1,x_0)
\]
is. The initial-initial case is symmetric.

Suppose now that \(\alpha=\omega\). The two reversals have mixed endpoint type. Up to symmetry write the tight-oriented exposed edges as
\[
\ldots,a_0,a_1
\qquad\text{and}\qquad
p_1,p_2,\ldots
\]
so that
\[
(w,a_1,a_0),\qquad(p_2,p_1,w)
\]
are tight. Exactly one of
\[
(p_1,w,a_1),\qquad(a_1,w,p_1)
\]
is tight. The first alternative gives the Hamiltonian five-path
\[
(p_2,p_1,w,a_1,a_0).
\]
In the second alternative \(w\) is a parallel middle between \(a_1\) and \(p_1\).

There are at least two choices of \(w\in W\). If neither gives a Hamiltonian five-support, choose distinct \(w,w'\) with
\[
(a_1,w,p_1),\qquad(a_1,w',p_1)
\]
tight. Exactly one of
\[
(w,a_1,w'),\qquad(w',a_1,w)
\]
is tight. Accordingly
\[
(w,a_1,w',p_1)
\quad\text{or}\quad
(w',a_1,w,p_1)
\]
is a tight four-path. Thus a Hamiltonian support of order four or five always occurs. \(\square\)

The proof deliberately uses the same physical carrier and two exposed edges from one chamber. It therefore does not require the false implication that two distinct reversers of one common edge force a four-support, and it does not require exposed edges belonging to two different witness orders to be disjoint.

Combining Lemmas 7.5–7.6 with Theorem 7.7 gives the non-diagonal face conclusion:
\[
\boxed{
\begin{array}{c}
\text{positively balanced carrier face with no zero root}
\\[2mm]\Longrightarrow\\[2mm]
\text{two-cover}
\ \vee\
\text{spanning three-cover with a component of order }\le3
\ \vee\
\text{Hamiltonian support of order }4\text{ or }5.
\end{array}}
\]

Thus the coordinated face structure eliminates the genuinely global giant-block residue. A nonzero recurrent chamber cannot remain trapped in an unbounded front-motion configuration.

### The diagonal branch is absorbed by global minimum span

A zero root need not itself be a two-cover, so it must not be silently identified with the exact target. There is, however, a face-independent version of the preceding carrier argument which absorbs this branch as well.

**Theorem 7.8 (global minimum-span compression).** Let \(H\) be a boundary \(3\)-tournament with no spanning two-cover. Choose a spanning order \(\pi\) with globally minimum switch span \(d=b-a\). Then exactly one of the following local outcomes occurs:

1. \(3\le d\le5\), and \(H\) has the spanning three-cover of Lemma 7.6 with a component of order at most three;
2. \(d\ge6\), and \(H\) contains a Hamiltonian support of order four or five.

**Proof.** A counterexample has no order with at most one switch, because such an order already splits into two monochromatic tight orientations. Lemma 7.5 excludes \(d\le2\).

For \(3\le d\le5\), apply Lemma 7.6.

Assume \(d\ge6\). Now the interval
\[
a+4,\ldots,b-1
\]
may be permuted freely in the full permutation space, rather than merely inside one face block. Repeat verbatim the two carrier tests from Theorem 7.7. If either extreme front moved inward, the resulting spanning order would have smaller switch span, contradicting global minimality. Thus the same carrier reverses the two disjoint exposed end edges. The same-end and mixed-end arguments above give a Hamiltonian support of order four or five. \(\square\)

This theorem is stronger as a compression statement than the topology needs: once a counterexample is assumed, large switch span is already impossible as an independent geodesic obstruction.

### Closure of the geodesic/topological branch

The root topology and the global geodesic extremal argument now meet at one precise interface.

Theorem 6.1 upgrades a convex zero to recurrence for every chamber of a carrier face. Theorem 7.7 converts every nonzero recurrent branch into a two-cover or bounded local GN3 structure. A zero-root chamber is not itself declared solved; Theorem 7.8 instead shows that the diagonal branch cannot retain an independent global geodesic obstruction either.

Consequently Article VII has no remaining unbounded permutahedral or antipodal-geodesic residue. In a hypothetical counterexample the output of the entire geodesic program is already local:
\[
\boxed{
\text{small-middle spanning three-cover}
\quad\vee\quad
\text{Hamiltonian }4\text{- or }5\text{-support}.
}
\]

This is a handoff, not a proof of the grand conjecture. In particular it does not assert
\[
R\cap A(R)\ne\varnothing.
\]
What has been closed is the specifically geodesic/topological conversion problem: balanced recurrence no longer needs to be synchronized into a global reachability state. Its only surviving consequences are the bounded GN3 configurations handled by the local path-cover machinery.


## Exact-deficiency sharpening: the one-hole four-support handoff


### Exact deficiency one in a minimum counterexample

The exact inversion coordinates from [[spanning_orders_and_defect_helly]] sharpen the minimum-span conclusion further. For a spanning order \(\pi\), write
\[
p(\pi)=\min\{i:\epsilon_i=0\},\qquad
q(\pi)=\max\{i:\epsilon_i=1\},
\]
and
\[
\delta(\pi)=q(\pi)-p(\pi)-1.
\]
By the exact inversion-window criterion,
\[
\operatorname{pc}(H)\le2
\iff
\exists\pi\text{ with }\delta(\pi)\le0.
\]
Thus every spanning order of a counterexample has \(\delta\ge1\).

**Theorem 7.9 (minimum exact deficiency is one).** Let \(H\) be a minimum counterexample to the two-cover conjecture. Then
\[
\min_\pi\delta(\pi)=1.
\]
More precisely, for every \(x\in V(H)\) and every displayed two-cover
\[
H-x=P\mid Q
\]
with \(P=(p_1,\ldots,p_r)\) and \(Q=(q_1,\ldots,q_s)\), the spanning order
\[
\pi=(p_1,\ldots,p_r,x,q_s,\ldots,q_1)
\]
has \(\delta(\pi)=1\).

**Proof.** First \(r,s\ge3\). Indeed, if one deletion-cover component had order at most two, adjoining \(x\) would give a set of order at most three, hence a Hamiltonian tight path; together with the other displayed component this would two-cover \(H\).

In \(\pi\), every status wholly inside \(P\) is \(1\), while every status wholly inside \(Q^{\rm rev}\) is \(0\). Hence only the three junction statuses
\[
(p_{r-1},p_r,x),\qquad
(p_r,x,q_s),\qquad
(x,q_s,q_{s-1})
\]
can interrupt the pattern \(1^*0^*\). Consequently
\[
p(\pi)\ge r-1,\qquad q(\pi)\le r+1,
\]
so
\[
\delta(\pi)=q(\pi)-p(\pi)-1\le1.
\]
Since \(H\) is a counterexample, the exact inversion-window criterion gives \(\delta(\pi)\ge1\). Therefore \(\delta(\pi)=1\). \(\square\)

Equality forces
\[
p(\pi)=r-1,\qquad q(\pi)=r+1.
\]
Thus the first and third junction statuses are forced:
\[
(p_{r-1},p_r,x)\text{ is non-tight},
\qquad
(x,q_s,q_{s-1})\text{ is tight}.
\]
By boundary reversal,
\[
(x,p_r,p_{r-1})
\]
is tight as well. Hence the omitted vertex \(x\) reverses the displayed terminal edge of each deletion path:
\[
(x,p_r,p_{r-1}),\qquad
(x,q_s,q_{s-1})
\quad\text{are tight}.
\]

This is exactly the deficiency-one instance of the canonical partial-cover construction in [[convex_root_balance_and_bourgin_yang]]: the exact root carries a two-path cover with one missing vertex, and the missing vertex controls both exposed terminal edges.

### The exact geodesic handoff is a four-support

The preceding double reversal has an immediate bounded consequence.

**Corollary 7.10 (canonical four-support from exact deficiency one).** Let \(H\) be a minimum counterexample. For every deletion cover
\[
H-x=P\mid Q,
\]
the terminal edges of \(P\) and \(Q\), together with \(x\), contain a Hamiltonian four-support. Its complement is non-Hamiltonian and has path-cover number exactly two.

**Proof.** Write the terminal edges of the displayed tight paths as
\[
\ldots,a_0,a_1,
\qquad
\ldots,b_0,b_1.
\]
Theorem 7.9 gives
\[
(x,a_1,a_0),\qquad(x,b_1,b_0)
\]
tight. Exactly one of
\[
(a_1,x,b_1),\qquad(b_1,x,a_1)
\]
is tight. In the first case
\[
(a_1,x,b_1,b_0)
\]
is a tight Hamiltonian four-path; in the second,
\[
(b_1,x,a_1,a_0)
\]
is.

Let \(K\) be this four-set. It is proper, since otherwise \(H\) itself would be Hamiltonian. By minimality, \(H-K\) has path-cover number at most two. It cannot be Hamiltonian, because a Hamilton path on \(H-K\) together with the displayed Hamilton path on \(K\) would two-cover \(H\). Hence
\[
\operatorname{pc}(H-K)=2
\]
and \(H-K\) is non-Hamiltonian. \(\square\)

This sharpens the minimum-counterexample endpoint of the geodesic investigation. The width-three switch-span formulation remains useful for arbitrary counterexamples and for the recurrent-face compression, but after minimum-counterexample induction the exact inversion coordinate removes the mixed-end ambiguity entirely:
\[
\boxed{
\text{minimum counterexample}
\Longrightarrow
\text{canonical Hamiltonian four-support with non-Hamiltonian two-coverable complement}.
}
\]

Thus no synchronization of an entire directed root cycle is needed to finish Article VII's own task. The exact-root coordinate already reaches the bounded local interface. What remains after this point is the local four-support/path-cover analysis, not an antipodal-geodesic obstruction.


## Metadata

- ID: topological_recurrence_to_local_gn3_structure
- Kind: section
- Version: 15
- Math version: 10
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Subsection 1 — crystallized, version 5: From balanced recurrence to local reversal structure
- Subsection 2 — crystallized, version 5: Recurrent-face and minimum-span compression
- Subsection 3 — crystallized, version 3: Exact-deficiency sharpening: the one-hole four-support handoff
- Subsection 4 — HOT, version 1: (untitled)
