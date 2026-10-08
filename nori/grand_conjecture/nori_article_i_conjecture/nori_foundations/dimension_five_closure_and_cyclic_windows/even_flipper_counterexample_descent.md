# Even flipper sets descend antipodal oddness

## Development

Statement:
Let c be an antipodally odd ordered-three-face coloring of Q_{A⊔B} satisfying the universal-flipper condition on A. Its induced coloring g_B on the B-subcube obeys g_B(bar F,rev π)=g_B(F,π)⊕1⊕(|A| mod 2). If |A| is even, a counterexample c forces an antipodally odd counterexample g_B in dimension |B|. In particular a minimum-dimensional NORI counterexample with n≥6 has at most one universal-flipper coordinate.

Proof:
For a face whose free triple lies in B, write c(F,π)= (⊕_{a∈A}x_a)⊕g_B(F_B,π). Antipodal complementation toggles all |A| fixed A bits. Comparing c(bar F,revπ)=1⊕c(F,π) yields g_B(bar F_B,revπ)=g_B(F_B,π)⊕1⊕(|A| mod2). By the backward-elimination theorem, a good B-geodesic lifts to a full good geodesic for c; contraposition proves the counterexample descent. If two universal flippers existed in a minimum-dimensional counterexample, choose those two as A. Then g_B is an antipodally odd counterexample on n−2≥4 coordinates, contradicting minimality.
