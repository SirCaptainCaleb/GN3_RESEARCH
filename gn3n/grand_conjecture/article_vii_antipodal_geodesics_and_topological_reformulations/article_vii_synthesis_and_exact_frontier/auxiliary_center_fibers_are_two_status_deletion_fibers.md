# Auxiliary-center fibers are two-status deletion fibers

## Composition

(none yet)

## Development

## Auxiliary-center fibers are two-status deletion fibers of one original order

Let
\[
\omega=(v_1,\ldots,v_n)
\]
be a fixed spanning order of the original boundary tournament \(H\), with status word
\[
\epsilon_i=h(v_i,v_{i+1},v_{i+2}),
\qquad 1\le i\le n-2.
\]
For \(0\le s\le n\), insert the auxiliary vertex \(r\) between \(v_s\) and \(v_{s+1}\), with the evident endpoint conventions. Denote the resulting auxiliary chamber by \(\pi_s\).

For an internal insertion \(2\le s\le n-2\), the status word of \(\pi_s\) is
\[
\epsilon_1\cdots\epsilon_{s-2},
\quad
1,\quad
\mu_s,\quad
0,\quad
\epsilon_{s+1}\cdots\epsilon_{n-2},
\]
where
\[
\mu_s=h(v_s,r,v_{s+1})
\]
is the unconstrained middle-\(r\) status. Thus insertion of \(r\) removes precisely the two consecutive old statuses
\[
\epsilon_{s-1},\epsilon_s
\]
and replaces the broken neighborhood by \(1,\mu_s,0\). The endpoint insertions have the corresponding truncated form.

**Fiber lemma.**
The auxiliary chamber \(\pi_s\) is directed one-change if and only if
\[
\epsilon_i=1\quad(i\le s-2),
\qquad
\epsilon_i=0\quad(i\ge s+1).
\]
The value of \(\mu_s\) is irrelevant.

**Proof.**
All statuses strictly left of the displayed \(1,\mu_s,0\) block are inherited old statuses, and all statuses strictly right are inherited. Since
\[
1,\mu_s,0
\]
is itself of the form \(1^*0^*\) for either \(\mu_s\in\{0,1\}\), the whole auxiliary word is directed one-change exactly under the displayed prefix/suffix conditions. \(\square\)

Let
\[
p=\min\{i:\epsilon_i=0\},
\qquad
q=\max\{i:\epsilon_i=1\},
\]
with the usual conventions when one set is empty. In the nontrivial case, the fiber lemma gives
\[
\pi_s\text{ is directed one-change}
\quad\Longleftrightarrow\quad
q\le s\le p+1.
\]
Hence some insertion of \(r\) is directed one-change if and only if
\[
q\le p+1.
\]
This is the same inversion-window condition as the exact positive-word/two-cover theorem: equivalently, the original status word avoids
\[
\mathcal W_+=\{001,011,0101\}.
\]

Thus the auxiliary exactification is literally a one-dimensional thickening of the original positive-word problem. For a fixed original chamber \(\omega\), the chambers
\[
\pi_0,\pi_1,\ldots,\pi_n
\]
form its **insertion fiber**; adjacent terms differ only by swapping \(r\) with one original vertex, and deleting \(r\) sends all of them back to the same \(\omega\).

This explains the moving-center obstruction in [[moving_the_auxiliary_center_can_reverse_arbitrary_large_nearest_radii_without_same_face_escape]]. Opposite auxiliary nearest labels can occur along one insertion fiber while the absolute positive occurrences in \(\omega\) do not change at all. Such cancellation is auxiliary-center motion, not a transition between two original witness geometries.

The strategic consequence is precise.

- The exact violation map remains valuable because its chamber zero is exactly the grand target and its low-radius neighborhoods admit the center-preserving repairs of [[bounded_radius_auxiliary_neighborhoods_have_exact_outward_replacements]].
- Large-radius sign cancellation produced only by \(r\)-motion should be quotiented or collapsed as insertion-fiber behavior.
- After deleting \(r\), the remaining obstruction is exactly the fixed-position positive-word obstruction on \(\omega\), where the persistent-orientation and separated-window theorems apply without the moving-center ambiguity.

Accordingly a promising hybrid proof should not try to prove that every large-radius auxiliary sign change is an outward event. It should first separate **fiber edges** (swaps involving \(r\)) from **base edges** (changes of the original order). Fiber edges encode movement of the two-status gap; base edges encode actual changes of the positive-witness geometry. The remaining topological task is to show that the extra dimension contributed by the insertion fibers can be collapsed without destroying the antipodal obstruction, leaving the positive-witness separator problem on the original Coxeter sphere.
