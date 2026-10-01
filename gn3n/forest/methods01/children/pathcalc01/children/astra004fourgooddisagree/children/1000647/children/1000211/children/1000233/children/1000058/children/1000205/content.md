# Universal six-set Hamiltonicity forces an edge reversal, a short cross triple, or a local tight cycle

## Statement

Let H be a minimum counterexample in which every six-set is Hamiltonian. Let H-x=P|Q be any deletion cover and write P=(p_0,...,p_{m-1}); by 16dcabd23b55, m>=6. Then inside V(P) union {x} at least one of the following occurs:

(1) a tight triple reverses a displayed ordered edge (p_j,p_{j+1}) of P;

(2) there are indices j<k with 1<=k-j<=3 such that (p_j,x,p_k) is tight;

(3) there is a vertex-simple tight cycle contained in {x} together with at most five consecutive vertices of P.

Thus every displayed component P of every deletion cover H-x=P|Q contains one of configurations (1)-(3) together with x.

## Body

The omitted vertex x is not insertable into the full displayed path P, since such an insertion together with Q would two-cover H.

For each i=0,...,m-5 let
W_i=(p_i,p_{i+1},p_{i+2},p_{i+3},p_{i+4}).
The six-set V(W_i) union {x} is Hamiltonian.

First suppose x is noninsertable into some W_i. Choose a Hamilton path R on V(W_i) union {x}. By noninsertableorderdisagree01, R has order disagreement with W_i. Apply the proof of pathcalc01 Section 4 to the pair W_i,R. Because R has only one vertex outside W_i, the detour between two consecutive common vertices has interior either empty or {x}. If the reversed-common-edge outcome occurs, it reverses an edge of W_i, hence of P. If one of the two join triples in the pathcalc proof fails, boundary reversal gives a tight triple reversing the adjacent W_i-edge, again outcome (1). If both joins are tight, the proof closes to a vertex-simple tight cycle contained in V(W_i) union {x}, giving (3).

Hence assume x is insertable into every W_i. Positions 2 and 3 in a five-window are impossible, since all new triples checked by an insertion at either middle position are also the new triples required in the full path P. Thus each W_i has a successful insertion on side L={0,1} or side R={4,5}. Choose one successful position for each window.

If all adjacent windows have the same chosen side, then every window has one common side. But W_0 cannot use L, since an insertion at position 0 or 1 extends verbatim to P, and W_{m-5} cannot use R for the symmetric reason. Contradiction. Since W_0 must use side R and W_{m-5} must use side L, there is some i for which W_i uses side R and W_{i+1} uses side L.

Let the chosen insertion in W_i be at position 4 or 5. Because p_i is still the first vertex of that inserted six-path, deleting p_i leaves a tight path on the common support {x,p_{i+1},p_{i+2},p_{i+3},p_{i+4}} in which x occupies gap 3 or 4 of the four-path B below. Let the chosen insertion in W_{i+1} be at position 0 or 1. Because p_{i+5} is still the last vertex of that inserted six-path, deleting p_{i+5} leaves a tight path on the same common support in which x occupies gap 0 or 1. Thus these are genuine left and right insertions of x into the same displayed four-path. Apply 0d2a8a61c45a to the four-path
B=(p_{i+1},p_{i+2},p_{i+3},p_{i+4}).
Either it yields a tight cycle on x and a consecutive subinterval of B, giving (3), or it yields a tight triple (a,x,b), where a is the vertex of B immediately after the left insertion gap and b is the vertex of B at the right insertion gap. The four cases are:
(ell,r)=(0,3): (p_{i+1},x,p_{i+3});
(0,4): (p_{i+1},x,p_{i+4});
(1,3): (p_{i+2},x,p_{i+3});
(1,4): (p_{i+2},x,p_{i+4}).
In every case the two P endpoints have distance between one and three, giving (2).

Therefore one of (1)-(3) always occurs.
