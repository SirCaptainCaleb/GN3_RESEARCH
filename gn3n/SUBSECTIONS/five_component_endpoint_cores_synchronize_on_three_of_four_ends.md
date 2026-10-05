# Five-component endpoint cores synchronize on three of four ends

## Metadata

- ID: five_component_endpoint_cores_synchronize_on_three_of_four_ends
- Parent Section: article_vii_synthesis_and_exact_frontier
- Position: 30
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Let X|P|Q be a spanning three-cover with |X|=5 and both displayed paths P,Q of order at least six. Assume that for each of the four displayed endpoints e of P,Q the six-set X union {e} is non-Hamiltonian. For such e define G_e={r in X : (X-{r}) union {e} is Hamiltonian}. By four-of-six, |G_e|>=3. Hence the four sets G_e contribute at least 12 incidences on five labels, so some r in X belongs to at least three of them. Therefore C=X-{r} is a common four-core for at least three of the four endpoints; in particular it works for both endpoints of one of P,Q and for at least one endpoint of the other. For every good endpoint e of a tail T, either (T-{e}) union {r} is Hamiltonian, in which case replacing X by C union {e} and T by (T-{e}) union {r} is an equal-cardinality neutral pairwise repartition, or that one-vertex extension is non-Hamiltonian. In the latter case endpoint_replacement_truncation_dichotomy01 makes r noninsertable at every position of the inherited truncated tail. Consequently, if both endpoint exchanges against the same tail T=(t_1,...,t_m) fail, then h(t_3,t_2,r)=1 and h(r,t_{m-1},t_{m-2})=1: the synchronized omitted label reverses both second-layer end edges of T. Thus the two-sided common-core obstruction is at worst one missing corner; absent a neutral exchange, the same label pushes reversal one step inward along an entire long tail.
