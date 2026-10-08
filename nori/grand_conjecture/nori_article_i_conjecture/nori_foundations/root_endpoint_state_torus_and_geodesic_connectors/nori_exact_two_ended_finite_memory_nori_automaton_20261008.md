# Exact two-ended one-switch automaton with free antipodal-reversal symmetry

# Exact bidirectional finite-memory automaton for one-switch NORI geodesics

Let \(c(F,\pi)\in\{0,1\}\) be any ordered-three-face coloring, with or without the antipodal axiom. Consider directed geodesic segments \(P=(v_0,\ldots,v_k)\), \(0\le k\le n\), with distinct direction word \(p=(d_1,\ldots,d_k)\), left endpoint \(x=v_0\), right endpoint \(y=v_k\), and used-coordinate set \(S=\{i:x_i\ne y_i\}\).

For \(k\ge2\), record the first two directions \((d_1,d_2)\) and last two directions \((d_{k-1},d_k)\), with the obvious truncated conventions for \(k<2\). For \(k\ge3\), also record the first and last ordered-three-face window colors \(a,b\). Record \(D\in\{0,1,2\}\), the number of window-color changes clipped at \(2\), where \(2\) means at least two. Call this data the **boundary state**
\[
B(P)=(x,y,\mathrm{head}_2,\mathrm{tail}_2,a,b,\min\{2,\#\mathrm{changes}\}).
\]

**Theorem 1 (exact Markov closure under two-ended extension).** If two directed geodesic segments have the same boundary state, then for every unused coordinate \(j\), prepending \(j\) and appending \(j\) are legal for both, and the two resulting boundary states agree. Consequently the reachable boundary-state transition graph is an EXACT finite acyclic automaton for the existence of an antipodal geodesic with at most one ordered-three-face color change. No full path history is needed for existence testing or witness reconstruction.

**Proof.** Both operations increase \(|S|\) by one and change exactly one endpoint. The new head/tail two-direction memories update locally by inserting \(j\) at the chosen end. When \(k<2\), no window exists yet and truncated memories suffice. When \(k=2\), the new path acquires precisely one window: prepend creates the color
\[
t_L=c(F(x;\{j,d_1,d_2\}),(j,d_1,d_2)),
\]
and append creates
\[
t_R=c(F(y;\{d_1,d_2,j\}),(d_1,d_2,j)).
\]
Here \(F(z;W)\) denotes the three-face with free coordinate set W and exterior bits inherited from z; note that moving along W does not change those exterior bits. For \(k\ge3\), prepending creates exactly one new first window with color \(t_L\) while retaining the other windows, so \(D'=\min(2,D+[t_L\ne a])\) and \(a'=t_L,b'=b\). Appending similarly gives \(D'=\min(2,D+[b\ne t_R])\), \(a'=a,b'=t_R\). The endpoint and direction-memory updates are deterministic in B(P). Thus identical boundary states have identical possible successors, and every successor is realized by extending an actual segment. Starting from all diagonal segments \((z)\), induction on rank proves the exactness of reachable state sets; storing a predecessor gives a witness. At rank n, the endpoints are antipodal automatically, and the automaton accepts exactly states with D≤1. \(\square\)

**Theorem 2 (exact antipodal-reversal equivariance).** Under NORI oddness, the path involution
\[
\Theta(P)=(\bar v_k,\bar v_{k-1},\ldots,\bar v_0)
\]
induces an involution on the boundary-state automaton. On endpoints it sends \((x,y)\mapsto(\bar y,\bar x)\); it exchanges and reverses head/tail direction memories. For \(k\ge3\) it sends \((a,b,D)\mapsto(1-b,1-a,D)\). It interchanges left extensions with right extensions and preserves transition legality and the accepting condition. The involution acts freely on every boundary-state vertex for \(n\ge3\).

**Proof.** The three-face windows of \(\Theta(P)\) are exactly the globally antipodal images of those of P, listed in reverse and with reversed direction orders, so their color word is \(1-\operatorname{rev}(w(P))\). This proves the state transformation, invariance of D, and commuting relation with opposite-end extensions. If \(k<n\), the endpoint pair is not fixed by \((x,y)\mapsto(\bar y,\bar x)\), because fixedness would imply \(y=\bar x\), hence rank n. At rank n, a fixed boundary state would require its first direction \(d_1\) to equal its last direction \(d_n\) (the first direction of the reversed word), contrary to distinctness of used directions when n≥3. Therefore the lifted state involution is free even though the underlying endpoint involution fixes the rank-n antidiagonal states. \(\square\)

**Topological direction and exact remaining problem.** The underlying 2n-bit root–endpoint state torus has a fixed antidiagonal under \((x,y)\mapsto(\bar y,\bar x)\). Remembering first and last two directions resolves these fixed endpoint fibers into free involution pairs. This is a natural **finite-memory free antipodal carrier** encoding all NORI one-switch constraints in its directed edges. It still requires an actual topological obstruction: free involution alone does not guarantee a directed path to an accepting top-rank state. One must determine the equivariant topology of this lift and establish a directed, color-compatible connector theorem.

**Sharpness of boundary-direction memory.** For arbitrary NORI colorings, knowledge of only the first (respectively last) direction at an end is insufficient to update the color of a prepended (respectively appended) three-face window. Indeed take two partial direction orders with identical endpoint pair and identical first direction a but different second directions b and c (obtainable by swapping b,c while retaining the same used set), and prepend an unused direction j. Their new first windows have ordered directions (j,a,b) and (j,a,c) and belong to different free-coordinate faces. The NORI antipodal axiom constrains only the respective antipodal-reversed partners, so these two new window colors can be chosen independently. Thus a universal deterministic updater must distinguish the two-direction boundary contexts (or store equivalent information). The last two directions are necessary by the same argument at the right endpoint. This minimality is in the sense of universal local update across arbitrary admissible ordered-face colorings, not a lower bound on every conceivable global compressed algorithm.
