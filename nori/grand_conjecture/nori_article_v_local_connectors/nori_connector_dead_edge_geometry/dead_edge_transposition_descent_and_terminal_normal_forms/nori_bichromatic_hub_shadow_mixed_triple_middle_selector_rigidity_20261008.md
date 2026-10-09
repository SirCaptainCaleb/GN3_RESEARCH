# At a bichromatic hub without opposite-color common edges, every mixed-class ordered face selects its middle edge color

# Bichromatic hub: all mixed-class ordered faces are forced by middle-edge shadow

Let \(n\ge6\) and \(c\) satisfy active NORI antipodal-reversal oddness. Consider the **no-common-edge alternative B** of Item \`nori_center_square_bichromatic_edge_or_antipodally_odd_edge_shadow_20261008\`: no physical cube edge is certified by monochromatic centered four-edge geodesics of **both** colors. Then every certified physical cube edge \(e\) has a unique square-witness color \(\sigma(e)\in\{0,1\}\).

By Item \`nori_antipodal_square_connectedness_forces_bichromatic_connector_hub_20261008\`, some center vertex \(z\) supports centered monochromatic four-geodesics of both colors. Let \(A=A(z)\subset[n]\) consist of cube coordinate directions \(b\) for which the physical edge \(\{z,z\oplus e_b\}\) has square-witness color \(0\), and \(B=B(z)\subset[n]\) those whose edge has witness color \(1\). Both \(|A|\) and \(|B|\) are at least 2, because every connector square involves two distinct middle directions. There is at most one remaining isolated direction by the certified minimum-degree \(n-1\) theorem.

For any ordered triple \((a,b,c)\) of distinct directions, write
\[
h_z(a,b,c)=c(F_z(a,b,c),(a,b,c)),
\]
where \(F_z(a,b,c)\) is the **physical three-face through \(z\)** with those free directions.

**Theorem (mixed-middle rigidity at a bichromatic hub).** Under the above no-common-edge alternative, for every ordered triple \((a,b,c)\) with \(b\in A\cup B\) and at least one of its neighboring directions \(a,c\) in the *opposite* class to \(b\),
\[
\boxed{h_z(a,b,c)=
\begin{cases}
0,&b\in A,\\
1,&b\in B.
\end{cases}}
\tag{1}
\]
Thus every ordered face through a bichromatic hub whose direction triple crosses the two shadow color classes has its color determined **solely by the color of its middle coordinate edge**. This is an honest physical-face identity, not an abstract coloring of permutations. No condition is claimed for a triple entirely within one color class, or for a triple involving the at-most-one isolated direction as the middle coordinate.

**Proof.** If \(b\in A\), \(c\in B\), then no centered four-edge connector with middle pair \(\{b,c\}\) can be monochromatic at \(z\). Such a connector would certify both physical edges in directions \(b,c\) with a common color, contradicting their already distinct singleton colors. For the ordered middle pair \((b,c)\), write
\[
I_a=h_z(a,b,c),\quad O_d=h_z(b,c,d)
\]
for outer directions \(a,d\notin\{b,c\}\). For every \(a\ne d\), \(I_a\ne O_d\). Since \(n-2\ge4\), for any \(a,a'\) choose a \(d\) distinct from both, giving \(I_a=I_{a'}\). Similarly the outgoing \(O_d\) are all equal and opposite the common incoming value. Thus there is a bit \(K_{bc}\) such that
\[
h_z(a,b,c)=K_{bc},\qquad h_z(b,c,d)=1-K_{bc}
\tag{2}
\]
for **every** allowed outer \(a,d\). There is an analogous bit \(K_{cb}\) for the reverse orientation \((c,b)\). Formula (2) holds for every cross pair of \(A,B\), in either order.

Now for \(b\ne b'\in A\), \(c\in B\), evaluate the triple \((b,c,b')\) twice, using the outgoing half of the \((b,c)\) constraint and the incoming half of the \((c,b')\) constraint:
\[
1-K_{bc}=K_{cb'}.
\tag{3}
\]
Likewise for \(c\ne c'\in B\), \(b\in A\), the triple \((c,b,c')\) gives
\[
1-K_{cb}=K_{bc'}.
\tag{4}
\]
Since \(|A|,|B|\ge2\) and \(n\ge6\) with at most one isolated coordinate, **at least one** class has size at least 3. If \(|A|\ge3\), fixing \(c\in B\) and comparing (3) for two distinct \(b,b'\) using a third \(b''\) shows all \(K_{bc}\) are equal as \(b\) varies. Then (3)-(4) show the common value is also independent of \(c\). If \(|B|\ge3\), the symmetric calculation first makes all reverse-oriented \(K_{cb}\) independent of \(c\) and then (3)-(4) make the forward-oriented \(K_{bc}\) constant as well. Thus one bit \(K\) satisfies
\[
K_{bc}=K\quad(b\in A,c\in B),\qquad
K_{cb}=1-K\quad(c\in B,b\in A).
\tag{5}
\]

Choose any existing color-0 connector at \(z\); its two middle directions \(b,b'\) belong to \(A\). Choose **distinct** outer directions \(a,d\in B\), which is possible because \(|B|\ge2\). Equations (2),(5) give
\[
h_z(a,b,b')=K,\qquad h_z(b,b',d)=K.
\]
Hence the centered path with ordered directions \((a,b,b',d)\) is monochromatic of color \(K\) and certifies the same physical middle square \(\{b,b'\}\) already certified in color 0. Alternative B forbids two colors on any physical edge of this square. Therefore \(K=0\), and (5) gives \(K_{cb}=1\).

Finally, take any triple \((a,b,c)\) with the asserted mixed-class adjacency. If \(b\in A,c\in B\), apply the first half of (2) to \((b,c)\) and get \(h_z=K=0\). If \(a\in B,b\in A\), apply the outgoing half of the constraint for \((a,b)\), where \(K_{ab}=1\), and get \(h_z=1-K_{ab}=0\). The cases with \(b\in B\) are symmetric and give 1. This proves (1). \(\square\)

**Consequences and exact research frontier.** A bichromatic hub in shadow alternative B carries a **locally reversal-even middle-coordinate selector** on all mixed-color ordered face triples. (Reversing a mixed triple preserves its middle direction, hence its value in (1).) This is substantial rigidity: the physical face coloring is forced on every triple crossing the two certified direction classes, though the remaining same-class triples can contain genuine defects. Antipodal reversal exchanges the certified 0/1 direction classes at \(\bar z\), so the local rule remains consistent with active global oddness. A possible route to eliminating alternative B is to propagate these mixed-triple identities along certified root moves, using the fact that the underlying physical faces are unchanged when any free direction is toggled. The missing theorem is **coherent propagation of the two direction partitions between different bichromatic hubs**; (1) alone does not imply a common opposite-color square or a full one-change antipodal geodesic.

The statement does not assert all faces depend only on their middle direction; it is precisely restricted to physically witnessed *mixed-class* triples.
