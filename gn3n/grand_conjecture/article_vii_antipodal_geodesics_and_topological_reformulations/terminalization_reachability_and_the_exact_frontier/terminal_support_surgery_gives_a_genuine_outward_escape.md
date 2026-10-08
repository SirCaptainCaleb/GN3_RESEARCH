# Terminal support surgery gives a genuine outward escape

## Composition

(none yet)

## Development


### Terminal support surgery gives a genuine outward escape

The previously recorded extension concern can be removed once the terminal support is taken to be the full positional span of the centered or overlapping reflected determining windows.

Let (e_i) be the current innermost selected witness edge. In the terminal branch, the dual-polarity classification leaves only a centered witness or overlapping reflected witnesses. Let (I) be the contiguous interval of vertex positions from the leftmost vertex used by those determining windows to the rightmost one. The finite classification gives
[
|I|le 10
]
and the induced boundary tournament (H[I]) has path-cover number at most two.

Choose a two-cover
[
Pmid Q
]
of (H[I]), and replace the old order on the positions of (I) by
[
P,Q^{m rev}.
]
By the exact forbidden-pattern theorem, the resulting internal status word on (I) contains none of
[
001,qquad 011,qquad 0101.
]

**Lemma (outward local replacement).** In the modified spanning order, no selected witness edge (e_j) with (jle i) occurs. Hence either the modified order is already a spanning two-cover, or its selected witness edge is strictly farther outward than (e_i).

**Proof.** The witness-path order is by distance from the status-word center. Every determining window belonging to (e_i), and every determining window belonging to an edge (e_j) closer to the center, is contained in the positional span (I): for the terminal centered case this is immediate, and for the overlapping reflected case (I) contains the full interval between the two reflected windows, so every more central reflected pair lies inside it.

After replacement, every forbidden-pattern occurrence whose determining window is contained in (I) is absent, because (P,Q^{m rev}) is a two-cover order of the induced subtournament on (I). Thus no witness (e_j) with (jle i) survives internally.

Only triple-status coordinates meeting one of the two ends of (I) can change outside the internal word. Any forbidden-pattern window using such a coordinate extends beyond the leftmost or rightmost determining position of (e_i). By construction of the fixed witness path, such a window represents an edge strictly farther outward than (e_i). Therefore boundary effects cannot recreate (e_i) or any closer edge. (square)

This is exactly the global extension clause missing from the induced-support theorem. The local finite theorem need not produce a spanning two-cover of (H); it only needs to produce a two-cover of the terminal central span. Replacing that span either closes the theorem immediately or creates an honest chamber whose selected witness has moved strictly outward.

Consequently the remaining terminalization problem is no longer finite-support extension. It is purely the topological promotion problem: use these outward replacement chambers to repair every mixed (+e_i/-e_i) crossing in the relative-index separator, so that the (e_i)-free separator retains index and the recursion can continue.
