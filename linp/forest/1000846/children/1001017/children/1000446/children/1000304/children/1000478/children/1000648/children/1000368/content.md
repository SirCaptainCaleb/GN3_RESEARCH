# Potential-oriented local bound for ascending terminal edges

## Statement

Let H be a finite linear 3-graph and let a(v) be the maximum length of a linear path ending at v. Fix v∈V(H). Then there are at most three ascending nonspecial edges e={x,v,u} for which v is a terminal vertex and a(u)>=a(v).

## Body

This removes the minimum-degree and P_ell-free hypotheses from the existing local conjecture 4e1c498f922a, but only in the potential-oriented form actually needed for global charging. The known counterexample 830b0775567f to unrestricted terminal degree does not refute this statement: its common terminal v has a(v)=21 and the four ascending edges have opposite-terminal potentials 21,12,18,21, so only two qualify. The unbounded common-terminal construction d5e0ab668a51 is likewise compatible: its excess terminal edges descend sharply in endpoint potential. A proof would likely use mutual tail-blocking of longest paths at the two terminal vertices rather than a raw pointwise-degree argument.
