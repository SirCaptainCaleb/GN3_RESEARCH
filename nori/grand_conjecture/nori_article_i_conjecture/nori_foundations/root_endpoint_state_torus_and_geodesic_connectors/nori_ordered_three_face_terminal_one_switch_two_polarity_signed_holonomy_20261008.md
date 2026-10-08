# Active NORI: terminal one-switch paths induce a signed ordered-window blocker graph with antipodal reversal

# Signed terminal-window blocker holonomy for the ACTIVE ordered-three-face NORI conjecture

Let n>=5, and let c(F,pi)∈{0,1} be an ordered-three-face coloring satisfying
\[
c(\bar F,\operatorname{rev}\pi)=1-c(F,\pi).
\]
Let m be the largest length (number of distinct-direction edges) of any directed cube geodesic whose successive ordered-three-face window colors change at most ONCE. Assume no full antipodal n-geodesic has this property, so 4<=m<n. Write P=(v_0,...,v_m), with direction word p=(p_1,...,p_m), and its window word w(P)=(w_1,...,w_{m-2}).

**Theorem 1 (maximal one-switch segments are terminal at BOTH ends).** Every length-m one-switch geodesic P has EXACTLY ONE window-color change:
\[
w_1(P)\ne w_{m-2}(P).
\]
For each unused coordinate i not among p_1,...,p_m, define the two ordered-three-face windows which would be created by extending P at the left or right endpoint:
\[
L_i(P)=\big(F(v_0;\{i,p_1,p_2\}),(i,p_1,p_2)\big),
\]
\[
R_i(P)=\big(F(v_m;\{p_{m-1},p_m,i\}),(p_{m-1},p_m,i)\big).
\]
Here F(v;W) is the W-free cube face containing v. Let a(P)=w_1(P). Then the terminal blocker identities are
\[
\boxed{c(L_i(P))=1-a(P),\qquad c(R_i(P))=a(P).}
\]

**Proof.** A length-four geodesic has only two three-edge windows and automatically at most one change, so m>=4. If P had no change, prepending/appending any unused coordinate creates exactly one new three-edge window, hence would still have at most one change, contrary to the maximality of m. Thus P has exactly one change and its first and last window colors differ, because the palette is binary. If c(L_i)=a, prepending i preserves the first-window transition and keeps the total at one; if c(R_i)=w_last=1-a, appending i does likewise. Both produce genuine geodesics of length m+1 because i is unused. Therefore c(L_i)=1-a and c(R_i)=1-w_last=a. QED.

**Theorem 2 (COLOR-FREE signed incidence obstruction).** Let \(\mathcal P_m\) be the family of all geometrically specified directed length-m geodesics whose color words have at most one change; do not include the color word in a state label. Construct a signed multigraph J_m^* on these states as follows: whenever the same EXACT ordered-three-face (F,pi) occurs among their terminal blockers, join the two path states, with sign
- 0 if that blocker is left for both paths or right for both;
- 1 if that blocker is left for one path and right for the other.

Then a(P) is a globally consistent \(\mathbb F_2\)-potential:
\[
a(P')=a(P)\oplus \operatorname{sign}(PP')
\]
along every such incidence edge. Hence every signed closed walk has EVEN total sign. Contrapositively, if a candidate no-closure reachability construction forces an ODD signed cycle in J_m^*, the grand ordered-three-face NORI conjecture follows.

**Proof.** A shared physical ordered window has one fixed color. A left blocker of P has color 1-a(P), while a right blocker has color a(P). Equating the two expressions yields a(P)=a(P') in the same-side case, and a(P)=1-a(P') in the mixed-side case. Telescoping these equalities around a closed walk forces even sign. QED.

**Theorem 3 (antipodal-reversal is a zero-sign state symmetry).** Define the reversal-antipodal involution on directed path states
\[
\Theta(P)=(\bar v_m,\bar v_{m-1},...,\bar v_0).
\]
Then \(\Theta\) preserves \(\mathcal P_m\), is fixed-point-free there, and
\[
w(\Theta P)=\mathbf1-\operatorname{rev}w(P),\qquad a(\Theta P)=a(P).
\]
For each i unused by P, \(\Theta\) sends the right blocker \(R_i(P)\) to the antipodal-reversed left blocker \(L_i(\Theta P)\), and vice versa. Adding a sign-0 edge between P and \Theta(P) therefore preserves the consistent potential. In particular, a geometrically forced ODD signed path from P to \Theta(P) made only of incidence edges would contradict terminality and establish the grand conjecture.

**Proof.** Reversing a path and complementing every cube vertex sends each ordered three-face window to its antipodal three-face with reversed coordinate order, in reverse temporal order. NORI oddness therefore complements and reverses w. Since w has exactly one change, its endpoints are complementary, so the initial color of \Theta P is 1-w_last(P)=w_first(P). The involution reverses the distinct-coordinate direction word, so it fixes no directed path of length m>=4. The exterior faces of terminal windows transform under the same antipodal reversal, exchanging the two ends. QED.

**Strategic meaning.** This transfers the user's reachability/antipodal-label program to the ACTIVE ordered-three-face conjecture with exact two-direction endpoint memory. Unlike the simpler edge case, there are TWO terminal-blocker polarities. Their relative signs encode the permitted single switch; NO edge color is attached to a reachability-state label. One may seek a Tucker/Hex/KKM/connector forcing theorem that makes the terminal-window incidence graph have odd signed holonomy (possibly using the zero-sign Θ symmetry). This is an exact conditional extraction theorem. Forcing the relevant odd cycle remains open.
