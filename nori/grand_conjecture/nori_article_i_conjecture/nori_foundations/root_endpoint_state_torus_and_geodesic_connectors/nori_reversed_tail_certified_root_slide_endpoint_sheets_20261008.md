# NORI reversed-tail root slides preserve certified endpoints and cross distinct geometric sheets

# Certified NORI reversed-tail root slides and endpoint-sheet crossing

Let \(n\ge4\), \(J=(a,b)\) be an ordered pair of distinct directions, \(D=[n]\setminus\{a,b\}\), and let \(R_J(x)\) consist of nonempty \(U\subseteq D\) for which there exists a monochromatic directed ordered-three-face geodesic from root \(x\) with direction word \((u_1,\ldots,u_k,a,b)\), where the \(u_i\) enumerate \(U\) and \(k\ge1\). The color of the witness is irrelevant to membership in \(R_J\).

**Lemma (endpoint-preserving, witness-certified root slide).** Suppose \((x,U,J)\) has a witness of the displayed form. For \(0\le t\le k-1\), let
\[
x_t=x\oplus e_{u_1}\oplus\cdots\oplus e_{u_t},\qquad
U_t=U\setminus\{u_1,\ldots,u_t\}.
\]
Then \(U_t\in R_J(x_t)\) is certified by the actual monochromatic suffix \((u_{t+1},\ldots,u_k,a,b)\). Its absolute endpoint
\[
y=x_t\oplus\chi_{U_t}\oplus e_a\oplus e_b
 =x\oplus\chi_U\oplus e_a\oplus e_b
\]
is constant along the slide. In particular, every nonempty certified support can be slid along actual witnesses to a singleton; the oriented slide graph is acyclic by strictly decreasing \(|U|\).

**Proof.** Each suffix of a monochromatic geodesic of ordered three-face windows is again monochromatic in those windows. Removing the first coordinate move deletes its first window but does not alter the remaining ordered faces: the new root is the second vertex of the original path and its direction order is the original suffix. The endpoint identity is the mod-2 cancellation of the removed direction in both root and support. Iterate until only one nonterminal direction remains. \(\square\)

**Lemma (crossing endpoint sheets).** Give a certified state coordinates \((x_i,U_i)\) for each \(i\in D\). The endpoint coordinate \(y_i=x_i\oplus U_i\) is conserved by a root slide deleting direction \(i\). At this coordinate the slide changes \((x_i,U_i)\) from \((0,1)\) to \((1,0)\) when \(y_i=1\), but from \((1,1)\) to \((0,0)\) when \(y_i=0\). These are the two opposite diagonals of a geometric unit square. Hence a naive single triangulation of the full root/support bit cube cannot simultaneously realize every such certificate-preserving slide as an unsplit edge. If the diagonals are subdivided at their crossing, the center must retain distinct endpoint-sheet/witness data: coincident geometric points do not by themselves certify a common path or matching endpoint.

**Exact reversed-tail collision geometry.** For certified supports \(U\in R_{(a,b)}(x)\) and \(D\setminus U\in R_{(b,a)}(x)\), write the two absolute endpoints
\[
y_A=x\oplus\chi_U\oplus e_a\oplus e_b,\qquad
y_B=x\oplus\chi_{D\setminus U}\oplus e_a\oplus e_b.
\]
Then \(y_A\oplus y_B=\chi_D\): the endpoints are antipodal *within a fixed \((a,b)\)-face*, not necessarily antipodal in all \(n\) coordinates. Moreover \(\bar y_B=x\oplus\chi_U\), exactly the vertex reached by the first witness's \(U\)-prefix. Thus the antipodal reversal of the second witness has the correct entry point, and the reversed terminal directions account for both junction windows. The pre-existing grand equivalence theorem proves that these two certified witnesses splice into a full one-change geodesic.

**Topological frontier (not claimed proved).** The root slides furnish a genuine acyclic, endpoint-preserving witness relation, but no boundary conditions or fixed-point theorem are yet known that force a complementary-support collision in the two different terminal families \(R_J(x)\) and \(R_{\mathrm{rev}J}(x)\) at the *same* root. Geometric intersection between different endpoint sheets without an actual witness is insufficient. This lemma is dimension independent and includes all exterior-face dependence allowed by NORI.

### Elevation pass II: universal singleton shores in every ordered-window dimension

The root-slide statement has a stronger universal terminal-layer interpretation. Fix an ordered \(k\)-face coloring, \(k\ge2\), an ordered terminal \((k-1)\)-tuple \(J\) of distinct directions, a root \(x\), and a coordinate \(i\notin J\). Define \(R_J(x)\) using monochromatic geodesics with directions \((U,J)\) and nonempty outside support \(U\). **For every coloring and every root,**
\[
\{i\}\in R_J(x).
\]
Indeed the direction word \((i,J)\) has exactly \(k\) directions and therefore only **one** ordered \(k\)-face window; it is monochromatic vacuously, irrespective of its color. A certified root slide along the first direction of a longer witness decreases its outside support by one and preserves the absolute endpoint and ordered terminal memory. Consequently every nonempty certified witness admits a terminating root-slide chain to a **universal singleton state**. The oriented slide system is rank-acyclic, but not necessarily a tree: a support may have several distinct witnesses and several possible first-move deletions.

For NORI (\(k=3\)), the two terminal families \(R_{(a,b)}(x)\) and \(R_{(b,a)}(x)\) therefore share every singleton label \(\{i\}\subseteq D=[n]\setminus\{a,b\}\) at every root, entirely independently of antipodal oddness. This supplies two ubiquitous shores in the terminal-memory label complex, but **equality of those labels is not the grand collision**. A valid extraction requires \(U\in R_{(a,b)}(x)\) and \(D\setminus U\in R_{(b,a)}(x)\), where both sides are nonempty. For \(n\ge5\), \(D\) has at least three directions, so the complement of a singleton has at least two directions; its reachability is not guaranteed by the trivial singleton shore. In \(n=4\), by contrast, \(D\) has two elements and the two singleton shores already produce complementary supports. A fixed-point proof that merely connects, identifies, or retracts onto the universal singleton layer cannot resolve the general conjecture: it must **force a transition to a nontrivial complementary support** at the same root and reversed terminal order. This explains why naive contractibility of witness-slide fibers is too weak even though every such fiber has a certified sink.
