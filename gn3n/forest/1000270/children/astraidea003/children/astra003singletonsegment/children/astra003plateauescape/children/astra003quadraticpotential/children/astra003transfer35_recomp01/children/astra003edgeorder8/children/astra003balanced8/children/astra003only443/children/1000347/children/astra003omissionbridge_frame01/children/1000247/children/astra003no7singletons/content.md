# The seven-label omission shell is impossible

## Statement

Let K be a trapped order-eleven Astra-003 component containing a 4|4|3 state, and let S be the set of labels occurring as singletons of reachable 5|5|1 states. Then |S| is not seven. Consequently |S|>=8.

## Body


Assume for contradiction that |S|=7, and let T=V(H)-S, |T|=4. By 50a62b7e1ffb, every reachable omission state P|Q|(x) has x in S, each five-side contains exactly three vertices of S and two of T, and in each six-set P union {x} the two T-labels on P are exactly the two bad five-deletions while x and the three S-labels on P are exactly the four good deletions.

Fix one reachable state

P|Q|(x),

and write

P=A union U,

where A is a three-subset of S and U is a two-subset of T. Write the other S-part as B=S-(A union {x}); then Q=B union (T-U).

We first show that, while keeping the T-pair U fixed on the P-side, every configuration (A',x') with A' a three-subset of S and x' in S-A' is reachable by omission swaps.

Indeed, from any configuration (A,x):
- swapping the singleton x with any b in B leaves A unchanged and changes the singleton to b;
- after first choosing any desired y outside A as singleton, swapping y with any a in A replaces A by A-a+y.

Thus the reachable configuration graph projects onto the Johnson graph J(7,3), and for each fixed A all four choices of singleton outside A are mutually reachable. Hence every pair (A',x') with |A'|=3 and x' outside A' occurs in a reachable omission state whose P-side is A' union U.

Therefore:

1. For every three-subset A' of S, the five-set A' union U is Hamiltonian.

2. Let W be any four-subset of S. Choose x' in W and put A'=W-{x'}. In the corresponding reachable state, the six-set

U union W = (A' union U) union {x'}

has exactly the two vertices of U as its bad deletion labels. Hence deleting either member of U leaves a non-Hamiltonian five-set. Equivalently, for every u in U and every four-subset W of S,

W union {u}

is non-Hamiltonian.

Now fix u in U and choose any five-subset Z of S. Consider the six-set

R=Z union {u}.

For every z in Z, deleting z leaves the five-set

(Z-{z}) union {u},

which is non-Hamiltonian by conclusion 2 because Z-{z} is a four-subset of S.

Thus R has at least five non-Hamiltonian five-vertex deletions. But the certified four-of-six theorem says that every six-vertex boundary tournament has at least four Hamiltonian five-vertex subsets, equivalently at most two bad deletions.

This contradiction excludes |S|=7. Therefore every trapped order-eleven Astra-003 component containing a 4|4|3 state has at least eight reachable singleton labels.
