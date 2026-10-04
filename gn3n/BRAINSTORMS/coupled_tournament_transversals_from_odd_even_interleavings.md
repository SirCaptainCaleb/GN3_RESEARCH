# Coupled tournament transversals from odd-even interleavings

Reformulate an arbitrary boundary 3-tournament H using its local tournaments T_b on V-{b}, where a->c in T_b iff (a,b,c) is tight. Split a spanning order into odd-position and even-position subsequences. The status word is then exactly two interleaved transversal-path conditions in these local tournaments. Pursue Hamilton-transversal, temporal-tournament, and global exchange arguments directly on this coupled system, with no minimum-counterexample hypothesis.

STEP-STREAM REDUCTION AND STEP-COMPATIBLE SWAPS.

For an alternating spanning order write alpha_i for the odd-position statuses and beta_i for the even-position statuses. Then the exact inversion-window criterion q<=p+1 is equivalent to:

  alpha=1^a 0^*,
  beta =1^b 0^*,
  |a-b|<=1.

Necessity: if either parity subword contains a 0 before a later 1, those full-word positions differ by at least two, forcing q>=p+2. If both parity words are step words, direct calculation gives p=min(2a+1,2b+2) and q=max(2a-1,2b), with endpoint conventions; q<=p+1 holds exactly for |a-b|<=1.

Thus the grand target in the alternating model is exactly two monotone tournament-transversal streams with aligned breakpoints.

ONE-STREAM BLOCK THEOREM (ASYMPTOTIC). On one side with r vertices and r mediator colors, choose any split of the mediators into large camps C,D. Reserve one bridge color and one spare color, leaving |C|-1 colors for the forward block and |D|-1 for the backward block. Partition the vertex side into sets U,W of sizes |C|,|D|. The tournament-transversal Hamilton-path theorem applied to the C-colors on U gives a directed rainbow Hamilton path; applied to the complements of the D-colors on W gives a directed rainbow Hamilton path. Concatenating the two vertex paths across the reserved bridge color produces a parity status stream 1^{|C|-1} * 0^{|D|-1}. Hence any chosen mediator bipartition can asymptotically be realized as a monotone stream with one arbitrary junction coordinate. The remaining difficulty is precisely coupling the opposite parity stream.

STEP-COMPATIBLE SWAP GADGETS. For a mediator pair b,b', a common agreement P3 x-z-y preserves the two A-status signs when b,b' are swapped. The common sign pair is:
- 11 (or 00 after reversal) when x->z->y is a common directed 2-path;
- 10 when z is a common sink;
- 01 when z is a common source.

Only 01 is incompatible with a monotone 1^*0^* stream. Therefore if a mediator pair has no monotone swap gadget, every agreement vertex of degree at least two must be a common source. The common-agreement digraph is consequently an outward-oriented star forest, with at most r-1 agreement arcs.

For r>=7, define the monotone-swap graph on mediator colors by joining pairs that admit a monotone agreement P3. Its complement is triangle-free: if c and d are both nonadjacent to b, then each agrees with b on at most r-1 arcs, so c and d agree on at least C(r,2)-2(r-1)>r-1 arcs. Their agreement digraph cannot be an outward star forest, so c,d admit a monotone swap gadget.

A stronger SIDE-SWAP gadget is a common directed 2-path. It can be oriented as 11 before the switch or reversed as 00 after the switch. If no side-swap gadget exists, the common-agreement digraph has no directed path of length two; hence every nonisolated vertex is purely a source or purely a sink and the agreement relation is an oriented bipartite graph. Thus failure of side-swappability again forces a cut/polarity structure rather than an arbitrary obstruction.
