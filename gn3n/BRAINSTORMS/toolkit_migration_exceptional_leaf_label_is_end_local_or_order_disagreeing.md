# Toolkit migration — An exceptional leaf label is end-local or order-disagreeing

Preserved from the retired Toolkit Limbo object [[exceptional_leaf_label_is_end_local_or_order_disagreeing]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 2,
    "created_at": "2026-10-03T12:40:22.725697+00:00",
    "updated_at": "2026-10-03T14:42:09.219699+00:00",
    "archived_at": "2026-10-03T14:42:09.219699+00:00",
    "original_id": "exceptional_leaf_label_is_end_local_or_order_disagreeing",
    "audit_status": "unaudited",
    "math_version": 1,
    "toolkit_type": "theorem",
    "refutation_status": "unrefuted",
    "author_session_ids": [
        61
    ],
    "audited_math_version": null
}

## Simplified statement

In a connected balanced support tree, an exceptional leaf label either creates an order disagreement on the neighboring support, or it lies in one of the two end positions of that support order; the second position forces an explicit reversal triple.

## Statement

Let H have path-cover number greater than two, let F_x=P|Q be a selected deletion cover whose support P is a leaf of a connected selected support tree, and let y in Q be exceptional in the sense that F_y has no edge between P and Q-{y}. Assume minimum-imbalance selection. Then there is an equally balanced deletion cover G_y=P|((Q-{y}) union {x}) support-compatible with F_x. For any Hamiltonian order Q, either the order induced by G_y on Q-{y} disagrees with the inherited order from Q, or y occupies one of the first two or last two positions of Q. If y occupies the second position from the relevant end, a tight triple reverses x and y across the endpoint vertex between their insertion slots.

## Body

Let \(H\) be a finite boundary \(3\)-tournament with \(\operatorname{pc}(H)>2\). Let \(F_x=P\mid Q\) be a selected deletion cover whose support \(P\) is a leaf of a connected selected support tree, and let \(y\in Q\) be an exceptional label: the selected cover \(F_y\) has no consecutive pair joining \(P\) to \(Q-\{y\}\). Assume the selected covers minimize component imbalance.

By [[exceptional_leaf_transfer_equals_support_order_gap]], there is an equally balanced deletion cover
\[
G_y=P\mid W,
\]
where \(W=(Q-\{y\})\cup\{x\}\) is Hamiltonian. Moreover the Hamiltonian order on \(W\) inherited from the exceptional comparison has one of the forms
\[
(x,B),\qquad(B,x),
\]
for some order \(B\) of \(Q-\{y\}\). Thus \(x\) occupies an extreme insertion slot relative to \(B\).

Fix the displayed Hamiltonian order of \(Q\), and compare its inherited order on \(Q-\{y\}\) with \(B\). If these orders disagree, the first conclusion holds. Assume therefore that they agree. Then \(F_x\) and \(G_y\), restricted to \(H-\{x,y\}\), have the same two support sets \(P\) and \(Q-\{y\}\) with the same relative orders.

Both omitted labels are therefore inserted into the same common ordered support \(B\): the cover \(F_x\) inserts \(y\) to recover \(Q\), while \(G_y\) inserts \(x\) to recover \(W\). Their insertion slots must be equal or adjacent. Indeed, if at least one whole slot separated them, inserting both \(x\) and \(y\) into \(B\) at their respective positions would create a tight path: every consecutive triple would be inherited from \(F_x\), from \(G_y\), or from the common order \(B\), and no new consecutive triple would contain both inserted labels. Together with the path on \(P\), this would two-cover \(H\), a contradiction.

Since the insertion slot of \(x\) is extreme, the slot of \(y\) is either the same extreme slot or the adjacent slot. Hence \(y\) occupies the first or second position of the displayed order on \(Q\), or symmetrically the last or penultimate position.

In the adjacent-slot case, write the common order locally as \(z,R\) at the relevant end. Up to reversal of the display, the two paths have local forms
\[
(x,z,R),\qquad(z,y,R).
\]
Every consecutive triple in \(x,z,y,R\) is known tight except possibly \((x,z,y)\). If that triple were tight, this path together with \(P\) would two-cover \(H\). Therefore \((x,z,y)\) is non-tight, and boundary reversal gives
\[
(y,z,x)
\]
tight. Thus the adjacent-slot alternative supplies an explicit reversal triple. \(\square\)

## Direct premises at migration

[
    {
        "premise_id": "exceptional_leaf_transfer_equals_support_order_gap",
        "premise_kind": "toolkit",
        "premise_title": "Exceptional leaf transfer equals the support-order gap",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "premise_toolkit_limbo": true
    }
]

## Direct consumers at migration

[
    {
        "consumer_id": "exceptional_leaf_label_gives_disagreement_reversal_or_neutral_recurrence",
        "consumer_kind": "toolkit",
        "consumer_title": "An exceptional leaf label gives disagreement, reversal, or neutral selected-lift recurrence",
        "compatibility_status": "confirmed",
        "premise_math_version": 1,
        "consumer_math_version": 1,
        "consumer_toolkit_limbo": true
    }
]

## Supersession records at migration

[]

## Retained passed-version snapshot at migration

null
