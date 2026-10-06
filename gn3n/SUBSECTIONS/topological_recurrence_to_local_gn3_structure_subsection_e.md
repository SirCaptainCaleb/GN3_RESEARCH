# Bounded central blocks and short cycles in recurrent exact-root faces

## Metadata

- ID: topological_recurrence_to_local_gn3_structure_subsection_e
- Parent Section: topological_recurrence_to_local_gn3_structure
- Position: 5
- Row version: 4
- Development version: 4
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

### Exact roots and the hypotheses

For a spanning order \(\pi\) of a boundary \(3\)-tournament \(H\) on \(n\) vertices, write \(m=n-2\), let \(p(\pi)\) be the first non-tight status position, and let \(c(\pi)=m+1-q(\pi)\), where \(q(\pi)\) is the last tight status position. Thus \(c(\pi)=p(\pi^{\mathrm{rev}})\). The exact root is \(e_p-e_c\), and the exact deficiency is
\[
\delta(\pi)=m-p(\pi)-c(\pi).
\]
These conventions and the two-cover criterion are established in [[spanning_orders_and_defect_helly]].

Let \(F\) be an ordered-partition face of the permutahedron. Assume:

1. \(\delta(\pi)>0\) for every chamber \(\pi\) of \(F\);
2. every coordinate occurring as a tail of an exact root on \(F\) also occurs as a head, and conversely;
3. \(p(\pi)\ne c(\pi)\) for every chamber of \(F\).

Hypothesis 2 is weaker than positive root balance. In particular, the positive carrier theorem of [[convex_root_balance_and_bourgin_yang]] supplies it. No minimum-counterexample hypothesis is used.

**Theorem (bounded central block).** Put
\[
s=\min_{\pi\in\mathcal V(F)}\min\{p(\pi),c(\pi)\},
\qquad L=m-2s.
\]
There is a single face block \(B\), with \(b=|B|\le7\), such that the numbers \(\ell,r\) of positions before and after \(B\) satisfy
\[
\ell,r\in\{s,s+1\}.
\]
Every other face block has order at most two. More precisely:
\[
\begin{array}{c|c|c}
(\ell,r)& b\text{ in terms of }L&\text{upper bound on }b\\ \hline
(s,s)&L+2&7\\
(s,s+1)\text{ or }(s+1,s)&L+1&5\\
(s+1,s+1)&L&7.
\end{array}
\]
In particular \(2\le L\le7\), and every exact-root coordinate on \(F\) lies in
\[
\{s,s+1,\ldots,s+L-1\}\subseteq\{s,\ldots,s+6\}.
\]

### Locating the central block

Coordinate recurrence gives both a chamber with \(p=s\) and a chamber with \(c=s\). Since no root is zero, a chamber with \(p=s\) has \(c\ge s+1\). Its positive deficiency gives
\[
m\ge2s+2,
\]
so \(L\ge2\).

The event \(p=s\) is determined by positions \(1,\ldots,s+2\); the event \(c=s\) is determined by positions \(n-s-1,\ldots,n\). If a block boundary followed a position
\[
s+2\le j\le n-s-2,
\]
the independent block orders from the two witnesses could be combined, giving \(p=c=s\). Consequently one block \(B\) contains every position
\[
s+2,\ldots,n-s-1.
\]
Thus \(\ell,r\le s+1\).

Every chamber has \(p,c\ge s\). Hence all status positions \(1,\ldots,s-1\) are tight in every chamber, and all the corresponding statuses read inward from the right end are also tight in every chamber. If \(\ell\le s-2\), then \(B\) contains the three positions \(s-1,s,s+1\). Swapping the first and third vertices of this window stays in \(F\) and reverses its status, contradicting uniform tightness at \(s-1\). Therefore
\[
s-1\le\ell,r\le s+1.
\]

Set
\[
\alpha=s+2-\ell,\qquad\beta=s+2-r.
\]
These numbers belong to \(\{1,2,3\}\). A witness for \(p=s\) uses exactly the first \(\alpha\) vertices of \(B\), together with some orders of the blocks before \(B\). A witness for \(c=s\) uses exactly the first \(\beta\) vertices of \(B\) read inward from the right, together with some orders of the blocks after \(B\). In particular
\[
b=L+\alpha+\beta-2.
\]

Let \(\mathcal L,\mathcal R\) be the families of supports of these ordered witness tuples, allowing all outside block orders on the relevant side. Both families are nonempty. Every member of \(\mathcal L\) meets every member of \(\mathcal R\): disjoint witness tuples can be placed at opposite ends of \(B\), with their own left and right outside orders, and the remaining positions filled arbitrarily. This would give \(p=c=s\).

The independent choices of outside orders are legitimate here because the two determining windows are disjoint and involve disjoint collections of outside blocks. We are not combining two arbitrary witnesses that constrain the same outside block.

If \(\alpha=3\), the determining status at \(s\) is wholly inside \(B\). Every three-element subset of \(B\) therefore supports a left witness: one of the two reversed orders, for any fixed middle vertex, is non-tight. But a right witness uses \(\beta\) vertices, and
\[
b-\beta=L+1\ge3.
\]
A left witness can be chosen disjoint from it, a contradiction. The case \(\beta=3\) is symmetric. Thus \(\alpha,\beta\in\{1,2\}\), which proves \(\ell,r\in\{s,s+1\}\).

A block before \(B\) with three consecutive positions would contain a status window starting at most at \(\ell-2\le s-1\), where tightness is uniform. Boundary reversal rules this out. The same argument read inward from the right treats every block after \(B\). Thus all exterior blocks have order at most two.

### Bounding the central block by disjoint witnesses

We use inward orders on both sides: on the right these are the orders in \(\pi^{\mathrm{rev}}\). A first non-tight inward status on the right determines \(c\), exactly as one on the left determines \(p\). This makes the following arguments symmetric.

**Case \(\alpha=\beta=2\).** The families \(\mathcal L,\mathcal R\) consist of two-element sets and are cross-intersecting. Fix \(U\in\mathcal L\) and \(T\in\mathcal R\). Suppose \(b\ge8\). Choose a three-set \(C\subseteq B\setminus T\), and then a three-set
\[
D\subseteq B\setminus(U\cup C).
\]
The second choice is possible because \(|U\cup C|\le5\).

Place \(C\) first in \(B\), in an inward order with its internal triple non-tight. Its first pair avoids \(T\), so that pair is not a member of \(\mathcal L\), whatever left outside orders are used. Thus the status at \(s\) is tight, and the internal status at \(s+1\) is non-tight: \(p=s+1\). Place \(D\) at the right end, likewise with its inward internal triple non-tight. Its first inward pair avoids \(U\), so \(c=s+1\). The two placements are disjoint, producing a zero root. Hence \(b\le7\).

**Case \(\alpha=1,\beta=2\).** Let \(A\subseteq B\) be the nonempty set of singleton left witnesses and choose \(a\in A\). Every member of \(\mathcal R\) contains \(a\).

Suppose \(b\ge6\). Any three-set in \(B\setminus\{a\}\), placed inward at the right end with its internal triple non-tight, gives \(c=s+1\): its first pair cannot belong to \(\mathcal R\). Coordinate recurrence therefore supplies a chamber with \(p=s+1\).

Retain the first two \(B\)-vertices, in their order, and the left outside orders of this witness; denote their support by \(U\). They determine \(p=s+1\), because \(\ell=s+1\). Choose a three-set in
\[
B\setminus(U\cup\{a\}),
\]
which is possible for \(b\ge6\). Place it inward at the right end with non-tight internal triple. This again gives \(c=s+1\), independently of the left witness, a contradiction. Thus \(b\le5\). The case \(\alpha=2,\beta=1\) is symmetric.

**Case \(\alpha=\beta=1\).** Cross-intersection of the two nonempty singleton families implies that both are \(\{\{z\}\}\) for one vertex \(z\in B\). A witness for \(p=s\) must therefore start \(B\) with \(z\), and a witness for \(c=s\) must end \(B\) with \(z\). We do not assert that every choice of outside orders realizes either witness. Whenever the first \(B\)-vertex is different from \(z\), the status at \(s\) is tight for every outside order.

Define \(\mathcal L'\) to consist of supports of ordered pairs that occur as the first two \(B\)-vertices in some chamber with \(p=s+1\). Define \(\mathcal R'\) analogously for \(c=s+1\). Coordinate recurrence implies that either both families are empty or both are nonempty.

If both are empty and \(b\ge6\), choose disjoint three-sets at the two ends of \(B\). Order each inward so that its first vertex is not \(z\) and its internal triple is non-tight. This is always possible: if the set contains \(z\), put \(z\) in the middle and choose the appropriate order of the other two vertices. The statuses at \(s\) are tight; the statuses at \(s+1\) are tight because the pair families are empty; and the internal statuses at \(s+2\) are non-tight. Hence \(p=c=s+2\), a contradiction.

If both families are nonempty, they are cross-intersecting: disjoint ordered witnesses for \(p=c=s+1\) could again be combined with independent outside orders. Fix \(U\in\mathcal L'\) and \(T\in\mathcal R'\). If \(b\ge8\), choose disjoint three-sets
\[
C\subseteq B\setminus T,\qquad D\subseteq B\setminus U
\]
as in the first case. Order them inward with first vertex different from \(z\) and internal triple non-tight. The statuses at \(s\) are tight. Their first pairs avoid respectively \(T,U\), so cross-intersection excludes membership in \(\mathcal L',\mathcal R'\); the statuses at \(s+1\) are therefore tight for every outside order. Consequently \(p=c=s+2\), again a contradiction. Thus \(b\le7\).

This proves all three bounds in the table. Finally
\[
p+c\le m-1=2s+L-1,\qquad p,c\ge s
\]
gives \(p,c\le s+L-1\), completing the theorem.

### A finite reduction of the nonzero-cycle branch

Translate every coordinate by \(-s\). The exact-root digraph then uses at most seven coordinates, and every simple directed cycle has length at most seven.

There is also a bounded description in terms of actual vertices. Keep \(B\) and the complete outside blocks meeting the last two positions before \(B\) or the first two positions after it. Because exterior blocks have order at most two, at most three vertices are retained on either side. Thus at most
\[
7+3+3=13
\]
actual vertices affect the varying exact-root labels.

To verify this, the uniform statuses before \(s\) make those earlier tests irrelevant. The first potentially non-tight window on either side begins no earlier than two positions before \(B\). Moreover
\[
p\le n-s-3\le n-r-2,
\]
so the first non-tight window on the left ends within \(B\); the symmetric statement holds on the right. Hence all determining triples use the retained vertices. Orders of all other blocks may be fixed arbitrarily without changing the attainable root labels. Coordinate recurrence is preserved.

This is a uniform finite reduction of the nonzero exact-root face geometry. It does not identify the retained induced tournament as a counterexample, and it does not reduce the grand conjecture to tournaments of order thirteen.

If \(k=\kappa_2(H)>0\), a chamber with \(p=s\) satisfies
\[
k\le\delta(\pi)\le L-1\le6.
\]
Consequently a positive exact-root carrier in a tournament with \(k\ge7\) must contain a zero-root chamber.

### The remaining conversion

For a positively balanced exact-root face whose chambers all have positive deficiency, the proved alternative is now:
\[
\text{a chamber with }p=c
\quad\text{or}\quad
\text{the bounded central-block configuration above}.
\]
A zero root gives equally long canonical tight paths but may leave a nonempty hole. The bounded alternative likewise gives no spanning cover by itself. Neither branch can therefore be declared closed as a proof of the grand conjecture.

The new reduction uses the full ordered-partition freedom and coordinate recurrence. It repairs the earlier unjustified identification of the central block with its guaranteed corridor: their sizes need not be equal, but the exact determining windows restrict the surplus to zero, one, or two, and the case analysis bounds the entire block.


### Sharpening the central block bound to four

The preceding bound can be strengthened by using two-cover certificates as well as zero-root certificates. Keep its notation. Read the right side inward, so that its first non-tight coordinate is \(c\).

**Lemma (disjoint nonedges on five vertices).** Let \(E,F\) be nonempty families of two-element subsets of a five-element set, and suppose every member of \(E\) meets every member of \(F\). Then there are disjoint pairs \(e\notin E\), \(f\notin F\).

**Proof.** If not, for every two disjoint pairs \(e,f\), exactly one of \(e\in E\) and \(f\in F\) holds: both are excluded by cross-intersection, and neither is excluded by the supposition. Any two pairs sharing a vertex have a common disjoint pair, namely the remaining two vertices. Consequently membership in \(E\) is the same for any two pairs sharing a vertex. The line graph of the complete graph is connected, so \(E\) is either empty or all pairs. The first contradicts its nonemptiness, and the second forces \(F\) to be empty. \(\square\)

**Lemma (two triples on six vertices).** Let \(E,F\) be nonempty cross-intersecting families of pairs on a six-element set \(W\). Either there is a partition \(W=C\sqcup D\), with \(|C|=|D|=3\), such that
\[
|E\cap\binom C2|\le1,\qquad |F\cap\binom D2|\le1,
\]
or \(E\) and \(F\) are both the full star at the same vertex.

**Proof.** By symmetry, a family with at most two pairs may be taken to be \(F\). If \(F\) is one pair, put that pair in \(D\); its complement \(C\) contains no \(E\)-pair. If \(F\) consists of two disjoint pairs, every \(E\)-pair lies in their four-element union. Put the two remaining vertices and one vertex of that union in \(C\). If \(F=\{\{z,a\},\{z,b\}\}\), every \(E\)-pair either contains \(z\) or equals \(\{a,b\}\). Put \(z,a\) and one vertex outside \(\{z,a,b\}\) in \(D\). In each case the required inequalities follow.

Assume both families have at least three pairs. If one contains two disjoint pairs, the other is supported on their four-element union and is a subgraph of \(K_{2,2}\). With at least three edges it also contains disjoint pairs, so both families are supported on the same four vertices. Put two of those vertices and one exterior vertex in each triple.

Otherwise both families are pairwise intersecting. A pairwise-intersecting graph is a star or a triangle. If one is a triangle, the other must be that triangle, and splitting its vertices one versus two suffices. If both are stars, cross-intersection and their having at least three edges force a common center. Unless both stars are full, put the center and a missing neighbor in the triple assigned to a nonfull star, together with any other vertex. That triple contains at most one edge of its assigned star, while the other triple avoids the center. \(\square\)

Whenever a triple contains at most one forbidden pair, its two remaining pair edges have a common vertex. Use that vertex as the middle. Both reverse orders then have permitted first pairs, and boundary antisymmetry lets us choose either internal status.

**Theorem (four central vertices and the remaining cases).** Under the hypotheses of the bounded-central-block theorem, only the following cases can occur:
\[
\begin{array}{c|c|c}
(\ell,r)&|B|&L\\ \hline
(s+1,s+1)&2\text{ or }4&2\text{ or }4\\
(s+1,s)\text{ or }(s,s+1)&3&2.
\end{array}
\]
Thus the complete central block has at most four vertices. All varying root coordinates lie in \(\{s,s+1,s+2,s+3\}\), and at most ten actual vertices determine the root labels.

**Proof.** We give the exclusions in decreasing block size.

For \(\alpha=\beta=2\), use the pair families \(E=\mathcal L,F=\mathcal R\) at coordinate \(s\). For \(\alpha=\beta=1\), use \(E=\mathcal L',F=\mathcal R'\) at coordinate \(s+1\), with the distinguished singleton witness \(z\) from the preceding proof. In the latter case the two pair families are simultaneously empty or nonempty by coordinate recurrence. In either case, disjoint witnesses would give a zero root, so nonempty pair families are cross-intersecting.

**Seven vertices.** If the pair families are empty, two disjoint triples with non-tight internal status give a zero root, arranging \(z\) in the middle of its triple when necessary. Otherwise choose \(U\in E,T\in F\). If \(U\ne T\), they intersect in one vertex. There are disjoint triples \(C\subseteq B\setminus T\), \(D\subseteq B\setminus U\): put the unique vertex of \(U\setminus T\) in \(C\), the unique vertex of \(T\setminus U\) in \(D\), and split the four vertices outside \(U\cup T\) two and two. Their first pairs cannot be forbidden. Choose non-tight internal statuses to obtain \(p=c=s+1\) when \(\alpha=\beta=2\), or \(p=c=s+2\) when \(\alpha=\beta=1\). In the latter case make the first vertex different from \(z\), placing \(z\) in the middle if present.

If no unequal \(U,T\) exist, both families consist of the same single pair. Choose disjoint triples which separate the two vertices of that pair; each triple then has no forbidden pair. The same construction applies. Thus seven vertices are impossible.

**Six vertices.** Empty pair families again immediately give a zero root. Otherwise apply the six-vertex lemma. For \(\alpha=\beta=2\), a partition into two triples containing at most one forbidden pair each permits both internal statuses to be chosen non-tight; this gives \(p=c=s+1\).

For \(\alpha=\beta=1\), choose the permitted middle in each triple as explained after the lemma. In the triple containing \(z\), choose one of the two reverse orders whose first vertex is not \(z\). Choose the internal status of the other triple to match it. The earlier boundary tests on both sides are tight. If the matched status is non-tight, \(p=c=s+2\). If it is tight, append the two triples to the two inward outside paths. This is a spanning two-cover.

It remains to handle the common full star, at a vertex \(w\). For \(\alpha=\beta=2\), put \(w\) last in one inward triple. Its first pair avoids \(w\), and so do all pairs in the other triple. Match the internal status of the other triple to that of the first: a non-tight match gives a zero root, and a tight match gives a spanning two-cover.

For \(\alpha=\beta=1\), if \(w=z\), again put \(w\) last. If \(w\ne z\), use \((x,z,w)\) as the first inward triple, for any remaining vertex \(x\). Its first vertex is different from \(z\) and its first pair avoids \(w\). The other triple contains neither \(z\) nor \(w\), so both its reverse orders satisfy the boundary tests. Match its internal status to the first triple. The same zero-root or two-cover alternative follows. Thus six vertices are impossible.

**Five vertices, equal outside lengths.** Apply the five-vertex lemma to \(E,F\); if both are empty, simply choose any disjoint pairs. Put the resulting permitted pairs at the two inward ends of \(B\), filling the middle position arbitrarily.

If \(\alpha=\beta=2\), this gives \(p,c\ge s+1\). Here \(L=3\), so positive deficiency forces \(p+c\le2s+2\), and therefore \(p=c=s+1\).

If \(\alpha=\beta=1\), order each pair with first vertex different from \(z\). The tests at \(s\) and \(s+1\) are tight, giving \(p,c\ge s+2\). Here \(L=5\), and positive deficiency forces \(p+c\le2s+4\), so \(p=c=s+2\). Both conclusions contradict the absence of a zero root.

**Five vertices, unequal outside lengths.** By symmetry take \(\alpha=1,\beta=2\). Let \(A\) be the singleton left witness set. Every right witness pair contains all of \(A\), so \(1\le|A|\le2\).

Partition \(B=U\sqcup D\), with \(|U|=2,|D|=3\), so that \(U\) contains a vertex outside \(A\) and \(D\) contains no right witness pair. If \(A=\{z\}\), choose \(D\) avoiding \(z\). If \(A=\{z,w\}\), the right pair family is just \(\{\{z,w\}\}\); choose \(D\) with one of \(z,w\) and two of the three remaining vertices.

Read \(U\) from the left with its first vertex outside \(A\), so the status at \(s\) is tight. Fix any left outside orders and denote by \(\eta\) the status at \(s+1\). At the right, every order of \(D\) passes the boundary test at \(s\); choose its internal status to equal \(\eta\). If \(\eta=0\), the roots have \(p=c=s+1\). If \(\eta=1\), the outside paths extended by \(U,D\) form a spanning two-cover. Thus this case is impossible.

**Four vertices, unequal outside lengths.** Again take \(\alpha=1,\beta=2\). If \(A=\{z\}\), put two vertices other than \(z\) at the inward right end; put the remaining vertex other than \(z\) first at the left. If \(A=\{z,w\}\), put one vertex of \(A\) and one vertex outside \(A\) at the right, and start the remaining left pair with its vertex outside \(A\). In either case the first test on each side is tight, so \(p,c\ge s+1\). Since \(L=3\), positive deficiency forces \(p=c=s+1\), a contradiction.

**Four vertices with \(\alpha=\beta=2\).** Let \(E,F\) be the two boundary pair families. Any tight order of three \(B\)-vertices whose first pair is absent from \(E\) could be appended to the left outside path; the remaining \(B\)-vertex can be appended to the right outside path because all earlier statuses are uniformly tight. This would be a two-cover. The same argument applies with \(F\) on the right. Hence the first pair of every tight ordered triple of \(B\) belongs to
\[
G=E\cap F.
\]
For each middle vertex \(y\) and distinct endpoints \(x,z\), at least one of \(\{x,y\},\{y,z\}\) must therefore belong to \(G\), by boundary antisymmetry. The complement of \(G\) has maximum degree at most one, so \(G\) has at least four edges on the four vertices. But cross-intersection of \(E,F\) makes \(G\) pairwise intersecting, and a pairwise-intersecting graph on four vertices has at most three edges. This is a contradiction.

Since \(L\ge2\), these exclusions leave only \(b=3\) in the unequal-length case and \(b\in\{2,3,4\}\) when \(\alpha=\beta=1\).

**Three vertices with \(\alpha=\beta=1\).** Place the distinguished singleton witness \(z\) in the middle of \(B\). Both first tests are tight, so \(p,c\ge s+1\). Now \(L=3\); positive deficiency forces \(p=c=s+1\), a contradiction.

This proves the table. The coordinate bound follows from \(p,c\le s+L-1\). The earlier determining-block argument retains at most three exterior vertices on either side, so at most \(4+3+3=10\) actual vertices determine all varying roots. \(\square\)

### The distinguished vertex in the three-vertex case

In the unequal-length case, take \(\alpha=1,\beta=2\) by symmetry and retain the singleton witness set \(A\). It cannot have two vertices. If it did, let \(u\) be the third vertex of \(B\). The right pair family would be the unique pair \(A\). Choose a tight order of \(B\) with middle vertex \(u\); its first pair is not \(A\). The whole triple can then be appended to the right outside path, giving a two-cover together with the left outside path.

Hence \(A=\{z\}\). Both pairs incident with \(z\) must occur in the right witness family. Otherwise start \(B\) on the left with the remaining vertex different from \(z\), and put the missing right pair at the inward right end. This gives \(p,c\ge s+1\), incompatible with positive deficiency when \(L=2\). Thus the right pair family is the full star at \(z\).

Accordingly every remaining nonzero case has a distinguished actual vertex: in the two- and four-vertex cases both singleton witness families equal \(\{\{z\}\}\); in the three-vertex case one singleton family equals \(\{\{z\}\}\), and the opposite pair family is the full star at \(z\). These are statements about attainable witness supports, not assertions that every outside order realizes every witness.

Finally, if \(k=\kappa_2(H)>0\), a chamber with \(p=s\) has
\[
k\le\delta(\pi)\le L-1\le3.
\]
Thus for \(k\ge4\), every positively balanced exact-root carrier must contain a zero-root chamber. For general \(k\), the theorem reduces the nonzero branch to the three configurations in the table. Converting these configurations, or a zero-root chamber with a nonempty hole, into a spanning two-cover remains open.


### Only two- and three-cycles remain

Suppose in addition that every occurring exact root lies on a directed cycle, as it does under positive carrier balance. After subtracting \(s\) from the coordinates, every arc \(i\to j\) satisfies
\[
0\le i,j\le3,\qquad i\ne j,\qquad i+j\le3.
\]
Its underlying unordered pair is therefore one of
\[
\{0,1\},\ \{0,2\},\ \{0,3\},\ \{1,2\}.
\]
This graph is a triangle on \(0,1,2\) with one additional edge \(0\,3\). Consequently every simple directed cycle has length two or three, and every occurring arc lies on such a cycle. In particular, an arc using coordinate \(3\) forces its opposite arc. Thus the original coordinated-cycle question, away from zero roots, has no long-cycle case.


### Corollary: deletion distance at least two forces a zero exact root

Let
\[
k=\kappa_2(H)\ge2,
\]
and let \(F\) be a positively balanced exact-root carrier face. Then \(F\) contains a chamber with
\[
p=c.
\]

**Proof.**
Suppose not. Every chamber has positive deficiency, the occurring tail and head coordinate sets agree by positive exact-root circulation, and no chamber has zero root. The preceding four-central-vertices theorem therefore leaves only three possible nonzero configurations:
\[
(\ell,r,|B|,L)
=
(s+1,s+1,2,2),\quad
(s+1,s+1,4,4),
\]
or, up to left-right symmetry,
\[
(s+1,s,3,2).
\]

In either \(L=2\) case, a chamber with \(p=s\) has
\[
\delta\le L-1=1,
\]
contradicting the global lower bound
\[
\delta\ge\kappa_2(H)=k\ge2.
\]

It remains that
\[
\ell=r=s+1,\qquad |B|=L=4.
\]
The preceding distinguished-vertex conclusion gives one vertex \(z\in B\) such that every \(p=s\) witness starts \(B\) with \(z\), and every \(c=s\) witness ends \(B\) with \(z\). Choose a chamber whose first and last vertices of \(B\) are both different from \(z\). Then
\[
p,c\ge s+1.
\]
Since
\[
m=2s+4
\]
and every chamber has deficiency at least \(k\ge2\),
\[
2
\le
\delta
=
m-p-c
\le
(2s+4)-2(s+1)
=
2.
\]
Hence equality holds throughout:
\[
p=c=s+1,
\]
contradicting the assumption that \(F\) has no zero root. \(\square\)

Thus
\[
\boxed{
\kappa_2(H)\ge2
\quad\Longrightarrow\quad
\text{every positive exact-root carrier contains an actual balanced chamber }p=c.
}
\]

This conclusion is global and structural. It uses neither minimum-counterexample induction nor disturbance analysis. The remaining problem in the \(k\ge2\) branch is no longer recurrence without a diagonal; it is to exploit a balanced canonical partial two-cover
\[
P_\pi\mid X_\pi\mid Q_\pi,
\qquad
|P_\pi|=|Q_\pi|,
\qquad
|X_\pi|=\delta(\pi)\ge k,
\]
and, ideally, force one with \(|X_\pi|=k\).


## Frontier

- Development version when composed: None
- Development version now: 4
