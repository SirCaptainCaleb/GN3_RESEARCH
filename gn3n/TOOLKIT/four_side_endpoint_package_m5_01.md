# The four-side endpoint package extends through the neutral order-five threshold

**Summary:** Let H be a boundary tournament and X|P|Q a spanning three-cover with |X|=4 and P=(p_1,...,p_m), m>=5. Put a=p_1, b=p_m, and M=(p_2,...,p_{m-1}). Then either there is a legal pairwise repartition of X|P with component orders (5,m-1), whose quadratic-potential change is 10-2m (strictly negative for m>=6 and zero for m=5), or both X union {a} and X union {b} are non-Hamiltonian and, for every t in X, F_t=(X-{t}) union {a,b} is Hamiltonian while L_t=V(M) union {t} is non-Hamiltonian. In the latter case there are distinct x,y,z in X such that {a,b,x,y} and {a,b,x,z} are Hamiltonian and their five-vertex union is Hamiltonian. In a minimum counterexample, every proper Hamiltonian support displayed has non-Hamiltonian path-cover-two complement and every L_t has path-cover number two.

## Statement

Let H be a boundary tournament and X|P|Q a spanning three-cover with |X|=4 and P=(p_1,...,p_m), m>=5. Put a=p_1, b=p_m, and M=(p_2,...,p_{m-1}). Then either there is a legal pairwise repartition of X|P with component orders (5,m-1), whose quadratic-potential change is 10-2m (strictly negative for m>=6 and zero for m=5), or both X union {a} and X union {b} are non-Hamiltonian and, for every t in X, F_t=(X-{t}) union {a,b} is Hamiltonian while L_t=V(M) union {t} is non-Hamiltonian. In the latter case there are distinct x,y,z in X such that {a,b,x,y} and {a,b,x,z} are Hamiltonian and their five-vertex union is Hamiltonian. In a minimum counterexample, every proper Hamiltonian support displayed has non-Hamiltonian path-cover-two complement and every L_t has path-cover number two.

## Body

The proof of four_side_four_five_supports_descent01 is unchanged except for keeping the potential difference rather than requiring it to be negative. If X+{a} or X+{b} is Hamiltonian, pair it with the inherited endpoint truncation of P; the component orders change from (4,m) to (5,m-1), with Delta Phi=25+(m-1)^2-16-m^2=10-2m, which is zero at m=5 and negative for m>=6. Otherwise both endpoint five-extensions are non-Hamiltonian. Apply two_bad_five_extensions_all_opposite01 to X,a,b to obtain all four Hamiltonian supports F_t. If some L_t=M+{t} is Hamiltonian, F_t|L_t gives the same legal (5,m-1) repartition and the same potential change. Hence absence of such a nonincreasing move forces all four L_t non-Hamiltonian. Apply two_bad_five_extensions_adjacent_four01 exactly as in the predecessor to obtain the two overlapping Hamiltonian four-sets whose union is one of the already-Hamiltonian F_t. The minimum-counterexample complement statements follow from mincex01.

## Metadata

- ID: four_side_endpoint_package_m5_01
- Kind: toolkit
- Version: 2
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
