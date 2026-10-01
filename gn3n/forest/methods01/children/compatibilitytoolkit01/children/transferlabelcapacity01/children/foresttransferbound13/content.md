# A disturbance-free forest without reciprocal direct crossings has at most thirteen selected edges

## Statement

Let H be a minimum counterexample in the sharp half-order shell, and let J be a lexicographically maximal forest deletion-cover transversal with one Hamilton order chosen on each support vertex. Suppose no length-two walk of J exposes inherited three-part support crossing or order disagreement, and suppose no two selected deletion covers from distinct components contain reciprocal ordinary core edges crossing the other cover's induced support partition on their common double deletion. Then |E(J)|<=13.

## Body

By 9d79ac6c14d5, every component of J is a path with at most five edges. Choose a largest component C and write alpha=|E(C)|, so alpha<=5. Fix one selected edge e_a in C.

Let e_b be any selected edge outside C, lying in a component D with beta=|E(D)|<=alpha. By 5e65e55c7ecd, the deletion covers F_a and F_b are support-incompatible on their common double deletion. The pair dichotomy 68deffb43319 applies. Its fully crossed branch is impossible, because c30a4d92d20b would then give reciprocal ordinary core crossing edges, contrary to hypothesis. Thus the pair takes the singleton-transfer branch; let x be its transfer label.

Apply d0c8789888c4 to C,D. The selected edge e_x cannot lie in D. If it lay in a third component E, then
|E(E)| >= alpha+beta+1 > alpha,
contradicting the choice of C as a largest component. Hence e_x lies in C.

The transfer label x is distinct from a and b. Since e_x lies in C, x is one of the alpha deletion labels carried by the selected edges of C, but not the fixed label a. Thus, as e_b ranges over all selected edges outside C, there are at most alpha-1 possible transfer labels x.

For each fixed such x, transferlabelcapacity01 shows that all selected partner edges e_b using x are incident with one common support T_x. Because every component of J is a path, deg_J(T_x)<=2. Therefore at most two outside selected edges use any fixed x. Consequently
|E(J)|-alpha <= 2(alpha-1),
and hence
|E(J)| <= 3alpha-2 <= 13.
∎