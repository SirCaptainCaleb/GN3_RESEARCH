# Every four-side label is locked out of each long interior at a local minimum

## Statement

Let H be a boundary tournament and let W|P|Q be a spanning three-cover minimizing quadratic potential within its connected pairwise-repartition component, with |W|=4. Let R=(r_1,...,r_m) be either P or Q with m>=6, let E_R={r_1,r_m}, and let R°=(r_2,...,r_{m-1}). Then for every w in W, the five-set (W-{w}) union E_R is Hamiltonian, while H[V(R°) union {w}] is non-Hamiltonian. Consequently every w in W is noninsertable into every position of the displayed path R°, and for every w in W some tight triple containing w reverses a displayed edge of R°. In particular, if both |P|,|Q|>=6, all four vertices of W are simultaneously noninsertable into both displayed interiors P° and Q°.

## Body

Fix a displayed endpoint e of R. If W union {e} were Hamiltonian, replacing W|R by a Hamilton path on W union {e} together with the inherited path R-e would change the pair sizes from (4,m) to (5,m-1), with new quadratic potential minus old equal to 25+(m-1)^2-[16+m^2]=10-2m<0. This contradicts minimality in the connected pairwise-repartition component. Hence W union {r_1} and W union {r_m} are both non-Hamiltonian.

Apply two_bad_five_extensions_all_opposite01 to the four-set W and exterior labels r_1,r_m. For every w in W it follows that F_w=(W-{w}) union {r_1,r_m} is Hamiltonian.

Fix w in W. If H[V(R°) union {w}] were Hamiltonian, then F_w and V(R°) union {w} would be disjoint Hamiltonian supports partitioning V(W) union V(R). Replacing W|R by these two paths is a legal pairwise repartition with sizes (4,m)->(5,m-1), again changing Phi by 10-2m<0, contradiction. Thus H[V(R°) union {w}] is non-Hamiltonian. Any insertion of w into the displayed path R° would Hamiltonize this support, so w is noninsertable into every position of R°. Since |R°|=m-2>=4, noninsertable_family_reversal01 applies and gives a tight triple through w reversing a displayed edge of R°.

The argument holds for every w in W and independently for each component R of order at least six.