# Sharp-residue exchange blockade

## Statement

In the sharp maximin residue with rho=r and longest-path order a, a>=2r and every one-vertex-deletion two-cover has both sides at least 2r. For every tight (r+1)-path T and complementary cover P|Q of orders a,r, no Hamilton-removable vertex of P can Hamiltonize Q; the displayed ends force two opposite tight four-vertex cross-tails.

## Body


Let H be a minimum counterexample in the sharp maximin residue with rho=r. By maximin01, n=a+2r+1, a is the global maximum tight-path order, and every tight (r+1)-path T has complementary exact covers P|Q of orders a,r, with P globally longest.

First, a>=2r. For any vertex v, an exact two-cover H-v=U|W has |U|+|W|=a+2r and each side at most a, so a+2r<=2a. The same identity shows both |U|,|W|>=2r.

Now fix T and P|Q as above. If p in P is such that P-p is Hamiltonian, then Q+p is non-Hamiltonian. Otherwise Hamilton paths on P-p and Q+p, together with T, give a spanning three-cover of orders a-1,r+1,r+1. Since rho>=3 and a>=2r, all three orders are at least r+1, contradicting rho=r. In particular both displayed endpoints of P are such forbidden transfers.

Write P=(p0,...,p_{a-1}) and Q=(q0,...,q_{r-1}). Global maximality of P makes P+q non-Hamiltonian for every q outside P. Hence prepend/append tests give (p1,p0,q) and (q,p_{a-1},p_{a-2}) tight for every q in Q. The exchange blockade makes Q+p0 and Q+p_{a-1} non-Hamiltonian, so similarly (q1,q0,p) and (p,q_{r-1},q_{r-2}) are tight for p in {p0,p_{a-1}}.

Therefore (q1,q0,p_{a-1},p_{a-2}) and (p1,p0,q_{r-1},q_{r-2}) are tight four-vertex paths.
