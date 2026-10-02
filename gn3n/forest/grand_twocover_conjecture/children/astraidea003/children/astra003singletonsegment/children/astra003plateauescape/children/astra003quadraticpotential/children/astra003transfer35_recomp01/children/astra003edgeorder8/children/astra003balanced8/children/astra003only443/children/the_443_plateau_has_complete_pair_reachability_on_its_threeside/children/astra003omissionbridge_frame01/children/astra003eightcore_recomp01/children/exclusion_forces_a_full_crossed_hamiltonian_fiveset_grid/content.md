# Eight-label exclusion forces a full crossed Hamiltonian five-set grid

## Statement

In the notation of 851be99bfc11, for every p in {a,b,c} and every q in {d,e,f}, both five-sets (Q-{q}) union {t,p} and (P-{p}) union {t,q} are Hamiltonian. Equivalently, the excluded target t lies in two symmetric 3-by-3 grids of Hamiltonian five-sets obtained by exchanging one reachable label across P|Q.

## Body

# Full crossed Hamiltonian grid around the excluded target

Retain the notation of 851be99bfc11:

P={u,a,b,c},  Q={v,d,e,f},

where t,u,v are the three excluded singleton labels and a,b,c,d,e,f are reachable singleton labels. From a45fe3097e08, P+t and Q+t are Hamiltonian, and the six-sets P+s+w and Q+s+w have exact bad deletion sets {u,s} and {v,s}. From 851be99bfc11, Q+p is non-Hamiltonian for every p in {a,b,c}, and P+q is non-Hamiltonian for every q in {d,e,f}.

Fix p in {a,b,c}. Since p is a good deletion of P+s+w, the five-set

R_p=(P-{p}) union {s,w}

is Hamiltonian. Thus the trapped Astra component contains the reachable state

R_p | (Q union {t}) | (p).

Consider the six-set

W_p=Q union {t,p}.

Deleting t leaves Q+p, which is non-Hamiltonian by 851be99bfc11. Deleting v is also bad. Indeed, if

W_p-{v}=(Q-{v}) union {t,p}

were Hamiltonian, then in the displayed reachable state the pair (Q+t)|(p) could be repartitioned as

(W_p-{v}) | (v),

producing a reachable 5|5|1 state with singleton v, contradicting v being excluded.

Hence t and v are two bad deletion labels of the six-set W_p. By four-of-six, a six-set has at most two bad deletions. Therefore these are exactly the bad labels of W_p, and every other deletion is Hamiltonian. In particular, for each q in {d,e,f},

(Q-{q}) union {t,p}

is Hamiltonian.

Since p was arbitrary, this gives all nine Hamiltonian five-sets in the first 3-by-3 grid.

The symmetric argument starts from the reachable states

(P+t) | ((Q-{q}) union {s,w}) | (q),

for q in {d,e,f}. The six-set

Z_q=P union {t,q}

has t as a bad deletion because P+q is non-Hamiltonian, and u as a second bad deletion because a Hamiltonian Z_q-u would make u a reachable singleton. Thus {t,u} is its exact bad-deletion set. Therefore for every p in {a,b,c},

(P-{p}) union {t,q}

is Hamiltonian.

So exclusion of t forces a symmetric pair of full crossed Hamiltonian grids: every one-for-one P|Q exchange through t produces a Hamiltonian five-set on both sides.