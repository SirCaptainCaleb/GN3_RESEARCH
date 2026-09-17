# Disconnected pair-deletion interaction currentizes source shortening without transition bounds

**Workspace:** D17
**State:** established
**Key:** `universal-source-disconnected-return-currentization`

**Summary:** If the class-interaction graph of an exact H-{p,z} two-cover disconnects the source three-cover L|R|B, one source class is a whole pure rail and the other two form one Hamilton mixed rail. Isolating B contradicts pc(L union R)=2; isolating L or R gives an exact H-p source in which z is an endpoint of a strictly smaller rail, with the mixed rail retained exactly. This is the arbitrary-fragmentation source-shortening theorem and subsumes the theta=1 currentization.

Retain the minimum-side universal-source setup

  C_p=A|B,
  A=L-z-R,

with L,R,B nonempty literal tight source paths, z internal on A, and

  W=H-{p,z}.

Let F=P|Q be any exact two-cover of W. Define J(F) on {L,R,B} by selected interclass adjacency as in `universal-source-connected-rainbow-splitstar`.

Suppose J(F) is disconnected. Since all three source classes are nonempty and P,Q are exactly two nonempty connected rails, J(F) has one isolated class K. Any F-rail containing a vertex of K cannot leave K, because the first selected edge leaving would create an interaction edge incident with K. Both rails cannot meet K, because then no rail would be available to cover the other two nonempty classes. Hence exactly one whole F-rail has support K and the other whole F-rail has support equal to the union of the other two source classes. In particular that pair-union is Hamiltonian in the ACTUAL order of the second F-rail.

If K=B, this says L union R=A-z is Hamiltonian, contradicting the non-Hamilton deletion branch pc(A-z)=2.

If K=R, the other F-rail is an actual Hamilton path P_LB on L union B. Replace the pure R rail, if necessary, by the original literal source order R. Since z-R is a literal tight suffix of A,

  P_LB | (z-R)

is an exact two-cover of H-p. The physical vertex z is an endpoint of the second source rail, whose order is |R|+1<|A|. The exact mixed order P_LB is retained unchanged. Thus the same physical offender z has been currentized to a strictly smaller endpoint source.

If K=L, dually one obtains

  (L-z) | P_RB

as an exact H-p cover with z endpoint on the strictly smaller rail L+z.

Therefore a minimum-side universal source can avoid immediate source shortening only if EVERY exact two-cover F of H-{p,z} has connected class-interaction graph. No bound on the number of selected transitions is needed. This exact unit replaces the theta=1-only source-currentization interface with the graph-level disconnected-interaction criterion.

If the smaller source produced above still makes z universally crossing on its smaller rail, global minimum-side choice is contradicted. Hence under that extremal choice z becomes quiet in the smaller source, and the seam-free substitution mechanism yields the saturated-port consequences described elsewhere. Those consequences are downstream; the established theorem here ends at the literal smaller source.

Status: complete direct proof; dependency-light. No R24/R5, transition counting, R176 payment, or path-order synchronization is used.

