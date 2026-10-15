# Full-rank Hamming galleries: permutation model and determinant transport

# Permutation galleries, unimodular transport, and endpoint degrees

Let \(H(k,q)=K_q^{\square k}\) with \(k\ge1,q\ge2\), and \(N_{\rm sp}\) its canonical spectral-resource matroid on graph edges. Fix a root \(x\), let \(d=k(q-1)\), and put
\[
D_x=\{(i,b): i\in[k],\ b\in[q]\setminus\{x_i\}\},
\qquad |D_x|=d.
\]
Orient a root edge by the direction of traversal. Its spectral difference vector is \(e_b-e_a\) in coordinate summand \(i\) when that coordinate changes from \(a\) to \(b\).

**Theorem 1 (full-rank gallery permutation correspondence).** Every \(N_{\rm sp}\)-independent path of length \(d\) beginning at \(x\) is obtained uniquely from a permutation \(\pi=(t_1,\ldots,t_d)\) of \(D_x\): for \(t_j=(i,b)\), replace the current \(i\)-th coordinate value by \(b\). Every such permutation yields a resource-independent path.

**Proof.** Resource independence means the transitions in each coordinate form a forest in the graphic matroid \(M(K_q)\). Since the coordinate transitions form a trail, they cannot revisit a coordinate symbol. Rank saturation forces \(q-1\) transitions in each coordinate, so the successive visited symbols are a permutation of the \(q-1\) symbols other than \(x_i\). Interleaving the \(k\) coordinate sequences gives a permutation of \(D_x\). Conversely a permutation of \(D_x\) gives a simple coordinate path in each complete-graph factor, hence a forest, and the resource vectors for different factors occupy direct-sum subspaces. The entire set of \(d\) edge vectors is therefore independent. \(\square\)

**Corollary 2 (diametral endpoints and uniform fibers).** Every full-rank path from \(x\) finishes at some \(y\) differing from \(x\) in all \(k\) coordinates. Every such \(y\) occurs, and the number of full-rank paths with prescribed directed endpoints \(x,y\) is
\[
\boxed{\frac{d!}{(q-1)^k}}.
\tag{1}
\]
In particular there are \(d!\) full-rank paths from \(x\), distributed uniformly among the \((q-1)^k\) diametral endpoints.

**Proof.** In each coordinate the prescribed terminal symbol is the last visited among \(q-1\) tokens. Choose the orders of the \(q-2\) remaining tokens in \((q-2)!\) ways, and interleave the \(k\) ordered coordinate sequences in \(d!/((q-1)!)^k\) ways. Their product is (1). \(\square\)

In the cube endpoint \(H(n,2)=Q_n\), this is the familiar \(n!\) antipodal geodesics between fixed endpoints. At \(H(1,n)=K_n\) the count becomes \((n-2)!\) Hamilton paths between prescribed distinct vertices.

**Theorem 3 (unimodular triangular change of basis).** Let \(w_{i,b}=e_b-e_{x_i}\), for \((i,b)\in D_x\), be the root-star basis of the spectral resource space. For \(\pi=(t_1,\ldots,t_d)\), write \(u_j\) for the vector of its \(j\)-th oriented path edge, and \(p(j)<j\) for the previous occurrence of the coordinate of \(t_j\), if one exists. Then
\[
u_j=w_{t_j}-w_{t_{p(j)}} ,
\]
where the second term is zero if \(p(j)\) does not exist. The matrix with columns \(u_j\) in the ordered basis \((w_{t_1},\ldots,w_{t_d})\) is unitriangular. Consequently, relative to any fixed ordering of the root-star basis,
\[
\boxed{\det(u_1,\ldots,u_d)=\operatorname{sgn}(\pi).}
\tag{2}
\]
Adjacent token swaps reverse this determinant, thereby connecting resource-basis orientation to the permutohedral exchange graph.

**Proof.** The changed coordinate goes from the value visited at its previous occurrence (or \(x_i\) for its first occurrence) to the newly named symbol. Subtracting their root-star vectors gives the identity above. The new token contributes diagonal coefficient one and any previous token contributes a coefficient in an earlier row. Hence the matrix is unitriangular, and the remaining determinant sign is the sign of the ordering permutation. \(\square\)

**Proposition 4 (signed endpoint enumeration).** Fix \(x\) and a diametral endpoint \(y\). The signed sum \(\sum_{\pi:x\to y}\operatorname{sgn}(\pi)\) is zero for \(q\ge4\), and also for \(q=2,k\ge2\). For \(q=3\), its absolute value is \(k!\), with the sign depending on the reference token order.

**Proof.** When \(q\ge4\), each factor has at least two nonterminal tokens. Interchange two chosen nonterminal tokens from one factor in the permutation word. The endpoint stays fixed, and the determinant changes sign; this is a sign-reversing fixed-point-free involution. For \(q=2,k\ge2\), each factor has one token, and every permutation has the same endpoint. Transpose the positions of two fixed tokens to pair signs.

For \(q=3\), the prescribed endpoint leaves a pair of ordered tokens in each coordinate. Every endpoint gallery is a shuffle of these \(k\) ordered pairs. Partition the \(2k\) word positions into adjacent slots \((1,2),(3,4),\ldots,(2k-1,2k)\). For a shuffle in which one slot contains tokens from different coordinates, choose the first such slot and swap its two tokens. This is a fixed-point-free sign-reversing involution, preserving each coordinate's internal token order. The surviving shuffles have every slot occupied by the two tokens of the same coordinate in their prescribed order. There are \(k!\) such shuffles. Permuting two complete slots makes four elementary transpositions, so all survivors have the same sign. The signed sum thus has absolute value \(k!\). \(\square\)

**Interpretation.** The cube and rank-two uniform endpoints have a common permutation-gallery and unimodular resource orientation algebra. The untwisted signed degree cancels at both endpoints for growing rank; the ternary Hamming interpolation retains a nonzero integer signed endpoint enumerator. This alone does not force any color-coherent gallery. Any determinant-degree attempt for arbitrary cube antipodal coloring must incorporate the coloring, root transport, or a signed-cover twist.
