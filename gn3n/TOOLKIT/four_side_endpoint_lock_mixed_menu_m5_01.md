# The four-side endpoint lock yields a mixed bounded support or one positioned interval path

**Summary:** Let H be a minimum counterexample and let X|P|Q be a spanning three-cover with |X|=4 and P=(p_1,...,p_m), m>=5. Put M=(p_2,...,p_{m-1}). Then at least one of the following holds: (1) there is a legal pairwise repartition of X|P with component orders (5,m-1), whose quadratic-potential change is 10-2m<=0, with equality only when m=5; (2) H contains a proper Hamiltonian induced set U of order four or five that meets both X and V(M), with H-U non-Hamiltonian of path-cover number two; more precisely U may be chosen in one of the forms: one vertex of X plus three consecutive vertices of M, two vertices of X plus three consecutive vertices of M, or two vertices of X plus the two vertices of one displayed gap of M; (3) there are distinct u,v in X and two displayed obstruction gaps of M separated by at least one intervening gap such that u and v are joined by the tight interval path through the corresponding displayed subinterval of M. Thus the bounded-support outcome is necessarily a genuine cross-component migration, not merely the original four-side.

## Statement

Let H be a minimum counterexample and let X|P|Q be a spanning three-cover with |X|=4 and P=(p_1,...,p_m), m>=5. Put M=(p_2,...,p_{m-1}). Then at least one of the following holds: (1) there is a legal pairwise repartition of X|P with component orders (5,m-1), whose quadratic-potential change is 10-2m<=0, with equality only when m=5; (2) H contains a proper Hamiltonian induced set U of order four or five that meets both X and V(M), with H-U non-Hamiltonian of path-cover number two; more precisely U may be chosen in one of the forms: one vertex of X plus three consecutive vertices of M, two vertices of X plus three consecutive vertices of M, or two vertices of X plus the two vertices of one displayed gap of M; (3) there are distinct u,v in X and two displayed obstruction gaps of M separated by at least one intervening gap such that u and v are joined by the tight interval path through the corresponding displayed subinterval of M. Thus the bounded-support outcome is necessarily a genuine cross-component migration, not merely the original four-side.

## Body

Apply four_side_endpoint_package_m5_01. In its hard branch, every t in X is noninsertable into the displayed interior path M. Choose distinct x,y,z in X and apply three_noninsertables_finite_menu01. If one label, say x, has a first-type obstruction, 0425e03e2aa3 gives a four-vertex window C consisting of x and three consecutive vertices of M. If C is Hamiltonian, take U=C; it has one vertex in X and three in M. If C is the exceptional cyclic non-Hamiltonian four-set, every exterior one-vertex extension is Hamiltonian; adjoining either y or z gives a Hamiltonian five-set U with two vertices in X and three in M. If two labels have second-type obstructions at the same gap, 36fccff06d48 gives a Hamiltonian four-set consisting of those two X-labels and the two vertices of that gap of M. These are exactly the bounded-support cases and all meet both sides. Since H is a minimum counterexample and each U is proper, mincex01 gives a non-Hamiltonian path-cover-two complement. The remaining alternative of three_noninsertables_finite_menu01 is the positioned interval path in (3). The first alternative is inherited unchanged from four_side_endpoint_package_m5_01.

## Metadata

- ID: four_side_endpoint_lock_mixed_menu_m5_01
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
