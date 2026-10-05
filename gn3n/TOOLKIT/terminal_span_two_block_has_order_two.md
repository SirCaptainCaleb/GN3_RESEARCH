# A terminal span-two witness block has exactly two vertices

**Summary:** In the terminal disjoint-window span-two branch, the bridging block is necessarily the two-vertex case alpha=beta=1.

## Statement

Assume a terminal single-sided configuration for a nearest span-two witness of type 001/011 or 110/100 with disjoint determining windows. Then alpha=beta=1 and |B|=2.

## Body

By [[terminal_local_block_sharpens_to_four]], alpha,beta<=2 and |B|=alpha+beta. The two five-vertex determining windows are adjacent. Between their witness endpoints lie four central status coordinates. Because the selected witness is nearest among both inversion polarities, these four statuses avoid all six local witnesses. In a left-witness chamber their left endpoint has the inward color of that witness, so all four statuses have that color; in a right-witness chamber all four have the opposite color. Terminality says every chamber has exactly one side witness, hence these four central statuses are monochromatic in every chamber and their common color is the terminal state. An adjacent transposition can change at most four consecutive status coordinates. To change the terminal state it must change all four central coordinates, so only the swap at the unique position between the two determining windows can change the state; every adjacent swap of B at a neighboring position preserves it. If |B|>=3, this central Coxeter generator has a neighboring generator in B. The braid relation s_i s_{i+1} s_i = s_{i+1} s_i s_{i+1} reaches the same chamber by two paths. The first path contains one occurrence of the central state-changing generator and the second contains two, while neighboring generators preserve the state, forcing opposite and equal terminal colors simultaneously. Contradiction. Therefore |B|<3. Both alpha and beta are positive, so alpha=beta=1 and |B|=2.

## Metadata

- ID: terminal_span_two_block_has_order_two
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: failed
- Refutation: unrefuted
- Toolkit status: Limbo
