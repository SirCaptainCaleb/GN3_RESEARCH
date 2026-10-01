# A locally minimal four-side has a complete endpoint-pair Hamiltonian five-set grid

## Statement

Let H be a boundary tournament and let W|P|Q be a spanning three-cover minimizing quadratic potential within its connected pairwise-repartition component, with |W|=4 and |P|,|Q|>=6. Let E be the four displayed endpoints of P and Q. Then for every w in W and every two-element set {e,f} subset E, the five-set (W-{w}) union {e,f} is Hamiltonian.

## Body

Fix any displayed endpoint e in E. If W union {e} were Hamiltonian, then moving e from its displayed path R into W and retaining the inherited truncation R-e would be a legal pairwise repartition in the same connected component, changing pair sizes from (4,m) to (5,m-1), where m=|R|>=6. The quadratic-potential change is 10-2m<0, contradicting componentwise minimality. Hence W union {e} is non-Hamiltonian for every e in E. Now fix distinct e,f in E and put S=W union {e,f}. The two five-vertex deletions S-{e}=W union {f} and S-{f}=W union {e} are non-Hamiltonian. Apply two_bad_five_extensions_all_opposite01 to the four-set W and exterior labels e,f. It follows that for every w in W, S-{w}=(W-{w}) union {e,f} is Hamiltonian. Since {e,f} was arbitrary, the complete endpoint-pair grid follows. No minimum-counterexample or global-minimality hypothesis is used.
