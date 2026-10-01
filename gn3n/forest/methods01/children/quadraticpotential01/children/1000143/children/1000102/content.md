# Order disagreement between one-label replacement paths yields a local reversal, an old-support cycle, or quadratic descent

## Statement

Let H be a minimum counterexample. Let X,Q partition V(H), with H[X] non-Hamiltonian and Q Hamiltonian. Let d,e be distinct vertices of X. Suppose P is a Hamilton path on X-{d}, R is a Hamilton path on X-{e}, and P|Q and R|Q are deletion covers of H-d and H-e respectively.

If P and R order two common vertices differently, then at least one of the following holds:

(1) an ordered edge on the common core X-{d,e} is reversed between P and R;

(2) a tight triple supported on X reverses an ordered edge of P or R at a path intersection;

(3) there is a vertex-simple tight cycle contained entirely in V(P)=X-{d};

(4) the singleton lift P|Q|{d} admits a legal pairwise repartition with strictly smaller quadratic potential.

In particular, a path-intersection cycle containing the restored label d always belongs to the strict-descent branch.

## Body

Apply the path-intersection calculus pathcalc01 to P and R. Read the common vertices in their order along R and choose consecutive common vertices v_i,v_j along R that occur in reverse order along P. Let E be the R-subpath from v_i to v_j. By construction the interior of E contains no common vertex.

Since
V(R)=(X-{e})
and
V(P)=(X-{d}),
the only vertex of R outside V(P) is d. Therefore the interior of E is either empty or consists only of d.

The reversed-common-edge and reversing-triple outcomes of pathcalc01 are exactly alternatives (1) and (2). Suppose pathcalc01 closes to a vertex-simple tight cycle.

If d lies in the interior of E, then the cycle consists of d together with one contiguous inherited interval of P. Choosing d as the starting vertex of this cyclic order gives
d,p_j,p_{j+1},...,p_i,d
for suitable indices j<i. Apply 2e9fafec259e. The singleton lift P|Q|{d} has a legal strict Phi descent, giving alternative (4).

If d is not in the interior of E, then E has no interior vertex at all. The cycle is therefore formed by one R-edge joining two common vertices together with the inherited P-interval between those vertices, and all of its vertices lie in V(P). This is alternative (3).

No other case exists. ∎
