# Six-move endpoint control and exterior-sensitivity rigidity

**Six-move endpoint square.** Let p=(a,b,c,d,e,f) be six distinct coordinate directions in Q_n (n≥6), and fix all starting bits other than those in directions c,d. The four consecutive ordered-three-face window colors have the form
(A(u), B, C, D(v)),
where u=x_d, v=x_c. Indeed the first window (a,b,c) ignores x_c, the last (d,e,f) ignores x_d, and the two middle windows (b,c,d) and (c,d,e) ignore both. This holds for arbitrary Boolean ordered-three-face colorings and arbitrary fixed coordinates outside the six-move block.

**Exact square criterion.** Put R_A={A(0),A(1)} and R_D={D(0),D(1)}. If B≠C, a choice of u,v has at most one color change precisely when B∈R_A and C∈R_D. If B=C, a choice has at most one change precisely when B∈R_A or C∈R_D. In particular, if both endpoint functions are nonconstant, independently choose A(u)=B and D(v)=C to produce (B,B,C,C), a one-change block.

**Theorem (dimension-six crossed sensitivity).** For n=6 fix any coordinate order (a,b,c,d,e,f). Assume the color of the ordered face (a,b,c) changes with its exterior coordinate d for at least one assignment of the other two exterior coordinates e,f, and the color of (d,e,f) changes with its exterior coordinate c for at least one assignment of its other two exterior coordinates a,b. Then a successful antipodal geodesic exists with exactly this order and at most one change. Proof: first sensitivity depends only on (x_e,x_f) and second only on (x_a,x_b); choose these disjoint sets of bits to witness both sensitivities simultaneously. The endpoint-square criterion supplies x_d and x_c. □

**Rigidity under fixed-order failure (n=6).** Write A=A(x_d,x_e,x_f), B=B(x_a,x_e,x_f), C=C(x_a,x_b,x_f), D=D(x_a,x_b,x_c). Suppose no choice of starting vertex works with order (a,b,c,d,e,f). Assume A(0,e_0,f_0)≠A(1,e_0,f_0) for some (e_0,f_0). For every x_a,x_b,x_c choose x_d so A=B. Failure of the resulting word (B,B,C,D) forces B≠C and D≠C, hence B=D=1⊕C. Holding e=e_0 and f=f_0 yields
B(x_a,e_0,f_0)=D(x_a,x_b,x_c)=1⊕C(x_a,x_b,f_0)
for every x_a,x_b,x_c. Since B ignores x_b and x_c, D is independent of x_b,x_c and C(.,.,f_0) is independent of x_b. In particular D cannot be sensitive in x_c. The mirror statement follows by reversing the four windows. This is a necessary structural restriction for any hypothetical dimension-six counterexample.

**Scope.** Crossed sensitivities provide local six-move control in larger dimensions, but concatenation into a full n-move geodesic requires compatible window colors outside the controlled block. Coordinate-only colorings have no exterior sensitivities and are not addressed by this argument.
