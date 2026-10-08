# Coboundary-flat NOR is exactly a tournament switching-class two-chord problem — preserved pre-item development

Exact switching-class formulation of the coboundary-flat pure-orientation sector. Let alpha be represented by a tournament bit t through alpha(a,b,c)=1 xor t(a,b) xor t(b,c) xor t(c,a), with the convention adjusted consistently with the existing edge-potential subsection. Vertex switching at a subset S toggles every tournament edge with exactly one endpoint in S. This preserves the parity of the three edge bits on every triangle, hence preserves alpha.

Fix any coordinate order O=(v_1,...,v_n). Let e_i=t(v_i,v_{i+1}). Choose switching bits s(v_1)=0 and recursively s(v_{i+1})=s(v_i) xor e_i (up to the fixed orientation convention). In the switched tournament T^s every adjacent edge v_i v_{i+1} is oriented forward along O. Therefore O is a directed Hamilton path of T^s. Since alpha is switching-invariant, along O the ternary status reduces exactly to the distance-two shortcut bit in T^s. Conversely, any directed Hamilton path in any switched representative produces the same alpha word by the same formula.

Hence the correct exact flat-sector reformulation is:

Find a tournament representative in the switching class and a directed Hamilton path in that representative whose distance-two shortcut directions change at most once.

Equivalently, after switching so the Hamilton path edges are all forward, NOR asks that the edges of the path square at distance two are forward and then backward in at most one phase (or the reverse).

This repairs the earlier audit: restricting to directed Hamilton paths of one fixed representing tournament is only sufficient, but allowing all vertex switchings is genuinely equivalent to arbitrary coordinate orders. The two-cyclic-component example that defeated the fixed-representative theorem is not an obstruction to the switching-class theorem; its alternating good order simply becomes a directed Hamilton path after the corresponding vertex switches.

Adversarial consequence: a coboundary-flat counterexample would have to defeat the two-chord one-change property in every switched representative of its tournament switching class, a substantially stronger requirement than defeating it in one tournament.
