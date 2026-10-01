# Cheap vertices carry balanced endpoint-lens packets on both host halves

## Statement

Let v be a low-defect active misaligned vertex of rank p whose switching-source mass is within o(p^2) of the generic 185/512 p^2 floor. On the chosen maximum p-edge host path P_v, there are at least
  [5(8-sqrt(42))/176-o(1)]p
distinct terminal-retained attachment vertices strictly on each side of the host midpoint. Every such attachment vertex u supports a clean balanced elementary endpoint lens between P_v and a maximum u-ending path.

Thus a locally cheap vertex carries two macroscopic, spatially separated endpoint-lens packets, one on each host half.

## Body

By f4182d73a95c, if k_- and k_+ count terminal-retained switcher contacts strictly left and right of the midpoint of P_v, then
  min{k_-,k_+} >= [5(8-sqrt(42))/176-o(1)]p.
Distinct terminal-retained switchers through v have distinct retained terminals u: two distinct hyperedges already share v, so linearity forbids a second shared vertex.

For every terminal-retained switcher e={x,v,u}, theorem 6f2198c7d34a applies because u lies on P_v and x does not. It supplies a clean balanced elementary endpoint lens between P_v and an arbitrary maximum endpoint path P_u, attached at u.

Therefore the k_- left-half contacts yield k_- distinct host attachment vertices carrying balanced endpoint lenses, and likewise the k_+ right-half contacts yield k_+ distinct host attachments. Substituting the lower bound from f4182d73a95c proves the claim.
