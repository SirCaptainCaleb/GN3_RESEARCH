# Bichromatic six-move hubs and two-color connector density

# Bichromatic six-move hubs and two-color connector density

A vertex supporting monochromatic four-geodesics in both colors is a bichromatic hub. Its incoming and outgoing directions support many genuine six-edge paths that are at most one switch away from monochromaticity. Quantifying those paths reveals forced root packets and separators under the additional hypothesis that no physical edge is certified in both colors.

## The unrestricted NORI root-chart gap has TWO logically independent missing obligations

The proved nonlinear fault robustness theorem nori_quadratic_nonlinear_triple_fault_robust_antipodal_chart_closure_20261008 is substantial, but DOES NOT itself approach arbitrary NORI through chart connectivity alone. Its exact proof requires TWO separate parity-reference features, both unavailable for an arbitrary active ordered-three-face coloring:

**(I) PREFIX POLARIZATION / SUFFIX FORCING.** Fix an ordered list p of outside directions D=[n]\K and a root x where its D-prefix is monochromatic. To force the three exceptional terminal windows to ALTERNATE under hypothetical grand failure, the proof flips ONE K-coordinate s_1 which is free in each of the last three windows, hence does not change their actual physical ordered-face colors. What is ALSO necessary is that this same bit flip sends ALL preceding D-only window colors from q to 1−q, keeping the preceding block monochromatic. Full exterior parity supplies precisely this property: each early face has s_1 as an exterior coordinate, so toggling its root bit flips every early color. An arbitrary NORI coloring need not have this property. NORI oddness only relates (F,π) to (bar F,rev π), not two D-only faces differing in a SINGLE outside K-bit at the same orientation.

**(II) ANTIPODAL CHART CONNECTIVITY.** Even if a root-specific antipodally odd suffix bit t(S) is successfully manufactured, to contradict it one needs a chain of ACTUAL monochromatic-prefix reachability witnesses whose first exceptional physical ordered faces agree and whose roots connect S to bar S. The clean parity baseline gives the six-periodic root code S_{p_{j+3}}=1−S_{p_j}, whose middle-layer chart graph has this connectivity. For arbitrary c, the set of monochromatically reachable prefixes and their physical face incidence may be sparse, disconnected, or lack this root-coupled structure. Connectedness of the separate physical certified-four-square complex does NOT automatically imply connectivity of a terminal-memory-compatible root chart.

**THEOREM (safe abstract two-obligation NORI extraction).** Fix K of size3, D its complement. Suppose a collection \mathscr P of D-direction geodesic witnesses possesses all the following genuine properties:
(a) For every outside root S in a set G invariant under complementation, there is a selected D-order p and K-root assignment with a monochromatic D-prefix, and for EACH of the 6 orders of K the corresponding first three exceptional windows refer to the actual physical colored faces.
(b) Each selected D-order witness is **polarized**: there exist two K-root choices yielding identical actual exceptional three-window colors but opposite uniform monochromatic prefix bits. Consequently under no full good geodesic the last three exceptional windows have at least2 internal changes, hence alternate.
(c) The six-order/reversal physical-face comparisons align these alternating suffixes into one well-defined label t:G→F2, independent of selected p, with t(bar S)=1−t(S).
(d) The graph on G linking selected root witnesses with IDENTICAL actual first exceptional physical ordered faces has a component containing S and bar S.
Then the full NORI one-switch conclusion follows.

**Proof.** Under no full good path, (b) forces the alternating suffix for each selected witness by comparing opposite prefix colors against the SAME suffix. Conditions (c) and (d) make t locally constant along a certified chain from S to bar S, while antipodal oddness makes it complementary at the two endpoints. Contradiction. QED.

**CAUTION.** The theorem is a modular, CONDITIONAL extraction theorem. Conditions (b) and (c) are NOT inherent to arbitrary monochromatic-prefix reachability and must be genuinely proved from each new construction; condition (d) is a separate topological forcing obligation. Simply declaring an uncolored reachability set R(x), an antipodal involution, or a connected lower-dimensional certified square complex does NOT discharge either obligation. An alternative global strategy is to target the already proved EXACT color-free reversed-two-tail complementary-support intersection, which bypasses the need for these polarization hypotheses entirely and automatically splices a full one-switch path.

**Main direction after latest robust closure.** Seek a topological connector theorem on actual reversed-terminal-memory reachability basins that forces complementary supports, rather than extrapolating the reference-dependent parity-root synchronization to unrestricted face colors.

## Every bichromatic hub has a local common-edge or uniform-cap alternative

Let \(n\ge6\) and let \(c\) satisfy the active NORI physical ordered-three-face axiom \(c(\bar F,\operatorname{rev}\pi)=1\oplus c(F,\pi)\). Let \(X_c\) be the genuine certified-middle-square complex of NORI. At a cube vertex \(z\), let \(K_z(i)\subseteq\{0,1\}\) be the set of colors \(q\) of actual centered monochromatic four-edge connectors whose middle-pair square contains the **incident physical cube edge** \(\{z,z\oplus e_i\}\). Every incident certified square carries the same certificate color at each of its four vertices; by the centered-link theorem all but at most one \(K_z(i)\) are nonempty.

Call \(z\) **bichromatic** if \(\bigcup_i K_z(i)=\{0,1\}\). Every valid active NORI coloring has at least one bichromatic \(z\), by the proved connected-certified-square topological overlap theorem.

**Theorem (local hub dichotomy, without any global shadow restriction).** For **every** bichromatic \(z\), one of the following alternatives holds.

**(I) A local color-overlap edge.** There exists a direction \(i\) such that \(K_z(i)=\{0,1\}\). This is an actual physical edge at \(z\), lying in two genuine centered monochromatic-connector squares of opposite colors.

**(II) A locally rigid two-color direction partition.** All nonempty \(K_z(i)\) are singleton sets. Put
\[
A_z=\{i:K_z(i)=\{0\}\},\quad B_z=\{i:K_z(i)=\{1\}\}.
\]
Then \(|A_z|,|B_z|\ge2\), \(|A_z|+|B_z|\ge n-1\), and for **every** actual ordered three-face through \(z\) with distinct ordered free directions \((u,v,w)\), when \(v\in A_z\cup B_z\) and one of \(u,w\) belongs to the opposite class,
\[
\boxed{c(F_z(\{u,v,w\}),(u,v,w))=\mathbf1_{\{v\in B_z\}}.}
\tag{1}
\]
In particular, for every mixed omission \(a\in A_z,\ b\in B_z\), every \(i\notin\{a,b\}\), and every choice of the omitted two starting bits above the projected \(U\)-root \(r=z|_U\), \(U=[n]\setminus\{a,b\}\), the actual cap labels are **uniform**:
\[
\boxed{c(F(x;\{a,b,i\}),(a,b,i))=1,\quad
c(F(x;\{a,b,i\}),(b,a,i))=0.}
\tag{2}
\]
Consequently, **a single monochromatic \(U\)-spanning geodesic from any of those four parallel-facet roots directly yields a full NORI geodesic with at most one color change**. Under hypothetical grand failure, all \(4|A_z||B_z|\) such root/bundle choices are free of any monochromatic \(U\)-spanning geodesic, with at least \(2(n-3)\) distinct forbidden mixed omission pairs.

**Proof.** If (I) is false, the sets \(A_z,B_z\) are disjoint. Each of the two certified monochromatic four-path colors at \(z\) certifies a physical square and hence at least two distinct incident coordinate directions; thus both classes have size at least two. At most one direction is isolated by the established \(n-1\) certified-degree theorem, giving \(|A_z|+|B_z|\ge n-1\). Every cross middle pair \(v\in A_z,w\in B_z\) is **uncertified at \(z\)**: any monochromatic middle-square certificate of color \(q\) would place the same bit in both already oppositely certified edge-label sets \(K_z(v)=\{0\}\) and \(K_z(w)=\{1\}\).

For a fixed ordered cross pair \((v,w)\), write \(I_t=c(F_z(\{t,v,w\}),(t,v,w))\), \(O_s=c(F_z(\{v,w,s\}),(v,w,s))\) for distinct outer \(t,s\notin\{v,w\}\). Since every centered four-path \((t,v,w,s)\), \(t\ne s\), is nonmonochromatic, \(I_t\ne O_s\). At least three outer coordinates exist since \(n\ge6\); comparing values using a common third outer direction forces every \(I_t\) to equal one bit \(K_{vw}\) and every \(O_s=1-K_{vw}\). Repeating this for the reverse cross orientation gives \(K_{wv}\). Shared physical ordered-face triples with two \(A_z\) and one \(B_z\), or vice versa, yield exactly the compatibility equations
\[
K_{wv'}=1-K_{vw}\quad(v,v'\in A_z,\ w\in B_z,\ v\ne v'),
\]
\[
K_{v w'}=1-K_{wv}\quad(w,w'\in B_z,\ v\in A_z,\ w\ne w').
\]
Since both classes have size at least two and at least one has at least three, elementary elimination of these equations gives a common bit \(K\) on all \(A\to B\) cross pairs and bit \(1-K\) on all \(B\to A\) cross pairs. Choose a genuine color-0 certified middle square at \(z\) with middle pair \(v,v'\in A_z\). Choose distinct outer \(w,w'\in B_z\). The ordered four-path \((w,v,v',w')\) has both window colors \(K\) by the cross-pair constraints, so it is a monochromatic certificate of color \(K\) on the SAME physical square that was already certified color 0. Since (I) is false, \(K=0\). The resulting incoming/outgoing cross-triple formulas yield (1), by whether the middle coordinate is in \(A_z\) or \(B_z\).

For \(a\in A_z,b\in B_z\), the ordered cap triples \((a,b,i)\), \((b,a,i)\) have their middle direction respectively in \(B_z\), \(A_z\), and an opposite-class adjacent direction. Thus their colors at \(z\) are 1 and 0. The physical face has both \(a,b\) free, so varying those two bits does not alter its identity, proving (2) simultaneously in all four parallel facets.

If \(P\) is a monochromatic full \(U\)-geodesic from one such facet root, color \(q=0\), prepend \((a,b)\) starting at the appropriately shifted full root. The new first cap has color 1 and the first original face color is 0; the one intermediate new window has arbitrary color, so the resulting full word has exactly one change. If \(q=1\), append \((b,a)\), whose final cap is \(1-c(F(x;\{a,b,j\}),(a,b,j))=0\) by the active antipodal-reversal law, and again there is exactly one change regardless of the intermediate color. Thus either monochromatic \(P\) forces grand closure.

Finally if \(|A_z|=p, |B_z|=q\), \(p,q\ge2\), \(p+q\ge n-1\), then \(pq\ge2(n-3)\). This counts distinct mixed omission pairs. \(\square\)

**Strength over earlier results.** Previously the mixed-direction selector theorem and uniform-cap blockade were stated inside global square-edge shadow alternative B, where *no* physical edge anywhere in the cube has both certification colors. The proofs actually use only **lack of a doubly certified incident edge at the chosen bichromatic center**. This local theorem therefore applies even in colorings where alternative A occurs elsewhere. It supplies a site-by-site topological obstruction to combine with genuine opposite-color edge overlaps, without an artificial global case split.

**Remaining closure obligation.** The theorem does not guarantee a monochromatic near-spanning \(U\)-geodesic for any prescribed projected root. To prove full NORI, one would need a fixed-point/connector principle forcing, for some bichromatic hub, either (I) an opposite-color common-edge configuration whose witnesses can be extended compatibly, or (II) one of the many forbidden near-spanning monochromatic cores. An opposite-color shared edge alone is also not yet a full-geodesic certificate. The new statement is exact and dimension independent, not grand closure.

## Topological global consequence: monochromatic six-geodesic hubs meet every certified antipodal path in the unique-color edge-shadow regime

Let n>=10 and let c be an ACTIVE NORI binary coloring of physical ordered three-faces. Assume the GLOBAL unique-color certified-square edge-shadow case B: no physical cube edge receives square certificates from monochromatic centered four-edge connectors of both colors. Let X_c be the genuine certified-center-square complex, let G_c=X_c^(1) be its spanning cube subgraph, and write M=E(Q_n)\E(G_c). By proved NORI theorems, M is an antipodally invariant matching, G_c is connected, and every vertex has certified-center degree at least n−1. Define the bichromatic hub set
\[
B=\{z: \text{genuine centered monochromatic four-edge connectors of BOTH colors exist at z}\},
\]
and the MONOCHROMATIC SIX-HUB set
\[
H_6=\{z: \text{there exists an ACTUAL monochromatic six-edge cube geodesic with ALL FOUR ordered-three-face windows physically containing z}\}.
\]

**THEOREM 1 (unavoidable monochromatic six-hub separator).** Under the stated assumptions,
\[
\boxed{B\subseteq H_6.}
\]
Moreover every G_c-graph path from any cube vertex x to its antipode bar x intersects H_6. In particular, for EVERY root x∈Q_n there exists a FULL antipodal n-edge cube geodesic from x to bar x (whose edges all belong to G_c) that passes through at least ONE vertex z∈H_6.

**Proof.** At each bichromatic hub z, the no-common-edge assumption splits the incident certified directions into two classes A,B, each of size at least2, of total size at least n−1. Since n>=10, the larger class has cardinality at least5. The proved five-majority odd-cycle theorem (Item nori_majority_five_bichromatic_hub_odd_cycle_forces_monochromatic_six_20261008) constructs a genuine monochromatic six-edge geodesic through z. Thus B⊆H_6.

The separate, unconditional bichromatic-hub antipodal separator theorem (Item nori_bichromatic_mono_four_hubs_hit_every_certified_antipodal_path_density_20261008) states that EVERY G_c-path from x to bar x meets B, since physical square certificates share a common monochromatic color across each G_c-edge, but the hub singleton color label flips under antipodality. Such a path consequently meets H_6.

Finally the general cube matching-avoidance theorem (Item nori_matching_avoidance_every_root_full_geodesic_20261008) says any cube matching that is NOT the entire set of parallel edges of one coordinate can be avoided by SOME full antipodal geodesic from ANY prescribed root x. Our matching M cannot be that entire parallel matching because G_c is CONNECTED and would otherwise split into opposite coordinate facets. Therefore from every x there is a full M-avoiding geodesic P(x), which is a G_c-path. It meets H_6. QED.

**THEOREM 2 (quantitative density of monochromatic six-hubs).** The same model satisfies
\[
\boxed{|H_6|\ge |B|\ge
\frac{2^n-2|M|}{n+1}.}
\]
Both hub sets are antipodally invariant. In the special case M=∅, at least a fraction 1/(n+1) of all Q_n vertices are centers of GENUINE monochromatic six-edge geodesics:
\[
|H_6|\ge 2^n/(n+1).
\]

**Proof.** Apply B⊆H_6 to the existing quantitative bichromatic-hub separator bound. Global antipodal reversal carries every monochromatic six-edge path through z to a complementary-color monochromatic six-edge path through bar z; hence H_6 is antipodally invariant. QED.

**Conceptual topological result.** This produces, in one structural branch of arbitrary ACTIVE NORI colorings, a physical Q_n antipodal hitting set of ACTUAL SIX-edge monochromatic paths. Its strength is global and root-mobile: the center of such a path is encountered by a fully spanning antipodal route from EVERY starting cube root, but the mono-six direction word may not match the route's entering/leaving used-direction support, and the route's unrelated local certificates need not share the mono-six color. The unproved GRAND-EXTRACTION step is to synchronize at least one of these mono-six hubs with a full legal root/terminal-memory geodesic so that its entire ordered-three-face word has <=1 switch. This theorem does not assert such synchronization.

Hub abundance is a robust local theorem. Extending those six-move witnesses to a full n-move geodesic without accumulating extra window defects is the outstanding global problem.
