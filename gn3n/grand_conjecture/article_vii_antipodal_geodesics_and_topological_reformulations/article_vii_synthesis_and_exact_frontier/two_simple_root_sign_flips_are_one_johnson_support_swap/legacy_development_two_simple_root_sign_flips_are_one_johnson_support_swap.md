# Two simple-root sign flips are one Johnson support swap — preserved pre-item development

## Composition

(none yet)

## Development

## Two simple-root sign flips are one Johnson support swap

Let \(X\) be a fixed minimum deletion set and suppose
\[
H-X=A\mid B,\qquad |A|=r,\quad |B|=r+1,
\]
is a normalized adjacent-simple-root two-cover.

Assume a neutral endpoint transfer moves a vertex
\[
q\in B
\]
from the long support to the short support. Thus
\[
A_1=A\cup\{q\},\qquad B_1=B-\{q\}
\]
are Hamiltonian and have orders
\[
r+1\mid r.
\]
The associated minimum-hole root changes sign.

Now suppose a second neutral endpoint transfer is made from the new long support \(A_1\) to the new short support \(B_1\). Let the moved vertex be
\[
p\in A_1.
\]
Then
\[
A_2=A_1-\{p\},\qquad B_2=B_1\cup\{p\}
\]
are Hamiltonian and again have orders
\[
r\mid r+1.
\]

If \(p=q\), then
\[
A_2=A,\qquad B_2=B,
\]
so the two sign flips are immediate support backtracking.

If \(p\ne q\), then necessarily \(p\in A\), and
\[
A_2=(A-\{p\})\cup\{q\},\qquad
B_2=(B-\{q\})\cup\{p\}.
\]
Hence the two-step move is exactly a one-element exchange between the original equal-cardinality layers:
\[
|A\cap A_2|=r-1.
\]
Equivalently, the \(r\)-support has traversed one edge of the Johnson graph
\[
J(|V(H)-X|,r).
\]

Therefore:

> **Two-flip support lemma.** Every pair of consecutive neutral simple-root sign flips either immediately backtracks or induces one Johnson one-swap of the \(r\)-vertex support, with both the exchanged \(r\)-supports and their complementary \((r+1)\)-supports Hamiltonian.

Thus any featureless simple-root transport trajectory can be sampled every two moves to obtain a walk in a fixed Johnson layer. A recurrent sign-flip trajectory projects to a closed Johnson support-exchange walk; a nonrecurrent trajectory must terminate at a state where both long-side endpoint transfers fail, which is already in the bounded four-component/lower-deletion interface by [[normalized_simple_root_faces_either_flip_root_sign_neutrally_or_descend_to_four_components]].

This converts the remaining adjacent-simple-root problem from root geometry to neutral support-exchange geometry. The next obstruction is therefore a closed Johnson walk of complementary Hamiltonian bipartitions, precisely the scale on which the existing support-compatibility, order-disagreement, and Johnson-density machinery operates.
