# The checkerboard equality shell forces all four endpoint extensions and strict descent above order fourteen

## Statement

Assume branch (B) of 27a05b61e8c3. Thus W=W_0 disjoint-union W_1, |W_0|=|W_1|=2, and for each cross endpoint pair (e,f) in E_P x E_Q exactly the two labels w in one of W_0,W_1 make (W-{w}) union {e,f} Hamiltonian, while the other two such five-sets are non-Hamiltonian.

Then every one of the four endpoint enlargements W union {p_0}, W union {p_m}, W union {q_0}, W union {q_s} is Hamiltonian.

Consequently, if |P|>=6 or |Q|>=6, the spanning three-cover W|P|Q admits an explicit strict Phi-decreasing endpoint transfer. Hence a checkerboard four-side state with no strict endpoint-transfer descent has |P|,|Q|<=5 and therefore |V(H)|<=14.

## Body

Fix any cross pair (e,f) and put U=W union {e,f}, a six-set. By the checkerboard hypothesis, exactly two of the four deletions U-{w}, w in W, are Hamiltonian and the other two are non-Hamiltonian. The certified four-of-six theorem in smallset01 says at least four of the six vertex deletions of U are Hamiltonian. The only remaining deletions are U-{e}=W union {f} and U-{f}=W union {e}; therefore both must be Hamiltonian. Varying (e,f) over E_P x E_Q shows that W enlarged by each of the four endpoints is Hamiltonian.

Now suppose |P|=m>=6 and take either displayed endpoint e of P. Since W union {e} is Hamiltonian and P-{e} remains a tight path, (W union {e}) | (P-{e}) | Q is a spanning three-cover. Relative to W|P|Q its quadratic-potential change is
5^2+(m-1)^2-4^2-m^2=10-2m<=-2.
Thus Phi strictly decreases. The Q case is symmetric. If neither descent is available, both complementary path orders are at most five, so n=4+|P|+|Q|<=14.
