# Recurrent-face and minimum-span compression

## Metadata

- ID: topological_recurrence_to_local_gn3_structure_subsection_b
- Parent Section: topological_recurrence_to_local_gn3_structure
- Position: 2
- Row version: 5
- Development version: 5
- Composition version: 1
- Composition stale: False

## Composition


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


## Development


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
