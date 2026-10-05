# Toolkit migration — Two bad endpoint extensions of a four-path give a two-path repartition or interior noninsertability

Preserved from the retired Toolkit Limbo object [[four_path_endpointpair_repartition_or_lock01]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 2,
    "created_at": "2026-09-29T19:20:00.209031+00:00",
    "updated_at": "2026-10-03T15:39:36.649056+00:00",
    "archived_at": "2026-10-03T15:39:36.649056+00:00",
    "original_id": "four_path_endpointpair_repartition_or_lock01",
    "audit_status": "unaudited",
    "math_version": 1,
    "toolkit_type": "other",
    "refutation_status": "unrefuted",
    "author_session_ids": [
    ],
    "audited_math_version": null
}

## Simplified statement

Two bad endpoint extensions of a four-path give a two-path repartition or interior noninsertability

## Statement

Let H be a boundary tournament, let W be a tight path on four vertices, write V(W)=D union {w} with |D|=3, and let Q=(f,q_1,...,q_{q-2},g) be a vertex-disjoint tight path of order q>=3. Suppose H[D union {f}] and H[D union {g}] are non-Hamiltonian. Put M=(q_1,...,q_{q-2}) and F=D union {f,g}. Then H[F] is Hamiltonian. Moreover either H[V(M) union {w}] is Hamiltonian, in which case F | (V(M) union {w}) is a two-path cover of V(W) union V(Q) whose quadratic potential differs from that of W|Q by 10-2q, or H[V(M) union {w}] is non-Hamiltonian, in which case w is noninsertable into every position of the inherited path M.

## Body

Choose any tight Hamilton order on the three-set D. Since D union {f} and D union {g} are both non-Hamiltonian, the certified two-bad-four-extensions lemma in localextend01 gives a Hamilton path on F=D union {f,g}. The supports F and V(M) union {w} are disjoint and partition V(W) union V(Q). If H[V(M) union {w}] is Hamiltonian, these two Hamilton paths give a two-path repartition of W|Q. Its component orders change from (4,q) to (5,q-1), so the quadratic-potential change is 25+(q-1)^2-16-q^2=10-2q. If H[V(M) union {w}] is non-Hamiltonian, inserting w into the inherited tight path M at any position would Hamiltonize that support, a contradiction. Hence w is noninsertable into M. No ambient third path, spanningness, extremality, or minimum-counterexample hypothesis is used.

## Direct premises at migration

[]

## Direct consumers at migration

[]

## Supersession records at migration

[]

## Retained passed-version snapshot at migration

null
