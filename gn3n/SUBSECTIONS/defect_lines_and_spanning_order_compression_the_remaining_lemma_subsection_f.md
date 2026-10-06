# Coherent residue collapses

## Metadata

- ID: defect_lines_and_spanning_order_compression_the_remaining_lemma_subsection_f
- Parent Section: defect_lines_and_spanning_order_compression_the_remaining_lemma
- Position: 6
- Row version: 13
- Development version: 13
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

### The coherent bridge residue already contains a bounded support

**Lemma 36 (coherent residue collapse).** In the coherent failure residue of Lemma 35, the four-set
[
K={c_4,d_1,p,q}
]
is Hamiltonian. Consequently either (H) has a two-cover, or
[
operatorname{pc}(H-K)=2.
]

**Proof.** Lemma 35 gives the tight triples
[
(d_1,q,p)
qquad	ext{and}qquad
(q,p,c_4).
]
Hence
[
(d_1,q,p,c_4)
]
is a Hamilton tight path on (K).

Since (K) is a proper Hamiltonian support, minimum-counterexample calculus gives
[
operatorname{pc}(H-K)le2.
]
If (H-K) were Hamiltonian, a Hamilton path on (K) together with a Hamilton path on (H-K) would form a spanning two-cover of (H). Thus, in a minimum counterexample,
[
operatorname{pc}(H-K)=2.
]
(square)

Therefore the two-label one-defect analysis has no independent terminal residue. In the opposite-endpoint synchronization case, either one of the three simultaneous completion orders already has
[

u(L_sigma)le1,
]
or the failure pattern produces a Hamiltonian four- or five-support with non-Hamiltonian two-coverable complement.

Combined with the bounded-support comparison reductions, the order-eleven synchronization route returns entirely to the single global interface
[
oxed{	ext{external endpoint reversal}.}
]

The remaining problem is thus genuinely the general local-to-global reversal problem, not a special order-eleven slot or completion obstruction.

### Two labels reversing both exposed sides force bounded support

**Lemma 37.** Let \(A=(\ldots,a_{r-1},a_r)\) and \(C=(c_1,c_2,\ldots)\) be disjoint tight paths, and let \(u,v\) be distinct exterior vertices. Suppose \((u,a_r,a_{r-1})\), \((v,a_r,a_{r-1})\), \((c_2,c_1,u)\), and \((c_2,c_1,v)\) are tight. Then these exposed vertices contain a Hamiltonian support of order four or five.

**Proof.** For \(z\in\{u,v\}\), if \((c_1,z,a_r)\) is tight, then \((c_2,c_1,z,a_r,a_{r-1})\) is a Hamilton five-path. Otherwise both central triples fail, so boundary antisymmetry gives \((a_r,u,c_1)\) and \((a_r,v,c_1)\) tight. The parallel-middle lemma in [[localextend01]] makes \(\{a_r,c_1,u,v\}\) Hamiltonian. \(\square\)

Thus simultaneous double-sided reversal by both middle labels is not a terminal configuration; in a minimum counterexample the resulting proper Hamiltonian support has non-Hamiltonian path-cover-two complement.


### The two-label bridge is not specific to order eleven

The completion argument above depends only on the local junction pattern, not on the lengths of the two inherited tight paths.

**Lemma 37 (abstract two-label one-defect bridge).** Let \(H\) be a minimum counterexample. Let \(p,q,x\) be distinct vertices, and suppose the remaining vertices are ordered as two nonempty tight paths
\[
L=(\ldots,\ell),\qquad R=(r,\ldots).
\]
Assume that the following three deletion orders have no possible defect triples except those displayed:
\[
\begin{aligned}
\sigma_0&=L,x,R,
&&(\ell,x,r),\\
\sigma_p&=L,p,x,R,
&&(\ell,p,x),\ (p,x,r),\\
\sigma_q&=L,x,q,R,
&&(\ell,x,q),\ (x,q,r).
\end{aligned}
\]
Then either \(H\) has a two-cover, or \(H\) contains a Hamiltonian support of order four or five whose complement is non-Hamiltonian with path-cover number two.

**Proof.** Consider the three spanning orders
\[
\begin{aligned}
\tau_1&=L,p,x,q,R,\\
\tau_2&=L,p,q,x,R,\\
\tau_3&=L,x,p,q,R.
\end{aligned}
\]
By the hypotheses on \(\sigma_p,\sigma_q\), every possible defect of these orders lies, respectively, among
\[
\begin{aligned}
&(\ell,p,x),\ (p,x,q),\ (x,q,r),\\
&(\ell,p,q),\ (p,q,x),\ (q,x,r),\\
&(\ell,x,p),\ (x,p,q),\ (p,q,r).
\end{aligned}
\]
In each line the three possible defect edges are consecutive in the defect line. Hence if any \(\tau_i\) has defect matching number at most one, the defect-line identity gives a two-cover of \(H\).

Assume therefore that all three have defect matching number two. For three consecutive possible defect edges, matching number two forces the first and third to be present. Thus the six triples
\[
(\ell,p,x),\ (x,q,r),\ 
(\ell,p,q),\ (q,x,r),\ 
(\ell,x,p),\ (p,q,r)
\]
are all non-tight. Boundary antisymmetry gives
\[
(x,p,\ell),\ (r,q,x),\ 
(q,p,\ell),\ (r,x,q),\ 
(p,x,\ell),\ (r,q,p)
\]
tight.

If at least one of
\[
(q,x,p),\qquad (x,q,p),\qquad (q,p,x)
\]
is tight, then respectively one of
\[
(r,q,x,p,\ell),\qquad
(r,x,q,p,\ell),\qquad
(r,q,p,x,\ell)
\]
is a Hamiltonian path on
\[
F=\{\ell,r,p,q,x\}.
\]
Hence \(F\) is a Hamiltonian five-support.

Otherwise all three displayed triples are non-tight, so their boundary reversals
\[
(p,x,q),\qquad (p,q,x),\qquad (x,p,q)
\]
are tight. But the already-forced triples
\[
(r,q,p),\qquad(q,p,\ell)
\]
then show directly that
\[
(r,q,p,\ell)
\]
is a Hamiltonian path on the four-set
\[
K=\{\ell,r,p,q\}.
\]

Thus in every case there is a proper Hamiltonian support \(S\) of order four or five. Minimum-counterexample calculus gives
\[
\operatorname{pc}(H-S)\le2.
\]
If \(H-S\) were Hamiltonian, \(S\) together with \(H-S\) would two-cover \(H\). Therefore
\[
\operatorname{pc}(H-S)=2.
\]
\(\square\)

Lemma 37 isolates the genuinely global part of the reversal problem. Once an external reversal can be placed inside a common one-defect bridge for two omitted labels, there is no further completion obstruction: the bridge either compresses directly to one defect cut or falls back into the bounded four/five-support comparison machinery.

Accordingly the remaining local-to-global task may be stated more sharply:

> starting from an external endpoint reversal in a minimum counterexample, manufacture two omitted labels whose deletion covers realize the three bridge orders \(\sigma_0,\sigma_p,\sigma_q\) of Lemma 37.

The difficult step is now **bridge manufacture**, not bridge completion.



### Correction: same-edge twins do not force bounded support

The former Lemma 38 and Corollary 39 are withdrawn.

Two distinct exterior vertices may both reverse the same displayed end edge without forcing any Hamiltonian four-set. From
\[
(u,a_r,a_{r-1}),\qquad (v,a_r,a_{r-1})
\]
tight, boundary antisymmetry gives only the two reverse triples on those same supports. It gives no relation between \(u\) and \(v\), and no relation sufficient to concatenate them into a Hamiltonian four-path. There are four-vertex boundary tournaments realizing this same-edge twin pattern without a Hamilton path.

Accordingly, the alternatives in the universal reversal lemma in which two prescribed labels reverse one common exposed edge do **not** by themselves collapse to bounded support. Any later argument using such a pair must obtain additional reversal data on a second edge or use another independent local constraint.

The valid nearby principle is the following.

**Lemma 38 (one carrier reversing two disjoint same-type edges).** Let
\[
A=(\ldots,a_{r-1},a_r),\qquad
P=(\ldots,p_{m-1},p_m)
\]
be vertex-disjoint tight paths, and let \(w\) lie outside both supports.

If
\[
(w,a_r,a_{r-1}),\qquad (w,p_m,p_{m-1})
\]
are tight, then the exposed vertices contain a Hamiltonian four-set. Indeed exactly one of
\[
(a_r,w,p_m),\qquad (p_m,w,a_r)
\]
is tight. In the first case
\[
(a_r,w,p_m,p_{m-1})
\]
is a tight four-path; in the second
\[
(p_m,w,a_r,a_{r-1})
\]
is a tight four-path.

The symmetric initial-initial form is also valid. If
\[
(a_2,a_1,w),\qquad (p_2,p_1,w)
\]
are tight, then exactly one of
\[
(a_1,w,p_1),\qquad (p_1,w,a_1)
\]
is tight, producing respectively
\[
(a_2,a_1,w,p_1)
\quad\text{or}\quad
(p_2,p_1,w,a_1).
\]

Thus a **single carrier** reversing two vertex-disjoint edges of the same endpoint type forces bounded support. The mixed initial-terminal case is a separate configuration and is not asserted here.

### The mixed universal pattern forces a bridge or a split

**Lemma 40 (bridge-or-split comparison).** Let (H) be a minimum counterexample and suppose
[
H-{z,w}=Amid C,
]
where
[
A=(a_1,ldots,a_r),qquad C=(c_1,ldots,c_s),qquad r,sge2,
]
and
[
(a_{r-1},a_r,z),qquad (z,c_1,c_2),
]
[
(w,a_r,a_{r-1}),qquad (c_2,c_1,w)
]
are tight.

Then:

1. ((a_r,z,c_1)) is non-tight, so
   [
   (c_1,z,a_r)
   ]
   is tight. Hence (H-w) has the two deletion covers
   [
   (A,z)mid C,qquad Amid(z,C).
   ]

2. Every two-cover (F) of (H-z) has one of the following forms:
   - (F) contains an ordinary path edge joining (A) directly to (C);
   - (w) is internal in one component of (F), with one path-neighbor in (A) and one in (C), and one of the old supports (A,C) is split between the two components of (F).

**Proof.** If ((a_r,z,c_1)) were tight, then
[
(a_1,ldots,a_r,z,c_1,ldots,c_s)
]
would be Hamiltonian on (H-w). Together with the singleton path ((w)), this would two-cover (H). Thus ((a_r,z,c_1)) is non-tight, and boundary antisymmetry gives ((c_1,z,a_r)) tight. The two displayed covers of (H-w) follow from the two assumed bridge triples.

Now let (F) be any two-cover of (H-z). The set (Acup{z}) is Hamiltonian, so [[hamiltonian_enlargement_forces_cut_edge01]] applied with deleted vertex (z) forces an (F)-edge crossing
[
Amid(Ccup{w}).
]
Likewise ({z}cup C) is Hamiltonian, so an (F)-edge crosses
[
Cmid(Acup{w}).
]

If an (F)-edge joins (A) directly to (C), we are done. Otherwise every required crossing is incident with (w). Since (w) has degree at most two in a path cover, there are exactly two such crossing edges: one joins (w) to (A), and one joins (w) to (C). Thus (w) is internal in one component of (F), lying between a nonempty (A)-block and a nonempty (C)-block.

The second component of (F) is nonempty because (H-z) is non-Hamiltonian. It cannot contain (w), and with no direct (A)-(C) edge it lies wholly in one of (A,C). That old support therefore occurs both in the mixed component and in the second component, so it is split between the two comparison paths. (square)

Thus the hard mixed universal endpoint pattern automatically manufactures the geometry needed for bridge construction. Deleting the bridge label (z) forces either direct (A)-to-(C) mixing or an explicit internal (A)-(w)-(C) bridge together with a split old support. The remaining task is to synchronize this mandatory comparison disturbance with the one-defect deletion orders of the abstract two-label bridge.



### Direct mixing in the universal mixed pattern reduces to the disturbance toolkit

**Lemma 41.** Retain the mixed universal pattern of Lemma 40:
[
H-{z,w}=Amid C,
]
with
[
A=(a_1,ldots,a_r),qquad C=(c_1,ldots,c_s),
]
and
[
(a_{r-1},a_r,z),qquad (z,c_1,c_2),
]
[
(w,a_r,a_{r-1}),qquad(c_2,c_1,w)
]
tight.

Let
[
H-w=(A,z)mid C
]
be the displayed deletion cover, and let (F) be any two-cover of (H-z) containing an ordinary path edge joining (A) directly to (C).

Then at least one of the following holds:

1. (F) has an order disagreement with the inherited order on (A);
2. an inherited edge of (A) has endpoints in two different paths of (F);
3. one path of (F) leaves (A) through a nonempty exterior segment and later returns;
4. a tight triple reverses the displayed endpoint edge (a_rz);
5. (H) has a two-cover;
6. the three-cover (Fmid{z}) admits a strict quadratic-potential decrease;
7. endpoint restoration is neutral and produces a deletion cover compatible with (F) on the common domain.

**Proof.** If (F) does not preserve the inherited relative order of the surviving vertices of (A), outcome 1 holds.

Otherwise apply [[path_disturbance_endpoint_reversal_descent_or_an_omission_swap]] with
[
y=w,qquad
R=(a_1,ldots,a_r,z),qquad
Q=C,
]
and with the omitted endpoint of (R) equal to (z). The hypothesis that (F) contains a direct (A)-to-(C) edge is exactly the required mixed-edge hypothesis. The theorem gives outcomes 2–7. (square)

Thus the direct-mixing alternative of Lemma 40 is not a new global obstruction. It enters the already-developed disturbance system immediately.

Consequently, bridge manufacture may be narrowed further: after excluding order disagreement, split/leave-and-return disturbance, fresh endpoint reversal, two-cover, and strict descent, the only coherent direct-mix residue is a neutral omission swap producing compatible deletion covers.

Together with the second alternative of Lemma 40, the unresolved bridge-manufacture problem is therefore reduced to **compatible omission swaps and split-support comparisons**.



### The split-support branch of the mixed pattern is already an external reversal

**Corollary 42.** In Lemma 40, suppose the second alternative occurs: the comparison two-cover of \(H-z\) has \(w\) internal between an \(A\)-block and a \(C\)-block, and one of the old supports \(A,C\) is split between the two comparison paths. Then \(H\) contains an external tight triple reversing an edge of one of the displayed paths.

**Proof.** Suppose \(A\) is split; the case of \(C\) is symmetric. Since \(A\) is a connected displayed path and its vertices occur in both comparison paths, some inherited ordinary edge of \(A\) has its endpoints in different comparison paths. In the spanning three-cover
\[
(A,z)\mid C\mid\{w\},
\]
that edge is an inherited displayed edge of the first component. Lemma 32 applies to this split edge and produces an external tight triple reversing an edge of one of the displayed components. The singleton third component causes no difficulty: the proof of Lemma 32 simply omits nonexistent junction triples. \(\square\)

Consequently Lemma 40 has no independent split-support residue. Together with Lemma 41 and Lemma 32, every branch of the mixed universal pattern reduces to a two-cover, strict descent, an external reversal, or a neutral omission swap producing compatible deletion covers. Thus the only coherent bridge-manufacture residue still not absorbed by the existing reversal machinery is the compatible neutral omission swap.


### Neutral omission swaps collapse to the external-reversal interface

The compatible neutral omission-swap residue in Lemma 41 is not independent.

**Lemma 43 (neutral omission-swap absorption).**
Suppose the Phi-neutral omission-swap outcome of
[[path_disturbance_endpoint_reversal_descent_or_an_omission_swap]]
occurs. Then either (H) has a two-cover or the existing disturbance reductions yield an external tight triple reversing a displayed endpoint edge.

**Proof.**
Use the normal form from the cited theorem. Write
[
H-y=Rmid Q,qquad
R=(r_0,ldots,r_m),qquad
z=r_0,qquad
B=(r_1,ldots,r_m),
]
and let
[
T=Cmid D
]
be the deletion cover of (H-z). In the no-disturbance branch, (B) is one inherited-order block of
[
C=L,B,K.
]

First suppose (K
earnothing). Neutrality forces (|L|=1); write (L=(w)). Then
[
T=(w,B,K)mid D
]
is a deletion cover of (H-z), while restoration gives
[
G_w=(z,B,K)mid D
]
as a deletion cover of (H-w). These are exactly the same-slot root-exchange hypotheses of Lemma 11 above, with common ordered core ((B,K)) and fixed path (D). Lemma 11 gives a two-cover, a direct mixed edge, an order disagreement, or an external reversal at the opposite endpoint. Direct mixing is absorbed by the current comparison reductions into split/leave-and-return unless a two-cover already exists; order disagreement yields an external reversing triple by the path-intersection calculus; and Corollary 33 absorbs split/leave-and-return into external reversal. Hence this branch yields a two-cover or external reversal.

Now suppose (K=arnothing). Write
[
L=L',w.
]
Neutrality forces (|L'|=1); write (L'=(u)). Then
[
T=(u,w,B)mid D
]
is a deletion cover of (H-z), and restoration gives the tight path
[
(w,z,B).
]
Omitting (u) gives the compatible deletion cover
[
G_u=(w,z,B)mid D
]
of (H-u).

If ((u,w,z)) is tight, then
[
(u,w,z,B)
]
is tight: the triple ((w,z,r_1)) is supplied by the restoration branch and all later triples are inherited from (B). Hence
[
(u,w,z,B)mid D
]
two-covers (H).

Otherwise ((u,w,z)) is non-tight, so boundary reversal gives
[
(z,w,u)
]
tight. Since (uw) is the displayed initial edge of ((u,w,B)) in (T), this is an external tight triple reversing a displayed endpoint edge. (square)

Thus the compatible neutral omission swap identified after Lemma 42 is absorbed as well. After the current reductions, bridge manufacture has no independent neutral residue: every branch returns to a two-cover, strict descent, or the single recurrent geometric interface of external endpoint reversal.


### Neutral omission swaps are not a terminal bridge residue

The compatible neutral omission-swap branch can now be removed from the list of unresolved bridge-manufacture outcomes.

**Corollary 43 (neutral recurrence collapse).** In a minimum counterexample, a neutral omission swap producing compatible deletion covers yields, after the selected-cover continuation of [[balanced_omission_swap_gives_descent_or_selected_singleton_recurrence]], at least one of the following:

1. a two-cover of \(H\);
2. an external reversing tight triple;
3. a Hamiltonian four-support with non-Hamiltonian path-cover-two complement;
4. a non-neutral disturbance already handled by the existing comparison machinery.

In particular there is no independent indefinitely neutral omission-swap residue.

**Proof.** In the forest branch, [[three_cover_repartitions_and_recurrence_several_deleted_labels_in_one_component]] shows that neutral recurrence reduces to immediate backtracking between a compatible pair, and the equal endpoint-slot closure turns that backtracking into a two-cover.

In the spanning odd-cycle support geometry, adjacent selected covers are support-compatible. The compatible-pair trichotomy of [[deletion_covers_and_the_support_graph_compatibility_of_deletion_covers]] gives either order disagreement, adjacent-slot reversal, an equal internal-slot Hamiltonian four-support, or an equal endpoint-slot two-cover. Thus the cyclic support geometry also has no quiet neutral recurrence.

Therefore a neutral omission swap cannot persist as an additional bridge-manufacture obstruction. \(\square\)

Combining Corollary 43 with Corollary 42 and Lemma 32 removes both coherent comparison residues produced by Lemmas 40--41. After all current reductions, the only unresolved global conversion is once again
\[
\boxed{\text{external endpoint reversal}.}
\]
The difference from Corollary 33 is that the neutral omission-swap escape route has now also been closed globally rather than merely isolated.


### The reversing label is globally noninsertable in the mixed bridge pattern

The mixed universal pattern of Lemma 40 carries a stronger obstruction than the two displayed endpoint reversals.

**Lemma 44 (cross noninsertability).** Retain the hypotheses and notation of Lemma 40:
[
H-{z,w}=Amid C,
]
where
[
A=(a_1,ldots,a_r),qquad C=(c_1,ldots,c_s),
]
and
[
(a_{r-1},a_r,z),qquad(z,c_1,c_2),
]
[
(w,a_r,a_{r-1}),qquad(c_2,c_1,w)
]
are tight.

Then each of the four vertex sets
[
Acup{w},qquad
Ccup{w},qquad
Acup{z,w},qquad
Ccup{z,w}
]
is non-Hamiltonian. Consequently (w) is noninsertable at every position of each of the four displayed Hamilton paths
[
A,qquad C,qquad (A,z),qquad (z,C).
]

In particular the mixed-pattern witness (w) is a globally blocked augmentation label on both sides of the bridge vertex (z).

**Proof.** The displayed triples give the Hamiltonian paths
[
(A,z)=(a_1,ldots,a_r,z)
qquad	ext{and}qquad
(z,C)=(z,c_1,ldots,c_s).
]

If (Acup{w}) were Hamiltonian, a Hamilton path on (Acup{w}) together with the displayed path ((z,C)) would two-cover (H), impossible. Thus (Acup{w}) is non-Hamiltonian. Similarly, if (Ccup{w}) were Hamiltonian, it would pair with ((A,z)) to two-cover (H).

If (Acup{z,w}) were Hamiltonian, that Hamilton path together with (C) would two-cover (H); hence this set is non-Hamiltonian. Likewise (Ccup{z,w}) is non-Hamiltonian because (A) is Hamiltonian.

Apply [[endpoint_replacement_truncation_dichotomy01]] first to the displayed paths (A,C) with exterior vertex (w), and then to the displayed paths ((A,z),(z,C)) with exterior vertex (w). In each case the augmented support is non-Hamiltonian, so the non-Hamiltonian branch of the dichotomy says that (w) is noninsertable at every inherited gap of the displayed path. (square)

Thus Lemma 40 may be viewed as an augmenting-path obstruction: (z) is simultaneously transportable across both old supports, while (w) is blocked from every inherited insertion slot before and after that transport. Any completion of bridge manufacture must exploit this global blockage rather than only the two exposed reversal triples.



### The universal prescribed-pair patterns collapse further

The endpoint classification for
\[
H-\{u,v\}=A\mid C
\]
has two same-edge-twin alternatives and one mixed alternative.

#### Same-edge twins are bounded-support branches

Suppose
\[
A=(a_1,\ldots,a_r),\qquad C=(c_1,\ldots,c_s),
\]
and
\[
(u,a_r,a_{r-1}),\qquad(v,a_r,a_{r-1})
\]
are tight.

If \((c_{s-1},c_s,u)\) is non-tight, then
\[
(u,c_s,c_{s-1})
\]
is tight, so the single carrier \(u\) reverses the terminal edges of the two disjoint tight paths \(A,C\). The common-carrier lemma gives a Hamiltonian four-support.

Hence outside bounded support both \(u,v\) append to \(C\). If \(u\) could prepend to \(A\), then
\[
(u,A)\mid(C,v)
\]
would two-cover \(H\); similarly for \(v\). Thus both prepend attempts fail and
\[
(a_2,a_1,u),\qquad(a_2,a_1,v)
\]
are tight.

If \(r\ge4\), the initial and terminal end edges of \(A\) are disjoint, and the two-label double-sided reversal lemma gives a Hamiltonian four- or five-support.

If \(r=2\), the Hamiltonian three-set \(A\cup\{u\}\), together with \((C,v)\), gives a two-cover.

If \(r=3\), apply the fixed-three-path extension theorem to \(A\) and \(u,v,c_s\). One of
\[
A\cup\{u,v\},\quad A\cup\{u,c_s\},\quad A\cup\{v,c_s\}
\]
is Hamiltonian. The first gives a two-cover with \(C\); the latter two have complements covered respectively by
\[
\{v\}\mid(C-c_s),\qquad \{u\}\mid(C-c_s).
\]
Thus they give proper Hamiltonian five-supports with path-cover-two complement.

The same-initial-edge twin case is symmetric.

#### The mixed pattern is bridge-ready on one side

Retain Lemma 40:
\[
H-\{z,w\}=A\mid C
\]
with
\[
(a_{r-1},a_r,z),\quad(z,c_1,c_2),\quad
(w,a_r,a_{r-1}),\quad(c_2,c_1,w)
\]
tight. Put
\[
J_L=(a_{r-1},a_r,c_1),\qquad
J_R=(a_r,c_1,c_2).
\]

The two \(J\)-triples cannot both be tight, or \(A,C\) would concatenate to a Hamilton path on \(H-\{z,w\}\). If both are non-tight, their flips give
\[
(c_2,c_1,a_r,a_{r-1})
\]
as a Hamiltonian four-path. Hence outside bounded support exactly one is tight.

If \(J_R\) is tight, set
\[
L=(a_1,\ldots,a_{r-1}),\quad R=C,\quad
p=w,\ q=z,\ x=a_r.
\]
The three orders in the abstract two-label one-defect bridge then have no possible defects outside the prescribed junctions, except possibly
\[
(a_{r-2},a_{r-1},w)
\]
when \(r\ge3\). If this triple is tight or absent, the abstract bridge lemma applies. If it is non-tight, then
\[
(w,a_{r-1},a_{r-2})
\]
is tight, so \(w\) reverses the final two consecutive edges of \(A\).

The case \(J_L\) tight is symmetric: the bridge applies unless
\[
(w,c_2,c_3)
\]
fails, in which case
\[
(c_3,c_2,w)
\]
is tight and \(w\) reverses the first two consecutive edges of \(C\).

Thus the only extra residue beyond the completed abstract bridge is an adjacent double reversal.

#### Adjacent double reversal gives strict descent

Treat the left-hand residue. Put
\[
u=a_{r-2},\qquad v=a_{r-1},\qquad t=a_r.
\]
Then
\[
(w,t,v),\qquad(w,v,u),\qquad(v,t,z),\qquad(w,z,t)
\]
are tight. Define
\[
F=\{z,w,u,v,t\},\qquad K=\{z,w,v,t\}.
\]

At least one of \(F,K\) is Hamiltonian. Suppose both were non-Hamiltonian. If
\[
X=\{w,u,v,t\}
\]
were also non-Hamiltonian, the non-Hamiltonian-five-set theorem would give two non-Hamiltonian four-deletions of \(F\), impossible. Hence \(X\) is Hamiltonian.

Represent \(F\) by an edge order. Since \(K\) is non-Hamiltonian, its opposite-edge matchings form strict blocks. The three tight triples
\[
(v,t,z),\qquad(w,t,v),\qquad(w,z,t)
\]
force
\[
\{zv,wt\}<\{zw,vt\}<\{zt,wv\},
\]
hence
\[
vt<wv.
\]
But
\[
(w,v,u),\qquad(u,v,t)
\]
give
\[
wv<vu<vt,
\]
a contradiction.

If \(F\) is Hamiltonian, the pairwise repartition
\[
A\mid\{z,w\}\longrightarrow
(a_1,\ldots,a_{r-3})\mid F
\]
has
\[
\Delta\Phi=6(5-r).
\]
If \(K\) is Hamiltonian,
\[
A\mid\{z,w\}\longrightarrow
(a_1,\ldots,a_{r-2})\mid K
\]
has
\[
\Delta\Phi=4(4-r).
\]
The non-strict small values are made strict by moving one or two endpoints of the untouched path \(C\) into the residual component of order one or two. Since \(|V(H)|>10\), the resulting changes are negative; the unique neutral subcase \(r=4,s=5\) in the \(F\)-branch is followed by
\[
5\mid2\mid4\longrightarrow5\mid3\mid3,
\]
which decreases \(\Phi\) by \(2\).

Therefore the adjacent-double-reversal branch yields a two-cover or a strict \(\Phi\)-descent, while the Hamiltonian four- or five-component produced above retains both \(z,w\).

Consequently the mixed universal pattern has no independent terminal geometry: it yields the completed abstract bridge, bounded support, a two-cover, or strict bridge-pair-preserving descent.


## Frontier

- Development version when composed: None
- Development version now: 13
