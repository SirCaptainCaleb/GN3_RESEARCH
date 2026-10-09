# In the unique-color edge-shadow regime five same-color hub directions force a monochromatic six-edge geodesic

# Active NORI: five directions of one certified hub color force a genuine monochromatic six-edge geodesic

Let n>=7 and let c be a valid active NORI ordered-3-face coloring. Assume NO physical cube edge belongs to certified monochromatic middle-pair squares of BOTH colors (the UNIQUE-EDGE-COLOR SHADOW case B). By the existing bichromatic hub theorem and edge-shadow selector rigidity, choose ANY bichromatic physical hub z with its incident square-certified direction sets A (color0), B (color1), satisfying A∩B=∅ and |A|,|B|>=2. For every ordered triple of distinct directions (u,v,w) through z, the *actual physical* ordered-face color is the class bit q(v) whenever the middle direction v belongs to A or B and at least one of u,w lies in the opposite class.

**THEOREM (five-majority six-edge monochromatic seed).** If |A|>=5, then there is a genuine MONOCHROMATIC SIX-edge geodesic of ordered-three-face color 0, with six distinct directions, all four windows passing through z. If |B|>=5, the symmetric statement holds with color1. Hence in the no-shared-certified-edge alternative B, for every n>=10 there is a genuine monochromatic six-edge geodesic centered at each bichromatic hub, and therefore a genuine one-switch seven-edge geodesic somewhere in Q_n whenever n>=10.

**Proof.** Suppose |A|>=5 and choose FIVE distinct A-directions p_0,...,p_4 in cyclic order. Form the cyclic list of FIVE actual physical ordered-three-face colors at z,
\[
t_j=c(F(z;\{p_j,p_{j+1},p_{j+2}\}),(p_j,p_{j+1},p_{j+2})),\qquad j\bmod5.
\]
No two cyclically adjacent t_j,t_{j+1} can BOTH equal 1: if they did, the actual centered four-edge geodesic with ordered directions (p_j,p_{j+1},p_{j+2},p_{j+3}) would have BOTH ordered-three-face windows color1, hence would certify the physical middle square whose free directions are p_{j+1},p_{j+2}, both in A. In particular the cube edge at z of direction p_{j+1} would receive a genuine color1 square certificate. But this SAME physical edge already has a color0 square certificate by definition of membership p_{j+1}∈A, contradicting the no-bichromatic-common-edge hypothesis.

Because FIVE is odd, a cyclic binary word of length5 cannot have all adjacent entries different. Its adjacent equal entries therefore CANNOT be (1,1); hence SOME adjacent pair equals (0,0). Let its corresponding four distinct consecutive cyclic directions be (a_1,a_2,a_3,a_4)∈A^4. Their two actual ordered triple window colors through z are BOTH 0.

Choose any TWO distinct b_1,b_2∈B. Consider the SIX-distinct-direction ordered word
\[
p=(b_1,a_1,a_2,a_3,a_4,b_2),
\]
rooted at x=z⊕\{b_1,a_1,a_2\}, so it visits z after exactly three edges. Every one of its FOUR ordered-three-face windows contains the PHYSICAL hub vertex z. Their ordered triples and actual colors are:
\[
(b_1,a_1,a_2)\mapsto0
\quad(\text{middle }a_1∈A,\ \text{opposite outer }b_1∈B),
\]
\[
(a_1,a_2,a_3)\mapsto0
\quad(\text{the proven adjacent pair}),
\]
\[
(a_2,a_3,a_4)\mapsto0
\quad(\text{the proven adjacent pair}),
\]
\[
(a_3,a_4,b_2)\mapsto0
\quad(\text{middle }a_4∈A,\ \text{opposite outer }b_2∈B).
\]
Thus all four colors equal0, and the six-edge path is a genuine monochromatic cube geodesic. If |B|>=5 interchange both colors and classes. \(\square\)

**Dimension corollaries.** The certified-square graph theorem gives |A|+|B|>=n−1 at EVERY bichromatic hub in case B, because at most one cube direction there is not square-certified. Consequently max(|A|,|B|)>=ceil((n−1)/2). For n>=10 this maximum is at least5, yielding the stated universal-in-case-B mono6 geodesic. Appending ANY fresh seventh coordinate to a monochromatic length-six geodesic creates exactly one NEW three-face window and hence produces a one-switch length-seven geodesic irrespective of its new color. In n=7, the same result directly proves FULL active NORI grand closure whenever a bichromatic hub has a certified class of >=5 directions.

**Why this does not close unrestricted NORI.** The other edge-shadow alternative (A), involving a physical cube edge with competing square certificates, is not addressed. Moreover for n>7 the six-edge monochromatic and seven-edge one-switch geodesics do not span all n directions. One cannot append more unused directions without creating additional switches. Thus the theorem is a substantial path-building extraction in a structurally constrained branch, not the universal grand conjecture.
