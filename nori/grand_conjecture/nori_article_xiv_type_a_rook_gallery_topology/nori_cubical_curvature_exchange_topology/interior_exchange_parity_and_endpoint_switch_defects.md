# Interior exchange parity and endpoint switch defects

# Interior exchanges preserve switch parity; endpoint exchanges control odd defects

Let \(c:E(Q_n)\to\mathbb F_2\) be an arbitrary coloring of undirected cube edges, with antipodal oddness imposed where stated. For a rooted full geodesic \(P(x,\pi)\), write \(w_j=c(e_j)\) and
\[
S(x,\pi)=\sum_{j=1}^{n-1}\mathbf1_{\{w_j\ne w_{j+1}\}}
\]
for its number of switches.

**Lemma 1 (endpoint parity).** For every binary word \(w\),
\[
\boxed{S(w)\equiv w_1+w_n\pmod2.}
\tag{1}
\]
If \(c\) is antipodally odd, define \(a_i(x)=c(\{x,x\oplus e_i\})\). Then
\[
\boxed{S(x,\pi)\equiv1+a_{\pi_1}(x)+a_{\pi_n}(x)\pmod2.}
\tag{2}
\]

*Proof.* The sum modulo two of neighboring comparison bits \(w_j+w_{j+1}\) telescopes to \(w_1+w_n\). The first edge of \(P(x,\pi)\) has color \(a_{\pi_1}(x)\), while its last edge is the antipodal mate of the edge incident to \(x\) in dimension \(\pi_n\), so \(w_n=1+a_{\pi_n}(x)\). Substitution proves (2). \(\square\)

**Theorem 2 (interior-exchange two-step law).** Let \(n\ge4\), and suppose \(\pi'\) differs from \(\pi\) by exchanging the dimensions at positions \(j,j+1\), with
\[
2\le j\le n-2.
\]
Then
\[
\boxed{S(x,\pi')-S(x,\pi)\in\{-2,0,2\}.}
\tag{3}
\]
No antipodal condition is needed for (3). In particular a single interior exchange cannot create or eliminate precisely one color switch.

*Proof.* Both geodesics start at \(x\), agree in their first \(j-1\) edges, traverse the two opposite routes through the same dimension-\(\{\pi_j,\pi_{j+1}\}\) square, and rejoin at the same cube vertex. Thus their color words agree outside positions \(j,j+1\). Write the common bits immediately before and after the square as \(A=w_{j-1}=w'_{j-1}\), \(B=w_{j+2}=w'_{j+2}\). The only possibly changed comparisons are
\[
(A,u,v,B)\quad\hbox{versus}\quad(A,u',v',B),
\]
where \(u,v,u',v'\) are the colors of the two routes through the square. For any binary pair \((u,v)\), the number of changes among the three comparisons has parity \(A+B\) and lies between 0 and 3. Therefore its difference for two pairs is in \(\{-2,0,2\}\). All other comparisons agree, proving (3). \(\square\)

**Proposition 3 (zero square curvature still permits a jump of two).** For \(n\ge4\) there are valid antipodally odd cube colorings and interior neighboring orders whose word segments are
\[
(A,u,v,B)=(0,0,0,0),\qquad
(A,u',v',B)=(0,1,1,0).
\]
Then the switch count increases by two, although the square curvature
\[
\kappa(F)=u+v+u'+v'=0\pmod2.
\tag{4}
\]

*Proof.* Choose any root and any dimension order with the exchanged positions interior, for instance \(n=4\), \(\pi=(1,2,3,4)\), and \(\pi'=(1,3,2,4)\). Color the common first and fourth edges zero, both edges of the \(2\)-then-\(3\) route zero, and both edges of the \(3\)-then-\(2\) route one. These six edges have distinct antipodal orbits; in a dimension different from those of the square their fixed bits distinguish the parallel edges from antipodal mates. Complete each orbit by giving the antipodal edge the complementary bit. The color words are \(0000\) and \(0110\), with zero and two switches, respectively, while (4) holds. \(\square\)

**Corollary 4 (two parity sectors at a cube root).** Fix \(x\) and ordered first and last dimensions \(p,q\ne p\). Every complete geodesic from \(x\) beginning with \(p\) and ending with \(q\) has the same switch-count parity,
\[
S\equiv1+a_p(x)+a_q(x)\pmod2.
\tag{5}
\]
The intermediate dimension orders are connected by interior adjacent exchanges and the switch count changes by zero or two at each exchange. In a hypothetical NORI1 counterexample, when \(a_p(x)=a_q(x)\) every such word must have at least three switches; when \(a_p(x)\ne a_q(x)\), every such word must have at least two switches.

*Proof.* Equation (5) follows from Lemma 1. The permutations of the remaining \(n-2\) dimensions are connected by swaps among positions \(2,\ldots,n-1\), each interior in the sense of Theorem 2. If no one-switch or monochromatic full geodesic exists, every full word has at least two switches; combine this with the parity distinction. \(\square\)

## Consequence for a Wu–Yang-type filtered chain argument

The rank-two color-comparison data produces a **parity-preserving exchange geometry** whenever both ends of the complete path are held fixed. The only adjacent dimension exchanges that can change the parity of the switch count are those touching the first or last position; the type-B sign-flip move changing the root can alter many later color bits without a uniform local switch bound. This independently explains the endpoint-sensitive exceptional parabolic cells identified earlier by the second-switch obstruction.

In particular, an equivariant correction scheme that attempts to use only ordinary cubical square curvature is insufficient: Proposition 3 exhibits a filtration jump without curvature. Such a scheme must retain the ordered neighboring color comparisons (or an equivalent switch filtration), as well as the distinct dimensions, when constructing its higher chain homotopies.
