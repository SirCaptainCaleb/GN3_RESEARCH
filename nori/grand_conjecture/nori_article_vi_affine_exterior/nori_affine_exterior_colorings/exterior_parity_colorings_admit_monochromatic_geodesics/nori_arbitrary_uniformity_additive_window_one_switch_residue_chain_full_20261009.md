# All-dimensional one-switch additive r-window sequencing by residue classes

# Universal one-switch sequencing of additive r-window parity in every dimension

Let n≥r≥2 and let w:V→F2 be ANY bit assignment on n distinct coordinate names. For an ordered r-tuple of distinct names define a(π)=d+Σ_(v∈π)w_v (mod 2), with arbitrary d∈F2.

**THEOREM (all r, all n, every prescribed weight).** There exists a permutation p=(p_1,...,p_n) of ALL n coordinates such that the consecutive r-window color word
 a(p_1,...,p_r), a(p_2,...,p_(r+1)), ..., a(p_(n-r+1),...,p_n)
has AT MOST ONE change.

**Proof (explicit modular-chain construction).** Write z_i=w_(p_i), and let y_i=d+Σ_(j=i)^(i+r−1)z_j be the resulting color word. The consecutive difference satisfies the exact identity

 y_(i+1)+y_i = z_i+z_(i+r) (mod 2).

Partition the n ordered positions into the r residue classes modulo r. Choose a class C of maximal size Q=ceil(n/r). Each of the other r−1 classes has size ≤Q. Assign ALL bits on each of these other classes to 0 or 1, leaving C available for partial occupation. List the other classes arbitrarily as D_1,...,D_(r−1), with sizes s_j≤Q. For t=0,1,...,r−1, the consecutive interval of feasible total one-counts

 [s_1+...+s_t, s_1+...+s_t+Q]

covers all integers between 0 and n, because adjacent starting points differ by s_(t+1)≤Q, the first starts at zero, and the last ends at n. For the prescribed m=|{v:w_v=1}| choose a t and an integer u∈[0,Q] with m=s_1+...+s_t+u. Fill D_1,...,D_t entirely with ones; fill the other D classes entirely with zeros. Along C in increasing position order put u ones followed by Q−u zeros.

This construction produces exactly m ones among all positions, so assign the actual coordinates of weight1/weight0 to the matching positions to obtain the permutation p. For every residue class other than C, z_(i+r)=z_i whenever both positions exist. In C, this same equality holds except possibly across its unique one-to-zero boundary. Therefore y_(i+1)+y_i is nonzero for at most ONE index i, and the full r-window color word is one-switch. QED.

**COROLLARY (full physical NORI-type odd-face subclass).** Let r≥3 be odd, n≥r+1 be even, and k=(n−r−1)/2. Suppose a coloring of actual physical ordered r-faces obeys
 c(F,π)=d+Σ_(v∈π)w_v  when the fixed exterior one-weight is k,
 c(F,π)=1+d+Σ_(v∈π)w_v when it is k+1,
and its values elsewhere are arbitrary subject to the antipodal reversal-odd rule. Then it has an actual full antipodal n-edge geodesic with at most one r-face window-color change.

Proof: use the theorem to choose p. Take initial cube root whose starting bits in order p are x_i=1 for odd i, 0 for even i. For the window starting at i the actual exterior one-weight is
 K_i=Σ_(j<i)(1−x_j)+Σ_(j>i+r−1)x_j.
Because r is odd, x_(i+r)=1−x_i; hence K_(i+1)−K_i=1−x_i−x_(i+r)=0. At i=1 the n−r exterior positions begin at the even position r+1 and alternate 0,1,...; since n−r is odd, exactly (n−r−1)/2=k are ones. Thus EVERY ordered r-face window of this true cube geodesic lies on the lower physical central layer, where its color is the additive a-window word just constructed. The antipodal relation holds because reversing π does not alter a and complementing exterior bits exchanges layers k,k+1. QED.

For the active r=3 NORI conjecture this proves dimension-independent closure of the ADDITIVE central two-layer class while allowing arbitrary physical-face dependence on all remaining exterior layers. The general unrestricted NORI conjecture remains open.
