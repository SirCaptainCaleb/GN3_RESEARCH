# Two opposite nonzero exits admit independent two-label repair — preserved pre-item development

## Two opposite nonzero exits can be repaired independently by two exterior labels

Let
\[
B=\{a,b,c,d\}
\]
have mutual terminal-pair graph the chordless cycle
\[
a-b-c-d-a
\]
before the fixed following label \(z\). Assume the exit values satisfy
\[
\delta(a)=\delta(c)=1,\qquad
\delta(b)=\delta(d)=0,\qquad
\delta(z)=1.
\]

Add two distinct exterior labels \(y_a,y_c\) to the movable reservoir and assume
\[
\delta(y_a)=\delta(y_c)=0.
\]
Suppose the mutual-pair graph before \(z\) contains
\[
y_a\sim d,\ a,\ b
\]
and
\[
y_c\sim b,\ c,\ d.
\]
No adjacency between \(y_a\) and \(y_c\) is required.

Then the original four-cycle pair locus is null-homotopic in the enlarged outward locus.

### Proof

With \(z\) fixed, use the terminal-pair clique-complex model.

The two triangles
\[
\{d,a,y_a\},\qquad \{a,b,y_a\}
\]
replace the old cycle segment
\[
d-a-b
\]
by
\[
d-y_a-b.
\]
Thus the original cycle
\[
a-b-c-d-a
\]
is homotopic in the fixed-\(z\) pair locus to
\[
b-c-d-y_a-b.
\]

Likewise the two triangles
\[
\{b,c,y_c\},\qquad \{c,d,y_c\}
\]
replace
\[
b-c-d
\]
by
\[
b-y_c-d.
\]
Therefore the old cycle is homotopic to
\[
\boxed{b-y_c-d-y_a-b.}
\]

Every label on this new cycle has zero exit status:
\[
\delta(b)=\delta(d)=\delta(y_a)=\delta(y_c)=0.
\]

Now apply the zero-exit endpoint-enlargement contraction, equivalently the first inclusion mechanism of [[moving_the_following_label_has_an_exact_first_homology_kernel]], to the subcomplex carried by these four terminal labels. Merging its final free block with \(z\) gives a null-homotopy inside the enlarged outward locus.

Hence the original \(C_4\) loop is null-homotopic.

### Interpretation

This is the two-vertex analogue of case (3) in [[a_four_cycle_has_an_exact_six_label_repair_classification_with_one_exterior_label]]. A single zero-exit exterior label can replace one nonzero-exit cycle vertex when it is mutually adjacent to that vertex and its two neighbors. When the two bad exit vertices are opposite, the two replacements commute: their triangle disks have disjoint bad vertices and do not require an edge between the new labels.

Thus a protected four-cycle with two opposite nonzero exits admits an explicit seven-label repair once two such replacement labels are available.
