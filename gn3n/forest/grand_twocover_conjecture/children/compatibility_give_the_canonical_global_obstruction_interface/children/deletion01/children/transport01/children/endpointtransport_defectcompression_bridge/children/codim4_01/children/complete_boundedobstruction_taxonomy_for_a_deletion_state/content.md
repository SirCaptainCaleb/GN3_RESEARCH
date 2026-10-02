# Complete bounded-obstruction taxonomy for a deletion state

## Statement

For every exact deletion two-cover H-x=P|Q in a minimum counterexample, the two failed-insertion obstructions reduce the state to one of four bounded frontiers: a Hamiltonian four-window with exact-two-cover complement; the universal cyclic non-Hamiltonian K4 kernel; a boundary-pivot matching-block K4, whose complement is either exact-two-coverable or triggers the certified codimension-four Hamiltonian-side structure; or the interior pivot-pivot cross-swap kernel with its two explicit three-way clauses and central five-set closure. Thus all arbitrary path lengths disappear before the unresolved endpoint-transport bridge.

## Body


# Complete bounded-obstruction taxonomy for a deletion state

Let H be a minimum counterexample and fix an exact deletion two-cover

H-x=P|Q.

The omitted vertex x is noninsertable into either displayed path. Apply the local failed-insertion theorem separately to P and Q.

Then at least one of the following four bounded frontiers occurs.

## 1. Hamiltonian four-window

If one component has a first-type obstruction whose four-window is Hamiltonian, or a boundary second-type obstruction whose four-window is Hamiltonian, there is a four-set X containing x such that H[X] is Hamiltonian.

Then H-X is non-Hamiltonian; otherwise Hamilton paths on X and H-X would two-cover H. By minimality,

pc(H-X)=2.

Thus the state enters a Hamiltonian-four / exact-two-cover-complement frontier.

## 2. Universal cyclic four-kernel

If one component has a first-type obstruction and its four-window is non-Hamiltonian, the first-type kernel theorem in the endpoint-transport module identifies that window with the exceptional cyclic non-Hamiltonian K4.

The cyclic-kernel conclusions of that module then apply: every fifth vertex extends the kernel Hamiltonianly, every three-kernel plus two exterior vertices is Hamiltonian, and the complementary induced tournaments supplied there are non-Hamiltonian of path-cover number exactly two.

## 3. Boundary matching-block four-kernel

Suppose no first-type obstruction has already put the state in the preceding cases, but one component has a second-type pivot at its first or last insertion gap.

The boundary-pivot classification gives a four-set X containing x such that either H[X] is Hamiltonian, which is case 1, or H[X] is a non-Hamiltonian edge-orderable K4 with explicitly forced opposite-edge matching blocks.

In the latter situation, H-X is a proper induced subtournament and hence has path-cover number at most two.

- If H-X is non-Hamiltonian, then pc(H-X)=2.
- If H-X is Hamiltonian, the certified codimension-four Hamiltonian-side structure applies to the decomposition
  V(H)=X disjoint-union (V(H)-X),
  with X the non-Hamiltonian four-set. In particular the matching-block order is intrinsic and the endpoint/deletion-cover conclusions of codim4_01 are available.

Thus the boundary-pivot branch lands either in an exact-two-cover complement or directly in the codimension-four structural package.

## 4. Interior pivot-pivot residual

If none of the first three cases occurs, neither component has a first-type obstruction and neither second-type obstruction is at a boundary gap. Hence both components have second-type obstructions at interior gaps.

The pivot-pivot cross-swap theorem in the endpoint-transport module therefore applies. The entire residual obstruction is supported on x and four consecutive vertices from each component and satisfies the two explicit three-way reverse clauses there.

Moreover, if both forward central cross-joins are tight, the associated five-set is Hamiltonian and its complement is non-Hamiltonian of path-cover number exactly two. Otherwise at least one of the two reverse central cross-joins is tight.

These cases are exhaustive because the failed-insertion theorem has only the first and second alternatives, and a second-type pivot is either at a boundary gap or an interior gap.

Hence before the unresolved endpoint-transport / defect-compression bridge is invoked, every arbitrary-length deletion state has already collapsed to a bounded four- or nine-vertex kernel, together with one of the exact complementary structures above. The remaining problem is not localization; it is to consume one of these finitely described kernels globally.
