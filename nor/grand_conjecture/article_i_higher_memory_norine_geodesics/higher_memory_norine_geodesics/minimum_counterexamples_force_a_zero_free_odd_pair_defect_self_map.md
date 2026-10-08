# Minimum counterexamples force a zero-free odd pair-defect self-map

## Composition

(none yet)

## Development

## Minimum counterexamples force a zero-free odd pair-defect self-map

Assume the directed translation-invariant sector has a counterexample on a ground set \(V\) of minimum size \(n\). Let
\[
D(\pi)
=
\sum_{\substack{i<j\\ d_i=d_j=1}}
(e_{v_i}-e_{v_{j+r}})
\in W_V
\]
be the canonical pair-defect from Subsection 25. Under the counterexample hypothesis every permutation is bad, so \(D(\pi)\ne0\), and
\[
D(\pi^{\rm rev})=-D(\pi).
\]

Use the standard barycentric face-average extension: at the barycenter of a Coxeter face \(F\), assign the average of \(D(\pi)\) over all permutation chambers \(\pi\) containing \(F\), then extend affinely on chains of faces. Denote the resulting continuous odd map by
\[
\overline D:S^{n-2}\longrightarrow W_V.
\]

### Theorem
\[
\overline D(x)\ne0
\qquad\text{for every }x\in S^{n-2}.
\]

### Proof

Suppose \(\overline D(x)=0\). Choose the unique barycentric simplex whose relative interior contains \(x\), corresponding to a strict chain of nonempty Coxeter faces
\[
F_0\subsetneq F_1\subsetneq\cdots\subsetneq F_t.
\]
All barycentric coefficients of \(x\) in this simplex are positive.

Expanding each face-barycenter label into its chamber average expresses \(0\) as a positive linear combination of \(D(\pi)\) over chambers containing \(F_0\). Moreover every chamber containing \(F_0\) occurs with positive coefficient, because the \(F_0\)-barycenter itself has positive coefficient and averages over all such chambers.

Write the ordered-partition face \(F_0\) as
\[
B_1|\cdots|B_s.
\]
The pair-defect face-localization lemma then forces, for every refinement \(\pi\) of \(F_0\), all changes of \(\pi\) to lie inside one face block. Since every refinement occurs positively, the host block is constant over all refinements: adjacent swaps inside a non-host block leave the host's two or more internal changes untouched, while a swap inside the host cannot create two internal changes in another block whose internal order did not change.

Thus one fixed block \(B\) contains all changes for every refinement of \(F_0\). Fix the orders in the other blocks and vary the order of \(B\). Every permutation of \(B\) then has at least two changes in its restricted \(r\)-window word. Hence \(h|_B\) is a counterexample on the proper subset \(B\), contradicting minimality. \(\square\)

### Corollary: the remaining obstruction is a self-map degree problem

Normalize:
\[
f(x)=\frac{\overline D(x)}{\|\overline D(x)\|}.
\]
Since
\[
\dim W_V=n-1,
\]
its unit sphere is \(S^{n-2}\). Therefore a minimum counterexample would produce a continuous odd self-map
\[
f:S^{n-2}\to S^{n-2}.
\]

In particular its degree is odd. The directed NOR conjecture is therefore reduced, along this route, to proving that the special pair-defect carrier map has degree \(0\) or otherwise cannot realize an odd-degree self-map.

This is the precise one-dimension obstruction: ordinary Borsuk--Ulam cannot kill an odd self-map in equal dimensions, but all lower-dimensional face zeros have already been eliminated by minimum-counterexample descent.

### Structural feature available for a degree computation

For a chamber
\[
\pi=(v_1,\ldots,v_n)
\]
with first and last change positions \(f<\ell\), every root in \(D(\pi)\) points forward in the chamber order, and in the simple-root basis of that order the support of \(D(\pi)\) is contained in the consecutive interval
\[
\{\alpha_f,\alpha_{f+1},\ldots,\alpha_{\ell+r-1}\}.
\]
The root from the first and last changes occurs, so every simple root in that interval has positive coefficient.

Hence \(D(\pi)\) lies on the boundary of the chamber's positive root cone unless
\[
f=1,\qquad \ell=n-r.
\]
A degree/carrier argument that forces an interior-cone chamber would therefore produce an order whose first and last transition positions are both extreme. In the minimum-counterexample fork language, that is exactly the regime where the deletion one-change word has a singleton outer branch on the relevant side.

This links the topological degree frontier directly back to the current augmentation frontier rather than creating a separate line of work.
