# A three-vertex component beside a path of order at least six strictly descends

**Summary:** At a Phi-minimum, a 3-vertex component cannot sit beside a path of order at least six; beside a 5-path, failure of direct enlargement forces an equal-Phi 3|5 to 5|3 endpoint rotation.

## Statement

Let H be a boundary tournament and let T|C be two components of a path cover, where T is a tight path of order three and C=(c_1,...,c_s) is a tight path with s>=5. If either T union {c_1} or T union {c_s} is Hamiltonian, there is a pairwise repartition with orders (4,s-1) and Delta Phi=8-2s<0. If both four-sets are non-Hamiltonian, then T union {c_1,c_s} is Hamiltonian and there is a pairwise repartition with orders (5,s-2) and Delta Phi=20-4s. Consequently no Phi-minimal three-cover contains component orders 3 and s>=6. For s=5, every Phi-minimal such pair has both endpoint four-extensions non-Hamiltonian and admits an equal-Phi 3|5 to 5|3 rotation.

## Body

Let
\[
T=(t_1,t_2,t_3),\qquad C=(c_1,\ldots,c_s),
\qquad s\ge5.
\]

Suppose first that
\[
H[T\cup\{c_1\}]
\]
is Hamiltonian. Let \(K\) be a Hamilton path on this four-set. Then
\[
K\mid(c_2,\ldots,c_s)
\]
is a two-cover of \(T\cup V(C)\), so replacing the displayed pair \(T\mid C\) gives a legal pairwise repartition with component orders
\[
(3,s)\longrightarrow(4,s-1).
\]
The change in the two affected square terms is
\[
4^2+(s-1)^2-3^2-s^2=8-2s<0.
\]
The same argument applies if \(T\cup\{c_s\}\) is Hamiltonian, using the inherited prefix \((c_1,\ldots,c_{s-1})\).

Assume therefore that both endpoint extensions
\[
T\cup\{c_1\},
\qquad
T\cup\{c_s\}
\]
are non-Hamiltonian. The two-bad-four-extensions lemma in [[localextend01]] applies to the tight three-path \(T\) and the exterior vertices \(c_1,c_s\). It yields a Hamiltonian five-path on
\[
T\cup\{c_1,c_s\}.
\]
Together with the inherited interior path
\[
(c_2,\ldots,c_{s-1}),
\]
this gives a pairwise repartition
\[
(3,s)\longrightarrow(5,s-2).
\]
Its potential change is
\[
5^2+(s-2)^2-3^2-s^2=20-4s.
\]

If \(s\ge6\), this quantity is strictly negative. Hence a \(\Phi\)-minimal three-cover cannot contain a 3-vertex component beside a component of order at least six.

When \(s=5\), direct Hamiltonian enlargement to order four still gives the strict change \(8-2s=-2\), so at a \(\Phi\)-minimum both endpoint four-extensions must be non-Hamiltonian. The preceding five-path construction then gives
\[
(3,5)\longrightarrow(5,3)
\]
with zero change in \(\Phi\). Thus the boundary case is an explicit neutral endpoint rotation.

## Metadata

- ID: three_vertex_component_long_neighbor_rotation01
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
