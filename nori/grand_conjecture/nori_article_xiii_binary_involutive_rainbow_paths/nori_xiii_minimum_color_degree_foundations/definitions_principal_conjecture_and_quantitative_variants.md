# Definitions, principal conjecture, and quantitative variants

# Foundations of the involutive rainbow one-switch problem

## 1. Graphs and the two independent edge labelings

Let \(G=(V,E)\) be a **finite connected undirected simple graph** with at least one edge. Equip its edges with an ordinary edge coloring \(\lambda:E\to\mathcal C\), where \(\mathcal C\) is merely a set of color names. No proper-coloring condition is assumed. Independently, assign a binary edge label \(\chi:E\to\mathbb F_2=\{0,1\}\). The binary label and the ordinary edge color serve different purposes and are not assumed to be correlated.

Assume \(G\) has an involutive automorphism \(\tau:V\to V\), with \(\tau^2=\mathrm{id}\), such that
\[
\boxed{\chi(\tau e)=1-\chi(e)\quad\text{for every undirected edge }e.}\tag{1}
\]
Call \(\tau\) a **binary-label-reversing involution**. No hypothesis requires \(\tau\) to preserve the ordinary edge coloring \(\lambda\), or even to induce a fixed permutation of its color names. Fixed vertices are allowed; equation (1) already rules out fixed undirected edges.

The underlying object of investigation is simply an ordinary edge-colored graph \(G\), with an additional binary edge labeling and the involution (1). There is no separate resource set beyond the available ordinary edge colors, and no other graph structure is assumed.

## 2. Degree parameters and witness length

For \(v\in V\), set
\[
\hat d(v)=|\{\lambda(e): e\ni v\}|,\qquad
\boxed{\hat\delta=\min_{v\in V}\hat d(v),}\qquad
\delta=\min_{v\in V}\deg_G(v).
\tag{2}
\]
Thus \(1\le\hat\delta\le\delta\). The principal degree parameter is **minimum color degree** \(k=\hat\delta\), not ordinary minimum degree.

A path \(P=v_0v_1\cdots v_m\) is always vertex-simple and has length \(m\), **counted in edges**. Write \(e_i=v_{i-1}v_i\). It is **rainbow** when \(\lambda(e_1),\ldots,\lambda(e_m)\) are pairwise distinct. Its **binary switch count** is
\[
\boxed{\operatorname{sw}_\chi(P)=\sum_{i=1}^{m-1}
\mathbf1_{\{\chi(e_i)\ne\chi(e_{i+1})\}}.}\tag{3}
\]
The inequality \(\operatorname{sw}_\chi(P)\le1\) means the binary-label sequence has at most two consecutive constant blocks. It does not restrict the number of ordinary edge colors, except through the rainbow requirement. Let
\[
L_s(G,\lambda,\chi)=
\max\{|E(P)|:P\text{ is vertex-simple, rainbow, and }
\operatorname{sw}_\chi(P)\le s\}
\tag{4}
\]
for integers \(s\ge0\); define \(L_\infty(G,\lambda)\) by omitting the binary-switch restriction. Then \(L_0\le L_1\le L_\infty\).

## 3. Main conjecture

**Conjecture XIII.1 (binary-involutive minimum-color-degree rainbow path; unproved and subject to counterexample search).** In every graph and labeling system of Sections 1–2,
\[
\boxed{L_1(G,\lambda,\chi)\ge\hat\delta(G,\lambda).}\tag{5}
\]
Equivalently: **every connected edge-colored graph of minimum color degree \(k\), additionally equipped with a binary edge labeling reversed by a graph involution, contains a rainbow path of at least \(k\) edges whose binary labels change at most once.**

No condition on \(\lambda(\tau e)\) is part of this conjecture. Its unrestricted truth is not established. The primary objective is to prove (5) or find an admissible counterexample.

## 4. Elementary properties and a necessary connectivity assumption

**Lemma 4.1 (orbit pairing).** Every orbit of \(\tau\) on the undirected edges has size two, consisting of one edge with binary label \(0\) and one with binary label \(1\). Consequently, \(|E|\) is even and the binary-label classes have equal cardinality.

*Proof.* A fixed edge contradicts (1); the remaining orbits of an involution are pairs, with complementary labels. \(\square\)

**Lemma 4.2 (path switches under the involution).** For any vertex-simple path \(P\), the path \(\tau P\) has the same length and the complement of its binary-label word. In particular, \(\operatorname{sw}_\chi(\tau P)=\operatorname{sw}_\chi(P)\). Without additional assumptions on \(\lambda\), however, \(\tau P\) is not necessarily rainbow.

*Proof.* Graph automorphisms preserve path simplicity. Complementing both members of each adjacent binary-label pair preserves equality and inequality. \(\square\)

**Proposition 4.3 (small color degree).** Conjecture XIII.1 holds for \(\hat\delta\le2\).

*Proof.* If \(\hat\delta=1\), any single edge works. If \(\hat\delta=2\), at any vertex choose two incident edges with different ordinary colors. As \(G\) is simple, they give a vertex-simple two-edge rainbow path, which automatically has at most one binary switch. \(\square\)

**Counterexample 4.4 (why connectivity is required).** Consider two disjoint copies of \(K_4\), one on each copy of \(\mathbb F_2^2\). Color each edge \(\{x,y\}\) by \(x+y\in\mathbb F_2^2\setminus\{0\}\), identically in the two components. This is a proper ordinary coloring with color degree three. A rainbow three-edge path inside a copy would use all three nonzero group elements, whose sum is zero. The edge-color sum also telescopes to its endpoint difference, forcing equal endpoints, a contradiction. Interchange the two copies by \(\tau\), label all edges of one component by \(\chi=0\) and the other by \(\chi=1\). Condition (1) holds, yet there is no rainbow path of length three. Thus (5) fails if connectivity is simply omitted. This example does not refute the connected conjecture.

## 5. Quantitative alternatives and strengthened subproblems

If (5) is false, test the following independent candidate lower-bound scales for \(L_1\):
\[
\boxed{L_1\ge k-C,\qquad
L_1\ge (1-o(1))k,\qquad
L_1\ge\alpha k,}\tag{6}
\]
for absolute constants \(C,\alpha>0\), with asymptotic quantifiers stated carefully. Separate two kinds of obstruction: failure of the ordinary rainbow length \(L_\infty\ge k\), and failure of the one-switch bound despite adequate rainbow paths.

A deliberately **stronger optional hypothesis** is
\[
\boxed{\lambda(\tau e)=\lambda(e).}\tag{7}
\]
Under (7), the involution maps rainbow paths to rainbow paths; without (7), only binary switch counts are preserved. Another optional condition is equivariance via a permutation \(\sigma\) of the color names: \(\lambda(\tau e)=\sigma(\lambda(e))\). Neither is assumed in (5). Determine whether an extra relation of this sort is necessary, and whether it allows quantitatively stronger conclusions.

Investigate the role of the total degree \(\delta(G)\) in addition to \(k=\hat\delta(G,\lambda)\); the ratio \(\delta/k\) measures the supply of incident edges beyond distinct ordinary colors but alone does not guarantee useful extensions.

## 6. Two-step color expansion

To quantify colors available on the second edge of a two-step rainbow walk from \(v\), define
\[
C_2(v)=\{\lambda(v_1v_2): v,v_1,v_2\text{ distinct},\
vv_1,v_1v_2\in E,\
\lambda(vv_1)\ne\lambda(v_1v_2)\},
\quad
\hat\delta_2=\min_v|C_2(v)|.
\tag{8}
\]
For each binary label \(\varepsilon\in\mathbb F_2\), define \(C_{2,\varepsilon}(v)\) by adding \(\chi(vv_1)=\chi(v_1v_2)=\varepsilon\) to the conditions in (8). These are ordinary graph parameters, not extra structure in the main conjecture.

A large two-step palette does not automatically yield a rainbow continuation of a given long path: its first required step may already use a forbidden ordinary color. Research should distinguish *local abundance of two-step candidates* from *endpoint mobility under previously used colors*. Possible techniques include endpoint rerouting, path rotations, two-ended augmentations, and global counts of binary-monochromatic rainbow two-step walks.

## 7. Research directions and reporting standard

First, test Conjecture XIII.1 computationally and structurally at the smallest unproved color degrees \(k\ge3\), allowing arbitrary ordinary edge colorings and both possible binary labels subject to involutive reversal. Search especially for connected counterexamples; evaluate color-preserving and non-color-preserving involutions separately. Second, derive lower bounds on \(L_1\) in terms of \(\hat\delta\), ordinary degree \(\delta\), and two-step palette parameters, recording whether each proof uses the involution substantially. Third, investigate the sharpest assumptions needed to obtain length \(k\) or an asymptotically close bound, and distinguish results about merely rainbow paths from those also controlling binary switches.

All statements, proofs, counterexamples, and open questions in this article concern only this simplified edge-colored graph problem.
