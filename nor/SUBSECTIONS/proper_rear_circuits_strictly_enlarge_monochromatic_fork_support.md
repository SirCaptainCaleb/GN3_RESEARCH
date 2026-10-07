# Proper rear circuits strictly enlarge monochromatic fork support

## Metadata

- ID: proper_rear_circuits_strictly_enlarge_monochromatic_fork_support
- Parent Section: directed_nor_union_closed_bridge
- Position: 31
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Proper rear circuits strictly enlarge monochromatic fork support

Work in arbitrary coordinate arity \(r\ge2\). Let
\[
P=(F,T)
\]
be a \(\sigma\)-tight path, where \(F\) is its first ordered \((r-1)\)-state, and let \(X=V\setminus V(P)\). Put \(\tau=1-\sigma\). Assume \(X\) is a whole front circuit in \(\mathcal F_{\tau,F}\): every proper subset of \(X\) is \(\tau\)-feasible ending at \(F\), while \(X\) is not.

Suppose a rear analysis produces a nonempty proper circuit support
\[
D\subsetneq X.
\]
The key point is that the strict containment itself implies a genuine monotone improvement, though not a new maximal path.

### Theorem: proper rear descent enlarges a same-color fork
Because \(D\subsetneq X\), the whole-front-circuit hypothesis gives a \(\tau\)-tight witness
\[
Q_D=(d_1,\ldots,d_s,F)
\]
on \(D\cup F\). Reverse it. By reversal antisymmetry,
\[
Q_D^{\rm rev}=(F^{\rm rev},d_s,\ldots,d_1)
\]
is \(\sigma\)-tight.

Thus \(P\) and \(Q_D^{\rm rev}\) are two \(\sigma\)-tight branches issuing from the two orientations of the same center state \(F\). Together they form a monochromatic divergent tight fork whose support is
\[
V(P)\cup D.
\]
Hence the fork covers exactly
\[
|V(P)|+|D|
\]
vertices, strictly more than the original path. The uncovered set is
\[
X\setminus D,
\]
so its size falls from \(|X|\) to \(|X|-|D|\). \(□\)

### Corollary: the correct descent potential is fork deficiency
A spanning monochromatic tight fork is equivalent to a spanning one-change order: reverse one branch and concatenate through the common center. Therefore the quantity
\[
\delta_{\rm fork}=|V|-\max\{|V(K)|:K\text{ is a monochromatic tight fork}\}
\]
is a natural closure potential.

A proper rear circuit does not by itself produce a smaller **path** circuit, so the earlier claim of automatic iterative circuit descent was too strong. What it does prove is a strict decrease in fork deficiency. The only way a whole-front circuit can fail to improve fork support via the rear-circuit mechanism is the bipolar case \(D=X\), where no residual vertex is removed.

### Consequence for strategy
This suggests changing the extremal object from a maximal monochromatic path to a maximum-support monochromatic fork. Starting from a whole-front circuit attached to one branch, any proper rear circuit is incompatible with fork-maximality because it would enlarge the fork. Thus an extremal-fork formulation should force the no-descent obstruction directly into the bipolar regime, avoiding the missing recentering step for paths.

The remaining technical obligation is to rebuild the punctured-Boolean front-circuit argument for an exposed branch of a maximum-support fork. If that branch-level analogue holds, the support-growth argument terminates automatically: proper rear circuits enlarge the fork, while equality gives a bipolar circuit and hence the four-change cyclic frontier in ternary arity.

## Frontier

- Development version when composed: None
- Development version now: 1
