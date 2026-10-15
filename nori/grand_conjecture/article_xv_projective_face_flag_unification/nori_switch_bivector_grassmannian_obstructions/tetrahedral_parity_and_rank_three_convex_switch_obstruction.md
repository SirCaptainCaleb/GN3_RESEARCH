# Tetrahedral parity and rank-three convex switch obstruction

### Tetrahedral parity and a sharp rank-three convex obstruction

**Theorem 1 (tetrahedral rank-three obstruction).** For every \(n\ge6\) there is an unrestricted reversal-odd boundary triple coloring and a rank-three dual type-A cell \(D\) with 24 Hamilton-order flags such that every flag has at least two switches, every flag has first and last switch-prefix ranks \((2,4)\), and
\[
\boxed{\sum_{\pi\in V(D)}Z_2(\pi)\wedge Z_4(\pi)=0.}\tag{1}
\]
In particular the nonzero flag wedges have zero in their convex hull, so the color-sensitive rank-two convex-filling theorem cannot be extended to all rank-three cells.

*Proof.* Select a four-element set \(A=\{a,b,c,d\}\), fix a suffix \(e,f,\ldots\) of the remaining \(n-4\) symbols, and let \(D\) consist of the 24 orders \((v_1,v_2,v_3,v_4,e,f,\ldots)\) as the first four symbols are permuted.

Fix an orientation of \(A\). For every ordered triple \((x,y,z)\) drawn from \(A\), let \(t\) be the omitted fourth symbol and set
\[
\boxed{b(x,y,z)=\operatorname{parity}(x,y,z,t).}\tag{2}
\]
Reversal of the triple swaps its outer entries and complements the bit. Moreover if \(t=b(v_1,v_2,v_3)\), then \(b(v_2,v_3,v_4)=1-t\), because rotating the four-symbol permutation by one place is odd.

Set \(b(v_3,v_4,e)=1\) for every two distinct \(v_3,v_4\in A\), and set \(b(v_4,e,f)=0\) for every \(v_4\in A\). Give all later consecutive triples of the fixed suffix color zero. Each prescription concerns an independent reversal orbit, apart from the deliberately linked inside-\(A\) triples (2). Hence it extends to a legal reversal-odd coloring of all distinct triples. Every flag of \(D\) has color word
\[
\boxed{(t,1-t,1,0,0,\ldots,0).}\tag{3}
\]
For \(t=0\), the switches are at positions \(1,3\); for \(t=1\), at \(1,2,3\). Thus every flag is bad and its extreme switch-prefix ranks are \(2,4\).

The prefix \(Z_4=\sum_{x\in A}e_x-(4/n)\mathbf1\) is fixed across the 24 orders. For every two-element subset \(S\subset A\), the complementary pair satisfies \(Z_2(A\setminus S)=Z_4-Z_2(S)\). Consequently
\[
\boxed{Z_2(A\setminus S)\wedge Z_4
=-Z_2(S)\wedge Z_4.}\tag{4}
\]
Each subset occurs as the first two symbols of four orders. The contributions of complementary subsets therefore cancel in the sum (1), and every wedge is nonzero by linear independence of prefix vectors. \(\square\)

**Proposition 2 (Grassmannian distinction).** Although the 24 bivectors surround zero, all 24 associated oriented planes contain the fixed line \(\mathbb R Z_4\). The space of oriented two-planes containing this line is \(S^{n-3}\). For \(n\ge6\), \(\pi_2(S^{n-3})=0\), so any three-cell boundary map that remains inside this common-factor sphere can be filled there.

*Proof.* Fix the orientation of \(\mathbb RZ_4\). An oriented plane containing it is specified by a unit transverse vector in \(W\cap Z_4^\perp\), which has dimension \(n-2\). Its unit sphere is \(S^{n-3}\), and this sphere is 2-connected when \(n\ge6\). \(\square\)

**Scope.** The local convex-carrier method is sharp through rank two for unrestricted boundary colorings. A three-cell can have all-bad flags and antipodal extreme-switch wedges. This example does not by itself produce a nontrivial obstruction to extending a map into the oriented Grassmannian. Coherence between adjacent cells, and the nonzero second homotopy of the full Grassmannian, remain the next proof targets.
