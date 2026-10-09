# Nonlinear faults, exterior sensitivity and holonomy

# Exterior sensitivity, nonlinear faults, and lifting holonomy

A physical ordered three-face coloring may depend arbitrarily on its fixed exterior coordinate bits. For a direction word p=(p_1,...,p_n), the consecutive windows along the full rooted geodesic are functions of the starting root x; every window ignores the three free coordinates in its own ordered triple.

## The six-move endpoint square

For six distinct directions (a,b,c,d,e,f), fix all root bits except x_d=u and x_c=v. The four consecutive window colors have the form

(A(u),B,C,D(v)).

Indeed the middle windows (b,c,d) and (c,d,e) contain both c and d among their free directions, so their colors are independent of u,v. The first window (a,b,c) may depend on d but ignores c; the last (d,e,f) may depend on c but ignores d.

If B≠C, a choice of u,v yields at most one change precisely when B is in the image of A and C is in the image of D: choose (B,B,C,C). If B=C, one change is achievable when at least one endpoint image contains the middle color, since the other endpoint can then contribute at most one switch. When A and D are both nonconstant, both middle colors can be matched independently. In an actual six-dimensional cube, crossed exterior sensitivity at the two opposite endpoint windows can be witnessed using disjoint remaining root bits, producing a full six-edge geodesic with at most one change.

## Affine change maps and controlled nonlinear tails

Consider the baseline exterior-parity coloring c_0(F,pi)=h(pi)+sum_{i outside F} x_i modulo two. Along a fixed direction order, the vector of consecutive color differences is an affine map of the root bits. In the full-parity case this change map is surjective, and fibers contain many roots with all but a selected change coordinate zero.

Suppose a coloring agrees with c_0 on the first L−2 window types of one fixed direction order, where L=n−2, while its last two ordered window types may depend arbitrarily and nonlinearly on the exterior bits. The robust-tail theorem proves that at least 2^(r+1) roots give full at-most-one-switch geodesics for ordered r-faces when its prescribed affine control hypotheses hold; for r=3 this yields sixteen roots. Its proof uses surjectivity of the prefix change map and an independent root-bit involution that flips the entire clean prefix without changing the last two physical windows. The latter property is an explicit ingredient, not a consequence of arbitrary NORI symmetry.

## Exterior-coordinate holonomy

A forcing certificate verified within a six-coordinate cube need not preserve antipodal physical-face identifications after embedding into Q_n. Fix an outside coordinate g. If three supposed antipodal-reversal identifications between rows 1,2,4 require exterior fixed-bit relations z_2=1−z_1, z_4=1−z_1 and z_4=1−z_2, the first two yield z_2=z_4 whereas the third requires z_2≠z_4. Thus no assignment of the g-bit realizes all three physical identifications at once.

More generally assign a parity requirement to each proposed identification edge in a diagram of root charts: zero for equality of fixed exterior bits and one for complementation. Realizability requires each cycle have even total parity. The six-path extension obstruction is exactly a nonzero mod-two holonomy cycle. This criterion explains why local Q_6 color equalities cannot simply be transported to arbitrary ambient dimension.

Together, these results give rigorous good-path closure for controlled nonlinear perturbations, exact endpoint sensitivity tests, and a complete parity obstruction to one class of naive lifting arguments. The unrestricted problem requires either stronger root-control structure or a global method which varies the exterior charts while preserving genuine physical window identities.
