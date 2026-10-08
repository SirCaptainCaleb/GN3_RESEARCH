#  — preserved pre-item development

## Composition

(none yet)

## Development

Suppose a state in \(\mathcal C\) has the form
\[
X\mid P\mid Q,
\qquad |X|=3,
\qquad
P=(p_1,\ldots ,p_m).
\]

If \(X\cup\{p_1\}\) is Hamiltonian, repartition \(X\mid P\) as
\[
(X\cup\{p_1\})\mid(p_2,\ldots ,p_m).
\]
The two affected orders change from \((3,m)\) to \((4,m-1)\), and
\[
16+(m-1)^2-(9+m^2)=8-2m.
\]
Hence the move strictly decreases \(\Phi\) for \(m\ge5\). The same holds at the other endpoint.

Assume neither endpoint extends \(X\). Boundary reversal then supplies reversed triples at both ends of \(P\). Comparing the six- and seven-vertex sets formed from \(X\), the two endpoints of \(P\), and one further path vertex gives one of two possibilities: a Hamiltonian four-set whose complement has a two-cover, or a Hamiltonian five-set containing both displayed endpoints of a long inherited interval. In either case the new three-cover lies in \(\mathcal C\), because it is obtained by repartitioning \(X\mid P\).

Consequently:

**Lemma 3.** From a three-vertex side adjacent to a path of order at least five, one obtains inside the same component of \(\mathcal R(H)\) either
1. a strict decrease of \(\Phi\);
2. a Hamiltonian four-vertex component with two-coverable complement; or
3. a Hamiltonian five-vertex component tied to displayed endpoints of a complementary path.

Repeated application either decreases \(\Phi\) or reaches a bounded Hamiltonian component carrying endpoint information.
