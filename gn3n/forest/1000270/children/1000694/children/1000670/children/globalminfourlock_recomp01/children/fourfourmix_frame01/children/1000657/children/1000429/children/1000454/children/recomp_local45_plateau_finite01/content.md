# A local 4|5|m minimum has an equal-profile cyclic cover or a finite locked-label geometry

## Statement

Let H be a boundary tournament and let C=X|Y|P minimize quadratic potential within its connected pairwise-repartition component, with |X|=4, |Y|=5, and P=(p_1,...,p_m) of order m>=7. Then at least one of the following holds: (1) there exists another spanning three-cover with the same component-order multiset {4,5,m}, obtained by a cyclic support exchange x from X to Y, y from Y to P, and one endpoint e of P to X; no pairwise-repartition reachability of this cover from C is asserted; (2) some y in Y has a first-type failed-insertion window on P, whose associated four-set is Hamiltonian or the universal cyclic non-Hamiltonian four-kernel; (3) two distinct labels y,z in Y have second-type obstructions at the same gap of P, and together with that displayed gap edge form a Hamiltonian four-set; (4) two distinct labels y,z in Y are joined by a tight connector (y,p_{r+1},...,p_s,z) through an interval of P with s>=r+2.

## Body

First synchronize one label of X with both ends of P. If X union {e} were Hamiltonian for an endpoint e of P, the legal repartition (4,m)->(5,m-1) would change Phi by 10-2m<0, contradicting componentwise minimality. Hence both endpoint five-sets X union {p_1}, X union {p_m} are non-Hamiltonian. For e in {p_1,p_m}, let I_e={x in X:(X-{x}) union {e} is Hamiltonian}. By the non-Hamiltonian five-set deletion theorem in smallset01, |I_e|>=3, so the two sets intersect in at least two labels. Fix x in their intersection.

We next show Y union {x} is non-Hamiltonian. If it were Hamiltonian, first repartition X|Y as (X-{x}) | (Y union {x}), changing sizes (4,5) to (3,6), and then use either endpoint e of P to repartition (X-{x})|P as ((X-{x}) union {e}) | (P-e), changing sizes (3,m) to (4,m-1). Relative to C the resulting cover has orders (4,6,m-1), so Delta Phi=12-2m<=-2, again contradicting componentwise minimality. Thus Y union {x} is non-Hamiltonian. Four-of-six applied to this six-set shows that at least three vertices y in Y satisfy (Y-{y}) union {x} Hamiltonian; let J be three such labels.

Apply certified 5c95da081ff4 to x and J. If for some y in J an endpoint truncation of P enlarged by y is Hamiltonian, the three displayed Hamiltonian supports form another spanning cover with the same orders 4,5,m, giving (1). This is only an existence conclusion; no same-component reachability is used or asserted. Otherwise all three labels of J are noninsertable into every position of P.

Apply insert01 to these three locked labels. If any has first-type obstruction, 0425e03e2aa3 gives (2). Otherwise all three have second-type obstruction gaps. If two gaps coincide, the same-gap case of 36fccff06d48 gives (3). If the three gap indices are distinct, the smallest and largest differ by at least two, and the separated-gap case of 36fccff06d48 gives (4).
