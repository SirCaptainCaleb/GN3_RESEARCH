# One fifth of all four-edge geodesics are monochromatic; quantitative rank-two color-free reachability

# At least a 1/5 density of monochromatic four-edge geodesics and terminal-tail support labels

Let n>=5 and let c be ANY binary coloring of ordered physical three-faces of Q_n, without antipodal-reversal assumptions. A directed four-edge geodesic is **monochromatic** when its two consecutive ordered-three-face windows have equal colors.

**Theorem (20-percent universal path density).** At least ONE FIFTH of all directed length-four cube geodesics are monochromatic:
\[
\boxed{\#\{\text{mono directed 4-geodesics}\}\ \ge\
\frac15\,2^n\,n(n-1)(n-2)(n-3).}
\]
The assertion holds separately for each fixed reference vertex r as SECOND vertex of the directed geodesic: at least one fifth of all ordered four-direction words with a path entering r on the first edge produce two equal window colors.

**Proof.** Fix r and a 5-element direction set D. There are 5!=120 ordered lists of four distinct elements of D, each specifying one directed 4-geodesic starting at r⊕e_{p_1} and entering r on its first edge. Partition these lists into 24 cyclic classes: a class is specified by a cyclic ordering of all five members of D, taken modulo rotation, and consists of the five length-four consecutive cyclic words of that cyclic order. For each class, consider the five ordered three-face colors at physical faces through r with consecutive cyclic direction triples. Since the cyclic word of five binary colors has at least one pair of adjacent equal colors, at least one of the five associated directed four-geodesics is monochromatic. Therefore at least 24 of the 120 paths associated with (r,D) are monochromatic.

For n>5, every ordered four-direction word is contained in exactly n-4 different five-element sets D. Summing the 24-per-D bound over all C(n,5) choices of D gives at least
\[
\frac{24\binom n5}{n-4}=\frac15\,n(n-1)(n-2)(n-3)
\]
monochromatic directed four-geodesics with second vertex r. Sum over the 2^n possible second vertices; every directed four-geodesic has exactly one second vertex. QED.

**Terminal two-tail color-free density.** For an ordered pair J=(a,b), x∈Q_n, and D_J=[n]\{a,b}, let \(\mathcal R_J^{(2)}(x)\) be the color-free family of two-element supports U for which there is a monochromatic directed four-geodesic from x with direction word (some order of U, a,b). Each reachable triple (x,J,U) accounts for at most 2!=2 distinct ordered four-geodesics, whereas each possible triple corresponds to exactly two candidate four-geodesics. Thus the same 1/5 lower density holds:
\[
\boxed{\sum_{x\in Q_n}\sum_{J\in[n]_{\ne}^2}|\mathcal R_J^{(2)}(x)|
\ \ge\ \frac15\,2^n n(n-1)\binom{n-2}{2}.}
\]
Here J ranges over all n(n-1) ordered direction pairs. This establishes an unconditional positive-density constraint for the EXACT color-free reachability regions in the NORI complementary-tail closure theorem.

**General uniform-k version.** Let k>=1 and m be the least odd integer ≥k+1, with n>=m. Every binary ordered-k-face coloring of Q_n has at least a 1/m fraction of its directed length-(k+1) geodesics monochromatic. The same cyclic m-order partition argument proves it: with a fixed reference second vertex r and m-set D, every cyclic order has m distinct (k+1)-direction subwords; at least one has two equal consecutive k-face colors. Every ordered (k+1)-word from D belongs to exactly the same number of cyclic m-classes (indeed one if m is k+1 or k+2), and the subsequent average over D preserves the 1/m bound. For k=3, m=5.

**Grand closure status.** The lower bound of 1/5 on rank-two tail reachability is BELOW the 1/2 middle-rank upper bound obtained assuming no grand NORI witness in n=6. Thus density alone does not yet close the conjecture. The exact next objective is an amplification or transfer inequality driving reachability from low ranks toward complementary higher ranks without introducing unwanted ordered-face seam windows.
