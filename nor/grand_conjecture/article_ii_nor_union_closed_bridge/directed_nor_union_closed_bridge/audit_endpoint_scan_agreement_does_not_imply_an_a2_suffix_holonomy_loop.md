# Audit: endpoint scan agreement does not imply an A2 suffix holonomy loop

## Composition

(none yet)

## Development

Audit of the residual A2 suffix-holonomy claim. In the recurrent flat A2 replacement setup define s_u(j)=alpha(u,t_j,t_{j+1}). Flatness gives, for every residual pair u,v, s_u(j) xor s_v(j)=alpha(u,v,t_j) xor alpha(u,v,t_{j+1}). This identity is correct. However §§210-211 infer that because all three scans agree at the first suffix edge and again at the last suffix edge, the residual tournament at the rear equals the initial directed 3-cycle. That inference does not follow. Telescoping the displayed identity yields alpha(u,v,t_1) xor alpha(u,v,t_L)= XOR_{j=1}^{L-1}(s_u(j) xor s_v(j)). Equality of the scan bits on the last edge only says the final local switching class is zero; it does not force the XOR of all preceding switching classes to vanish. Likewise equality on the first edge says only that the first local switch is trivial. Thus the total class in F_2^3/<111> may be nonzero even though the endpoint scan vectors are each constant across U. Consequently a suffix excursion need not return to the original residual tournament, and the asserted Klein-four holonomy loop and its length-2/3/4 first-return classification are conditional on an additional zero-total-switch hypothesis not yet proved. The valid part of §210 is the local transport identity. The flat A2 recurrence remains reduced to a common-suffix switching path, but not necessarily a loop. A corrected target is to determine the rear residual tournament from the endpoint-blocker data, or exploit the possibility of nonzero total switch directly.
