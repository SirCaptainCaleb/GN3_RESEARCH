# No farther positive witness forces monochromatic outward status rays

## Composition

### No-farther-witness rays

If a selected left \(011\) occurrence has no farther positive witness on its outward side, every status farther outward is \(1\). Dually, if a selected right \(001\) occurrence has no farther positive witness outward, every farther status is \(0\). Hence the exterior portions adjacent to a terminal reflected double are tight guard paths in their forced orientations.

## Development

## No farther positive witness forces monochromatic outward status rays

Let
\[
J=(x,c_1,\ldots,c_N,y)
\]
be the full determining span of a genuine protected reflected span-two double with
\[
\kappa_2(H[J])=2.
\]
By [[genuine_two_deletion_doubles_have_a_fixed_mixed_polarity_and_forced_first_outward_shell]], its endpoint words are necessarily
\[
011\quad\text{on the left},\qquad 001\quad\text{on the right}.
\]

Write the ambient status sequence as \(\epsilon_i=h(v_i,v_{i+1},v_{i+2})\), and let the selected left occurrence begin at \(a\):
\[
\epsilon_a\epsilon_{a+1}\epsilon_{a+2}=011.
\]

**Lemma (left outward ray).** If there is no positive witness from
\[
\mathcal W_+=\{001,011,0101\}
\]
beginning strictly to the left of \(a\), then
\[
\epsilon_i=1\qquad\text{for every }i<a.
\]

**Proof.** Suppose instead that some \(\epsilon_i=0\) for \(i<a\), and choose the largest such \(i\). Then all statuses \(\epsilon_{i+1},\ldots,\epsilon_{a-1}\) are \(1\).

If \(i=a-1\), then
\[
\epsilon_{a-1}\epsilon_a\epsilon_{a+1}=001.
\]
If \(i=a-2\), then
\[
\epsilon_{a-2}\epsilon_{a-1}\epsilon_a\epsilon_{a+1}=0101.
\]
If \(i\le a-3\), then
\[
\epsilon_i\epsilon_{i+1}\epsilon_{i+2}=011.
\]
Each case gives a positive witness strictly farther outward, contradiction. \(\square\)

There is an exact right-hand dual. Let the selected right occurrence begin at \(b\):
\[
\epsilon_b\epsilon_{b+1}\epsilon_{b+2}=001.
\]

**Lemma (right outward ray).** If there is no positive witness beginning strictly to the right of \(b\), then
\[
\epsilon_i=0\qquad\text{for every }i>b+2
\]
for which the status is defined.

**Proof.** If not, choose the least \(j>b+2\) with \(\epsilon_j=1\). Then every status between \(b+3\) and \(j-1\) is \(0\). If \(j=b+3\), the block
\[
\epsilon_{b+1}\epsilon_{b+2}\epsilon_{b+3}=011
\]
is positive. If \(j=b+4\), then
\[
\epsilon_{b+1}\epsilon_{b+2}\epsilon_{b+3}\epsilon_{b+4}=0101.
\]
If \(j\ge b+5\), then
\[
\epsilon_{j-2}\epsilon_{j-1}\epsilon_j=001.
\]
Again there is a strictly farther positive witness. \(\square\)

### Geometric consequence

In a no-farther-witness chamber, the entire ambient prefix ending at the left root is a tight path in ambient order: every consecutive triple before the selected initial zero is tight. In particular, whenever two exterior vertices \(z_2,z_1\) precede \(x\),
\[
(z_2,z_1,x,c_1)
\]
is a tight four-vertex path.

Dually, the entire right exterior suffix is a tight path in reverse ambient order. If \(w_1,w_2\) are the first two vertices after \(y\), then
\[
(w_2,w_1,y,c_N)
\]
is a tight four-vertex path.

Thus the surviving genuine double is not surrounded by arbitrary exterior data. If no strictly farther positive witness already exists, both outward sides are organized into rooted tight guard paths. Combining this with [[outward_buffer_vertices_bypass_the_internal_two_deletion_obstruction]], a blocked left side simultaneously has
\[
h(c_2,c_1,z)=1
\]
for every vertex \(z\) of a tight outward guard path; the right side has the mirror structure.

This does **not** imply a two-cover or an outward repair. In particular [[uniform_buffer_blocking_alone_does_not_force_a_farther_positive_witness]] shows that an all-\(1\) left ray, an all-\(0\) right ray, and uniform buffer blocking can coexist at the status-word level. The new information is structural rather than closing: the remaining rooted packet-gluing theorem may treat each unbounded exterior side as a tight path attached to a bounded packet interface, rather than as an arbitrary set of outside vertices. Any successful next step must still use deletion-distance-two connector exclusion, packet Hamiltonicity, or exterior-assisted absorption.
