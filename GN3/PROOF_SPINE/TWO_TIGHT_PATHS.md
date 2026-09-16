# Two tight paths in a boundary tournament

**Reauthored research draft — 16 September 2026.** Based on the four GN3 files at commit `9ae9f366b69ebb3d394a57708e76bfd4ce77e9cf`. The theorem remains open. This is new mathematical text for independent review, not an assertion of inherited certification. The three finite lemmas in §2 and the two operations in §4 are explicit inputs from the supplied spine; their proofs were not supplied there. All other arguments needed below are included. A correspondence with the source statements appears at the end.

## 1. The problem and its elementary reduction

A **boundary tournament** on a finite vertex set assigns to each ordered triple of distinct vertices a truth value, called tightness, such that exactly one of
\[
(x,y,z),\qquad (z,y,x)
\]
is tight. Equivalently, for each vertex \(y\), the relation \(x\to_y z\) defined by tightness of \((x,y,z)\) is a tournament on the other vertices. No transitivity assumption is imposed on these tournaments.

A **tight path** is an ordered list of distinct vertices whose consecutive triples are tight. Singletons and ordered pairs are paths. The order \(|P|\) of a path is its number of vertices. Its ordinary edges are its consecutive unordered pairs; when an edge's direction matters, its order along the path will be stated. A **tight cycle** is a cyclic ordering of at least three distinct vertices in which every cyclic consecutive triple is tight. Deleting any one cycle edge gives a tight path on the same vertices.

A **path cover** is a partition of the vertex set into tight paths. Write \(\operatorname{pc}(G)\) for its minimum size, and use \(P|Q\) to denote disjoint path components. A Hamilton path uses every vertex of its specified induced subgraph. A proper path in \(H\) omits at least one vertex of \(H\).

**Conjecture.** Every finite boundary tournament has a path cover of size at most two.

Suppose otherwise, and fix a counterexample \(H\) of minimum order \(n\). Every proper induced subgraph has a cover by at most two paths. Adding a deleted vertex as a singleton therefore gives
\[
\operatorname{pc}(H)=3.
\]
All subsequent assertions about \(H\) use this hypothesis.

### Lemma 1.1. Complements of paths

If a nonempty proper set \(S\subset V(H)\) has a Hamilton tight path, then
\[
\operatorname{pc}(H-S)=2.
\]
Consequently every proper tight path can be completed to a spanning three-path cover.

**Proof.** Minimality gives a cover of \(H-S\) by at most two paths. A Hamilton path there would combine with the path on \(S\) to cover \(H\) by two paths. ∎

### Lemma 1.2. Deleting two vertices

For distinct \(a,c\), every minimum path cover of \(H-\{a,c\}\) consists of two nontrivial paths.

**Proof.** Lemma 1.1 applies to the path \((a,c)\). If one component of a two-path cover were the singleton \((s)\), order \(\{a,s,c\}\) as a tight path and retain the other component. This would cover \(H\) by two paths. ∎

Every spanning three-path cover has exactly \(n-3\) ordinary edges. This number is maximal among spanning forests whose components are tight paths, because a forest with more edges would have at most two components. Thus edge maximality adds no further restriction to a spanning three-path cover of \(H\).

## 2. The order of a smallest counterexample

We use the following three finite lemmas as supplied inputs.

**Input 2.1.** If \(P\) is a tight three-vertex path and \(x,y,z\) are distinct vertices outside it, at least one of
\[
V(P)\cup\{x,y\},\quad V(P)\cup\{x,z\},\quad V(P)\cup\{y,z\}
\]
has a Hamilton tight path. Every six-vertex set contains at least four Hamiltonian five-subsets.

**Input 2.2.** A five-vertex set contains at most three four-subsets without Hamilton tight paths.

**Input 2.3.** Let \(\Omega\) have ten elements, and let \(\mathcal F\subseteq\binom{\Omega}{5}\) contain no complementary pair. Set
\[
\overline{\mathcal F}=\{\Omega-A:A\in\mathcal F\}.
\]
In the Johnson graph \(J(10,5)\), whose adjacent sets intersect in four elements,
\[
e(\mathcal F,\overline{\mathcal F})\le15|\mathcal F|.
\]

### Theorem 2.4

\(n>10\).

**Proof.** Every set of at most three vertices has a tight Hamilton path, so every set of at most six vertices has a two-path cover. For orders seven and eight, Input 2.1 supplies a five-vertex path; its complement has at most three vertices and is Hamiltonian.

Suppose \(n=9\). Let \(\mathcal F_5\) be the Hamiltonian five-subsets and \(\mathcal B_4\) the non-Hamiltonian four-subsets. Counting incidences with six-sets and five-sets, respectively, gives
\[
4|\mathcal F_5|\ge4\binom96,
\qquad
5|\mathcal B_4|\le3\binom95.
\]
Thus \(|\mathcal F_5|\ge84\), whereas \(|\mathcal B_4|\le75\). The complement of every member of \(\mathcal F_5\) belongs to \(\mathcal B_4\), a contradiction.

Suppose \(n=10\), and let \(\mathcal F\) be the Hamiltonian five-subsets. This family is nonempty by Input 2.1 and has no complementary pair. Fix \(A\in\mathcal F\), put \(E=V(H)-A\), and fix \(a\in A\). For \(z\in E\), define
\[
B_z=(E-\{z\})\cup\{a\}.
\]
At most one \(B_z\) is non-Hamiltonian. Indeed, if \(B_x,B_y\) were both non-Hamiltonian, order \(E-\{x,y\}\) as a tight three-vertex path and apply Input 2.1 with outside vertices \(x,y,a\). One of \(E,B_x,B_y\) would be Hamiltonian, which is impossible.

For each of the five choices of \(a\), at least four sets \(B_z\) therefore belong to \(\mathcal F\). Their complements
\[
(A-\{a\})\cup\{z\}
\]
are twenty distinct neighbors of \(A\) in \(\overline{\mathcal F}\). Consequently
\[
e(\mathcal F,\overline{\mathcal F})\ge20|\mathcal F|,
\]
contrary to Input 2.3. ∎

The ten-vertex argument uses no assumption on the minimum intersection of two members of \(\mathcal F\).

## 3. Longest paths and endpoint transfers

Let \(A|B|C\) be a spanning three-path cover. If \(x\) is an endpoint of a component other than \(A=(v_0,\ldots,v_{\ell-1})\), an **endpoint transfer** removes \(x\) from that component and appends or prepends it to \(A\), provided the resulting order is tight. Deleting an endpoint leaves the donor's remaining order unchanged. If the donor is a singleton, such a transfer gives a two-path cover.

For \(\ell\ge2\), appending \(x\) requires just \((v_{\ell-2},v_{\ell-1},x)\) to be tight, and prepending it requires just \((x,v_0,v_1)\) to be tight.

### Proposition 3.1. Finite endpoint improvement

Start from any spanning three-path cover and choose a longest component \(A\). Successively transfer endpoints into \(A\) whenever possible. Every nonclosing transfer increases \(|A|\) by one, and \(A\) remains a longest component. The process terminates either with a two-path cover or with a three-path cover in which no endpoint can be transferred into \(A\).

In particular, for any integer \(M\), one may stop either when a component exceeds \(M\), when a two-path cover appears, or at such a terminal cover. This applies after completing any prescribed proper tight path by Lemma 1.1.

**Proof.** A nonclosing transfer increases the recipient and decreases only the donor. Thus the chosen component remains longest, and its order strictly increases. There can be only finitely many transfers. ∎

If \(M\) is the largest component order in a prescribed finite family of spanning three-path covers, this gives precisely the threshold comparison with that family. It does not assert that the terminal output has a component of order at least \(M\).

### Proposition 3.2. The ends of a terminal longest component

Suppose \(A|B|C\) is terminal for transfers into its longest component \(A=(v_0,\ldots,v_{\ell-1})\). Then \(\ell\ge4\), at least one of \(B,C\) is nontrivial, and for every endpoint \(x\) of either other component,
\[
(x,v_{\ell-1},v_{\ell-2}),
\qquad
(v_1,v_0,x)
\tag{3.1}
\]
are tight.

**Proof.** Since \(n>10\), the longest of three spanning components has order at least four. If \(B,C\) were both singletons, their two vertices could be combined into one path. The two possible extensions of \(A\) by \(x\) are forbidden; boundary antisymmetry gives (3.1). ∎

In particular the two reversed ordered end pairs
\[
(v_{\ell-1},v_{\ell-2}),\qquad(v_1,v_0)
\]
are disjoint, and (3.1) gives their specified left and right extensions. No case with a longest component of order three is possible here.

### Proposition 3.3. A globally longest component

There is a spanning three-path cover whose longest component is a globally longest tight path of \(H\). It satisfies Proposition 3.2.

**Proof.** Complete a globally longest path using Lemma 1.1. Any endpoint transfer into it would produce a longer tight path. ∎

## 4. A fixed pair and retained path extensions

Fix distinct vertices \(a,c\), and partition the remaining vertices as
\[
X=\{s:(a,s,c)\text{ is tight}\},
\qquad
Y=\{s:(c,s,a)\text{ is tight}\}.
\]
For \(s\in X\), put \(L_s=(a,s)\), \(R_s=(s,c)\); for \(s\in Y\), put \(L_s=(c,s)\), \(R_s=(s,a)\).

An **end-extension record** consists of an ordered tight path \(P\), a vertex \(w\notin V(P)\), and a choice of left or right, such that \((w,P)\) or \((P,w)\), respectively, is tight. The record identifies the vertex \(w\) and the extension side. The relevant end of \(P\) is its first vertex for a left extension and its last vertex for a right extension.

The source triple at every \(s\) gives a right-extension record for \(L_s\) and a left-extension record for \(R_s\). All these paths and records are retained. They need not be components of the path system currently under consideration.

To preserve the exact historical content of this part of the supplied argument, consider pairs consisting of (i) a current system of disjoint tight paths and (ii) retained extension records and their derivations. Neither spanning nor a fixed number of current components is assumed. The following operations are supplied inputs, not consequences of the definition of a path system.

**Input 4.1.** If two disjoint two-vertex paths have retained extension records, one on the left and the other on the right, then, for either prescribed vertex \(x\) of the first path, an allowed finite sequence of operations produces either a spanning two-path cover or a current system containing singleton components \((x),(q)\). All prior records remain available.

**Input 4.2.** From a current system containing \((x),(q)\), for any prescribed \(y\notin\{x,q\}\), an allowed finite sequence produces either a spanning two-path cover or a current system containing \((x),(y)\). All prior records remain available.

Thus, for arbitrary prescribed vertices in the two disjoint paths of Input 4.1, one can obtain both as singleton components: apply Input 4.1 to the first prescribed vertex and then, if necessary, Input 4.2 to the second.

The only additional operation required for the next theorem is the following elementary restriction of a retained path. Adding its conclusion to the records changes no current component.

### Lemma 4.3. Restricting an extended path

Suppose \((w,v_0,\ldots,v_k)\) is tight and a path \(Q\) meets \((v_0,\ldots,v_k)\) but avoids \(v_0\). If \(i\) is the least index for which \(v_i\in V(Q)\), then
\[
(v_0,\ldots,v_{i-1})
\]
is a nonempty proper subpath, is disjoint from \(Q\), and still has left-extension vertex \(w\). The corresponding assertion for a right extension retains the suffix after the last intersection.

**Proof.** The retained extension is a contiguous subpath of the original extended path. The choice of the first, or last, intersection gives disjointness. ∎

When this restriction is recorded, retain the original path, the path \(Q\) used for the intersection, the restricted subpath, the extension vertex, and the extension side. This records the derivation as well as the resulting tight path.

### Theorem 4.4. Simultaneous restrictions at every remaining vertex

There is an allowed finite sequence producing either a spanning two-path cover or a current system containing \((a),(c)\) with the following two retained restrictions for **every** \(s\notin\{a,c\}\):

| Orientation at \(s\) | Retained original path | Current singleton used | Restricted path | Inherited extension |
| --- | --- | --- | --- | --- |
| \(s\in X\) | \((a,s)\) | \((a)\) | \((s)\) | right, by \(c\) |
| \(s\in X\) | \((s,c)\) | \((c)\) | \((s)\) | left, by \(a\) |
| \(s\in Y\) | \((c,s)\) | \((c)\) | \((s)\) | right, by \(a\) |
| \(s\in Y\) | \((s,a)\) | \((a)\) | \((s)\) | left, by \(c\) |

All incoming records persist.

**Proof.** Since \(|X|+|Y|=n-2\ge9\), one class has at least two vertices. Interchange \(a,c\) for the construction if necessary, and choose distinct \(s,t\in X\). The paths \((a,s)\) and \((t,c)\) are disjoint and have right and left extensions, respectively. Inputs 4.1–4.2 give the current singleton pair \((a),(c)\), unless a two-path cover has already appeared.

Keep this current system fixed. Apply Lemma 4.3 to each original two-vertex path using the appropriate one of these two singleton components. These are exactly the four cases in the table. Each application adds a record and leaves the current system unchanged, so all applications can be made in the same finite sequence. ∎

In the notation \(C_{a,c}\) for vertices with both recorded restrictions, the conclusion is therefore
\[
C_{a,c}=V(H)-\{a,c\}.
\tag{4.1}
\]
In particular any two disjoint two-vertex paths have at least two of their four vertices in \(C_{a,c}\); if their vertices all avoid \(a,c\), all four belong to it.

The restricted singleton is a retained path with a specified derivation. It is not asserted to be a current component. Equally, the presence of the current components \((a),(c)\) does not imply that the other current components form one or two paths.

### Proposition 4.5. An explicit contact away from the fixed pair

Let \(s\in X\) and \(u\notin\{a,s,c\}\).

* For \(Q=(s,u)\), either \((a,s,u)\) is tight, or \((u,s,a)\) is tight.
* For \(Q=(u,s)\), either \((u,s,c)\) is tight, or \((c,s,u)\) is tight.

In the first alternative in each row, the three-vertex path contains both \(Q\) and the indicated original two-vertex path as ordered subpaths. In the second alternative it traverses both of those edges in the opposite order. The same statements hold for \(s\in Y\) after interchanging \(a,c\).

**Proof.** Apply boundary antisymmetry to the two displayed reversal pairs. ∎

This records an actual three-vertex path containing \(u\) and the exact ordered edges involved. Its conclusion does not require (4.1). The only two-vertex vertex sets through \(s\) excluded from this statement are \(\{a,s\}\) and \(\{s,c\}\). Neither this proposition nor Theorem 4.4 asserts that these two sets cannot occur again.

### Lemma 4.6. Four vertices of one orientation

If \(S\) consists of four vertices outside \(\{a,c\}\) and \((a,s,c)\) is tight for every \(s\in S\), then some distinct \(x,y,z\in S\) give the tight path
\[
(x,a,y,c,z).
\]

**Proof.** On \(S\), define tournaments \(T_a,T_c\) by the tight triples \((x,a,y)\) and \((x,c,y)\). Suppose no distinct \(x,y,z\) satisfy \(x\to_a y\to_c z\). A vertex of indegree at least two in \(T_a\) must then have outdegree zero in \(T_c\).

The sum of indegrees in \(T_a\) is six, so such a vertex \(y\) exists. It is the unique sink of \(T_c\). Every other vertex has positive outdegree in \(T_c\), hence indegree at most one in \(T_a\). The indegree sum forces \(y\) to have indegree three and the other vertices to have indegree one. Thus \(y\) is also a sink of \(T_a\).

Choose \(v\ne y\). Then \(v\to_c y\). The unique predecessor \(x\) of \(v\) in \(T_a\) is not \(y\), since \(y\) is a sink. Hence \(x\to_a v\to_c y\), a contradiction. The resulting mixed two-edge path supplies the three tight triples of \((x,a,y,c,z)\). ∎

One of \(X,Y\) has at least five vertices. Consequently there is a five-vertex path of the displayed form, or with \(a,c\) interchanged, whose three other vertices all have both restrictions in Theorem 4.4.

## 5. Deletion and comparison of path covers

### Lemma 5.1. Counting components after deletion

Let \(F\) be an ordinary path forest with \(k\) components, including any isolated vertices, and let \(S\subseteq V(F)\). Then
\[
\operatorname{comp}(F-S)
=k+\sum_{v\in S}(\deg_F(v)-1)-e_F(S).
\tag{5.1}
\]
Here \(e_F(S)\) counts edges with both ends in \(S\), and the empty forest has zero components. For an ordered tight-path forest, the remaining components inherit their orders and are tight.

**Proof.** If \(F\) has \(N\) vertices, it has \(N-k\) edges. Deleting \(S\) removes
\(\sum_{v\in S}\deg_F(v)-e_F(S)\) edges. Subtract the remaining edge count from the remaining vertex count. ∎

### Proposition 5.2. One internal deletion suffices for a crossing

Fix \(a,c\), an exact two-path cover \(U|V\) of \(H-\{a,c\}\), and an internal vertex \(s\) of one of its paths. Let \(T\) be any exact two-path cover of \(H-\{a,c,s\}\). Such a cover exists.

Deleting \(s\) from \(U|V\) leaves three nonempty ordered paths. Some edge \(xy\) of \(T\) joins two different such paths. Moreover one may choose an endpoint of this edge, call it \(x\), and a vertex \(h\ne x,y\) so that \(hx\) is an edge of the original \(U|V\). Exactly one of
\[
(h,x,y),\qquad(y,x,h)
\tag{5.2}
\]
is tight.

If a crossed remaining path is nontrivial, \(h\) can be chosen on that path. Otherwise \(h=s\).

**Proof.** The set \(\{a,s,c\}\) has a Hamilton tight path, so Lemma 1.1 gives the stated exact cover \(T\). Deleting the internal vertex \(s\) splits one original path into two nonempty paths and retains the other. If every edge of \(T\) stayed within one of these three vertex sets, its two components could not cover all three sets. Thus a crossing edge exists.

If one of its endpoints belongs to a nontrivial remaining path, take an adjacent vertex \(h\) there. It differs from the other crossing endpoint. Otherwise both crossed paths are singletons. The untouched original component is nontrivial by Lemma 1.2, so these singleton paths are the two pieces created by deleting \(s\). Both are adjacent to \(s\) in the original cover. Take \(h=s\). Boundary antisymmetry gives (5.2). ∎

The conclusion retains the original cover, the deleted vertex, the new cover, the three remaining paths, and the two adjacent edges that produce the tight triple. It is a path on three vertices, not a replacement spanning cover.

### Proposition 5.3. Three internal vertices of one orientation

For any fixed \(a,c\) and exact two-path cover \(U|V\) of \(H-\{a,c\}\), at least five vertices are internal in their paths. Three of them, say \(p,q,r\), have the same orientation through \(a,c\). After interchanging \(a,c\),
\[
(a,p,c),\quad(a,q,c),\quad(a,r,c)
\]
are tight.

**Proof.** There are \(n-2\ge9\) vertices and exactly four endpoints, since both components are nontrivial. Partition the at least five internal vertices into \(X,Y\). ∎

### Proposition 5.4. The eight induced subgraphs

With \(P=\{p,q,r\}\), \(K=\{a,c,p,q,r\}\), and \(W=V(H)-K\), put
\[
G_J=H[W\cup J]\qquad(J\subseteq P).
\]
Then \(K-J\) is Hamiltonian and \(\operatorname{pc}(G_J)=2\) for every \(J\subseteq P\). Every exact two-path cover of \(G_J\), together with a Hamilton path on \(K-J\), gives a spanning three-path cover of \(H\).

**Proof.** Hamiltonicity of \(K\) is the five-vertex lemma proved in Appendix A. With two vertices of \(P\) left, say \(s,t\), exactly one of \((s,c,t)\), \((t,c,s)\) is tight, giving either \((a,s,c,t)\) or \((a,t,c,s)\). With one vertex left, use \((a,s,c)\); with none, use \((a,c)\). Lemma 1.1 now applies to every \(K-J\). ∎

Proposition 5.2, applied to any \(s\in P\), compares the original cover of \(G_P\) directly with any cover of \(G_{P-\{s\}}\). It already gives the proper tight path required by the eight-cover comparison. The other six covers are not needed for that conclusion. They remain available, with the exact complements specified in Proposition 5.4, for stronger comparisons.

For comparisons that depend on differing orders rather than a deleted internal vertex, the separate path-intersection arguments are given in Appendix B. No cycle produced there is treated as a spanning improvement merely because it can be opened into a path.

## 6. The remaining augmentation problem

### 6.1. A finite extremal choice

For a spanning three-path cover \(F\), let
\[
\lambda(F)=(\ell_1,\ell_2,\ell_3),
\qquad \ell_1\ge\ell_2\ge\ell_3,
\]
be its component orders in decreasing order. Choose \(F=A|B|C\) to maximize this triple lexicographically. Such a cover exists because \(H\) is finite. By Lemma 1.1, its first component is a globally longest tight path: every proper tight path belongs to some spanning three-path cover.

No endpoint can be transferred from a component to another component of at least equal order. A transfer from a singleton would give a two-path cover; every other such transfer increases the sorted triple lexicographically. This supplies the endpoint restrictions of Proposition 3.2 for \(A\), and also for transfers from \(C\) into \(B\).

As a small additional consequence, \(|B|\ge3\). If \(|B|\le2\) and \(|C|=1\), the complement of \(A\) has at most three vertices and is Hamiltonian. If \(|B|=|C|=2\), write \(B=(b_0,b_1)\), \(C=(c_0,c_1)\). The forbidden transfers of \(c_0\) to the right of \(B\) and \(c_1\) to its left give
\[
(c_0,b_1,b_0),\qquad(b_1,b_0,c_1)
\]
tight. Thus \((c_0,b_1,b_0,c_1)\), together with \(A\), is a two-path cover.

This extremal choice is a genuine finite comparison of complete covers. It does not assign progress to a local path whose complement has not been accounted for.

### 6.2. Choosing the fixed pair from the other component

Write \(A=(v_0,\ldots,v_{\ell-1})\), and choose a nontrivial component \(X=(x_0,\ldots,x_m)\) among \(B,C\). Set
\[
a=x_0,\qquad c=x_m.
\]
The terminal inequalities give the tight paths
\[
(a,v_{\ell-1},v_{\ell-2}),\qquad(v_1,v_0,c).
\tag{6.1}
\]
Apply Theorem 4.4 for this same pair \(a,c\). All four vertices in the two reversed end pairs of \(A\) have both retained singleton restrictions. Both two-vertex end sets avoid \(a,c\), so Proposition 4.5 applies at **each** of their vertices, after choosing the appropriate orientation class.

These are simultaneous statements about paths and derivations in \(H\). The fixed-pair operations are not asserted to preserve \(A|B|C\) as their current path system.

This avoids the two exceptional vertex sets in Proposition 4.5 at the chosen end pairs. The remaining difficulty is therefore already present in its ordinary three-vertex outcomes: they do not by themselves enlarge \(A\), preserve \(|A|\) while improving another component, or join all vertices into two paths.

### 6.3. The exact missing implication

A sufficient augmentation statement is the following.

**Proposed lemma — not proved.** Let \(H\) be a smallest counterexample and \(F\) a spanning three-path cover to which no endpoint transfer from a component to one of at least equal order is possible. Then there exists a spanning two-path cover, or a spanning three-path cover \(F'\) with
\[
\lambda(F')>_{\mathrm{lex}}\lambda(F).
\tag{6.2}
\]

This would contradict the extremal choice in §6.1. It allows an improvement of the second component while preserving the largest order, so it asks less of the replacement than requiring a strictly longer largest path at every step. Since the component orders sum to \(n\), only the first two coordinates are needed.

The established lemmas do not yet prove (6.2). In particular:

* A three-vertex contact in §4 or §5 comes with specified edges, but not with a replacement cover having a favorable component-order triple.
* Completing a new proper path by Lemma 1.1 may lose the former long component. Proposition 3.1 controls transfers only after that completion.
* The records in §4 preserve actual ordered paths, extension vertices, sides, and derivations. They do not forbid those same paths from being used again. After Theorem 4.4 there are no further vertices to count as newly restricted.

A concrete construction of \(F'\) must specify the retained subpaths, the inserted edges, all tight triples at joins, vertex-disjointness, and the disposition of every vertex. Formula (5.1) determines exactly how many components a deletion creates. For example, deleting one internal vertex from a two-path cover creates three components; adjoining a separate three-vertex path on that vertex and the fixed pair produces four components, not a spanning three-path cover. A crossing edge and its associated tight triple cannot be substituted for the missing joins.

The next mathematical target is to use the full incidence data in (6.1), the restrictions in Theorem 4.4, or the deletion comparison in Proposition 5.2 to make such a replacement. The currently proved reduction stops here.

## Appendix A. Five vertices with three equal orientations

**Lemma.** If \(a,c,p,q,r\) are distinct and \((a,p,c),(a,q,c),(a,r,c)\) are tight, then their five-set has a Hamilton tight path.

**Proof.** On \(P=\{p,q,r\}\), define tournaments \(\to_a,\to_c\) using tightness of \((x,a,y)\), \((x,c,y)\). If \(x\to_a y\to_c z\) for distinct \(x,y,z\), then \((x,a,y,c,z)\) is the required path. Assume no such triple exists.

The tournament \(\to_a\) cannot be transitive: if \(x\to_a y\to_a z\) and \(x\to_a z\), excluding the mixed chains through \(y\) and through \(z\) forces both \(z\to_c y\) and \(y\to_c z\). Thus, after relabelling,
\[
p\to_a q\to_a r\to_a p.
\]
Excluding the three mixed chains forces
\[
r\to_c q,\quad p\to_c r,\quad q\to_c p.
\]

Suppose the five-set is not Hamiltonian. In each row below, all consecutive triples of the candidate word except the reversal of the displayed triple are already tight. Non-Hamiltonicity therefore forces the displayed triple to be tight.

| Candidate word | Forced tight triple |
| --- | --- |
| \(a\ p\ c\ r\ q\) | \((q,r,c)\) |
| \(a\ q\ c\ p\ r\) | \((r,p,c)\) |
| \(a\ r\ c\ q\ p\) | \((p,q,c)\) |
| \(p\ q\ a\ r\ c\) | \((a,q,p)\) |
| \(q\ r\ a\ p\ c\) | \((a,r,q)\) |
| \(r\ p\ a\ q\ c\) | \((a,p,r)\) |

Using those triples gives six further implications of the same form:

| Candidate word | Forced tight triple |
| --- | --- |
| \(a\ p\ r\ c\ q\) | \((c,r,p)\) |
| \(a\ q\ p\ c\ r\) | \((c,p,q)\) |
| \(a\ r\ q\ c\ p\) | \((c,q,r)\) |
| \(p\ a\ q\ r\ c\) | \((r,q,a)\) |
| \(q\ a\ r\ p\ c\) | \((p,r,a)\) |
| \(r\ a\ p\ q\ c\) | \((q,p,a)\) |

Let \(u,v,w\) be the respective truth values of \((q,p,r),(p,q,r),(p,r,q)\). The following table is exhaustive. In each row, every consecutive triple of the first and second candidates is now tight except, respectively, for the first and second members of the displayed reversal pair.

| \((u,v,w)\) | First candidate | Second candidate | Remaining reversal pair |
| --- | --- | --- | --- |
| \(000\) | \(a\ c\ q\ r\ p\) | \(r\ p\ q\ c\ a\) | \((a,c,q)\) / \((q,c,a)\) |
| \(100\) | \(c\ a\ r\ q\ p\) | \(q\ p\ r\ a\ c\) | \((c,a,r)\) / \((r,a,c)\) |
| \(010\) | \(a\ c\ p\ q\ r\) | \(q\ r\ p\ c\ a\) | \((a,c,p)\) / \((p,c,a)\) |
| \(110\) | \(a\ c\ p\ q\ r\) | \(q\ r\ p\ c\ a\) | \((a,c,p)\) / \((p,c,a)\) |
| \(001\) | \(c\ a\ p\ r\ q\) | \(r\ q\ p\ a\ c\) | \((c,a,p)\) / \((p,a,c)\) |
| \(101\) | \(c\ a\ p\ r\ q\) | \(r\ q\ p\ a\ c\) | \((c,a,p)\) / \((p,a,c)\) |
| \(011\) | \(a\ c\ r\ p\ q\) | \(p\ q\ r\ c\ a\) | \((a,c,r)\) / \((r,c,a)\) |
| \(111\) | \(c\ a\ q\ p\ r\) | \(p\ r\ q\ a\ c\) | \((c,a,q)\) / \((q,a,c)\) |

Boundary antisymmetry makes exactly one of the last two triples tight. The corresponding candidate is Hamiltonian, a contradiction. ∎

## Appendix B. Intersecting ordered paths

The following statements retain the order-sensitive comparisons independently of the shorter deletion argument. A triple **traverses an edge of a path in the opposite order** when two consecutive entries of the triple are the reversal of a consecutive ordered pair in that path. This phrase specifies an ordinary relation between two orders, not an additional kind of tightness.

### Lemma B.1. Reversed order of common vertices

Let \(P=(v_0,\ldots,v_k)\) and \(Q\) be tight paths. Suppose their common vertices do not occur in the same order. Then one can find either:

1. a consecutive ordered pair in \(Q\) reversing one in \(P\);
2. a tight triple, on vertices of \(P\cup Q\), traversing an edge of \(P\) and an edge of \(Q\) in the opposite order;
3. a vertex-simple tight cycle on vertices of \(P\cup Q\).

In particular this applies to two different Hamilton orders on the same vertex set.

**Proof.** Along \(Q\), choose consecutive common vertices \(v_i,v_j\) with \(i>j\), and let \(E\) be the subpath between them. Its interior avoids \(P\). If \(E=(v_i,v_j)\) and \(i=j+1\), the first alternative holds.

Otherwise let \(x\) be the successor of \(v_i\) in \(E\) and \(y\) the predecessor of \(v_j\). Test
\[
(v_{i-1},v_i,x),\qquad(y,v_j,v_{j+1}).
\]
All entries in each triple are distinct; the excluded case is exactly the one that could violate this. A failed test supplies its tight reversal, which reverses the adjacent edges from both paths. If both tests hold, follow \(E\) from \(v_i\) to \(v_j\), then \(P\) from \(v_j\) to \(v_{i-1}\), and close back to \(v_i\). The two tested triples give the joins, and the disjoint interiors make the cycle vertex-simple. ∎

### Lemma B.2. Contact at an extended end

Let \(P=(v_0,\ldots,v_k)\) have left extension \((w,P)\), and let \(Q\) be a tight path containing \(v_0\). Then either \(P=Q=(v_0)\), or there exists:

1. a tight path properly containing \(P\) as an ordered subpath;
2. a tight path properly containing \(Q\) as an ordered subpath;
3. a vertex-simple tight cycle;
4. a tight triple traversing an edge of \(P\) or \(Q\) in the opposite order.

All vertices in the conclusion lie in \(V(P)\cup V(Q)\cup\{w\}\). The right-extension assertion is obtained by the corresponding right-end argument. Together with Lemma 4.3, this covers both positions of an intersection with an end-extended path.

**Proof.** If \(k=0\), either \(Q=(v_0)\) or \(Q\) properly contains \(P\). Assume \(k\ge1\).

If the common vertices of \(P,Q\) occur in different orders, apply Lemma B.1. Its second and third outcomes suffice. For its first outcome, take a tight triple of \(P\) containing the reversed edge; such a triple exists if \(|P|\ge3\). If \(|P|=2\), use the tight triple \((w,P)\). In either case this triple traverses an edge of \(Q\) in the opposite order.

Otherwise \(v_0\) is the first common vertex along \(Q\). If \(Q\) has a predecessor \(u\) of \(v_0\), test \((u,v_0,v_1)\). If it is tight, the prefix of \(Q\) ending at \(v_0\), followed by the rest of \(P\), is a proper extension of \(P\); the prefix has no other vertex of \(P\). If it is not tight, \((v_1,v_0,u)\) is the required reversed triple.

It remains that \(Q\) starts at \(v_0\). If \(Q=(v_0)\), use \((w,v_0)\). Otherwise write its next vertex as \(q_1\). If \(w\notin V(Q)\), testing \((w,v_0,q_1)\) gives either the extension \((w,Q)\) or the tight reversal \((q_1,v_0,w)\).

If \(w\in V(Q)\), the common vertices of \((w,P)\) and \(Q\) occur in different orders, since their orders on \(w,v_0\) differ. Apply Lemma B.1 to these two paths. A failed test in its proof reverses an edge of \(Q\), and a cycle suffices. If it gives a reversed common edge instead, a tight triple of \((w,P)\) containing that edge exists because \(|(w,P)|\ge3\); it reverses an edge of \(Q\). ∎

Within the smallest counterexample, any tight cycle obtained here omits vertices of \(H\): a spanning tight cycle could be opened into a Hamilton path. Opening a cycle preserves its vertex set, not any prior covering of the complement.

## Correspondence and review notes

The mathematical development above is intended to replace the three supplied proof-spine files as one sequential draft. This table records where their conclusions remain available.

| Supplied statement | Location here | Change |
| --- | --- | --- |
| Preliminaries: definitions, \(\operatorname{pc}(H)=3\), pair deletion | §1 | Common complement lemma extracted; pair deletion follows immediately. |
| Three finite preliminary lemmas | Inputs 2.1–2.3 | Retained explicitly as supplied inputs. |
| Order greater than ten | Theorem 2.4 | The final complement-neighbor count proves the ten-vertex case directly; the intersection case analysis is unnecessary. |
| Internal vertices of one orientation | Proposition 5.3 | Same count and same selected vertices. |
| Two prescribed singleton endpoints | Inputs 4.1–4.2 and following paragraph | Same hypotheses and preservation guarantees; the operations remain explicit imported inputs. |
| General contact and retained restriction | Lemmas 4.3, B.1, B.2 | Exact orders, witnesses, and reversed edges specified. |
| Fixed-pair restrictions and four-vertex intersection | Theorem 4.4 and (4.1) | Strengthened to all vertices outside the fixed pair by retaining one current singleton pair. New deduction requiring independent review. |
| Contact with a new endpoint | Proposition 4.5 | Direct antisymmetry gives explicit three-vertex outputs; no general contact lemma is needed. |
| Four equally oriented vertices | Lemma 4.6 | Same mixed-chain argument and five-vertex order. |
| Terminal three-path lemma | Proposition 3.2 | The impossible \(|A|\le3\) cases removed using \(n>10\); restrictions stated for every external endpoint. |
| Globally longest path | Proposition 3.3 | Same construction. |
| Hamiltonicity of the five-set and its subsets | Appendix A and Proposition 5.4 | Finite table retained in full; all-but-one, rather than first-two, is the accurate description of the forced-turn rows. |
| Eight exact two-path covers | Proposition 5.4 | All eight induced graphs and complementary Hamilton paths retained. |
| Different Hamilton orders | Lemma B.1 | Explicit reversed-edge, tight-triple, and cycle alternatives. |
| Proper path from the eight-cover comparison | Proposition 5.2 | Direct deletion of one of the three internal vertices gives a crossing and a specified tight triple; no exhaustive comparison of eight chosen covers is needed. |
| Endpoint-transfer threshold theorem | Proposition 3.1 | Arbitrary threshold formulation retains the finite-family conclusion and its source-relative limitation. |

The original broad phrase “reversed tight ordered triple” is given an explicit edge-order interpretation in Appendix B; the appendix supplies proofs for that interpretation. No unexpressed legacy condition is assumed. The full three-path-cover and path-history data remain distinct throughout.

The new frontier deductions are the lexicographic extremal choice and \(|B|\ge3\) in §6.1, together with simultaneous applicability of the fixed-pair restrictions at all four end vertices in §6.2. None proves the proposed augmentation lemma. No migration state, source document, audit status, or repository has been changed by this draft.
