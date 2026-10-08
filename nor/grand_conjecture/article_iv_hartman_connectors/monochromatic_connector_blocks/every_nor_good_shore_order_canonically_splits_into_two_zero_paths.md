# Every NOR-good shore order canonically splits into two zero paths

## Composition

A bichromatic good shore order splits into a zero prefix and a reversed zero suffix covering the entire shore. These paths need not have compatible exposed pairs. The three switch-adjacent cuts elevate the construction; the remaining problem is port repair and compatible gluing.

## Development


Let O=(a_1,...,a_k) be a NOR-good order of the shore A, normalized so its ternary word is
0^p 1^q,
with p+q=k-2 and p,q>=1.

Define two disjoint ordered paths
P=(a_1,...,a_{p+1})
and
Q=(a_k,a_{k-1},...,a_{p+2}).

They partition A.

Every ternary window internal to P is one of the original windows of ranks 1,...,p-1, hence has color zero.

Every ternary window internal to Q is the reversal of an original window whose rank is at least p+2, hence lies in the old one-phase. Reversal complements ternary color, so all internal windows of Q have color zero.

Thus every bichromatic NOR-good shore order canonically yields a two-zero-path cover of the entire shore. If one phase has length one, the corresponding path has only two vertices and the assertion is vacuous there.

The only discarded information is concentrated in the two switch-straddling windows of O. Consequently the whole-shore connector problem is not existence of a two-zero-path cover: such a cover is automatic by minimum-counterexample induction. The remaining obligation is to modify or glue the two paths so that the resulting monochromatic connector has compatible exposed endpoint pairs.

This reduction remains valid whether x and z are adjacent or move independently. Independent motion enlarges the set of allowable gluing repairs, but the path-cover itself is already supplied canonically.
