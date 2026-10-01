# Separated insertions of one label across a four-path force a cross triple or a tight cycle

## Statement

Let B=(p_1,p_2,p_3,p_4) be a tight four-vertex path and let x be exterior to B. Suppose x can be inserted into the displayed order of B at a left gap ell in {0,1} and also at a right gap r in {3,4}, where gaps are numbered 0 before p_1, j between p_j and p_{j+1}, and 4 after p_4. Put a=p_{ell+1} and b=p_r. Then either (a,x,b) is tight, or the cyclic word
(x,a,p_{ell+2},...,p_r)
is a vertex-simple tight cycle. In particular the support has order between three and five.

## Body

The successful left insertion shows that the linear sequence
(x,a,p_{ell+2},...,p_r)
is a tight path: it is a contiguous subpath of the left-insertion Hamilton order.

The successful right insertion shows that the final wrap triple
(p_{r-1},b,x)
is tight (with the evident interpretation when r=3 or 4). Thus every cyclic consecutive triple of the displayed cyclic word
x,a,p_{ell+2},...,b,x
is already tight except possibly (b,x,a).

If (b,x,a) is tight, the displayed cyclic word is a vertex-simple tight cycle.

If (b,x,a) is non-tight, boundary reversal antisymmetry gives its reverse
(a,x,b)
tight. This is the stated cross triple.

The four possible pairs (ell,r) are (0,3),(0,4),(1,3),(1,4), so the cycle has respectively four, five, three, or four vertices. No cyclic permutation of any tight ordered triple is assumed.
