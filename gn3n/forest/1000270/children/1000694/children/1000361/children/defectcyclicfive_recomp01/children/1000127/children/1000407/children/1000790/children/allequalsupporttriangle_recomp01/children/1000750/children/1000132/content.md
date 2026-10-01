# Adjacent barrier families force three cyclic mixed four-paths

## Statement

Assume case (3), the synchronized endpoint-barrier branch, of e5d3ccfef9bb. Then for every i modulo three the ordered four-tuple (b_i,t_i,t_{i+2},a_{i+1}) is a tight path. Hence the barrier residue contains the cyclic family Q_i=(b_i,t_i,t_{i+2},a_{i+1}), i=1,2,3, whose pairwise overlaps are exactly transferred labels.

## Body

Fix i. Since t_{i+2} is the initial endpoint of A_{i+2}, it belongs to E_i. The initial barrier family from e5d3ccfef9bb therefore gives (b_i,t_i,t_{i+2}) tight. Next, t_i is the initial endpoint of A_i, hence t_i belongs to E_{i+1}. The terminal barrier family for support S_{i+1} gives (t_i,t_{i+2},a_{i+1}) tight. These are exactly the two consecutive triples of the ordered four-tuple (b_i,t_i,t_{i+2},a_{i+1}), so it is a tight path. No rotation or reversal of an ordered tight triple is used. Apply cyclically.