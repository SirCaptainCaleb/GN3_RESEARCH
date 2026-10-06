# Frankl union-closed families as pedestrian semilattices and a NOR intermediate

Explore whether the union-closed sets conjecture has a structural relationship to directed NOR, keeping the edge-ordered origin and pedestrian dimension-sweep lemma in view.

## Frankl / union-closed perspective on NOR and pedestrian sweeps

### 1. Semilattice pedestrian reformulation of Frankl

Let \(\mathcal F\subseteq 2^U\) be finite and union-closed, \(m=|\mathcal F|\), and
\[
f_i=|\{A\in\mathcal F:i\in A\}|.
\]
Put one pedestrian at each \(A\in\mathcal F\). When a member \(B\in\mathcal F\) is called, move every pedestrian by
\[
A\mapsto A\cup B.
\]
Because \(\mathcal F\) is union-closed, walkers remain in \(\mathcal F\). These maps are commuting idempotents:
\[
T_B T_C=T_C T_B=T_{B\cup C}.
\]

After a sweep whose called sets have union \(U\), every walker ends at \(U\). Coordinate \(i\) is acquired exactly once by each walker that initially lacked \(i\), hence exactly
\[
m-f_i
\]
walkers traverse coordinate \(i\).

Therefore Frankl's conclusion
\[
\exists i:\ f_i\ge m/2
\]
is exactly
\[
\exists i:\ m-f_i\le m/2.
\]

**Pedestrian form of Frankl:** in every finite union-closed semilattice sweep, some coordinate is traversed by at most half the pedestrians.

For each starting set \(A\), the set of coordinates its walker traverses is
\[
C_A=U\setminus A.
\]
These trajectory-support sets satisfy
\[
C_{A\cup B}=C_A\cap C_B.
\]
Thus they form an intersection-closed family. Frankl is equivalently a low-congestion coordinate theorem for an intersection-closed family of ambient-cube geodesic supports.

This is parallel to the existing pedestrian dimension-sweep lemma. In the cube-subgraph lemma, coordinate calls are invertible matching permutations and averaging forces one pedestrian to travel far. In the Frankl sweep, calls are idempotent many-to-one contractions and the conjecture asks for a coordinate used by few pedestrians. The two statements are opposite mass-transport faces of commuting cube updates.

### 2. Relation to the edge-ordered origin of directed NOR

For coordinate arity \(r=3\), write the directed NOR coloring as center-indexed tournaments
\[
a\to_{T_b}c
\iff
h(a,b,c)=0.
\]
In the edge-ordered-graph subclass,
\[
h(a,b,c)=0
\iff
\lambda(ab)<\lambda(bc).
\]
For fixed \(b\), the extension sets
\[
E_b(a)=\{c:h(a,b,c)=0\}
\]
are suffixes of the total order of edges incident to \(b\). Hence they are nested, and in particular union-closed.

Passing from edge-ordered graphs to unrestricted directed NOR therefore replaces a locally nested family of feasible extensions by arbitrary tournament neighborhoods. Union-closed families suggest a natural intermediate structural class: retain closure under joining extension possibilities without retaining a total local order.

This may provide a useful interpolation:
\[
\text{nested/transitive local extension families}
\subset
\text{union-closed local extension families}
\subset
\text{arbitrary directed NOR}.
\]

### 3. Feasible-support families and the augmentation obstruction

For color \(\sigma\) and ordered terminal \((r-1)\)-tuple \(S\), define
\[
\mathcal F_{\sigma,S}
=
\{A\subseteq V\setminus S:
\text{some ordering of }A,S\text{ is }\sigma\text{-tight}\}.
\]
Union closure of \(\mathcal F_{\sigma,S}\) is essentially a branch-merging property: two feasible tight branches with the same terminal state could be merged onto the union of their supports.

This is very close to the current one-vertex tight-fork augmentation obstruction. The blocked-front recentering lemma absorbs a missing vertex but can discard the opposite branch; the unresolved issue is precisely retention/merging of feasible support.

Suggested dichotomy:
1. if a relevant feasible-support family is union-closed, apply Frankl-style frequency/mass transport to find a coordinate appearing in many compatible branches and try to synchronize the two sides of a fork;
2. if it is not union-closed, choose an inclusion-minimal pair \(A,B\) with \(A,B\) feasible but \(A\cup B\) infeasible. The minimal failure of union closure should localize the exact branch-merging obstruction and may yield a finite exchange certificate.

This is particularly attractive because a minimum NOR counterexample already makes every vertex deletion feasible. The missing global object is a union of near-spanning certificates.

### 4. Broader heuristic

The edge-ordered origin, the pedestrian lemma, Frankl, and NOR can all be viewed through update systems on cube coordinates:

- edge-ordered monotone paths: ordered local comparisons;
- cube pedestrian lemma: commuting invertible coordinate swaps;
- Frankl: commuting idempotent union maps;
- directed NOR: noncommuting finite-window shift/extension maps.

The difficulty seems to increase exactly as commutativity/invertibility is lost. A useful strategy may be to project directed NOR onto a commutative support semilattice, prove a Frankl-type low-congestion/frequent-coordinate statement there, and then use the retained ordered-tail data only to lift that coordinate statement back to a tight-path exchange.

No claim is made that Frankl itself implies NOR or conversely. The concrete research targets are:
- characterize when \(\mathcal F_{\sigma,S}\) is union-closed;
- analyze minimal failures of its union closure;
- test whether reversal pairs the corresponding support-frequency functions strongly enough to force a spanning fork;
- investigate the local-extension intermediate class where \(E_b(a)\)-families are union-closed.
