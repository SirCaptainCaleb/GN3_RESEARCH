# Every positive protected-root dependence has a consecutive incomparable-cut junction

## Composition

Every positive dependence of protected type-A roots contains a directed root cycle, and every such cycle has two consecutive roots x→y and y→z whose certified cuts C,D are incomparable. Indeed, if adjacent cuts were comparable then y∉C and y∈D force C⊊D; comparability at every junction would give a strict inclusion cycle. At an incomparable junction, either z∉C or x∈D, so one existing cut already certifies the algebraic shortcut x→z, or else C,D restrict on {x,y,z} as 101 and 010. Thus the global compatible-cut obstruction localizes to one shared-endpoint two-root junction: realize the certified shortcut and shorten the root circuit, or resolve the exact alternating cut crossing by a realized square/A2 braid surgery.

## Development

## Consecutive roots in every positive protected dependence have an incomparable-cut junction

Let
\[
\rho_i=e_{x_i}-e_{x_{i+1}}
\]
be actual protected roots equipped with certified cuts \(C_i\) satisfying
\[
x_i\in C_i,\qquad x_{i+1}\notin C_i.
\]

Any positive dependence among type-A roots decomposes as a positive weighted union of directed cycles. Hence it suffices to study one directed cycle
\[
x_1\to x_2\to\cdots\to x_k\to x_1.
\]

### Adjacent-cut lemma

For every adjacent pair \(C_i,C_{i+1}\), if they are comparable then necessarily
\[
C_i\subsetneq C_{i+1}.
\]

Indeed \(x_{i+1}\notin C_i\) while \(x_{i+1}\in C_{i+1}\), so \(C_{i+1}\subseteq C_i\) is impossible. Equality is impossible for the same reason.

Therefore a directed cycle cannot have every adjacent pair comparable: otherwise
\[
C_1\subsetneq C_2\subsetneq\cdots\subsetneq C_k\subsetneq C_1,
\]
a contradiction.

### Theorem

Every positive dependence of protected roots contains two **consecutive** roots
\[
x\to y,\qquad y\to z
\]
whose certified cuts \(C,D\) are incomparable.

This sharpens the earlier chain-separation theorem: incomparability can be localized at a shared physical endpoint of two consecutive roots rather than somewhere arbitrarily far apart in the support.

### Shortcut-or-alternating-cut dichotomy

For such a consecutive incomparable pair,
\[
x\in C,\quad y\notin C,\qquad y\in D,\quad z\notin D.
\]

There are two possibilities.

1. If \(z\notin C\) or \(x\in D\), then one of the two existing certified cuts already separates the shortcut pair \(x,z\). Algebraically
\[
(e_x-e_y)+(e_y-e_z)=e_x-e_z.
\]
Thus the remaining issue is physical realization of the shortcut root in the admissible carrier.

2. Otherwise
\[
z\in C,\qquad x\notin D.
\]
Then on the three cycle vertices
\[
C\cap\{x,y,z\}=\{x,z\},\qquad
D\cap\{x,y,z\}=\{y\}.
\]
Equivalently their membership words are \(101\) and \(010\). This is the irreducible local crossing pattern.

Hence every positive protected-root dependence contains an adjacent junction which is either shortcut-certifiable by an already present cut or has the exact three-vertex alternating cut pattern.

### Closure relevance

The compatible-cut problem reduces to a bounded two-root junction. A terminating extraction theorem need only realize the certified shortcut \(x\to z\), allowing cycle shortening, or resolve the alternating \(101/010\) cut crossing by a realized square/A2 braid surgery yielding a spanning one-change order or a strict admissible improvement.
