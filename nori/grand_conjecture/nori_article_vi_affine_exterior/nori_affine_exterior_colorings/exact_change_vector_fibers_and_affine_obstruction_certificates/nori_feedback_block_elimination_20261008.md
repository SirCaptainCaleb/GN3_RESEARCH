# Bijective feedback blocks control one-change geodesics

# Strongly connected Boolean influence blocks

Let \(c\) be any binary coloring of ordered three-faces of \(Q_n\), \(n\ge4\), with or without antipodal symmetry. Fix a coordinate order \(p=(p_1,\ldots,p_n)\), a starting vertex \(x\), and write \(w_1(x),\ldots,w_{n-2}(x)\) for its consecutive colors. Put \(s=n-3\) and \(d_i(x)=w_i(x)\oplus w_{i+1}(x)\) for \(i\in[s]\).

**Theorem (feedback-block elimination).** Let \(J\subseteq[s]\), and let \(\phi:J\hookrightarrow[n]\) be an injection identifying distinct pivot starting bits \(z_i=x_{p_{\phi(i)}}\). Construct the directed influence graph on \(J\): an edge \(i\to j\), for \(i\ne j\), means that \(d_i\) depends nontrivially on the bit \(z_j\), with all other starting bits allowed to vary. Let \(\mathcal C\) be its strongly connected components. Suppose that for every \(C\in\mathcal C\) and every assignment of all starting bits outside \(\{z_i:i\in C\}\), the block map
\[
 \mathbb F_2^C\longrightarrow\mathbb F_2^C,\qquad
 (z_i)_{i\in C}\longmapsto(d_i(x))_{i\in C}
\]
is a bijection. Then the restricted change map \(x\mapsto(d_i(x))_{i\in J}\) is exactly \(2^{n-|J|}\)-to-one onto \(\mathbb F_2^J\). In particular, if \(|J|\ge n-4\), the fixed coordinate order has a geodesic with at most one color change. If \(J=[s]\), every complete change vector occurs exactly eight times, giving exactly \(8(n-2)\) good starting vertices, of which eight are monochromatic.

**Proof.** Fix arbitrarily all \(n-|J|\) nonpivot starting bits and prescribe any target vector \(t\in\mathbb F_2^J\). The condensation of the influence graph into strongly connected components is acyclic. Process its components in reverse topological order, starting at sinks. When processing \(C\), every pivot variable on which an equation \(d_i\) for \(i\in C\) can depend, except those within \(C\), belongs to an already processed component: this is exactly the definition of the directed influence edges and reverse topological order. The stated bijectivity now supplies a unique assignment to the pivots \(z_C\) meeting the prescribed targets \(t_C\). Subsequent assignments to upstream components do not alter already solved equations, since a processed component has no influence edge to any unprocessed component. Induction gives a unique pivot assignment for every choice of the nonpivot bits and every target. Thus the restricted map has constant fiber size \(2^{n-|J|}\).

Setting all controlled differences to zero leaves at most \(s-|J|\) color changes, proving the sufficient criterion. If \(J=[s]\), then \(n-|J|=3\), and the \(s+1=n-2\) change vectors of Hamming weight at most one each have eight preimages. \(\square\)

The earlier acyclic uniform-pivot theorem is the case where each strongly connected component is a singleton and the corresponding Boolean derivative equals one everywhere. The present theorem also accommodates genuine feedback components, including nonlinear component permutations; acyclicity is sufficient but not necessary.

**Example (irreducible cyclic feedback in dimension seven).** Take \(p=(1,2,3,4,5,6,7)\). Prescribe its five window colors, as functions of the initial bits, by
\[
 (w_1,w_2,w_3,w_4,w_5)
   =(x_4,x_1,x_2,x_3,x_4\oplus x_1).
\]
Each \(w_i\) is independent of the starting bits in the free triple \(\{i,i+1,i+2\}\), so it specifies a well-defined ordered-face color (with the appropriate fixed-coordinate toggles on preceding moves). The five ordered triples are pairwise distinct and none is the reversal of another; the prescribed colors therefore extend to an antipodal-reversal-odd coloring of all ordered three-faces by pairing each \((F,\pi)\) with \((\bar F,\operatorname{rev}\pi)\).

The four differences are
\[
 d=(x_4\oplus x_1,\ x_1\oplus x_2,\ x_2\oplus x_3,\
 x_3\oplus x_4\oplus x_1).
\]
Choose pivots \((z_1,z_2,z_3,z_4)=(x_4,x_1,x_2,x_3)\). Their coefficient matrix is
\[
 M=\begin{pmatrix}
 1&1&0&0\\0&1&1&0\\0&0&1&1\\1&1&0&1
 \end{pmatrix}.
\]
The equations \(Mz=0\) first give \(x_4=x_1=x_2=x_3\), and the final equation then forces their common value to be zero; hence \(M\) is invertible over \(\mathbb F_2\). Nonetheless the influence graph contains the directed cycle \(1\to2\to3\to4\to1\) (and \(4\to2\)), so the acyclic theorem does not apply. The sole strongly connected block is bijective; therefore every four-bit change vector occurs at precisely eight starting vertices, with 40 good starts for this order.

The example remains valid with arbitrary nonlinear perturbations \(G_i\) using only nonpivot variables, respecting window exteriority:
\[
\begin{aligned}
w_1&=x_4\oplus G_1(x_5,x_6,x_7),\\
w_2&=x_1\oplus G_2(x_5,x_6,x_7),\\
w_3&=x_2\oplus G_3(x_6,x_7),\\
w_4&=x_3\oplus G_4(x_7),\\
w_5&=x_4\oplus x_1.
\end{aligned}
\]
For each assignment of \((x_5,x_6,x_7)\), the change map is \(Mz\oplus b\) and is still bijective. For example \(G_1=x_5x_6\) and \(G_3=x_6x_7\) make the face coloring genuinely nonlinear.

**Frontier.** A NORI counterexample must defeat all almost-complete pivot matchings whose strongly connected influence blocks are bijective, for every coordinate order. The block criterion gives an additional full-dimensional closure mechanism but does not by itself establish the grand conjecture.
