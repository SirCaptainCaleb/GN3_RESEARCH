# Every bichromatic hub locally forces a doubly-certified incident edge or uniform cross-class near-spanning cap obstruction

# Every bichromatic hub has a local common-edge or uniform-cap alternative

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
