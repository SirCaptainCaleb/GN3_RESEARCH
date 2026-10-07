# Every maximal tight path has punctured-Boolean obstructions at both ends

## Metadata

- ID: every_maximal_tight_path_has_punctured_boolean_obstructions_at_both_ends
- Parent Section: directed_nor_union_closed_bridge
- Position: 20
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Every maximal tight path has punctured-Boolean obstructions at both ends

Fix coordinate arity \(r\ge2\) and a reversal-antisymmetric label \(h\). Let
\[
P=(v_1,\ldots,v_m)
\]
be an inclusion-maximal \(\sigma\)-tight path in a directed NOR counterexample. Let
\[
F=(v_1,\ldots,v_{r-1}),\qquad R=(v_{m-r+2},\ldots,v_m),\qquad X=V\setminus V(P),
\]
and write \(\tau=1-\sigma\).

The front theorem gives
\[
h(x,F)=\tau\qquad(x\in X),
\]
so every singleton of \(X\) is feasible in \(\mathcal F_{\tau,F}\), while \(X\) itself is infeasible there: otherwise a \(\tau\)-tight witness on \(X\) ending at \(F\) splices to \(P\) and gives a spanning one-change order.

### Theorem: the same obstruction occurs at the rear
The reversed path
\[
P^{\rm rev}=(v_m,\ldots,v_1)
\]
is an inclusion-maximal \(\tau\)-tight path. Its exposed front is \(R^{\rm rev}\). Therefore
\[
h(x,R^{\rm rev})=\sigma\qquad(x\in X),
\tag{1}
\]
every singleton of \(X\) is feasible in \(\mathcal F_{\sigma,R^{\rm rev}}\), and \(X\) itself is infeasible there.

#### Proof
Reversal antisymmetry sends every \(\sigma\)-window of \(P\) to a \(\tau\)-window of \(P^{\rm rev}\), so the reversed path is \(\tau\)-tight. If some \(x\in X\) could be prepended to \(P^{\rm rev}\) in color \(\tau\), reversing the resulting longer path would append \(x\) to \(P\) in color \(\sigma\), contradicting inclusion-maximality of \(P\). Thus \(P^{\rm rev}\) is inclusion-maximal. Applying the maximal-front theorem to it yields (1) and singleton feasibility in \(\mathcal F_{\sigma,R^{\rm rev}}\). If \(X\) were feasible in that family, its witness would splice to \(P^{\rm rev}\) and give a spanning one-change order, impossible in a counterexample. \(□\)

### Corollary: paired punctured Boolean caps
There exist subsets
\[
U_L,U_R\subseteq X,\qquad |U_L|,|U_R|\ge2,
\]
such that
\[
\mathcal F_{\tau,F}|_{U_L}=2^{U_L}\setminus\{U_L\},
\qquad
\mathcal F_{\sigma,R^{\rm rev}}|_{U_R}=2^{U_R}\setminus\{U_R\}.
\tag{2}
\]
Namely choose inclusion-minimal infeasible supports on the two sides. Each cap has uniform Frankl bias \(-1\) in every coordinate, but the two caps have opposite colors and opposite terminal orientations.

Thus every maximal monochromatic branch in a counterexample is trapped between two minimal witness-synchronization failures. This is strictly stronger than the one-sided punctured-cube reduction.

### Full-omitted-set specialization
If on one side the minimal circuit is all of \(X\), then for every \(x\in X\) there is a deletion witness
\[
Q_x=(\text{an ordering of }X\setminus\{x\},F)
\]
which is \(\tau\)-tight. Concatenating with the suffix of \(P\) gives a one-change deletion order of \(V\setminus\{x\}\), with word \(\tau^*\sigma^*\). In a minimum counterexample endpoint blocking then forces
\[
h(R,x)=\tau\qquad(x\in X),
\]
which is equivalent by reversal to (1). Hence the rear cap can also be recovered directly from the deletion certificates when the front circuit equals the whole omitted set.

### Closure target
The new frontier is a paired-circuit problem: exploit the interaction of \(U_L\) and \(U_R\). If their witness systems can be made to cover the omitted set compatibly, they produce a full-support \(\tau\)-\(\sigma\)-\(\tau\) sandwich. If they overlap, a coordinate participates in two opposite-color deletion-complete witness systems anchored at opposite ends of the same maximal path. Either configuration carries information unavailable to a single punctured cube and is the natural next place to seek circuit elimination or a terminating recentering move.

## Frontier

- Development version when composed: None
- Development version now: 1
