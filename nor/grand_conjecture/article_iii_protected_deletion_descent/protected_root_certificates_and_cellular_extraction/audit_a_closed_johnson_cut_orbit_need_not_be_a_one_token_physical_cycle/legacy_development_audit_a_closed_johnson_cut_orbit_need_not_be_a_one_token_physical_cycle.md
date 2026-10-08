# Audit: a closed Johnson-cut orbit need not be a one-token physical cycle — preserved pre-item development

## Audit: a closed Johnson-cut orbit need not be a one-token physical cycle

Root §66 correctly proves that a successor-closed finite family of realized shores contains a directed Johnson cycle, and its corresponding physical edge vectors sum to zero. Its next assertion, that restricting to a simple shore cycle makes the cuts one-token over a common core, does not follow.

### A simple shore cycle with two moving tokens

Let K be a fixed (p-2)-set, with p>=2, disjoint from a,b,c,d. The following four p-cuts are distinct:
\[
C_0=K\cup\{a,b\},\quad C_1=K\cup\{c,b\},\quad
C_2=K\cup\{c,d\},\quad C_3=K\cup\{a,d\}.
\]
Choose their crossing roots in chronological order as
\[
\rho_0=e_a-e_c,\quad\rho_1=e_b-e_d,\quad
\rho_2=e_c-e_a,\quad\rho_3=e_d-e_b.
\]
Every forced Johnson successor is exactly the next cut, including C_3 -> C_0. Thus the cut graph has a simple directed four-cycle and the whole cut trajectory is successor-compatible.

But its physical roots decompose into TWO coordinate two-cycles, a<->c and b<->d. The intersection of all four shores is K, of size p-2. A one-token orbit would have a common (p-1)-core, so this orbit is not one-token.

The example may be embedded in any larger coordinate set, including n>=2p+3, so the ternary short-phase cardinality inequality does not exclude the geometry.

### Cutting into physical circuits reintroduces defects

For the physical two-cycle a<->c, the two carrying cuts are C_0 and C_2. The forced successor of C_0 is C_1, not C_2. The mismatch is
\[
\mathbf1_{C_2}-\mathbf1_{C_1}=e_d-e_b.
\]
The reverse mismatch is
\[
\mathbf1_{C_0}-\mathbf1_{C_3}=e_b-e_d.
\]
Both have Johnson distance one. Thus this physical two-cycle has total cut defect two. The other physical component similarly has positive defect.

So zero displacement error along the whole shore trajectory does not imply zero cut defect for each physical circuit extracted from its vector circulation. Deleting other cycle edges from the temporal order changes which attained cut follows a physical edge.

### Corrected conclusion

Successor closure supplies a directed cycle of attained shores and a positive physical dependence with preserved witness labels at its vertices. It does not by itself supply a zero-defect simple physical cycle, a one-token normal form, or a surgery whose outside coordinate orders agree.

The one-token lemma in root §54 remains valid when its hypothesis is supplied: the roots must themselves be ONE directed simple physical coordinate cycle and the carrying cuts must concatenate along that same cycle. A simple cut-graph orbit is a different notion of simplicity.

Accordingly root §66's second dichotomy branch should be 'a realized directed Johnson cycle with its witnessed edge data'. Extraction still needs either a compatible simple physical subcycle or an argument that handles several interacting coordinate cycles without losing the attained-shore chronology.

This is a counterexample to a cut-geometry implication, not a NOR counterexample and not a claim that arbitrary chosen shore data have been realized by an actual ternary coloring. Additional coloring constraints might rule out such an orbit, but require a separate proof.
