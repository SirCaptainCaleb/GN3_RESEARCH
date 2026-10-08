# Exact NORI grand equivalence: complementary monochromatic support regions with reversed two-direction tails

# Exact COLOR-FREE complementary-tail reachability equivalence for active NORI

Let \(Q_n\) carry an ordered-three-face binary coloring satisfying the ACTIVE antipodal-reversal axiom
\[
c(\bar F,\operatorname{rev}\pi)=1-c(F,\pi).
\]
Along a directed geodesic, the color of each window of three successive distinct coordinate changes is the color of the physical ordered three-face containing that window. Let \(n\ge4\).

For an ordered pair \(J=(a,b)\) of distinct coordinate directions, write \(D_J=[n]\setminus\{a,b\}\). Define the **UNCOLORED monochromatic geodesic terminal-memory reachability region**
\[
\mathcal R_J(x)=\bigl\{U\subseteq D_J,\ |U|\ge1:\ 
\exists\text{ a directed monochromatic three-face-window geodesic from root }x
\text{ with direction word }(u_1,\ldots,u_{|U|},a,b)
\text{ for some ordering of }U\bigr\}.
\]
The word monochromatic means that ALL its three-face window colors are the same, of EITHER color. Its terminal two-direction memory is J. NO color index belongs to the region label.

**MAIN THEOREM (EXACT NORI GRAND-CLOSURE EQUIVALENCE).** The following are equivalent:

(i) There exists a full antipodal n-edge geodesic whose ordered-three-face window colors change at most once.

(ii) There exist a root x, an ordered pair of directions J=(a,b), and nonempty disjoint supports U,V⊆D_J such that
\[
U\sqcup V=D_J,\qquad
U\in\mathcal R_{(a,b)}(x),\qquad
V\in\mathcal R_{(b,a)}(x).
\]
Equivalently, with complement relative to D_J,
\[
\boxed{\exists x,\ J:\ 
\mathcal R_J(x)\cap
\{D_J\setminus V:V\in\mathcal R_{\operatorname{rev}J}(x)\}
\ne\varnothing.}
\]
In words: TWO MONOCHROMATIC GEODESICS FROM THE SAME ROOT, of arbitrary and possibly different colors, have coordinate supports covering [n], overlapping in EXACTLY two coordinates a,b, with reversed terminal ordered pairs (a,b) and (b,a). That coincidence is necessary and sufficient for an at-most-one-change full antipodal geodesic.

**Proof (ii⇒i, actual splice with no uncontrolled windows).** Choose the two monochromatic directed geodesics
\[
A=(u_1,\ldots,u_s,a,b),\qquad
B=(v_1,\ldots,v_t,b,a)
\]
starting at x, where U={u_1,...,u_s}, V={v_1,...,v_t}, s,t>=1, and U,V,{a,b} are disjoint and partition [n]. Let their window colors be q and r, respectively. The endpoint of B is \(x\oplus(V\cup\{a,b\})\). Its antipodal reversal
\[
\Theta B=(\overline{\operatorname{end}(B)},\ldots,\bar x)
\]
begins at
\[
\overline{x\oplus(V\cup\{a,b\})}=x\oplus U,
\]
has direction word \((a,b,v_t,\ldots,v_1)\), and has ALL windows color \(1-r\) by the antipodal-reversal axiom.

Take the first s edges of A (direction word U), ending at x⊕U, and append the entire \Theta B. The resulting complete path has direction word
\[
P=(u_1,\ldots,u_s,a,b,v_t,\ldots,v_1),
\]
changes every cube coordinate exactly once, and joins x to bar x. Its FIRST s ordered-three-face windows lie entirely within A, because its first s+2 edges exactly reproduce A. Therefore they all have color q. Its LAST t windows lie entirely within \Theta B, because its final t+2 edges exactly reproduce \Theta B. Therefore they all have color 1-r. Since s+t=n-2 equals the TOTAL number of ordered-three-face windows of P, these two blocks exhaust all windows. Their colors are \(q^s(1-r)^t\), with ZERO changes when q=1-r and EXACTLY ONE change when q=r. In particular P is good. Note that the two shared directions a,b absorb both junction windows: there are no uncontrolled seam windows. QED.

**Proof (i⇒ii, exact decomposition).** Let P be a full good geodesic from x to bar x, with direction order \(p=(p_1,\ldots,p_n)\) and n-2 window colors changing at most once. Choose an index \(s\in\{1,\ldots,n-3\}\) such that windows 1,...,s have constant color q and windows s+1,...,n-2 have constant color r. If P has exactly one switch, take its location; if P is monochromatic, any such s works. Set
\[
U=\{p_1,\ldots,p_s\},\quad
J=(a,b)=(p_{s+1},p_{s+2}),\quad
V=\{p_{s+3},\ldots,p_n\}.
\]
The prefix A of P with direction word \((p_1,\ldots,p_s,a,b)\) is a monochromatic geodesic from x of window color q, witnessing U∈\mathcal R_J(x). The suffix C of P beginning after the first s edges has direction word \((a,b,p_{s+3},\ldots,p_n)\), ends at bar x, and has window color r. Apply global antipodal reversal to C. The resulting geodesic B begins at \(\overline{\bar x}=x\), has direction word \((p_n,\ldots,p_{s+3},b,a)\), and is monochromatic of color 1-r. Hence V∈\mathcal R_{(b,a)}(x). By construction U,V are nonempty, disjoint and partition D_J. QED.

**Uniformity-k extension.** The same theorem holds for binary colors on ORDERED k-faces satisfying c(bar F, reverse pi)=1-c(F,pi), with k>=1 and n>=k+1. Replace J by an ordered (k-1)-tuple of distinct directions and define \(\mathcal R_J(x)\) by monochromatic k-window geodesics ending with J. Then full antipodal k-window at-most-one-change closure is EXACTLY equivalent to complementary support sets U,V in regions \(\mathcal R_J(x)\) and \(\mathcal R_{\operatorname{rev}J}(x)\), with U∪V=[n]\setminus J. The spliced full path consists of a prefix with U followed by the antipodal reversal of a second branch, and the shared (k-1)-direction terminal memory causes EVERY k-window of the full path to belong to one of the two monochromatic branches. The k=1 case has empty J, recovers the original color-free R(x) complementary-support/antipodal-vertex criterion, and reproduces the monochromatic edge-geodesic strengthening via antipodal rotation.

**CRITICAL STRATEGIC CONSEQUENCE.** The hoped-for topological coincidence for active NORI is now fully specified WITHOUT COLOR LABELS:
\[
\mathcal R_{(a,b)}(x)\cap
\operatorname{complement}_{D_J}(\mathcal R_{(b,a)}(x))\ne\varnothing.
\]
A Tucker/Sperner/Borsuk–Ulam/KKM/Hartman proof may target this exact complementary-support overlap. NO additional two-window seam compatibility is needed once the two branch labels share reversed TWO-DIRECTION TERMINAL MEMORIES. This repairs the earlier overbroad warning that monochromatic reachability pairs in ordered-three-face NORI always require separate bridge-color checking. General arbitrary branch pairs do require it; the precise reversed-tail connector class proven here makes the two junction windows automatically belong to the two monochromatic blocks. The remaining open step is a dimension-independent topological/combinatorial theorem FORCEING existence of these complementary uncolored reachability labels.
