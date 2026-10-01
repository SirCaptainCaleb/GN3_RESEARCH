# A global four-side minimum carries a complete label-by-long-path reversal family

## Statement

Let H be a boundary tournament and let X|P|Q be a spanning three-cover globally minimizing quadratic potential, with |X|=4 and |P|,|Q|>=6. Then for every x in V(X), there is a displayed edge of P reversed by a tight triple containing x, and there is a displayed edge of Q reversed by a tight triple containing x. More precisely, for each R in {P,Q}, writing R=(r_1,...,r_m), some t gives either (x,r_t,r_{t-1}) or (r_{t+1},r_t,x). Thus the four labels of X simultaneously supply four label-specific reversal witnesses on each long component.

## Body

By certified aab7e8e9fe4a, for every x in X and each long path R in {P,Q}, both endpoint truncations of R enlarged by x are non-Hamiltonian; equivalently x is noninsertable into the entire displayed order of R. Apply certified acdec36ae3ca separately to each ordered pair (x,R). It gives a tight triple containing x and reversing one displayed edge of R, with the explicit forms stated. Since x and R were arbitrary, this gives the complete 4-by-2 family.