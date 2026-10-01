# A locally quadratic-minimal four-side carries the shared-endpoint transport package

## Statement

Let H be a minimum counterexample of order n>=15 and let W|P|Q be a spanning three-cover with |W|=4 that minimizes quadratic potential within its connected component of the pairwise-repartition graph. Then there exist w in W, D=W-{w}, one displayed endpoint e of one of P,Q, and both displayed endpoints f,g of the other such that D union {e,f} and D union {e,g} are Hamiltonian five-sets and the associated six-set carries the bounded path-cover-two transport package of four_window_transport15. Moreover either one of D union {e}, D union {f}, D union {g} is a Hamiltonian four-set, or some d in D makes both (D-{d}) union {e,f} and (D-{d}) union {e,g} Hamiltonian four-sets; every such proper four-set has non-Hamiltonian path-cover-two complement.

## Body

Apply four_window_transport15 to W|P|Q. Its strict endpoint-transfer alternative is a legal pairwise repartition from the present cover with smaller Phi, impossible because W|P|Q is Phi-minimal in its connected pairwise-repartition component. Therefore its bounded transport alternative holds, giving w,D,e,f,g and the associated pc2 one/two-label package. Apply shared_endpoint_fork_compression01 to the two Hamiltonian five-sets D union {e,f} and D union {e,g}. It yields either a Hamiltonian four-set among D+e,D+f,D+g or a label d in D for which both forked four-sets are Hamiltonian. Since n>=15, each such four-set is proper. If its complement were Hamiltonian, the two Hamilton paths would form a spanning two-cover of H, contradiction; minimum-counterexample calculus therefore gives path-cover number two. Global Phi-minimality is nowhere used.
