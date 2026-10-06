# Audit: zero exact root does not by itself supply a balanced deletion cover

## Metadata

- ID: audit_zero_exact_root_does_not_by_itself_supply_a_balanced_deletion_cover
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 289
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Audit of the premise in 287

The implication "a zero exact-root chamber supplies a balanced deletion cover" is not established by 284. A zero exact root means p=c and therefore supplies a symmetric canonical partial cover P|X|Q with |P|=|Q|. It does not assert |X|=1.

With m=n-2, the positive order deficiency is d=m-p-c. At p=c it is d=m-2p. For n=2r+1, this can be any positive odd value, not necessarily one. The global condition kappa_2(H)=1 means that some order has deficiency one; it does not say the zero-root order furnished by topology minimizes deficiency.

Accordingly the potential argument in 287 is valid CONDITIONALLY on the existence of a balanced deletion cover, but its attribution of that premise to the zero-root theorem is a gap. In the odd uniform residue of 269 the premise is available independently: every balanced partition of H-x has Hamiltonian r-sides. No correction to that application is needed.

The same premise issue applies to [[the_zero_root_support_component_is_uniformly_balanced]]. Its support-size propagation proof is correct once a balanced edge is given: sizes transform by s -> 2r-s along every deletion-cover edge. The zero-root theorem alone has not supplied that initial balanced edge.

## Precise bridge and proof

Let H have n=2r+1 vertices, r>=2, and no spanning two-cover. Then H has a balanced deletion cover if and only if there is a zero exact-root chamber of deficiency one.

For the forward direction take actual Hamilton orders P=(p_1,...,p_r), Q=(q_1,...,q_r) of a deletion cover at x, and form
pi=(p_1,...,p_r,x,q_r,...,q_1).
Every internal triple of P is tight. Since P+x cannot be Hamiltonian, (p_{r-1},p_r,x) is non-tight; hence the first non-tight status is p=r-1.
Every internal triple in Q reversed is non-tight by boundary antisymmetry. Since Q+x cannot be Hamiltonian, (q_{r-1},q_r,x) is non-tight, so (x,q_r,q_{r-1}) is tight. Thus the last tight status is q=r+1. With m=2r-1 we obtain c=m+1-q=r-1=p and d=q-p-1=1.
The triple centered at x can have either status and does not change these extremes.

Conversely p=c and d=1 give 2p=m-1=2r-2, so p=r-1 and q=r+1. The canonical prefix path and reversed suffix path each contain r vertices, with the single uncovered vertex between them. They form a balanced deletion cover.

## What remains valid in 287

Assuming a balanced deletion cover exists, a singleton lift has potential 2r^2+1, the absolute minimum among singleton lifts on n vertices. Hence a proved alternative returning a singleton lift at strictly smaller potential is impossible, and any singleton lift at that same potential has r|r deletion sides.

This does not show that every neutral three-cover on that potential level has a singleton, or that every zero-root chamber has a one-vertex hole. The neutral recurrence conclusions must retain the exact hypotheses of the cited omission-swap lemma.

Repair obligation outside the uniform residue: prove the existence of a deficiency-one zero-root chamber (equivalently, a balanced deletion cover) before applying the absolute minimum singleton-lift argument. This audit supplies no new global closure reduction.

## Frontier

- Development version when composed: None
- Development version now: 1
