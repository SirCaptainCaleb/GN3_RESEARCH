# Three failed-absorption hooks force an explicitly rooted interface four-path — preserved pre-item development

## Three failed-absorption hooks force an explicitly rooted interface four-path

Retain three distinct labels
\[
t_1,t_2,t_3
\]
arising from failed rooted corridor absorption at the interface
\[
T=(x,y,z,\ldots),
\]
so
\[
h(y,x,t_i)=1
\qquad(i=1,2,3).
\]

Partition the three hook labels by their orientation through the fixed pair
\[
\{x,y\}:
\]
\[
E_+=\{t:h(x,t,y)=1\},
\qquad
E_-=\{t:h(y,t,x)=1\}.
\]
Boundary antisymmetry makes this a partition.

By pigeonhole, two hook labels, say \(t_i,t_j\), lie in the same class.

### Positive class

If
\[
h(x,t_i,y)=h(x,t_j,y)=1,
\]
the two-parallel-middle lemma gives exactly one of the Hamilton paths
\[
(x,t_i,y,t_j),
\qquad
(x,t_j,y,t_i).
\]
Thus the interface vertex \(x\) is a prescribed initial endpoint and \(y\) is penultimate.

### Negative class

If
\[
h(y,t_i,x)=h(y,t_j,x)=1,
\]
the same lemma with \(x,y\) exchanged gives one of
\[
(y,t_i,x,t_j),
\qquad
(y,t_j,x,t_i).
\]
Thus \(y\) is a prescribed initial endpoint and \(x\) is penultimate.

Therefore:

> **Rooted interface-four theorem.** Three failed-absorption hook labels always contain a pair \(t_i,t_j\) such that
> \[
> \{x,y,t_i,t_j\}
> \]
> is Hamiltonian, with an explicit order in which one corridor-interface vertex is the first vertex and the other is penultimate.

This is the prescribed-pair mixed-four theorem specialized to the actual corridor interface, with the useful Hamilton order retained.

Combining with [[failed_rooted_corridor_absorption_supplies_three_zero_exit_carrier_labels]], failed direct absorption therefore produces simultaneously:
1. three zero-exit labels for the oriented edge \((x,y)\);
2. a Hamiltonian four-support containing both interface vertices and two of those labels.

The remaining packet-repartition problem is now concentrated on the four unused packet labels and on the final junction from the rooted four-support back into the frozen corridor.
