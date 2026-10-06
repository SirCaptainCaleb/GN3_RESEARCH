# Four endpoints force a threefold core or two double-hole equality endpoints

## Metadata

- ID: four_endpoints_force_a_threefold_core_or_two_double_hole_equality_endpoints
- Parent Section: article_vii_synthesis_and_exact_frontier
- Position: 58
- Row version: 2
- Development version: 2
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Let Y|P|Q be a spanning three-cover with |Y|=5, where Y contains distinguished hole labels x,y. Put N=Y-{x,y}, so |N|=3. For each of the four displayed endpoints e of P,Q assume Y union {e} is non-Hamiltonian, and define G_e={r in Y : (Y-{r}) union {e} is Hamiltonian} and A_e=G_e intersect N. By four-of-six, |G_e|>=3, hence A_e is nonempty.

Then at least one of the following holds.

(1) Threefold hole-preserving core. Some ordinary label r in N belongs to A_e for at least three of the four endpoints. Equivalently, the four-label core C=Y-{r}, which still contains x,y, accepts at least three exposed endpoints.

(2) Two double-hole equality endpoints. At least two exposed endpoints e satisfy |A_e|=1. For each such endpoint, if A_e={r}, then both hole labels belong to G_e. Thus (Y-{x}) union {e}, (Y-{y}) union {e}, and (Y-{r}) union {e} are Hamiltonian, while the two remaining ordinary deletions are the only failed five-deletions of Y union {e}. Since Y itself is Hamiltonian, this endpoint is an equality case of the four-of-six bound.

Proof. Suppose (1) fails. Then every ordinary label r in N lies in A_e for at most two endpoints, so sum_e |A_e|<=2|N|=6. If at most one endpoint had |A_e|=1, the other three endpoints would have |A_e|>=2, giving sum_e |A_e|>=7, a contradiction. Hence at least two endpoints have |A_e|=1. Fix such e with A_e={r}. Since |G_e|>=3 and only one ordinary label lies in G_e, both x and y lie in G_e. Together with deletion of e, which leaves Y Hamiltonian, the deletions e,x,y,r are good. The two remaining ordinary deletions must fail, for otherwise A_e would have order at least two. Hence the six-set is exactly a four-of-six equality case. ∎

In branch (1), pigeonhole among three endpoints puts two on one tail and at least one on the other; failed neutral transports therefore force the same omitted ordinary label to reverse both second-layer ends of one tail and a second-layer end of the other. In branch (2), the remaining difficulty is concentrated in at least two six-vertex four-of-six equality configurations.

## Frontier

- Development version when composed: None
- Development version now: 2
