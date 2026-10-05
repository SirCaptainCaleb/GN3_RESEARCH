# Toolkit migration — Componentwise four-side fork interior lock

Preserved from the retired Toolkit Limbo object [[local_four_fork_interior_lock01]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 2,
    "created_at": "2026-09-29T20:18:57.833634+00:00",
    "updated_at": "2026-10-03T15:39:36.649056+00:00",
    "archived_at": "2026-10-03T15:39:36.649056+00:00",
    "original_id": "local_four_fork_interior_lock01",
    "audit_status": "unaudited",
    "math_version": 1,
    "toolkit_type": "other",
    "refutation_status": "unrefuted",
    "author_session_ids": [
    ],
    "audited_math_version": null
}

## Simplified statement

Componentwise four-side fork interior lock

## Statement

Let H be a boundary tournament and W|P|Q a spanning three-cover minimizing quadratic potential in its connected pairwise-repartition component. Write W=D union {w}, |W|=4. Let Q=(f,q_1,...,q_{q-2},g) have order q>=5. If D union {f} and D union {g} are non-Hamiltonian, put M=(q_1,...,q_{q-2}). Then D union {f,g} is Hamiltonian. For q>=6, M union {w} is non-Hamiltonian, so w is noninsertable into the inherited path M. For q=5, either the same lock holds or W|Q has a legal Phi-neutral repartition of orders 5 and 4.

## Body

By the two-bad-four-extension lemma in localextend01, F=D union {f,g} is Hamiltonian. If M union {w} is Hamiltonian, then F and M union {w} partition V(W) union V(Q), so replacing W|Q by those two Hamiltonian paths is one legal pairwise repartition in the same connected component. The potential change is 5^2+(q-1)^2-(4^2+q^2)=10-2q. For q>=6 this is negative, contradicting componentwise minimality. Hence M union {w} is non-Hamiltonian, and any insertion of w into M would contradict that. For q=5 the same repartition has zero potential change, giving the stated neutral alternative. No global minimality hypothesis is used.

## Direct premises at migration

[]

## Direct consumers at migration

[]

## Supersession records at migration

[]

## Retained passed-version snapshot at migration

null
