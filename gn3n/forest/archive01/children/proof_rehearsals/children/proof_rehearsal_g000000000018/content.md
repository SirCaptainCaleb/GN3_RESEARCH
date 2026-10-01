# Proof rehearsal 18 — 2026-09-25 11:57 UTC

## Statement

Given a bounded insertion obstruction, support crossing, reversed common edge, reversing tight triple, tight cycle, or endpoint-deletion order disagreement, construct a direct spanning two-cover or a valid transport sequence with proved termination that reaches endpoint absorption / a spanning ordering of defect span at most two.

## Body

End-to-end rehearsal confirmed the existing shortest proof composition without changing its mathematics: minimum counterexample -> exact deletion two-cover -> omitted vertex noninsertable in each component -> certified bounded local insertion obstructions -> [unsupported bridge] -> defect span <=2 -> spanning two-cover. The eight recent high-level certified results strengthen alternative producers of crossing/support/order disagreement (especially the sharp half-order endpoint probes) but none proves the global consumption/termination step. Refreshed composition 76a4b8652534 against current exact source versions at repository revision 1426.