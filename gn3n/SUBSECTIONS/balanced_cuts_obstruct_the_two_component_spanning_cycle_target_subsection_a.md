# balanced_cuts_obstruct_the_two_component_spanning_cycle_target_subsection_a

## Metadata

- ID: balanced_cuts_obstruct_the_two_component_spanning_cycle_target_subsection_a
- Parent Section: balanced_cuts_obstruct_the_two_component_spanning_cycle_target
- Position: 1
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

### Transition colors and ordered edges

Let \(H\) be a boundary \(3\)-tournament on \(n\geq 3\) vertices. For an oriented Hamilton cycle \(C=(v_1,\ldots,v_n,v_1)\) of the complete graph on \(V(H)\), color the transition at \(v_i\) red if \((v_{i-1},v_i,v_{i+1})\) is tight and blue otherwise, with cyclic indices. Write \(\rho_H(C)\) for the number of monochromatic components in this cyclic word, using adjacency of consecutive cycle vertices. A monochromatic word has one component.

If the ordinary edges carry a strict total order \(<\), define \(H\) by
\[
(u,v,w)\in H \quad\Longleftrightarrow\quad \{u,v\}<\{v,w\}.
\]
This is a boundary tournament: the two distinct edges are comparable, and reversing the triple reverses the inequality. Its tight paths are precisely the paths with strictly increasing edge sequences.

**Lemma 1.** In this edge-ordered model, a Hamilton cycle with at most two monochromatic transition components has the following property: for every threshold in the edge order, the cycle edges above the threshold form a single cyclic interval, or the empty set, or the whole cycle.

**Proof.** A cyclic sequence of distinct edge ranks cannot have all its consecutive comparisons increasing or all decreasing. Thus at most two components means exactly one increasing run and one decreasing run. Starting at its unique minimum edge, the edge ranks increase strictly to the unique maximum edge and then decrease strictly back to the minimum. The edges above any threshold are consequently consecutive around the maximum. \(\square\)

### A balanced-cut obstruction

**Lemma 2.** Let \(C\) be a Hamilton cycle on a vertex set partitioned into equal parts \(U,W\). If the edges of \(C\) joining \(U\) to \(W\) form one cyclic interval, then every edge of \(C\) joins \(U\) to \(W\).

**Proof.** Let \(a,b,c\) count the cycle edges internal to \(U\), internal to \(W\), and joining the parts, respectively. Summing cycle degrees on the two sides gives
\[
2|U|=2a+c,\qquad 2|W|=2b+c,
\]
so \(a=b\).

There is at least one edge between the two parts because the cycle is connected and both parts are nonempty. If any internal edges remain, the complement of the single interval of edges between the parts is a nonempty single interval of internal edges. Consecutive edges in that interval share a vertex, so they all lie in the same part. Exactly one of \(a,b\) is then positive, contradicting \(a=b\). \(\square\)

**Theorem 3.** For every integer \(s\geq 1\), there is an edge-orderable boundary \(3\)-tournament \(H_s\) on \(4s\) vertices such that
\[
\operatorname{pc}(H_s)=2,
\qquad
\min_C\rho_{H_s}(C)=4.
\]
Moreover, \(H_s\) has a spanning linear order whose tightness word changes exactly once, from tight to non-tight.

**Construction.** Partition the vertices into four classes
\[
A=\{a_1,\ldots,a_s\},\quad B=\{b_1,\ldots,b_s\},\quad
C=\{c_1,\ldots,c_s\},\quad D=\{d_1,\ldots,d_s\}.
\]
Assign an ordinary edge its level according to the following table:
\[
\begin{array}{c|l}
0&\text{both endpoints in one class}\\
1&AB\text{ or }CD\\
2&AC\text{ or }BD\\
3&AD\text{ or }BC .
\end{array}
\]
Every edge of lower level precedes every edge of higher level. Within each level choose any strict total order satisfying these additional requirements:

- the edge sequences of \((a_1,\ldots,a_s)\) and \((d_1,\ldots,d_s)\) are increasing;
- the edge sequences of
\[
P=(a_1,d_1,a_2,d_2,\ldots,a_s,d_s)
\quad\text{and}\quad
Q=(b_1,c_1,b_2,c_2,\ldots,b_s,c_s)
\]
are increasing.

These requirements are consistent: the first two sequences use disjoint sets of level-zero edges, and the last two use disjoint sets of level-three edges. Empty edge sequences impose no conditions. Define \(H_s\) from this total edge order.

**No cycle has at most two color components.** Suppose a Hamilton cycle \(Z\) did. The balanced partition
\[
A\cup B\ \mid\ C\cup D
\]
has precisely the level-two and level-three edges between its parts. These form an upper interval of the edge order. Lemma 1 makes their occurrences on \(Z\) a single cyclic interval. Lemma 2 therefore forces every edge of \(Z\) to have level two or three.

Now use the balanced partition
\[
A\cup C\ \mid\ B\cup D.
\]
Among the remaining edges, exactly the level-three edges join its parts: level-two edges lie within its parts. The level-three edges again form an upper interval of the total edge order. Lemmas 1 and 2 force every edge of \(Z\) to have level three.

But the graph of level-three edges is the disjoint union of the complete bipartite graphs on \(A,D\) and on \(B,C\). It is disconnected and contains no Hamilton cycle on all \(4s\) vertices. This is a contradiction.

**There is a two-cover, and the cyclic minimum is four.** The displayed increasing paths \(P,Q\) form a two-cover. Concatenate them in their displayed orders and close the result to a Hamilton cycle. Its two joining edges, \(d_sb_1\) and \(c_sa_1\), have level two. All edges internal to \(P,Q\) have level three and increase along each path.

At each joining edge the comparison from the last path edge down to the joining edge is blue, and the comparison from the joining edge up to the first edge of the next path is red. All internal comparisons along \(P,Q\) are red. Hence this cycle has exactly two isolated blue transitions and exactly four monochromatic components, including when \(s=1\).

A tight Hamilton path, if one existed, would have strictly increasing edges. Adding its closing edge produces a cyclic rank sequence with only one increasing run and one decreasing run, whatever the rank of the closing edge. This would give a cycle with two color components, which has been ruled out. Thus \(\operatorname{pc}(H_s)=2\). A mixed cyclic two-color word has an even number of components, so the minimum cyclic component count is exactly four.

**There is nevertheless a one-change linear order.** Consider
\[
R=(a_1,\ldots,a_s,\ b_1,c_1,b_2,c_2,\ldots,b_s,c_s,\ d_s,\ldots,d_1).
\]
Its edge sequence consists successively of:

1. an increasing level-zero sequence in \(A\);
2. the level-one edge \(a_sb_1\);
3. the increasing level-three edge sequence of \(Q\);
4. the level-one edge \(c_sd_s\);
5. a decreasing level-zero sequence in \(D\).

The sequence increases strictly through the last edge of \(Q\), then decreases strictly. Both portions are present even when \(s=1\). Thus the consecutive-triple word is a nonempty tight block followed by a nonempty non-tight block. \(\square\)

### Consequences for the antipodal formulation

A spanning cycle with at most two color components remains a sufficient condition for a two-cover. Theorem 3 shows that this sufficient condition is not universally available, even in the edge-orderable subclass and even when a two-cover and a one-change spanning order both exist.

In particular, the linear one-change target and the cyclic two-component target are not equivalent. Closing a one-change linear order introduces two additional triple comparisons, and these can produce a second pair of color changes. The family above demonstrates this obstruction at every order divisible by four.

The construction leaves the general two-cover conjecture and the universal linear one-change question open. It refutes the universal cyclic two-component strengthening. Any use of an antipodal theorem to force that strengthening needs hypotheses excluding this family.

### A cyclic formulation equivalent to the two-cover conjecture

The cyclic encoding can retain the intended theorem without imposing a bound of two on the number of color components.

For an oriented Hamilton cycle \(Z=(v_1,\ldots,v_n,v_1)\), put \(e_i=\{v_i,v_{i+1}\}\). Define a graph \(D_Z\) with vertex set \(\{e_1,\ldots,e_n\}\), adding the edge \(\{e_{i-1},e_i\}\) precisely when the transition \((v_{i-1},v_i,v_{i+1})\) is blue. Thus \(D_Z\) is a subgraph of the cycle on the cut positions. Let \(\tau(D_Z)\) be its minimum vertex-cover size.

**Proposition 4.** For every finite boundary \(3\)-tournament \(H\) of order at least three,
\[
\operatorname{pc}(H)=\min_Z\max\{1,\tau(D_Z)\},
\]
where \(Z\) ranges over all oriented Hamilton cycles of the complete graph on \(V(H)\). Consequently,
\[
\operatorname{pc}(H)\leq2
\quad\Longleftrightarrow\quad
\text{some }D_Z\text{ has a vertex cover of size at most two}.
\]

**Proof.** Choose a nonempty set \(S\) of ordinary cycle edges to cut. Deleting \(S\) leaves \(|S|\) vertex-disjoint paths in the inherited cyclic orientation, including singleton paths when appropriate. A blue transition at \(v_i\) remains internal to one such path exactly when neither \(e_{i-1}\) nor \(e_i\) is cut. Therefore all resulting paths are tight exactly when \(S\) is a vertex cover of \(D_Z\). The minimum number of nonempty inherited path components is \(\max\{1,\tau(D_Z)\}\).

Conversely, concatenate the displayed tight orders in any path cover and close them cyclically. Cutting the joining edges recovers that cover; for a single Hamilton path cut only its added closing edge. Hence minimizing the preceding quantity over all cyclic orders gives precisely \(\operatorname{pc}(H)\). \(\square\)

The equivalent cyclic target is therefore to cover every blue transition by two cut positions. It allows separated short blue components, as the four-class construction requires. The color-component count alone loses this distinction.
