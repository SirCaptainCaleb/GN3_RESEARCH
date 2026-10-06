# Reverse shared bridges have an exact six-packet normal form

## Metadata

- ID: reverse_shared_bridges_have_an_exact_six_packet_normal_form
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 91
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Exact six-packet normal form in the reverse/reverse shared-bridge residue

Retain the reverse/reverse configuration from [[reverse_shared_bridges_reduce_to_one_tight_path_and_a_six_vertex_packet]]. Thus
\[
J=R\sqcup S,\qquad S=A\sqcup\{r,s\},\qquad |A|=4,
\]
where \(R\) is a tight path, \(S\) has order six, and there are Hamilton orders on \(R+r\) and \(R+s\). Assume the full span \(J\) has no two-cover. Then the preceding reduction gives
\[
S,\quad A+r,\quad A+s
\]
all non-Hamiltonian, while
\[
S-w\ \text{is Hamiltonian for every }w\in A.
\]

Apply [[sixset_prescribed_pair_menu01]] to the six-set \(S\) with prescribed pair \(p=r,q=s\). Alternatives (1) and (2) of that theorem are excluded by the displayed non-Hamiltonicity. Hence exactly one of the following two structural branches occurs.

### Branch I: rooted adjacent four-cores

There are distinct \(d,e,f\in A\) such that
\[
S-\{d,e\}\quad\text{and}\quad S-\{d,f\}
\]
are Hamiltonian four-sets. Writing \(A=\{d,e,f,g\}\), these two four-sets are
\[
\{r,s,f,g\},\qquad \{r,s,e,g\},
\]
so they share the rooted triple \(\{r,s,g\}\).

Moreover, because \(J\) has no two-cover,
\[
H[R\cup\{d,e\}]\quad\text{and}\quad H[R\cup\{d,f\}]
\]
are both non-Hamiltonian. Indeed, if \(R+d+e\) were Hamiltonian, its complement in \(J\) would be the Hamiltonian four-set \(S-\{d,e\}\), giving a two-cover; the other pair is identical.

Thus a surviving Branch-I obstruction transfers to two adjacent bad two-vertex extensions of the same long tight path \(R\), sharing the label \(d\), while the complementary rooted four-cores through \(r,s\) are Hamiltonian.

### Branch II: matching-block packet

The four-set \(A\) is the non-Hamiltonian matching-block residue of [[sixset_prescribed_pair_menu01]], and for every \(d\in A\),
\[
(A-d)+r\quad\text{and}\quad(A-d)+s
\]
are Hamiltonian.

In this branch the no-two-cover assumption forces
\[
H[R\cup\{r,d\}]\ \text{and}\ H[R\cup\{s,d\}]
\]
to be non-Hamiltonian for every \(d\in A\). For if \(R+r+d\) were Hamiltonian, its complement \((A-d)+s\) would be Hamiltonian; similarly \(R+s+d\) pairs with \((A-d)+r\).

Equivalently, the absorption sets \(G_r,G_s\) of [[reverse_shared_bridges_reduce_to_one_tight_path_and_a_six_vertex_packet]] are both empty, not merely of total order at most two.

### Consequence

The reverse/reverse shared-bridge residue is therefore not an arbitrary six-packet beside a long path. It has the exact dichotomy
\[
\boxed{
\begin{array}{l}
\text{two rooted Hamiltonian four-cores through }r,s\text{ plus two adjacent bad tail-pairs},\\[1mm]
\text{or a matching-block packet plus eight forbidden one-label absorptions.}
\end{array}}
\]

No minimum-counterexample hypothesis or direct computation is used. The next gluing step may attack these two branches separately.

## Frontier

- Development version when composed: None
- Development version now: 1
