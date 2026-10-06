# Two bad five-extensions either edge-order the six-set or expose a Hamiltonian support

## Metadata

- ID: two_bad_five_extensions_either_edge_order_the_six_set_or_expose_a_hamiltonian_support
- Parent Section: article_vii_synthesis_and_exact_frontier
- Position: 70
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Two bad five-extensions either amalgamate to an edge order or expose a Hamiltonian support through both exterior labels

Let
\[
U=C\cup\{a,b\},
\qquad |C|=4,
\]
where \(a,b\notin C\). Assume both five-sets
\[
C\cup\{a\},
\qquad
C\cup\{b\}
\]
are non-Hamiltonian.

By the non-Hamiltonian-five-set theorem, their comparison digraphs are acyclic. Equivalently, each admits an edge-order representation.

Then exactly one of the following alternatives is forced:

1. the full comparison digraph \(\Gamma(H[U])\) is acyclic, so \(H[U]\) is edge-orderable; or
2. \(U\) contains a Hamiltonian support \(R\) satisfying
   \[
   \{a,b\}\subseteq R\subseteq U,
   \qquad
   4\le |R|\le6.
   \]

### Proof

Assume \(\Gamma(H[U])\) is cyclic and choose a shortest directed cycle \(\mathcal C\). By the general comparison-cycle classification, \(\mathcal C\) is one of:

- a star triangle;
- the three ordinary edges of an ordinary triangle; or
- the edges of a vertex-simple ordinary cycle of length at least four.

Because the induced comparison digraphs on \(C+a\) and \(C+b\) are acyclic, \(\mathcal C\) cannot be contained in either one. Hence its underlying ordinary edges necessarily involve both exterior labels \(a,b\).

#### Ordinary cycle of length at least four

If \(\mathcal C\) is an ordinary cycle of length \(\ell\ge4\), its directed comparison cycle
\[
e_1\to e_2\to\cdots\to e_\ell\to e_1
\]
opens at any edge to give a tight Hamilton path on the \(\ell\) underlying ordinary-cycle vertices. Since the cycle uses both \(a,b\),
\[
R=V(\mathcal C)
\]
is Hamiltonian, contains \(a,b\), and
\[
4\le |R|=\ell\le6.
\]

#### Star triangle

Suppose \(\mathcal C\) is a star triangle. Since it is not contained in \(C+a\) or \(C+b\), the corresponding four actual vertices contain both \(a,b\). Call this four-set \(R_4\).

If \(H[R_4]\) is Hamiltonian, take \(R=R_4\).

Otherwise \(H[R_4]\) is a non-Hamiltonian four-vertex boundary tournament with cyclic comparison digraph. By the cyclic-\(K_4\) classification it is the exceptional cyclic \(K_4\). The cyclic-\(K_4\) extension theorem says that every fifth vertex Hamilton-extends it. Choose any
\[
z\in U-R_4.
\]
Then
\[
R=R_4\cup\{z\}
\]
is Hamiltonian, contains \(a,b\), and has order five.

#### Ordinary triangle

Suppose \(\mathcal C\) is the comparison cycle on the three ordinary edges of a triangle. To involve both \(a,b\) while not lying in one bad five-set, its actual triangle must be
\[
\{a,b,c\}
\]
for some \(c\in C\).

Choose
\[
d\in C-\{c\}
\]
and put
\[
R_4=\{a,b,c,d\}.
\]
If \(H[R_4]\) is Hamiltonian, take \(R=R_4\).

Otherwise \(R_4\) is a non-Hamiltonian four-set whose comparison digraph is cyclic, because it contains the directed comparison triangle on \(\{a,b,c\}\). Hence \(R_4\) is again the exceptional cyclic \(K_4\). Choose
\[
z\in C-\{c,d\}.
\]
The cyclic-\(K_4\) extension theorem makes
\[
R=R_4\cup\{z\}
\]
Hamiltonian. It has order five and contains \(a,b\).

These cases exhaust every shortest directed comparison cycle. Therefore cyclicity of \(\Gamma(H[U])\) always exposes a Hamiltonian support of order at most six containing both exterior labels. If no such cyclicity occurs, \(\Gamma(H[U])\) is acyclic and the comparison-representation theorem gives a single edge order on all fifteen ordinary edges of \(K_U\). \(\square\)

### Article VII consequence

In the active six-shadow frontier, one need not first prove that the two bad \(K_5\) edge orders agree on a common fourteen-edge shadow and then analyze insertion of \(ab\). The stronger dichotomy above is available immediately:

> either the entire six-label packet is edge-orderable, or the failure of edge-order amalgamation already produces a Hamiltonian \(4\)-, \(5\)-, or \(6\)-support containing both distinguished exterior labels.

Thus the genuinely unresolved branch of the mostly-edge-ordered six-shadow is the fully edge-orderable \(K_6\) branch. Any non-orderability is already a bounded Hamiltonian-support output suitable for the existing Article III--VII transport machinery.

## Frontier

- Development version when composed: None
- Development version now: 1
