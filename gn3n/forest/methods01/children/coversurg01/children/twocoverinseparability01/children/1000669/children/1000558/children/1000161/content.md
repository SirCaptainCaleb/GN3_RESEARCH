# Equality-two-crossing separations have a global support normal form

## Statement

Under the hypotheses of ac412d91495d, suppose a separating two-cover T of H-v has exactly two ordinary edges crossing V(L)|V(R)|V(B). Then exactly one of L,R,B is split into two maximal blocks. If B is split, T necessarily has the crosswise support form (L union B_1)|(R union B_2), up to interchanging B_1,B_2. If L is split into L_s and L_o with s in L_s, then either T has the crosswise support form (L_s union B)|(L_o union R), or L_s is an entire component of T and the other component has support L_o union R union B. The symmetric alternatives hold when R is split, with the t-containing block in place of L_s.

## Body

Deleting the two crossing edges of T leaves four maximal monochromatic path blocks. The old classes L,R,B are nonempty, so exactly one old class contributes two blocks and the other two contribute one each.

Suppose first that B splits as B_1,B_2. Since T separates s in L from t in R, L and R lie in different T-components. If the four blocks form two two-block components, each component must pair one of L,R with one B-block, giving the crosswise form. If instead one component contains three blocks and the other is isolated, the three-block component cannot contain both L and R. Thus, up to symmetry, L is isolated and the other component has blocks B_1,R,B_2, or R is isolated and the other has B_1,L,B_2. In the first case T contains a Hamilton path on V(R) union V(B), contradicting cc27560d3e40; in the second it contains one on V(L) union V(B), again a contradiction. Hence only the crosswise form occurs.

Now suppose L splits into blocks L_s,L_o, with s in L_s. If the block forest consists of two two-block components, L_s cannot pair with R because T separates s and t. The two L-blocks cannot be adjacent in T, since then they would be one maximal L-block. Therefore L_s must pair with B and L_o with R, giving the crosswise form.

If one T-component contains three blocks and the other is isolated, the isolated block cannot be R: the other component would be a Hamilton path on V(L) union V(B), contradicting cc27560d3e40. It cannot be B, since then the other component contains both s and t. It cannot be L_o for the same reason. Thus only L_s may be isolated, and the other component has support V(L_o) union V(R) union V(B).

The case where R splits is symmetric. No minimality is used. In a minimum prescribed-separation counterexample, astra005minblock supplies the additional lower bound on the isolated prescribed-side block after adjoining v; that size conclusion is separate from this support classification.