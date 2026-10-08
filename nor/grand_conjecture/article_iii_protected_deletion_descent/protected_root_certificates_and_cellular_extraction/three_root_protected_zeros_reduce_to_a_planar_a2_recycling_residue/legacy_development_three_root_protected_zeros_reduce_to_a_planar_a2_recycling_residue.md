# Three-root protected zeros reduce to a planar A2 recycling residue — preserved pre-item development

## Development

Work in the pure alternating ternary sector. Consider a support-minimal positive zero of actual window-slide roots contained in one ordered-partition carrier cell, and suppose the support has exactly three roots.

For type-A roots, a support-minimal positive three-term dependence is necessarily a directed triangle with equal coefficients:
rho_1=e_a-e_b,
rho_2=e_b-e_c,
rho_3=e_c-e_a.
Indeed coordinate balance forces the three directed edges to form one directed 3-cycle; after scaling, every coefficient is equal.

Because the three root certificates occur in refinements of one ordered partition, their endpoint block indices satisfy
block(a)<=block(b)<=block(c)<=block(a).
Hence a,b,c all lie in one tied block B.

Take the chamber carrying rho_1. Its certified 10 packet has the form
(a,u,v,b)
with alpha(a,u,v)=1 and alpha(u,v,b)=0.
Since a,b lie in B and u,v occur between them in a refinement, u,v also lie in B. Therefore the adjacent middle swap u<->v is a legal chamber edge inside the same carrier cell. In the swapped chamber the packet is
(a,v,u,b)
and alternation gives colors 0,1, so this chamber carries no 10 certificate parallel to either rho_1 or -rho_1 on those packet endpoints.

Counterexamplehood guarantees that the swapped full order still has some actual 10 descent; let its actual root be sigma.

If sigma has an endpoint outside {a,b,c}, then sigma is not contained in the two-dimensional type-A subspace
W_{abc}=span{rho_1,rho_2}.
Use sigma as an interior label in a local subdivision of the triangular zero carrier. The old boundary loop has vertices rho_1,rho_2,rho_3. Cone each boundary edge to sigma. No coned triangle contains zero: if
lambda sigma+mu rho_i+nu rho_{i+1}=0
with lambda,mu,nu>=0 and lambda>0, projection to W/W_{abc} is nonzero because sigma is transverse; if lambda=0, the segment joining two consecutive directed triangle roots does not contain zero because they are not opposite. Hence the coned filling lies in W minus {0}.

Thus the three-root zero is locally removable whenever one middle-swapped certificate chamber supplies an actual descent root transverse to W_{abc}.

Consequently an essential three-root zero can survive only in the following planar residue:

For EACH of the three directed-cycle certificate chambers, after swapping the two middle coordinates of its certified 10 packet, every actual 10 root used to prevent a good full order has both endpoints in the same three-coordinate set {a,b,c}.

Equivalently, all available descent directions in those middle-swapped chambers lie in the A2 root subsystem on {a,b,c}.

This reduces the next extraction problem from an arbitrary ternary carrier cell to a rigid planar A2 residue. Any opposite root appearing there is already covered by the two-root blow-up theorem. Therefore a genuinely essential three-root zero must keep recycling only the three forward triangle directions through the middle-swapped chambers.

The remaining task is to show that this planar recycling forces a same-middle switch repair, a one-change order, or a two-root removable subzero.
