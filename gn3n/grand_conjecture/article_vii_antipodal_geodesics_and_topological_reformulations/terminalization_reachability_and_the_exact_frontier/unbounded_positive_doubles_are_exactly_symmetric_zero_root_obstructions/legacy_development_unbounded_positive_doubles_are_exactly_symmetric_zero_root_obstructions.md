# Unbounded positive doubles are exactly symmetric zero-root obstructions — preserved pre-item development

## Development

## The unbounded reflected-double branch is exactly a local zero-root obstruction

Let J be the full determining span of a protected positive span-two reflected double, written in its displayed chamber order. Let m_J=|J|-2 be the length of its status word.

Each positive span-two word is either 001 or 011. Hence its first status is 0 and its last status is 1. Since the two reflected occurrences occupy the two ends of J, the status word of the displayed order on J satisfies
[
epsilon_1=0,qquad epsilon_{m_J}=1.
]

For the exact inversion coordinates on H[J],
[
p=min{i:epsilon_i=0}=1,
qquad
q=max{i:epsilon_i=1}=m_J,
]
and therefore
[
c=m_J+1-q=1.
]
Thus the exact root of the displayed induced order is
[
psi_J=e_p-e_c=0.
]

So every positive reflected span-two double is, on its full determining span, a **symmetric exact-root chamber**.

At the same time [[reflected_double_spans_have_deletion_distance_at_most_two]] gives
[
kappa_2(H[J])le2,
]
because deleting the two exterior endpoint vertices leaves the positive-word-free corridor two-cover.

These two facts identify the obstruction very sharply:

- in local-witness coordinates it is the only unbounded protected reflected-double branch;
- in exact-root coordinates it is precisely a zero-root chamber with potentially very large displayed deletion hole;
- nevertheless its induced tournament lies at two-cover deletion distance at most two.

This explains why both proof routes stalled at apparently different places. The local route cannot repair a genuine kappa_2=2 instance inside J by [[genuine_two_deletion_doubles_admit_no_internal_outward_repair]], while the exact-root route cannot bound the hole size of a zero-root chamber merely from p=c. They are the same phenomenon.

Accordingly the next theorem should be formulated jointly rather than duplicated:

**Symmetric two-deletion interface theorem.**
Let H have an order with exact root zero, first status 0 and last status 1, such that deleting the two endpoint vertices leaves a two-cover. Under the additional reflected-positive protection inherited from the local-witness carrier, either H has a two-cover or the configuration admits an enlarged-window/protected-carrier bypass.

A proof of this theorem would simultaneously remove the unbounded reflected-double branch from the positive filtration and the symmetric zero-root alternative from the exact-root route.
