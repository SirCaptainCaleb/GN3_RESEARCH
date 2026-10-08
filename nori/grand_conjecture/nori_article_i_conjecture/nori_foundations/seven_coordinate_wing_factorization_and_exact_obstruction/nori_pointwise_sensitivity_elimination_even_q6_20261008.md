# Complete reversal-even Q6 obstruction classification and all-dimensional six-nonflipper NORI closure

# Pointwise exterior sensitivity cannot survive in a bad reversal-even six-cube

Let \(B\) consist of six coordinate directions. Color the ordered three-dimensional faces of \(Q_B\) by a Boolean map \(h\), satisfying **reversal-even antipodality**
\[
h(\bar F,\operatorname{rev}\pi)=h(F,\pi).
\]
Call a full six-direction geodesic *good* when its four ordered-three-face colors change at most once.

**Theorem (complete position-rigidity of bad reversal-even \(Q_6\) colorings).** If **every** full six-direction geodesic is bad, then \(h(F,\pi)\) is independent of the three exterior face bits for each ordered triple \(\pi\). Equivalently, there exists a reversal-even ternary function \(H(\pi)\) with \(h(F,\pi)=H(\pi)\) for every face.

**Proof.** Suppose some ordered triple \((a,b,c)\) depends on an exterior coordinate \(d\) at *some* assignment of its other two exterior coordinates \(e,f\). This is pointwise sensitivity, without any uniformity assumption. There are fixed bits \((\eta_e,\eta_f)\) such that toggling \(d\) changes the face color. Complementing coordinates \(e,f\) if necessary and globally complementing all colors, we may assume
\[
h((a,b,c);x_d=0,x_e=x_f=0)=0,\qquad
h((a,b,c);x_d=1,x_e=x_f=0)=1. \tag{1}
\]
Coordinate translations commute with antipodality and preserve all geodesic change counts.

**Analytic complementary-block collapse.** Take the complete direction order \((a,b,c,d,e,f)\), with \(x_e=x_f=0\), and vary freely \(x_a,x_b,x_c\). Its first color toggles with \(x_d\) by (1), and its three terminal colors are independent of \(x_d\) because \(d\) is free in each terminal window. If those three colors had at most one change, choose \(x_d\) to match the first two colors and obtain a good full geodesic. Hence the terminal triple must alternate for every \(x_a,x_b,x_c\), giving
\[
h(b,c,d)=h(d,e,f) \tag{2}
\]
at their respective faces. The left face has fixed exterior bits \(a,e,f\), with \(e,f\) fixed to the witness values, while the right face has fixed exterior bits \(a,b,c\) and does not depend on \(e,f\). Equality for every \(x_a,x_b,x_c\) forces the whole exterior-bit function \(h(d,e,f)\) to depend at most on its \(a\)-bit.

By reversal-even antipodality, the reversed ordered triple \((c,b,a)\) is sensitive to \(d\) at the **complemented** fixed exterior bits \((x_e,x_f)=(1,1)\). Repeating the same argument for \((c,b,a,d,e,f)\) shows that the same exterior-bit function \(h(d,e,f)\) depends at most on its \(c\)-bit. A Boolean function depending only on \(x_a\) and also only on \(x_c\), with \(a\ne c\), is constant. Let this constant be \(K\).

Now run the original witness first triple in order \((a,b,c,d,f,e)\). Its second face \((b,c,d)\) is identical to the second face in \((a,b,c,d,e,f)\), with the same exterior values. The terminal three colors again alternate, and the last face \((d,f,e)\) must equal that second color, already \(K\). Varying all its exterior bits \(a,b,c\) proves that **every** face of ordered type \((d,f,e)\) has color \(K\). Reversal-even antipodality then makes the reversed triples \((f,e,d)\) and \((e,f,d)\) constant \(K\), too. In short, the hypothetical bad coloring has the following **position-independent constant block**:
\[
h(F,\pi)=K\quad\text{for every exterior position whenever }
\pi\in\{(d,e,f),(d,f,e),(f,e,d),(e,f,d)\}. \tag{3}
\]

**Finite forcing contradiction.** It remains to show that (1) and (3) are incompatible with the assumption that **every** six-geodesic is bad. By renaming coordinates, set \((a,b,c,d,e,f)=(0,1,2,3,4,5)\); only \(K=0\) and \(K=1\) remain.

Identify ordered faces under reversal-even antipodality: \((F,\pi)\sim(\bar F,\operatorname{rev}\pi)\). There are exactly
\[
\binom63\cdot 3!\cdot 2^3/2=480
\]
equivalence classes. Each six-coordinate permutation and starting vertex produces four such face labels. Reversing the permutation while keeping the same starting vertex reverses these **equivalence-class labels** (the corresponding faces are antipodal reversals), so it suffices to check \(360\cdot64=23040\) four-label path constraints. A bad four-bit word is one of the eight patterns with at least two adjacent color changes.

Seed (1) as the values \(0,1\) on the ordered face \((0,1,2)\) with exterior masks \(\varnothing,\{3\}\). Seed (3) for all eight exterior assignments on each of the four ordered triples \((3,4,5),(3,5,4),(5,4,3),(4,5,3)\). Reversal-even identification merges these 32 constant-face assignments into 16 variables, so there are **18 distinct seeded variables** in either branch \(K\in\{0,1\}\).

Apply **unit propagation** to the 23040 path constraints: delete all admissible bad words incompatible with assigned labels; any unassigned label that has the same value in every remaining word is forced. Iterate. If a constraint has no remaining admissible word, it is a formal contradiction to the existence of the presumed coloring. This uses only logically forced assignments and never assumes a particular value for an otherwise free face variable.

The complete, self-contained, standard-library certificate is recorded in the companion file \`nori_point_sensitivity_certificate.py\`. It constructs the 480 face classes and 23040 path constraints directly from the definitions; verifies that reversal of the full coordinate order with the same starting vertex reverses the canonical face sequence; and applies the exact forcing rule. Its deterministic outcomes are:

| Constant \(K\) | Initial face variables | Face variables reached before contradiction | Result |
|---|---:|---:|---|
| 0 | 18 | 396 | no admissible completion |
| 1 | 18 | 228 | no admissible completion |

Thus (1) and (3) cannot hold in a globally bad coloring, contrary to our initial sensitivity assumption. No ordered-face value can depend on any of its exterior bits, so \(h\) is coordinate-only. \(\square\)

**Corollary 1 (full classification of bad reversal-even ordered-face colorings of \(Q_6\)).** Combining the theorem with the previously established **exact classification of bad reversal-even coordinate-only triples**, every globally bad reversal-even ordered-three-face coloring of \(Q_6\), allowing arbitrary Boolean exterior dependence initially, is necessarily
\[
h(F,(a,b,c))=\varepsilon\oplus
\mathbf1_{\{b\notin M,\ \{a,c\}\cap M\ne\varnothing\}},
\qquad |M|=2, \tag{4}
\]
with a two-element marked set \(M\) and \(\varepsilon\in\mathbb F_2\). Conversely all these 30 templates are globally bad. This is an exact classification of the **full face-dependent** reversal-even \(Q_6\) problem, not merely its affine subclass.

**Corollary 2 (complete one-universal-flipper \(Q_7\) NORI closure).** Every antipodal-reversal-odd ordered-three-face coloring \(c\) of \(Q_7\) with **one universal exterior flipper** \(g\) admits a full geodesic with at most one color change, with no exterior-dependence restriction.

Indeed, the induced \(Q_6\) residual \(h\) is reversal-even. If it has a one-change full geodesic, the exact universal-flipper elimination theorem lifts that geodesic. Otherwise, (4) makes \(h\) a two-mark template, up to complement, and the previously established sparse two-mark seven-dimensional lifting theorem forces a good geodesic **even if every \(g\)-containing face has unrestricted exterior-bit dependence**.

**Corollary 3 (all-dimensional closure with at most six nonflipper directions).** Let \(c\) be a NORI coloring of \(Q_n\), and suppose all but at most six directions are universal exterior flippers. Then \(c\) has a full one-change antipodal geodesic.

For at most five remaining directions, apply the unrestricted five-residual flipper-lifting theorem. For exactly six nonflippers, write \(r\) for the number of flippers. If \(r\) is even, the induced six-residual is antipodal-reversal odd and the established NORI \(Q_6\) theorem lifts. If \(r\) is odd, retain one flipper, eliminate the other \(r-1\) (even), use Corollary 2 on the induced odd \(Q_7\), and lift back by exact flipper elimination.

**Remaining frontier.** The unrestricted NORI conjecture still asks for all colorings, including \(Q_7\) colorings with **no** universal exterior flipper, and arbitrary higher-dimensional colorings with at least seven nonflipper directions. The present result completely eliminates the former six-residual bottleneck.
