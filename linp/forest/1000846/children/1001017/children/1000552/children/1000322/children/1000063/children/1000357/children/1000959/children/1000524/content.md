# Affine-plane boosters preserve an ascending edge at minimum degree four

## Statement

For every L>=2 there is a finite linear 3-graph H_L with minimum degree 4 containing an ascending nonspecial edge. In fact H_L has a distinguished edge e with φ(e)=L+3 and unique entrance x satisfying φ(x)=L+2.

## Body

Construction. Start with the linear path E_1,...,E_L, where E_i={a_{i-1},b_i,a_i}. For every ground vertex w of this path, take a fresh copy B_w of the affine plane STS(9), identify one chosen point of B_w with w, and keep all other booster vertices disjoint from everything else. The affine plane has 12 lines in four parallel classes of three; its intersection graph is K_{3,3,3,3}, hence every induced path in a booster has at most three edges. Moreover for the identified point w there is a three-edge linear path inside B_w ending physically at w: choose first and third lines parallel, with the third through w, and the middle line transversal and not meeting the third at w.

The resulting hypergraph is linear. Every new booster vertex has degree 4, while every original path vertex has its path degree plus the four booster lines through the identified point. Hence δ(H_L)=4.

Let e=E_L and x=a_{L-1}. Any induced path that uses both a booster and base-path edges can use that booster only as an initial or terminal segment: all booster lines through the identified root form a clique, so an induced path cannot enter a booster from the base and later return to the base. A booster prefix has length at most three. After leaving a booster, the base edges used on a path ending in E_L form a contiguous suffix of E_1,...,E_L. Therefore every path ending in E_L has length at most L+3. Equality is attained by a three-edge path in B_{a_0} ending at a_0 followed by E_1,...,E_L. Any path ending in E_L through b_L or a_L has predecessor in the corresponding terminal booster and therefore has length at most four. Hence every longest path ending in E_L enters through x=a_{L-1}; thus E_L is nonspecial and φ(E_L)=L+3.

Similarly, a three-edge path in B_{a_0} followed by E_1,...,E_{L-1} has length L+2 and ends physically at a_{L-1}. Any path ending physically at a_{L-1} with last edge E_L has length at most four, and a path with last edge in B_{a_{L-1}} has length at most three. Hence φ(a_{L-1})=L+2=φ(E_L)-1, so E_L is ascending.

In fact the longest path in H_L has length L+6: take a three-edge booster prefix at a_0, traverse E_1,...,E_L, and append a three-edge booster suffix at a_L. Thus H_L is P_{L+7}^{(3)}-free, but its minimum degree remains 4. Consequently this family does not enter the admissible regime δ>2ell/3 when ell=L+7; it refutes only fixed-threshold minimum-degree statements and reinforces the need for minimum degree scaling with ell.
