# Distinct covers of one sharp-shell deletion have a two-crossing gap

## Statement

Assume H is a minimum counterexample with |V(H)|=2lambda+1, where lambda is the maximum tight-path order. Fix x and an exact deletion cover H-x=A|B. For any other exact two-cover T of H-x, let t be the number of ordinary T-edges crossing the support cut V(A)|V(B). Then either t=0, in which case T has the same unordered support partition {V(A),V(B)}, or t>=2. If t=2, cutting the two crossing edges yields exactly two A-blocks and two B-blocks, and the two components of T each consist of one A-block and one B-block joined by one crossing edge.

## Body

By the sharp-shell theorem, |A|=|B|=lambda and every tight path in H has order at most lambda. Let T be an exact two-path cover of H-x and let t be its number of crossings of A|B. Cutting the t crossing edges yields b_A A-blocks and b_B B-blocks, with b_A+b_B=t+2.

If t=0, every connected component of T lies in one side of the cut. Since T has exactly two nonempty components covering the two nonempty sides, its unordered support partition is exactly {A,B}.

Now suppose t>0. If b_A=1, all lambda vertices of A lie in one contiguous block of one T-component. Because t>0, this block is adjacent in that component to a nonempty B-block, producing a tight path of order greater than lambda, contradiction. Thus b_A>=2. Symmetrically b_B>=2. Therefore t+2=b_A+b_B>=4, so t>=2.

If t=2, then b_A=b_B=2. Contract the four monochromatic blocks. If both crossing edges lie in the same T-component, that component has three alternating blocks. It is either A_1-B_1-A_2, containing all of A plus a nonempty B-block, or B_1-A_1-B_2, containing all of B plus a nonempty A-block. Either has order greater than lambda, contradiction. Hence the two crossing edges lie in different T-components, and each component consists of exactly one A-block and one B-block.