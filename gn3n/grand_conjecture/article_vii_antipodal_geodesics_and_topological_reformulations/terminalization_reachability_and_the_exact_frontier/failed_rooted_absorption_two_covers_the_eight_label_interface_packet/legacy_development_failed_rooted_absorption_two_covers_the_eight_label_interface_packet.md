# Failed rooted absorption two-covers the eight-label interface packet — preserved pre-item development

## Development

## Failed direct rooted absorption always two-covers the eight-label interface packet

Retain the rooted corridor setup
\[
T=(x,y,z,\ldots)
\]
and the six-vertex endpoint packet \(A\). Suppose direct absorption fails and produces three distinct hook labels
\[
t_1,t_2,t_3\in A
\]
with
\[
h(y,x,t_i)=1.
\]
Put
\[
B=A-\{t_1,t_2,t_3\},
\qquad |B|=3,
\]
and let
\[
W=A\cup\{x,y\}.
\]

For \(i=1,2,3\), write
\[
G_i=B\cup\{t_i\},
\]
and for \(i<j\) write
\[
F_{ij}=\{x,y,t_i,t_j\}.
\]

Then
\[
\boxed{\operatorname{pc}(H[W])\le2.}
\]

### Case 1: two of the \(G_i\) are non-Hamiltonian

Suppose \(G_i,G_j\) are non-Hamiltonian, with \(k\) the remaining index.

Apply the two-bad-four-extension lemma from [[localextend01]] to the common three-set \(B\) and exterior labels \(t_i,t_j\). It gives
\[
B\cup\{t_i,t_j\}
\]
Hamiltonian.

Its complement in \(W\) is
\[
\{x,y,t_k\},
\]
and every three-vertex boundary tournament is Hamiltonian. Hence these two supports form a two-cover of \(W\).

### Case 2: at most one \(G_i\) is non-Hamiltonian

The fixed-pair bad-extension theorem applied to the prescribed pair
\[
\{x,y\}
\]
and exterior triple \(\{t_1,t_2,t_3\}\) says that at least one \(F_{ij}\) is Hamiltonian.

If all three \(G_i\) are Hamiltonian, choose any Hamiltonian \(F_{ij}\); its complementary four-set in \(W\) is \(G_k\), so
\[
F_{ij}\mid G_k
\]
is a \(4|4\) two-cover.

It remains that exactly one \(G_i\) is non-Hamiltonian. Relabel so
\[
G_3\text{ is non-Hamiltonian},\qquad G_1,G_2\text{ are Hamiltonian}.
\]

If \(F_{13}\) is Hamiltonian, then
\[
F_{13}\mid G_2
\]
is a \(4|4\) two-cover. Likewise, if \(F_{23}\) is Hamiltonian then
\[
F_{23}\mid G_1
\]
is a two-cover.

Assume both \(F_{13},F_{23}\) are non-Hamiltonian. Apply the two-bad-four-extension lemma again, now to the common three-set
\[
\{x,y,t_3\}
\]
with exterior labels \(t_1,t_2\). It gives
\[
\{x,y,t_1,t_2,t_3\}
\]
Hamiltonian. Its complement in \(W\) is \(B\), a Hamiltonian three-set. Thus \(W\) has a \(5|3\) two-cover.

The cases are exhaustive. \(\square\)

### Consequence for rooted terminalization

The three-hook residue is therefore stronger than a bounded Hamiltonian-support certificate:

> if direct absorption into the frozen corridor fails, the endpoint packet together with the first two corridor-interface vertices already has path-cover number at most two.

This does **not** yet give a rooted repair of the whole corridor, because the resulting two-cover need not expose the ordered pair \(x,y\) in a position that can be concatenated with the fixed suffix \(z,\ldots\). The remaining obligation is now purely a **boundary-ordering problem for a known local two-cover**, rather than Hamiltonicity or path-cover existence on the endpoint packet.
