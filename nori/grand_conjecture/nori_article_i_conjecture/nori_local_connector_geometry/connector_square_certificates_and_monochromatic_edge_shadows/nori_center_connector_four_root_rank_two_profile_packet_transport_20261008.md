# Each centered monochromatic connector yields a certified four-root rank-two reachability simplex with twisted antipodal transport

# Exact four-root rank-two reachability packets and the antipodal involution mismatch

Consider active NORI (ordered three-face coloring satisfying \(c(\bar F,\operatorname{rev}\pi)=1\oplus c(F,\pi)\)); the first packet theorem works without antipodal oddness. Fix a monochromatic centered four-edge connector
\[
P_z(a,b,c,d):
\quad z\oplus\{a,b\}\to z\oplus\{b\}\to z\to z\oplus\{c\}\to z\oplus\{c,d\},
\]
where \(a,b,c,d\) are pairwise distinct. Its direction word is \((a,b,c,d)\). Define \(J=(c,d)\), support \(U=\{a,b\}\), and root \(x=z\oplus\{a,b\}\).

**Theorem 1 (genuine rank-two four-root packet).** The **same nontrivial reachability label**
\[
u=(J,U)=((c,d),\{a,b\})
\]
belongs to the uncolored ordered-three-face terminal profile \(L_{x\oplus T}\), for **every** \(T\subseteq\{b,c\}\):
\[
\boxed{\forall T\subseteq\{b,c\}:\quad
\{a,b\}\in R_{(c,d)}(x\oplus T).}
\tag{1}
\]
Each membership is witnessed by an actual monochromatic four-edge geodesic with the **same ordered physical three-faces** and the same color. Hence in the signed-root reachability nerve, the four positive-root vertices
\[
(x,+),\ (x\oplus b,+),\ (x\oplus c,+),\ (x\oplus\{b,c\},+)
\]
span a genuine 3-simplex witnessed by a common rank-two (non-singleton) label; this remains meaningful after all universal singleton labels are removed from the positive-root profiles.

**Proof.** The two window triples of \(P_z\) are \((a,b,c)\) and \((b,c,d)\); **both** have \(b,c\) free. Replacing \(z\) by \(z\oplus T\), \(T\subseteq\{b,c\}\), translates every path vertex by \(T\), which only changes free-coordinate bits on both window faces and therefore leaves the actual ordered faces and their colors unchanged. The direction word, support \(U=\{a,b\}\), and terminal pair \((c,d)\) remain fixed. Its initial vertex is \(x\oplus T\). This proves all four membership certificates. \(\square\)

**Theorem 2 (twisted antipodal transport of a connector packet).** Under the active NORI oddness law, the antipodal reversal of \(P_z(a,b,c,d)\) is monochromatic with complementary color, centered at \(\bar z\), and has order \((d,c,b,a)\). Its associated terminal label and root are
\[
u^\Theta=((b,a),\{d,c\}),\qquad
x^\Theta=\bar z\oplus\{d,c\}.
\tag{2}
\]
Writing \(T_4=\{a,b,c,d\}\), this root satisfies the exact transport identity
\[
\boxed{x^\Theta=\bar x\oplus T_4.}
\tag{3}
\]
The partner four-root packet is
\[
\forall T\subseteq\{b,c\}:\quad
\{d,c\}\in R_{(b,a)}(\bar x\oplus T_4\oplus T).
\tag{4}
\]

Crucially, **the involution \(\Theta\) on physical four-edge witnesses is NOT the terminal-label complement involution** used by the exact reversed-tail grand theorem:
\[
\tau((c,d),\{a,b\})
=\big((d,c),[n]\setminus\{a,b,c,d\}\big)
\ne ((b,a),\{d,c\})=u^\Theta.
\tag{5}
\]
Equality fails already at the ordered terminal pair. Thus taking antipodal mates of local rank-two packets alone cannot produce the same-root complementary-support collision.

**Proof.** Reversing the physical vertex sequence and complementing every vertex reverses the direction order and complements both ordered-window colors by the active axiom. Its new root is the antipode of the original endpoint \(z\oplus\{c,d\}\), namely \(\bar z\oplus\{c,d\}\). With \(x=z\oplus\{a,b\}\), this equals \(\bar x\oplus\{a,b,c,d\}\), proving (3). Apply Theorem 1 to the reversed path for (4). The explicit grand-collision involution \(\tau\) keeps the *original terminal direction set* but reverses its order and complements the *outside support*; (5) follows by direct substitution. \(\square\)

**Consequence for a topological fixed-point program.** The certified center-square complex provides unconditional **rank-two four-root profile simplices**, one for every monochromatic centered connector. By centered pentagon parity, in every set of five directions at every hub such a simplex exists. These tetrahedra supply genuinely witnessed cubical incidence absent from purely abstract singleton-shore profile nerves. However physical path reversal changes both the **root endpoint** and the **terminal direction pair** according to (2)-(3). A correct equivariant map into the full reversed-tail collision complex must therefore record BOTH initial and terminal memories, or implement a further certificate-preserving transport that compensates for the four-coordinate shift in (3) and changes terminal pair from \((b,a)\) to \((d,c)\). Simply identifying a connector packet with its antipodal counterpart as opposite *complementary* support labels is mathematically invalid. The rank-two packet and transport formulas are fully proved; the global index and grand extraction remain open.
