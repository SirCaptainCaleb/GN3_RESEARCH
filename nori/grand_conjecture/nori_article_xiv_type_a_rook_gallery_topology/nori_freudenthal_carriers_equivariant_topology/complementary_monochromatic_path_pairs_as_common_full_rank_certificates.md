# Complementary monochromatic path pairs as common full-rank certificates

# Complementary monochromatic path pairs as common full-rank certificates

The two original one-switch conjectures can be characterized by the existence of **two monochromatic partial paths of the same color** that have complementary dimension or vertex supports. Applying the involutive color reversal to the second path and gluing their compatible boundaries produces a complete one-switch path. This provides a common intrinsic proof certificate inspired by the ordered-pair step of Wu–Yang's construction, without introducing an auxiliary graph of galleries or relaxing dimension-simplicity.

## NORI1: two red geodesic cones with antipodal ends

Fix an antipodally odd edge coloring of \(Q_n\), a root \(x\), and a bit \(a\in\mathbb F_2\). Let
\[
R_x^a=\{y\in Q_n:\text{some color-}a\text{ geodesic from }x\text{ ends at }y\}.
\tag{1}
\]

**Theorem 1 (opposed endpoints).** The following are equivalent for a fixed root \(x\) and color \(a\):

(i) Some full antipodal geodesic from \(x\) has color word consisting of an initial run of \(a\) followed by a terminal run of \(1-a\), with either run possibly empty.

(ii) The rooted monochromatic reachability cone \(R_x^a\) contains an antipodal pair:
\[
\boxed{\exists y:\quad y,\bar y\in R_x^a.}
\tag{2}
\]

*Proof.* If (ii) holds, take color-\(a\) geodesics \(P:x\to y\) and \(Q:x\to\bar y\). Their dimension supports are respectively \(S=\{i:x_i\ne y_i\}\) and \(S^c\). Apply cube antipodality to \(Q\), producing a color-\((1-a)\) geodesic \(\bar Q:\bar x\to y\); reverse it to get a color-\((1-a)\) path \(y\to\bar x\). The concatenation \(P\cdot(\bar Q)^{\rm rev}\) is a full dimension-simple antipodal geodesic from \(x\), with at most one switch, proving (i).

Conversely, split a geodesic as in (i) at its color boundary \(y\). Its first part is a color-\(a\) geodesic from \(x\) to \(y\). Antipodally translate and reverse the color-\((1-a)\) suffix from \(y\) to \(\bar x\), giving a color-\(a\) geodesic from \(x\) to \(\bar y\). Thus both endpoints belong to \(R_x^a\). \(\square\)

In particular, NORI1 is equivalent to the statement that for some root \(x\) and either color \(a\), the corresponding geodesic reachability cone contains an antipodal pair. Under a hypothetical counterexample, every cone \(R_x^a\) is antipodal-free. The paths in this theorem use disjoint dimension supports, hence the union of their move vectors has full rank \(n\).

## Boundary tournaments: two same-color paths ending in reversed ordered pairs

Let \(V\) be an \(n\)-element set and \(b(a,h,c)\in\mathbb F_2\) an arbitrary reversal-odd boundary 3-tournament. For an ordered pair \((h,c)\) and color \(a\), define
\[
\mathcal F_{h,c}^a=
\bigl\{\,S\subseteq V\setminus\{h,c\}:\ 
\exists\text{ a vertex-simple color-}a\text{ tight path}
\text{ using }S\cup\{h,c\}
\text{ and ending }(h,c)\,\bigr\}.
\tag{3}
\]
Allow the length-two ordered path \((h,c)\), with no triple colors, so that \(\varnothing\in\mathcal F_{h,c}^a\) for both bits.

**Theorem 2 (opposed-terminal-pair gluing).** The boundary tournament admits a Hamilton tight path whose color word switches at most once if and only if there exist distinct \(h,c\in V\), a color \(a\), and a subset \(S\subseteq V\setminus\{h,c\}\) such that
\[
\boxed{
S\in\mathcal F_{h,c}^a,\qquad
\bigl(V\setminus\{h,c\}\bigr)\setminus S
\in\mathcal F_{c,h}^a.
}
\tag{4}
\]

*Proof.* Suppose (4) holds, witnessed by color-\(a\) tight paths
\[
P=(p_1,\ldots,p_r,h,c),\qquad
Q=(q_1,\ldots,q_s,c,h).
\]
The used vertex sets meet only in \(\{h,c\}\) and together equal \(V\). Reverse \(Q\): by boundary reversal oddness it becomes a color-\((1-a)\) tight path \((h,c,q_s,\ldots,q_1)\). Glue this reversed path to \(P\) along their common ordered terminal/initial pair \((h,c)\):
\[
(p_1,\ldots,p_r,h,c,q_s,\ldots,q_1).
\tag{5}
\]
All vertices are distinct, all are used, and the tight-path color word is an initial run of \(a\) followed by a terminal run of \(1-a\). Either run may be empty. Hence (5) is a one-switch Hamilton path.

Conversely, let a Hamilton ordering have a bit word with at most one switch, and let \(a\) be the initial bit (if the whole word is constant, take that bit). Split it at the switch, with \(P\) the initial color-\(a\) tight path up to the shared boundary pair \((h,c)\). Reverse the remaining color-\((1-a)\) tight suffix, including that same boundary pair. Reversal oddness makes the reversed suffix a color-\(a\) tight path ending in \((c,h)\). The used vertex sets intersect at \(\{h,c\}\) and are complementary elsewhere. This gives (4). \(\square\)

The undirected edges of \(P\) and \(Q\) in (4), with their common \(\{h,c\}\) edge identified, form a spanning tree of \(K_V\). Their type-\(A\) incidence vectors therefore have full graphic-matroid rank \(n-1\). Thus (4) enforces Hamilton vertex-simplicity and cannot be satisfied by a walk that repeats an original vertex.

## A common rank-preserving gluing principle

Theorems 1 and 2 expose the same selection mechanism:

1. Find two *same-color monochromatic partial paths* with a pair of opposed interfaces.
2. Require their dimension or vertex supports to complement one another in the natural independence geometry.
3. Apply the original reversal/antipodal operation to one path, making its color complementary.
4. Concatenate along the compatible interface. Independence of supports guarantees a full dimension-simple output with at most one color change.

The cube interface consists of a common initial root and antipodal terminal vertices. The boundary interface consists of opposite terminal ordered pairs \((h,c),(c,h)\), with the shared two vertices counted once. The distinct appearances of the interfaces should not be erased by imposing an unjustified extra state-graph axiom.

**Topological proof target.** Wu–Yang's rook-label map records paired red components and uses the involution to obtain an odd map into a type-\(A\) root sphere. Here the relevant paired objects are the rank-sensitive reachable families \(R_x^a\) and \(\mathcal F_{h,c}^a,\mathcal F_{c,h}^a\). A successful extension would prove, by an equivariant chain obstruction, that *some pair has complementary supports*. That would imply the original one-switch conclusions by the above equivalences. The existence of the complementary pair remains unproved in both unrestricted classes; the theorems in this subsection establish the common full-rank decoding certificate, not its topological existence.
