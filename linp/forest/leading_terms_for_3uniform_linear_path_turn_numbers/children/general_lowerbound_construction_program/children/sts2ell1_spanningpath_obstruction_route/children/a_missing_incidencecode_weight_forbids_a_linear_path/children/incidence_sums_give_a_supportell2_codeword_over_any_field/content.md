# Alternating incidence sums give a support-(ell+2) codeword over any field

## Statement

Let H be a 3-uniform hypergraph, let F be any field, and let C_F be the F-linear span of the edge-incidence vectors. If H contains a linear path P_ell^(3), then C_F contains a vector whose support has size exactly ell+2. Hence if every nonzero vector of C_F has support size different from ell+2, then H is P_ell^(3)-free.

## Body


Let e_1,...,e_ell be a linear path and let chi_i be the incidence vector of e_i over F. Consider
  z = chi_1 - chi_2 + chi_3 - ... + (-1)^{ell-1} chi_ell.
At each joint e_i intersect e_{i+1}, the two contributions have opposite coefficients and cancel. Every other path vertex lies in exactly one path edge, so its coordinate in z is either +1 or -1, hence nonzero in every field (in characteristic 2 the two signs coincide, but the joint still cancels because 1+1=0). Therefore supp(z) is exactly the set of vertices used once by the path. A 3-uniform linear ell-edge path has 2ell+1 vertices and ell-1 joints, so |supp(z)|=(2ell+1)-(ell-1)=ell+2.
