# Endpoint deletion and affine obstruction rigidity

# Endpoint truncation and affine influence restrictions

Let \(V\) be a set of \(n\ge5\) cube coordinates. A full geodesic \(P=(x;p_1,\ldots,p_n)\) has ordered-three-face color word \(w(P)=w_1\cdots w_{n-2}\), with \(w_i\in\mathbb F_2\). Put \(\delta_i=w_i+w_{i+1}\in\mathbb F_2\), interpreted as an integer in \(\{0,1\}\) when counting changes. The coloring is of *physical ordered three-faces*: a window color depends on the exterior fixed cube coordinates and the order of its three free directions, and is independent of the corner at which the window is traversed.

## 1. A two-ended deletion lemma

**Lemma.** Suppose that both paths obtained from \(P\) by deleting its first edge and by deleting its last edge have at most one change in their respective window words. If \(P\) has at least two changes, its window word has precisely the shape
\[
0\,1^{\,n-4}0\quad\text{or}\quad1\,0^{\,n-4}1.
\]

**Proof.** Deletion of the last edge gives \(\sum_{i=1}^{n-4}\delta_i\le1\), while deletion of the first gives \(\sum_{i=2}^{n-3}\delta_i\le1\). An interior change \(\delta_i=1\), \(2\le i\le n-4\), would use the entire allowance of both truncated paths, excluding changes at all other positions and contradicting the assumption that \(P\) has at least two changes. Therefore all interior \(\delta_i\) vanish. The assumed two changes must be exactly \(\delta_1=\delta_{n-3}=1\), yielding the displayed words. \(\square\)

This is a word-theoretic lemma, applicable to arbitrary binary ordered-face colorings. It isolates the sole way two individually good truncations can fail to fit into a full good path: the two terminal seams change and the interior stays constant.

## 2. Affine starting-root images

Fix a direction permutation \(p\). Suppose every window color \(w_i(x,p)\) is an affine function of the starting vertex \(x\in\mathbb F_2^n\), as holds if the ordered-face colors are affine in their exterior bits. Define
\[
\Delta_p(x)=\bigl(w_1+w_2,\ldots,w_{n-3}+w_{n-2}\bigr)
             \in\mathbb F_2^{n-3}.
\]
This is an affine map; its Hamming weight is the number of changes of the corresponding full path.

**Proposition (codimension-one criterion).** If the linear part of \(\Delta_p\) has rank at least \(n-4\), some start \(x\) makes the fixed order \(p\) good. Consequently a fixed order that is bad for every root in dimension six has change-map rank at most one.

**Proof.** Put \(r=n-3\). The nonempty affine image of \(\Delta_p\) has codimension at most one in \(\mathbb F_2^r\). A full image contains \(0\). An affine hyperplane is of the form \(\{z:\lambda\cdot z=b\}\), with \(\lambda\ne0\). When \(b=0\) it contains \(0\), and when \(b=1\) it contains \(e_j\) for any \(j\) with \(\lambda_j=1\). Either way the image contains a vector of weight at most one, as required. \(\square\)

Thus, in the affine subclass, failure for a given order is accompanied by a strong and explicitly testable rank deficiency; no antipodal-reversal condition was needed.

## 3. Complementary-triple influence in dimension six

Now let \(n=6\) and impose the actual NORI condition
\[
c(\bar F,\operatorname{rev}\pi)=1+c(F,\pi).
\]
For a free triple \(T\subset V\) and its designated middle direction \(b\in T\), define \(I(T,b)\subset V\setminus T\) to be the exterior directions that influence the color of an ordered face of type \(T\), for some assignment of its other exterior bits. Reversing the first and third directions leaves this influence set unchanged: antipodal reversal carries the Boolean exterior function to its complemented-input, complemented-output version, preserving each coordinate's Boolean sensitivity.

**Proposition (opposite influence sparsity).** Let \(U=V\setminus T\). If \(d\in I(T,b)\), then \(I(U,e)\subseteq\{b\}\) for every \(e\in U\setminus\{d\}\), under the assumption that no full geodesic has at most one change. If \(|I(T,b)|\ge2\), then \(I(U,e)\subseteq\{b\}\) for all \(e\in U\).

**Proof.** Write \(T=\{a,b,c\}\), \(U=\{d,e,f\}\) and take the order \((a,b,c,d,e,f)\). The four three-face colors are \(A,B,C,D\). Both middle windows have \(c,d\) free and hence are independent of the starting bits \(x_c,x_d\). By hypothesis on \(d\), the first window's color \(A\) can be chosen by varying \(x_d\), holding its other exterior bits fixed. If the last-window color \(D\) were sensitive to \(x_c\), it could be chosen by varying \(x_c\), holding its own other exterior bits fixed. The two exterior choices are independent: \(A\) does not depend on \(x_c\) and \(D\) does not depend on \(x_d\). Choose \(x_d\) to enforce \(A=B\) and \(x_c\) to enforce \(D=C\); the resulting word \((B,B,C,C)\) is good, a contradiction. Therefore the ordered \(U\)-face with middle \(e\) is insensitive to \(c\). Reversing the order of \(T\) preserves sensitivity in \(d\) and similarly excludes sensitivity in \(a\). The only potentially influential coordinate of \(T\) is \(b\). Exchanging \(e\) and \(f\) gives the same conclusion for the other middle direction of \(U\). Finally, if \(d,d'\in I(T,b)\) are distinct, each \(e\in U\) differs from at least one of them, so the first statement applies to all three choices. \(\square\)

The three results expose complementary restrictions on a hypothetical bad coloring: terminal truncation confines switches to two seams, affine dependence forces low change-map rank, and two exterior influences on one triple suppress almost all influences on its complementary triple. The affine and dimension-six statements are conditional structural constraints; neither independently establishes the arbitrary-dimensional NORI conjecture.
