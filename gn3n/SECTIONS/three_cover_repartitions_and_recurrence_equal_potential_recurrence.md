# Equal-potential recurrence

## Cold composition

Equal-\(\Phi\) moves occur at the equitable size profiles and in the one-vertex transfer case. They must therefore be treated directly.

Consider first the size multiset
\[
\{r+1,r+1,r\}.
\]
An equal-\(\Phi\) repartition transfers one endpoint from a large path to the small path. If no order disagreement or smaller Hamiltonian support appears, the transfers cycle through two labels \(x,y\) and three core paths \(A,B,C\):
\[
x:A\to B,\quad y:C\to A,\quad
x:B\to C,\quad y:A\to B,\quad
x:C\to A,\quad y:B\to C.
\]
Hence both \(x\) and \(y\) extend the same end of each of \(A,B,C\).

Let \(T\) be a two-cover of
\[
H-\{x,y\}=A\cup B\cup C.
\]
Decompose its paths into maximal blocks lying in \(A,B,C\). If \(t\) is the number of edges of \(T\) joining distinct cores and \(b_A,b_B,b_C\) are the block counts, then
\[
t=b_A+b_B+b_C-2.
\]
If \(t=1\), the three cores occur as whole blocks and the same-end extensions by \(x,y\) give a two-cover of \(H\). Thus \(t\ge2\). If \(t=2\), either an edge of one displayed core has endpoints in different paths of \(T\), or one path of \(T\) leaves and later returns to the same core. If \(t\ge3\), there are already three specified edges joining distinct cores.

Therefore a neutral cycle cannot return with only the size data changed: it leaves a concrete order or support discrepancy.

The profiles \(\{r,r,r\}\) and \(\{r+1,r,r\}\) admit the same endpoint comparison. A neutral transfer with opposite endpoint realizations gives a displayed end-edge reversal by greedy endpoint transport. If all endpoint realizations use the same side, Hall's theorem on the two transferred labels and the two paths of a double deletion gives either a two-cover, two reverse triples through one end edge, or two deletion covers differing by one transferred label.

We obtain:

**Lemma 4.** At a minimum of \(\Phi\) in \(\mathcal C\), equal-potential motion produces at least one of:
1. an order disagreement;
2. an edge of a comparison cover joining distinct displayed supports;
3. an inherited path edge whose endpoints lie in different paths of a comparison cover;
4. two separated blocks from one displayed support on one comparison path;
5. a tight triple reversing a displayed edge;
6. two Hamiltonian five-sets with a common four-set;
7. a one-vertex transfer whose endpoint realizations all use the same side.

These are the local recurrence residues.

## Metadata

- ID: three_cover_repartitions_and_recurrence_equal_potential_recurrence
- Kind: section
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False

## Development tree

- [Subsection 1 — (untitled)](../SUBSECTIONS/three_cover_repartitions_and_recurrence_equal_potential_recurrence_subsection_a.md) (\`three_cover_repartitions_and_recurrence_equal_potential_recurrence_subsection_a\`; development v1; composition vNone; stale=True)
