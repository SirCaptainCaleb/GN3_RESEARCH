# Root-endpoint torus has equivariant index one and canonical color-free zeros

# The root-endpoint torus has equivariant index one: a sharp obstruction to naive Borsuk–Ulam closure

Continue with the uncolored root-endpoint state torus T_n=(S^1)^n whose coordinate square has vertices 00,01,11,10 in cyclic order. Assign each coordinate square an angle theta with theta(00)=0, theta(01)=pi/2, theta(11)=pi, theta(10)=3pi/2, and extend linearly along each square edge. The product gives actual angular coordinates (theta_1,...,theta_n) on the torus.

Let alpha(x,y)=(bar x,bar y) be simultaneous cube antipodality and sigma(x,y)=(y,x) be endpoint exchange, and set tau=alpha sigma. The actions are exactly
alpha(theta) = theta + (pi,...,pi),
sigma(theta) = -theta,
tau(theta) = (pi,...,pi)-theta
(modulo 2pi in every coordinate).
The diagonal D=Fix(sigma) is {0,pi}^n; the antipodal-endpoint set A=Fix(tau) is {pi/2,3pi/2}^n.

**Theorem (sharp equivariant-index no-go).** For every n>=2 there exists a continuous, everywhere nonzero alpha-odd map T_n -> R^2, namely
h(theta)=(cos theta_1,sin theta_1).
Indeed h(alpha theta)=-h(theta), and ||h||=1. Therefore any putative proof that uses only a free alpha-involution on the whole root-endpoint torus cannot invoke a dimension-n Borsuk–Ulam zero theorem: the torus admits an equivariant map to S^1 in every dimension n.

More precisely, the double cover T_n -> T_n/<alpha> has first Stiefel–Whitney class w satisfying w!=0 and w^2=0. The equivariant h descends to a map of quotients T_n/<alpha> -> RP^1 and identifies the classifying bundle as the pullback of S^1 -> RP^1; hence w^2=0 because H^2(RP^1;F_2)=0. The class w is nonzero because the total space T_n is connected, so the double cover does not split. Thus its mod-two cohomological index is exactly one.

**A tautological zero map.** The map F:T_n -> R^n with F_i(theta)=cos theta_i satisfies F(alpha theta)=-F(theta) and F(sigma theta)=F(theta), and has exactly the 2^n zeros A. These zeros are intrinsic antipodal-endpoint states, independent of all edge colors and of monochromatic geodesic reachability. They have no automatic directed-path certificate from the starting diagonal D. In fact h gives an explicit global odd zero-free map to R^2, so in n>=2 the existence of zeros for this particular F cannot be defended by a dimension-n Borsuk–Ulam principle.

**Implication.** The product-circle realization genuinely encodes both endpoint moves and protects geodesicity, but its free antipodal geometry alone has too little equivariant index to force a colored D-to-A directed chain. Any topological closure must involve the coloring-dependent directed reachability structure, an additional relative boundary condition, or a different carrier space. This no-go is for the ordinary antipodally odd *edge* problem; it does not refute NORI's ordered-three-face conjecture.
