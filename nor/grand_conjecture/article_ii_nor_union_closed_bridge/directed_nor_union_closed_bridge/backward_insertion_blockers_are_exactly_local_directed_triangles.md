# Backward insertion blockers are exactly local directed triangles

## Composition

At a ternary insertion transition along a deletion witness for a front circuit, either the missing vertex creates a shifted two-element front circuit or the backward-blocker alternative creates a directed triangle in the center tournament at the crossed vertex. Indeed the three relevant comparisons are p->x, x->b, and b->p in the color-sigma center tournament. Hence failure of circuit contraction is exactly a local failure of neighborhood union closure. In particular, if all center tournaments are transitive, every front circuit contracts immediately to a shifted two-circuit.

## Development

## Backward insertion blockers are exactly local directed triangles

Continue the insertion-sliding setup for ternary arity. Let \(U\) be a front circuit in color \(\tau\), let \(x\in U\), and let
\[
W_x=(\ldots,p,a,b,c,\ldots,F)
\]
be a \(\tau\)-tight witness for \(U\setminus\{x\}\). At a first insertion transition suppose
\[
h(x,a,b)=\sigma,\qquad h(x,b,c)=\tau,\qquad \sigma=1-\tau.
\]
The transition lemma says that either \(\{a,x\}\) is a shifted two-circuit at tail \((b,c)\), or
\[
h(a,x,b)=\tau,\qquad h(p,a,x)=\sigma.
\tag{1}
\]
The latter was called a backward blocker.

### Proposition: a backward blocker is a directed triangle
In the backward-blocker case, the color-\(\sigma\) center tournament at \(a\), defined by
\[
u\to_a v\quad\Longleftrightarrow\quad h(u,a,v)=\sigma,
\]
contains the directed triangle
\[
p\to_a x\to_a b\to_a p.
\tag{2}
\]

### Proof
The first edge in (2) is exactly \(h(p,a,x)=\sigma\) from (1). The second is \(h(x,a,b)=\sigma\), the blocking value at the insertion transition. Since \(W_x\) is \(\tau\)-tight,
\[
h(p,a,b)=\tau=1-\sigma.
\]
Reversal antisymmetry therefore gives
\[
h(b,a,p)=\sigma,
\]
which is the third edge \(b\to_a p\). \(□\)

### Corollary: circuit contraction or local union-closure failure
At every \(\sigma\to\tau\) insertion transition along a deletion witness, exactly one of the following occurs:

1. a shifted two-element front circuit is produced; or
2. a center tournament contains a directed triangle.

For a tournament, absence of directed triangles is equivalent to transitivity, and Article II has already identified transitivity with union closure of the corresponding center-neighborhood family. Hence the backward-blocker alternative is precisely a local neighborhood-union-closure defect.

In particular, if all center tournaments are transitive, every front circuit—of arbitrary size—yields a shifted two-element circuit by sliding any missing vertex from its blocked front toward the common tail. No indefinite backward-blocker chain is possible in the locally transitive class.

### Significance
This ties together the two previously separate Article II obstruction languages. Whole-witness union closure can fail through a punctured Boolean support circuit. Trying to contract that circuit by insertion either succeeds immediately at size two or exposes a directed triangle, which is exactly the obstruction to union closure of the local center-neighborhood family. Thus any general closure proof may split cleanly:

- exploit the resulting two-circuit geometry; or
- exploit a certified directed triangle at a specific center.

The remaining challenge is to show that these local obstructions cannot propagate indefinitely through recentering in a genuine counterexample.
