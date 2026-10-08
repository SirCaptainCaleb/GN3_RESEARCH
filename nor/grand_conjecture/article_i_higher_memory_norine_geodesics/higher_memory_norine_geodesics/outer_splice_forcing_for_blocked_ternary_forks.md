# Outer-splice forcing for blocked ternary forks

## Composition

(none yet)

## Development

## Outer-splice lemma for ternary coordinate labels

Work in coordinate arity \(r=3\), the directed translation-invariant sector of \(N_4\). Normalize the fork color to \(0\).

Let
\[
P=A,(u,v),\qquad Q=B,(v,u)
\]
be a near-spanning converging tight fork covering \(V\setminus\{x\}\), with
\[
A=(a_1,\ldots,a_p),\qquad B=(b_1,\ldots,b_q),
\qquad p,q\ge1.
\]
Thus every consecutive triple in \(P\) and \(Q\) has color \(0\).

Assume the missing vertex is blocked at both outer fronts:
\[
h(x,F_P)=h(x,F_Q)=1.
\]
Equivalently,
\[
h(F_P^{\rm rev},x)=h(F_Q^{\rm rev},x)=0.
\]

Define the cross bit
\[
\beta=h(a_1,x,b_1).
\]

### Lemma

The cyclic coordinate order
\[
C=(v,u,A^{\rm rev},x,B)
\]
has cyclic status word
\[
1^p\,0\,\beta\,1\,0^q.
\]

### Proof

The initial segment
\[
(v,u,A^{\rm rev})
\]
is the reversal of the \(0\)-tight path
\[
(A,u,v)=P,
\]
so its \(p\) consecutive triple colors are all \(1\).

The next triple consists of the reversed outer front of \(P\) followed by \(x\), hence has color \(0\). The next triple is
\[
(a_1,x,b_1)
\]
and has color \(\beta\). The following triple is \(x\) followed by the outer front of \(Q\), hence has color \(1\).

Finally, continuing cyclically through
\[
(B,v,u)=Q
\]
gives \(q\) consecutive \(0\)-colored triples. This yields the displayed cyclic word.

### Consequence for a minimum counterexample

A linear coordinate order on \(n=p+q+3\) vertices has \(n-2\) ternary windows. Cutting the cycle therefore keeps \(n-2\) consecutive cyclic statuses.

For the cyclic word
\[
1^p\,0\,\beta\,1\,0^q
\]
one checks directly:

- if \(\beta=0\) and \(q=1\), some cut has at most one change;
- if \(\beta=1\) and \(p=1\), some cut has at most one change.

Indeed, in the first case cut so that the omitted two cyclic statuses cover the isolated \(1\) and one neighboring \(0\); in the second use the reversed placement. Equivalently, among the cyclic transition bits, three of the four transitions then lie in the three-edge arc excluded by a suitable cut.

Hence in any minimum counterexample,
\[
q=1\implies \beta=1,
\qquad
p=1\implies \beta=0.
\]

In particular \(p=q=1\) is impossible. The outer-splice construction therefore gives a local cross-color constraint whenever one branch of a blocked near-spanning ternary fork has only one outer vertex.

### Interpretation

Endpoint blocking does more than prevent direct augmentation. Splicing the two blocked outer ends through the missing vertex produces a four-transition cyclic profile. A short branch forces three of those transitions to cluster closely enough that one value of the cross bit would expose a one-change cut. Thus minimum counterexamples impose a definite cross orientation at every one-vertex branch.
