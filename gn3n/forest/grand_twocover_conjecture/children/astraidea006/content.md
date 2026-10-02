# Contiguous block moves escape every three-path plateau

## Statement

For a vertex ordering pi of a boundary tournament, let c(pi) be the minimum number of contiguous tight subpaths partitioning pi. If c(pi)=3, then some finite sequence of contiguous block relocations, each preserving c<=3, reaches an ordering with c<=2.

## Body

Unproved conjecture. A relocation removes one nonempty interval of the current ordering and reinserts it in another gap without reversing its internal order. Unlike bounded support exchange, the moved interval may be arbitrarily long. The candidate asks for connectivity across equal-value plateaus, not strict improvement after each move. Starting from a deletion two-cover plus its omitted singleton would suffice for the grand theorem. Attack: characterize a connected component of the sublevel set c<=3 closed under all relocations. Missing outgoing moves impose tightness restrictions at a small number of boundaries, but many overlapping relocations may force a global contradiction. Main risk: the landscape may have genuine barriers requiring four components temporarily. If so, replace the bound three by four and seek a controlled return argument; that relaxation is not asserted here. No local-minimum or termination theorem has been proved.