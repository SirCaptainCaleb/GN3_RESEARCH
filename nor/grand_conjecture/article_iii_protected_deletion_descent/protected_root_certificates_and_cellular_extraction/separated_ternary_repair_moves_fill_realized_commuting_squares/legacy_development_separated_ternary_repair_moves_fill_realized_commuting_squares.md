# Separated ternary repair moves fill realized commuting squares — preserved pre-item development

## Development

## Separated ternary repair moves fill realized commuting squares

Work in the alternating ternary repair graph on full coordinate orders. An adjacent transposition at bond i swaps the coordinates in positions i,i+1.

For ternary window labels, such a swap can change only the four window ranks

i-2, i-1, i, i+1

after clipping at global endpoints. Call this its influence interval.

Suppose two legal repair moves occur at bonds i and j with

|i-j|>=4.

Then their influence intervals are disjoint.

### Theorem

The two repairs commute as actual coordinate permutations, and each remains a legal repair after performing the other. Hence the four full coordinate orders obtained by applying neither move, either move, or both moves form an honest realized commuting square in the repair-state complex.

### Proof

Adjacent transpositions on disjoint bonds commute as permutations.

Because |i-j|>=4, no ternary window whose status can be changed by the i-move has a start rank that can be changed by the j-move, and conversely. Therefore every local status/curvature condition used to certify legality of the i-repair is unchanged by the j-repair. The same holds symmetrically.

Thus both two-step orders are legal and end at the same full coordinate order.

### Locality consequence

Any first branching/rejoining failure that is not filled by a commuting square must involve repair bonds at distance at most three.

For ternary arity, the union of the two influence packets is then contained in at most nine consecutive coordinate positions: if j=i+3, the affected windows range from start i-2 through i+4, whose union uses positions i-2 through i+6.

Hence every noncubical gluing obstruction of two elementary ternary repair moves is supported on a bounded at-most-nine-coordinate packet.

This is not a small-order cutoff: the ambient coordinate set is arbitrary and all outside coordinates remain in their original order.

### Topological consequence

Combined with:
- zero-freeness of every one-sided transport flag;
- the exact flat-repair square and its two-bit Sperner chart;

the global compatible-state topology can fail to be cubically filled only in bounded overlapping packets. The next genuinely new cells are therefore overlapping-swap / braid-type residues, not long-range interactions of distant repairs.

A global fixed-point carrier may safely fill all separated branchings by these realized squares and reserve explicit extraction only for the bounded overlap cells.
