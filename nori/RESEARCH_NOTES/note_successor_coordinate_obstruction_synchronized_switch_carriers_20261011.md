# Successor-coordinate obstruction and dependency-graph criterion for synchronized switch carriers

- Stable ID: note_successor_coordinate_obstruction_synchronized_switch_carriers_20261011
- Author: unspecified; session provenance retained
- Primary home: subsection:penultimate_length_extension_and_parallel_face_endpoint_exclusion
- Labels: obstruction, counterexample, affine, reachability
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6263_2
- Updated session: session_nori_r6263_2
- Disposition: none
- Successor: none

## Related references

- subsection:penultimate_length_extension_and_parallel_face_endpoint_exclusion

## Research note

# Successor-coordinate obstruction to synchronized opposite-phase switch carriers

**Theorem.** For every \(n\ge4\), the undirected edge coloring of \(Q_n\)
\[
c_i(x)=x_{i+1},\qquad i\in\mathbb Z/n\mathbb Z
\]
is antipodally odd. Every complete direction order has precisely one root realizing an all-\(0\) color word and one root realizing an all-\(1\) word. Nevertheless, there are **no** paired one-switch geodesics in adjacent codimension-two faces with corresponding initial vertices, corresponding switch vertices, and opposite initial colors, even allowing arbitrary different direction orders inside both monochromatic blocks.

**Proof.** The color \(c_i\) is independent of the free \(i\)-bit, and global antipodal complementation flips the \(i+1\) bit. For a full direction permutation \(\pi\), take the root with
\[
x_{i+1}=\mathbf1_{\{i+1\text{ precedes }i\text{ in }\pi\}}.
\]
At the \(i\)-step the successor bit then equals \(0\), producing an all-\(0\) path. The prescription determines every root bit uniquely; its complement produces the unique all-\(1\) path.

Suppose \(P\subset F\) and \(Q\subset F^a\) give the prohibited paired witness, with \(F\) fixing directions \(a,b\), and let \(D=[n]\setminus\{a,b\}\). The matching switch vertex determines a partition \(D=A\sqcup B\) into nonempty prefix and suffix supports, used in that block order by both paths. Opposite phases require the edge of \(P\) and edge of \(Q\) in **each** direction \(i\in D\) to have opposite colors.

If the predecessor \(j=b-1\) (cyclic indices) belongs to \(D\), then its edge color on either path equals the fixed \(b\)-bit, the same in \(F\) and \(F^a\). This is a contradiction. Thus \(j=a\), i.e. \(b=a+1\).

Now \(D\) is a single connected path in the cyclic successor graph. A nontrivial partition \(A,B\) has a successor-adjacent pair \(i,i+1\in D\) crossing it. Their relative order is the same in \(P\) and \(Q\), because all directions in \(A\) precede all those in \(B\). The initial \(i+1\)-bit is likewise the same, since the two roots differ only in coordinate \(a\), and \(i+1\in D\). Hence their traversed \(i\)-edges have equal color, again a contradiction. \(\square\)

**Implication.** A universal intersection theorem for synchronized opposite-phase one-switch carriers is false, even within a simple affine subfamily where monochromatic full geodesics exist for every direction permutation. This does not affect the correct sufficient gluing theorem. Any prospective topological extraction must encode additional witnesses, including monochromatic paths without paired one-switch certificates.

## Graph-theoretic criterion for permutation-dependency colorings

Let \(\tau\) be any fixed-point-free permutation of \([n]\) and color \(i\)-edges by \(c_i(x)=x_{\tau(i)}\). For distinct exterior directions \(a,b\), put \(D=[n]\setminus\{a,b\}\), and let \(H\) be the undirected graph on \(D\) with edge \(i\tau(i)\) whenever both endpoints are in \(D\).

**Proposition.** There exist spanning one-switch geodesics in \(F,F^a\), for some face \(F\) with fixed directions \(a,b\), starting and switching at corresponding vertices and having opposite initial colors, **if and only if**
\[
\tau(a)=b\quad\text{and}\quad H\text{ is disconnected}.
\]

*Necessity.* If the witness has switch support \(A\subset D\), let \(B=D\setminus A\), both nonempty. On every direction \(i\in D\) its two path colors must differ. The direction \(i=\tau^{-1}(b)\) would have the identical fixed \(b\)-bit on both paths, so it cannot belong to \(D\). As \(\tau\) has no fixed points, \(\tau^{-1}(b)=a\), giving \(\tau(a)=b\).

If an edge \(i\tau(i)\) of \(H\) crossed the partition \(A,B\), the relative order of \(i,\tau(i)\) would be identical on both paths (all \(A\)-directions precede all \(B\)-directions). Their initial \(\tau(i)\)-bits also coincide, so their \(i\)-edge colors would agree, contradiction. Thus every connected component of \(H\) lies wholly in \(A\) or \(B\). Both sets are nonempty, hence \(H\) is disconnected.

*Sufficiency.* Split the components of \(H\) into nonempty unions \(A,B\). Choose a direction order \(p\) traversing \(A\) and then \(B\), and let \(q\) reverse the order **within each block** while retaining the block order \(A,B\). When \(\tau(i)\in D\), the relative order of \(i,\tau(i)\) is reversed between \(p,q\), since they lie in one block. When \(\tau(i)=a\), the initial \(a\)-bit is complemented between \(F,F^a\). Finally, \(\tau(i)=b\) never occurs for \(i\in D\). It follows that the \(i\)-edge color of the \(p\)-path is opposite that of the \(q\)-path for every \(i\in D\).

Choose internal root bits so that the \(p\)-path has constant color \(s\) on \(A\) and \(1-s\) on \(B\). This is feasible since the conditions prescribe the bits \(x_{\tau(i)}\) for \(i\in D\), all different; at most one is an exterior bit (the fixed \(a\)-bit), and \(s\) may be selected accordingly. The \(q\)-path then has colors \(1-s\) on \(A\) and \(s\) on \(B\). Both switch at the prefix support \(A\). \(\square\)

For a single \(n\)-cycle \(\tau\), deleting a successive pair \(a,b\) leaves a connected path, whereas a nonsuccessive pair violates \(\tau(a)=b\); thus no synchronized witness occurs. For permutations with multiple cycles, the graph criterion determines precisely which exterior pairs admit such a witness. Checked independently by exhaustive enumeration of all derangements of orders four and five.
