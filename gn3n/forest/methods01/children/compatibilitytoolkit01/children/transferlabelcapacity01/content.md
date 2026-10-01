# A fixed singleton-transfer label determines one opposite support

## Statement

Let H be in the sharp half-order shell and let J be a selected deletion-cover transversal. Fix a selected edge e_a of J and a deletion label x distinct from a. For every selected edge e_b such that the comparison of the deletion covers F_a and F_b takes the singleton-transfer branch of 68deffb43319 with transfer label x, the endpoint of e_b used by the resulting x-labelled alternative deletion edge is one Hamiltonian support T_x determined uniquely by e_a and x. Consequently the number of such selected edges e_b is at most deg_J(T_x). In particular, if every component of J is a path, there are at most two.

## Body

Write the endpoints of e_a as the disjoint Hamiltonian lambda-supports R and R', so R union R'=V(H)-{a}. Because x is distinct from a, exactly one of R,R' omits x; call it S.

Now let e_b be any selected edge whose comparison with e_a takes the singleton-transfer branch with transfer label x. In the lifted form of 68deffb43319, the resulting alternative deletion edge labelled x has one endpoint equal to the component support of F_a that omits x. Thus that endpoint is S.

An x-labelled edge in the Hamiltonian-support odd graph joins two disjoint lambda-supports whose union is V(H)-{x}. Once S is fixed, its other endpoint is therefore forced:
T_x = V(H) - (S union {x}).

The same lifted form says that this other endpoint T_x is a component support of F_b. Hence the selected edge e_b is incident with T_x. This holds for every e_b using the fixed pair (e_a,x), so their number is at most deg_J(T_x). If every component of J is a path then deg_J(T_x)<=2. ∎
