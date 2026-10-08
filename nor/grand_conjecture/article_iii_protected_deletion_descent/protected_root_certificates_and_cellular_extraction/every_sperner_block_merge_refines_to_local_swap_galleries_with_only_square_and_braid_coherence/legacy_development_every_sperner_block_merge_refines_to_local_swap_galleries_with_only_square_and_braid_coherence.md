# Every Sperner block merge refines to local swap galleries with only square and braid coherence — preserved pre-item development

## Development

Use the symmetric consecutive-change defect label C(pi) of root 155.

Consider one codimension-one canonical Sperner face merge
A | D  ->  B=A union D.
With frozen outside prefix P and suffix Q, the fine and coarse witness orders are
pi_0=P g(A)g(D) Q,
pi_M=P g(B) Q.
They differ only by the permutation of the proper coordinate block B.

Choose any reduced adjacent-transposition gallery inside the B-permutahedron from g(A)g(D) to g(B):
U_0 -> U_1 -> ... -> U_M.
Put
pi_j=P U_j Q.
Then every pi_j is a genuine full ambient coordinate order and consecutive states differ by one adjacent swap supported inside B.

The coarse Sperner merge increment telescopes exactly:
C(pi_M)-C(pi_0)
=
sum_{j=0}^{M-1} [C(pi_{j+1})-C(pi_j)].

Each elementary increment is uniformly local. If the swapped positions are r,r+1, only the four ternary-window ranks r-2,...,r+1 can change. Change positions outside this packet are unchanged. In the consecutive-change defect, a macro root joining an unchanged exterior change to the first changed local transition has the same exterior endpoint before and after the swap, so that exterior basis term cancels in the difference. The analogous cancellation holds at the right side. Hence
C(pi_{j+1})-C(pi_j)
is supported in the swapped four-window packet and its immediate macro-root endpoints, a bounded coordinate collar independent of |B| and ambient n.

Under counterexamplehood none of the intermediate full orders pi_j is NOR-good; if one had at most one change, closure is already achieved. Thus the gallery may be treated entirely inside the bad-state repair complex.

Now compare two REDUCED adjacent-swap galleries joining the same two block orders. By the Coxeter presentation of the symmetric group, they are related by repeated local moves of only two kinds:

1. commuting disjoint adjacent swaps:
   s_i s_j <-> s_j s_i for |i-j|>1;
2. braid moves:
   s_i s_{i+1} s_i <-> s_{i+1} s_i s_{i+1}.

The first move is an exact realized commuting square of full coordinate orders with frozen exterior.
The second is an exact realized A2 braid hexagon on three neighboring physical coordinates, again with frozen exterior.

Therefore every canonical Sperner codimension-one merge increment admits a decomposition into genuine adjacent-swap local increments, and the ambiguity of that decomposition is generated entirely by realized commuting squares and A2 braid hexagons.

This refines the coarser block-merge coherence of root 167. The global symmetric Sperner carrier can be expanded, merge by merge, into the same local Coxeter cells already appearing in the threshold-repair and Tucker programs.

The remaining extraction obligation is now sharply local:
construct a label/repair homotopy across one elementary adjacent-swap increment, and verify compatibility around the two primitive gallery relations above. No higher-dimensional permutation relation is needed.
