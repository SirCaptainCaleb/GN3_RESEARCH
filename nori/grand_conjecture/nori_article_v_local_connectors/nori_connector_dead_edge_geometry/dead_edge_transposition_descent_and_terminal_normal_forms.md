# Dead-edge transposition descent and terminal normal forms

# Dead-edge transposition descent and terminal normal forms

Let the switch defect of a full geodesic be the number of changes in its consecutive ordered-three-face color word. At a dead physical edge, swapping adjacent travel directions can change only a controlled set of windows. The resulting local exchange inequalities allow a variational descent in the order/root space while preserving the full geodesic property.

## Bichromatic hub: all mixed-class ordered faces are forced by middle-edge shadow

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

THEOREM (ANTIPODAL FOUR-SPACING OF DEAD EDGES). Let n>=5 and let c satisfy the ACTIVE NORI c(bar F,reverse pi)=1-c(F,pi) on ordered physical three-faces of Q_n. Let M be the set of physical cube edges traversed by NO genuinely monochromatic four-edge geodesic. The proved local rigidity theorem says that any TWO dead edges in DISTINCT coordinate directions have physical endpoint-set Hamming distance at least THREE; also M is invariant under cube antipodality.
Fix any FULL directed n-edge antipodal geodesic P(x,p) with physical edges e_1,...,e_n, where each coordinate direction occurs once. Complete it to the simple symmetric 2n-edge belt by following the antipodal translates bar e_1,...,bar e_n in the SAME coordinate order. The dead-edge status of each belt edge is antipodally repeated, so its 2n-bit indicator is (d_1,...,d_n,d_1,...,d_n), where d_k=1 iff e_k is dead.
If two different positions k,l in [n] are both dead, their coordinate directions differ. Write their CYCLIC index distance s=min(|k-l|,n-|k-l|). If s<=3, there are two dead belt edges of distinct directions at cyclic edge-index separation s<=3: choose e_k and e_l if |k-l|=s, or e_l and bar e_k if n-|k-l|=s. On the 2n-edge cube belt the nearest endpoints of these two edges are joined by a segment containing at most s-1<=2 cube edges. Thus their physical endpoint-set Hamming distance is <=2, contradicting the different-direction dead-edge separation theorem. Therefore
  min(|k-l|,n-|k-l|)>=4
for every pair of dead positions k,l.
COROLLARIES. The dead positions form a 4-separated code on the cyclic n-position set, so their number is at most floor(n/4) (for n<8, at most one). This is strictly stronger than the matching-only bound ceil(n/2). When a hypothetical active NORI counterexample in dimensions <=10 has any dead edges, the separately proved mixed-dead-direction extraction theorem forces all dead edges to lie in ONE coordinate direction. Every full antipodal geodesic uses that direction exactly once; hence in a hypothetical counterexample on Q_5,...,Q_10 every full geodesic has AT MOST ONE dead physical edge.
The rule is an all-dimensional COLOR-INDEPENDENT packing fact once dead-edge rigidity and active antipodal reversal are in place. It does not imply the full one-switch conjecture, but it removes complex multi-dead configurations from each root/permutation chamber, narrowing the cyclic-seam and adjacent-swap descent analysis.

THEOREM (SHARP Q8 DEAD-HUB POLARITY BOOTSTRAP). In EVERY binary coloring of the physical ORDERED three-dimensional faces of Q8, with NO antipodal/reversal constraint assumed, if some physical cube edge e_i={z,z xor i} belongs to NO genuinely monochromatic directed four-edge geodesic, then Q8 has a FULL antipodal eight-edge geodesic with AT MOST ONE color change among its six ordered-three-face windows. Consequently any hypothetical active NORI Q8 counterexample is COMPLETELY DEAD-EDGE-FREE. This strengthens the earlier Q8 at-most-one-antipodal-dead-pair obstruction to NO dead edges.
PROOF. The exact dead-edge rigidity theorem assigns one bit t such that EVERY ordered three-face containing z and whose free triple omits i has color t (similarly at z xor i). Set D=[8] minus {i}, |D|=7. Argue by contradiction: suppose EVERY full eight-edge geodesic has at least two window-color changes.
STEP 1 (FORCED ONE-SHELL ANTIPOLARITY). Fix ANY r in D and ordered distinct (a,b,c) in D minus {r}. Let (u,v,w) be the other three directions of D, excluding {r,a,b,c}. Consider the full eight-coordinate order (u,v,w,r,a,b,c,i), starting from x=z xor {u,v,w}, so after the first three moves the path reaches z. Its FIRST FOUR ordered-three-face windows, (u,v,w),(v,w,r),(w,r,a),(r,a,b), ALL contain z, have no free direction i, and are therefore color t. Its FIFTH face window is (a,b,c), through the vertex z xor r; its SIXTH is (b,c,i), of arbitrary color. For the full word (t,t,t,t,X,Y) to have >=2 changes, it is NECESSARY that X=1-t and Y=t. Since r,a,b,c were arbitrary, this forces
  for EVERY r in D and ALL ordered distinct a,b,c in D minus {r}: c(F(z xor r;{a,b,c}),(a,b,c))=1-t.
STEP 2 (SECOND HUB MAKES A GOOD PATH). Choose distinct r,s in D. Choose any six directions q1,...,q6 giving an order of D minus {r}, with q4=s; write q5=a,q6=b. Put y=z xor r, and start a directed full eight-edge path at y xor {q1,q2,q3} using order (q1,q2,q3,s,a,b,r,i). Its first SIX edges are centered at y after three moves, and their FIRST FOUR ordered-three-face windows are all through y and omit r and i, so by the one-shell polarity from Step1 they have color 1-t. Its FIFTH ordered window has directions (a,b,r) and is a physical face through the vertex y xor s=z xor {r,s}. Because r is a FREE coordinate of this window, the same physical face contains z xor s. Its ordered free triple (a,b,r) excludes i and s, so Step1 with hub z xor s says its color is ALSO 1-t. The SIXTH, final window has arbitrary color. Therefore the full eight-edge antipodal geodesic has window word (1-t,1-t,1-t,1-t,1-t,Y), with at most ONE color change, contradiction. QED.
GEOMETRIC MECHANISM. A dead-edge hub yields a monochromatic star on all ordered faces avoiding its direction. Failure of one-switch closure forces the next outer coordinate shell to have COMPLEMENTARY uniform color on triples not containing the shell direction. This forced shell is itself rich enough to produce a new monochromatic six-edge hub geodesic whose first extension window is physically IDENTICAL to a face on a neighboring shell hub, contradicting the putative necessary color flip. The proof is fully face-geometric and does not use numerical enumeration or the active NORI parity condition.
SCOPE. It leaves arbitrary DEAD-FREE ordered-three-face colorings of Q8 unresolved by this argument. In dimensions larger than 8, six-window hub propagation leaves more than two uncontrolled tail windows and requires an additional memory-boundary forcing lemma.

The descent yields a terminal normal form and sharp constraints on its remaining caps. It does not by itself force zero or one switch in every dimension; the residual plateau requires an additional cross-root or cap comparison.
