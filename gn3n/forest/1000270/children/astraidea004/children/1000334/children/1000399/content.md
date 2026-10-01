# Local insertion failure permits arbitrary side-sign alternation

## Statement

Let B=(b_1,...,b_m) be a tight path, m>=4, and x a vertex outside B. Subject only to the boundary-tournament axioms, the truth values of the side triples (b_{i-1},b_i,x) and (x,b_{i+1},b_{i+2}) at internal gaps may be prescribed arbitrarily while insertion of x into every position of the displayed order of B fails. Consequently no interval or no-ABAB theorem for these side-feasibility signs can follow from failed insertion alone.

## Body

Fix any desired truth values for the triples
[
L_i=(b_{i-1},b_i,x)qquad (2le ile m-1)
]
and
[
R_i=(x,b_{i+1},b_{i+2})qquad (1le ile m-2).
]
These choices involve reversal pairs with middle vertices among the b_j. They are independent of the triples with middle x.

Declare each path triple
[
(b_i,b_{i+1},b_{i+2})qquad (1le ile m-2)
]
tight, so B is a tight path. For every internal gap between b_i and b_{i+1}, declare
[
(b_i,x,b_{i+1})
]
non-tight. This alone prevents insertion of x at that gap, regardless of the chosen values of the adjacent side triples L_i and R_i. Also declare
[
(x,b_1,b_2)quad	ext{and}quad (b_{m-1},b_m,x)
]
non-tight, preventing insertion at the two ends. Complete all still unspecified reversal pairs arbitrarily; the boundary-tournament axiom permits this independently for each reversal pair.

Thus every insertion position in the displayed order fails, while the internal left- and right-side signs can realize any prescribed binary pattern, including arbitrarily long alternation.

This does not refute the full insertion-slot conjecture for a globally longest path, because global maximality rules out many reordered extensions in addition to the displayed insertions. It does refute the proposed local first step: a no-ABAB or interval statement cannot be deduced from boundary antisymmetry plus failure of the displayed insertions alone. Any successful proof must use genuinely nonlocal maximality information, comparison-cycle structure, or an additional global invariant.
