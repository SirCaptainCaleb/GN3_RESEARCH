# Odd signed holonomy on the 2n-bit uncolored reachability state graph forces geodesic closure

# A color-free 2n-bit reachability holonomy graph: odd signed cycles force closure

Let c be an antipodally odd binary UNDIRECTED edge coloring of Q_n. Define the uncolored monochromatic-geodesic reachability relation
\[
\mathcal E=\{(x,S):x\in Q_n,\ \varnothing\ne S\subseteq[n],\ x\oplus S\in R(x)\}.
\]
These are exactly ROOT–SUPPORT states with n root bits plus n support bits. They are defined solely by the COLOR-FREE sets R(x). Associate a signed graph H_R to the states with THREE types of (undirected) edges:

(A) **Antipodal root flip**, sign 1:
\[
(x,S)\longleftrightarrow(\bar x,S).
\]
(B) **Endpoint reversal/root swap**, sign 0:
\[
(x,S)\longleftrightarrow(x\oplus S,S).
\]
(C) **Near-complementary supports at the same root**, sign 1:
\[
(x,S)\longleftrightarrow(x,T)
\quad\text{if } S\cap T=\varnothing,\ S\cup T=[n]\setminus\{i\}\text{ for some i}.
\]
All endpoints of all these edges are in \(\mathcal E\): (A) by odd coloring, (B) by undirected path reversal, and (C) by definition. Retain edge types if parallel edges arise.

**Theorem (odd-holonomy extraction).** If H_R contains a closed walk whose edge-sign sum is odd and that traverses at least one (C) edge, then c has a MONOCHROMATIC FULL ANTIPODAL GEODESIC. Conversely, in any hypothetical counterexample, every connected component of H_R containing a (C) edge carries a unique consistent binary vertex potential q such that
\[
q(\bar x,S)=q(x,S)\oplus1,\quad
q(x\oplus S,S)=q(x,S),\quad
q(x,T)=q(x,S)\oplus1
\]
on the corresponding edge types. Thus such a component has zero signed holonomy around every closed walk.

**Proof.** For a state (x,S), define \(C(x,S)\subseteq\mathbb F_2\) to be the NONEMPTY set of colors of all monochromatic geodesics joining x to x⊕S. This auxiliary witness-color set is used ONLY IN THE PROOF; it is absent from the state graph and reachability-label definition. Under (A), the antipodal copy complements edge colors exactly, giving C(bar x,S)=1-C(x,S). Under (B), reversal of an undirected edge path preserves each edge color, giving C(x⊕S,S)=C(x,S). At a (C) edge, if C(x,S) and C(x,T) shared any color q, their two q-geodesics would have disjoint coordinate supports covering n-1 coordinates. Their concatenation is a q-colored length-(n-1) geodesic. Its two end-extension edges are antipodal with opposite colors, so one completes it to a full q-geodesic. Therefore, in the absence of a full monochromatic antipodal geodesic, C(x,S) and C(x,T) are disjoint nonempty subsets of the two-element color set. They must be complementary SINGLETONS. The bijections in (A),(B) preserve singleton cardinality, so every state in a connected component containing a (C) edge has a unique witness color. The displayed potential q is then its unique element. Along any closed walk q must return to itself, requiring an even number of sign-1 edges. Hence an odd-signed closed walk implies closure. QED.

**No premature role for the colors.** The graph H_R and the existence of an odd signed cycle depend only on R(x), the cube's root/coordinate geometry, and the sign of three structural operations. The two color indices appear only inside the extraction proof to establish the obstruction. This is exactly an 'antipodal-label coincidence implies actual monochromatic witness' certificate with explicit extraction.

**Relation to odd-dimensional Kneser cycles.** Restrict to a single root x and the (C) edges. This recovers the near-complement graph \(\Gamma_x\). For n odd, middle-layer Kneser odd cycles give odd holonomy immediately. For n even, \(\Gamma_x\) is bipartite by support-cardinality parity, but root antipodality (A) and endpoint exchange (B) can create new cross-root signed cycles. This gives a unified dimension-independent target: force a NONTRIVIAL Z_2-holonomy cycle in the root-coupled reachable state graph.

**Scope and challenge.** A signed frustrated cycle is a SUFFICIENT condition, not asserted to exist for every coloring. Proving its existence from antipodal-odd edge incidence would establish the edge-geodesic conjecture. The graph may be balanced for some colorings that already have a monochromatic antipodal geodesic; the theorem is not an equivalence. One can also treat any reachable support S=[n] as immediate closure, independently of holonomy. Its value is a precise, color-free, topologically meaningful inconsistency criterion, with no small-dimension classification.
