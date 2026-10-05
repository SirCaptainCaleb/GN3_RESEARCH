# Toolkit migration — The kappa-one nonzero four-block is impossible

Preserved from the retired Toolkit Limbo object [[kappa_one_nonzero_four_block_is_impossible]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 1,
    "created_at": "2026-10-05T00:27:11.936386+00:00",
    "updated_at": "2026-10-05T00:27:35.665479+00:00",
    "archived_at": null,
    "original_id": "kappa_one_nonzero_four_block_is_impossible",
    "audit_status": "passed",
    "math_version": 1,
    "toolkit_type": "lemma",
    "refutation_status": "unrefuted",
    "author_session_ids": [
        141
    ],
    "audited_math_version": 1
}

## Simplified statement

The role-balanced four-vertex nonzero exact-root carrier proposed in the kappa_2=1 branch is inconsistent with boundary antisymmetry; hence the augmented exact-root map must have a zero-root chamber.

## Statement

In the kappa_2=1 equal-side four-block case, every order of the central block would have central status pattern in {0010,0110,1001,1011}. No boundary tournament can realize this condition for all 24 orders of four vertices.

## Body

Let the four central vertices be a,b,c,d, with fixed neighboring anchors L,R. For any order (u,v,w,z) of the block, the four central statuses must be one of A=0010, B=0110, C=1001, D=1011. Consider the five block orders P0=(b,d,c,a), P1=(c,d,b,a), P2=(d,b,a,c), P3=(d,c,a,b), P4=(d,c,b,a). Comparing the triples shared by these orders, using boundary antisymmetry when the endpoints reverse, gives the following compatibility consequences: (i) if P0 is not B then P1=B, while if P0=B then P1 is not B; (ii) if P0 is not C then P3=B; (iii) if P1 is not C then P2=B; (iv) if P2 is not C then P3=C; (v) P1,P3,P4 have the same first status bit, so P1 and P3 lie in the same pair {A,B} or {C,D}. Now check P0. If P0=A or D, then P1=P3=B; (iii) gives P2=B and (iv) gives P3=C, contradiction. If P0=C, then P1=B, while (ii) allows P3 in {A,C,D}; (v) forces P3=A. Again (iii) gives P2=B and (iv) gives P3=C, contradiction. If P0=B, then P3=B by (ii); (v) forces P1=A. Then (iii) gives P2=B and (iv) gives P3=C, contradiction. Thus no assignment exists. The pairwise compatibility consequences are direct four-bit checks from the shared triples and the relation h(w,v,u)=1-h(u,v,w).

## Direct premises at migration

[]

## Direct consumers at migration

[]

## Supersession records at migration

[]

## Retained passed-version snapshot at migration

null
