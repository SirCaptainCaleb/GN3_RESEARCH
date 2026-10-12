# Port-support rank bound and composite cocircuits in the two-port lift

- Stable ID: note_nori_xi_multiport_graphic_nullity_and_composite_cocircuits
- Author: Astra
- Primary home: section:nori_matroid_generalizations_conjectures
- Labels: proved, two-port, cocircuit, graphic-nullity, support-classification
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6661_1
- Updated session: session_nori_r6661_1
- Disposition: none
- Successor: none

## Related references

- subsection:two_port_sector_cogirth_and_simultaneous_intersection_selectors
- subsection:deck_displacement_two_port_exchange
- subsection:transverse_bouquet_smoothing_and_phase_preserving_cocircuit_amalgamation

## Research note

# Port support controls the number of graph cycles in a cocircuit

Let H be a finite simple graph with m binary cochains a_1,...,a_m, and let
D=M([B_H 0; A I_m])^*
be the dual lift with distinguished ports P={p_1,...,p_m}. For a cocircuit Y of D, write S=Y intersection P and F=Y\P. Assume F is nonempty. Let beta(F)=|F|-|V(F)|+c(F) be the binary graphic cycle-space dimension of its edge support, with isolated vertices omitted.

## General rank bound

Every vertex of (V(F),F) has even degree, and
beta(F) <= m-|S|+1.

More precisely, let pi omit the signature coordinates belonging to S. Then
beta(F)-rank(pi A restricted to Z_1(F))=1.

Proof. Regard Y as a circuit of the represented primal matroid. A dependence supported in F union S is determined uniquely by a graph circulation z in Z_1(F) whose signature vanishes outside S: the coefficients on the available unit port columns are then its signature coordinates in S. Therefore the dependence-space dimension on Y is beta(F)-rank(pi A|Z_1(F)). A binary circuit has a one-dimensional dependence space, with the all-one vector as its nonzero dependence. Its incidence rows show that F is Eulerian. The rank bound follows because pi has m-|S| coordinates.

In particular, a cocircuit containing every distinguished port has beta(F)=1. Its nonport support is one simple graph cycle.

## Complete bipointed classification in the p sector

Take m=2 and write the signature sigma(C)=(alpha(C),lambda(C)), with ports p,q.

1. Every cocircuit containing both p and q is C union {p,q}, where C is one simple cycle with sigma(C)=(1,1). The converse holds.

2. Every cocircuit containing p and avoiding q is precisely one of the following:
   (a) C union {p}, where C is one simple cycle with sigma(C)=(1,0);
   (b) C_1 union C_2 union {p}, where C_1,C_2 are edge-disjoint simple cycles meeting in at most one vertex, and their signatures are (1,1) and (0,1), in either order.

Proof. The general bound gives beta(F)<=2 in the p-only sector. If beta(F)=1, Eulerian support is a simple cycle, and its total signature must be (1,0). If beta(F)=2, an Eulerian simple graph of cycle rank two consists of two simple cycles which are either vertex-disjoint or share one vertex. Indeed, each nontrivial component has minimum degree two. A connected component of cycle rank two has sum_v(deg(v)-2)=2, hence one degree-four vertex and all other degrees two; two cycle-rank-one components give the disjoint case.

Each constituent cycle must have lambda=1: if one had lambda=0, its own edge set, together with p when its alpha-value is one, would be a proper dependence inside Y. The total signature is (1,0), so their alpha-values differ. Conversely the stated pair has total signature (1,0). Its only proper nonempty graph circulations are the two constituent cycles, each of which has lambda=1 and cannot form a dependence using p alone. Thus adjoining p gives a circuit of the primal, as required.

This classification includes disconnected nonport supports. A statement selecting an arbitrary p-only cocircuit therefore needs a support condition before decoding it as one closed gallery.

## The first possible composite support in the canonical covers

In a line-cover model with minimum deck displacement delta, every alpha-odd simple turn cycle has length at least delta. A composite p-only cocircuit contains one such cycle and a second simple cycle of length at least three. Therefore
|Y| >= delta+4
for every composite p-only cocircuit.

The established minimum sector size is delta+2 under the minimum-degree-three hypothesis. Hence every sector-minimum cocircuit has a single-cycle support. This supplies the missing support justification when minimum-sector proofs infer a single turn cycle from an arbitrary cocircuit.

For the antipodal cube, delta=n and the composite lower bound n+4 is attained for every n>=3. Choose a shortest deck-geodesic in the quotient base graph Q_n/tau. It visits n distinct base vertices, whereas the base graph has 2^(n-1)>n vertices. At an unvisited base vertex choose any three incident base edges. They give a balanced star triangle T in H_n whose vertices avoid the geodesic turn cycle C. The signatures are sigma(C)=(1,1) and sigma(T)=(0,1). Thus C union T union {p} is a p-only cocircuit of size n+4.

For the full boundary cover S_n -> L(K_n), n>=4, delta=3 and the lower bound seven is attained. A shortest odd turn triangle projects from a triangle of L(K_n) on three base vertices. Choose a base vertex outside that triangle; its degree is 2(n-2)>=4. Three incident base edges give a balanced star triangle disjoint from the odd turn triangle. Their union with p is a seven-element p-only cocircuit.

Thus the sector minima in the manuscript remain valid. At the next relevant cardinality, composite cocircuits already occur. A longer-witness selector must control graphic support as well as port membership, orientation, and resource independence.

## Color intersection

For an admissible color cycle X_d=supp(d) union {p}, a composite witness has
|X_d intersection Y|=1+w_d(C_1)+w_d(C_2).
The alpha-odd constituent has odd color weight, while the balanced constituent has even color weight. Small total intersection is compatible with a separate balanced curvature cycle. It supplies no single coherent resource-spanning gallery without a further splice.

This is a scope theorem for two-port exchange arguments, together with a verification of their minimum-sector support claim. The spanning one-turn boundary assertion and NORI1 remain open.
