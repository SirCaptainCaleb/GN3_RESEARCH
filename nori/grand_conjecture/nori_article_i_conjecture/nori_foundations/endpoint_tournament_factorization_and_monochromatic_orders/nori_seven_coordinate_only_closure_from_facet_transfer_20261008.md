# Full seven-direction coordinate-only closure from monochromatic facet transfer

Let h be a binary coloring of ordered triples of distinct directions in a seven-element set V, with h(c,b,a)=1-h(a,b,c).

**Theorem.** Some permutation of V has at most one color change in its five consecutive triple labels. Thus the NORI grand conjecture holds in dimension seven for the coordinate-only reversal-odd subclass.

**Proof.** The six-direction monochromatic-facet theorem (Item nori_six_direction_monochromatic_facet_transfer_20261008) supplies five distinct directions a,b,c,d,e with h(abc)=h(bcd)=h(cde). Name the two remaining directions f,g and complement all colors to make those three labels 0.

Suppose every seven-direction permutation has at least two changes. For a permutation p_1...p_7, write W(p)=(h(p_1p_2p_3),...,h(p_5p_6p_7)). A question mark denotes a value not yet determined. Reversal gives h(cba)=1-h(abc); because the coloring is coordinate-only, each previously determined ordered triple has the same value whenever it reappears.

Read the following table from top to bottom. The middle column uses only the seed, reversal, and earlier rows. The right column follows from the requirement that W have at least two changes.

| permutation | known word | forced word |
|---|---|---|
| abcdefg | 000?? | 00010 |
| edcbafg | 111?? | 11101 |
| edcbagf | 111?? | 11101 |
| bcdagfe | 0??11 | 01011 |
| dcbaefg | 11??0 | 11010 |
| abcdegf | 000?? | 00010 |
| afgbcde | 1??00 | 10100 |
| bcdeagf | 00??1 | 00101 |
| cbgaefd | 0?11? | 0?110 |
| cbgadfe | 0?1?1 | 0?101 |
| abcdfge | 00??1 | 00101 |
| ecbadfg | ?1?00 | 01?00 |

Every forcing pattern follows directly from counting adjacent unequal pairs. The pattern 000?? has two changes only when the final two bits are 10; complementation handles 111??. The patterns 0??11 and 1??00 force 01011 and 10100. The patterns 11??0 and 00??1 force 11010 and 00101. In 0?11?, the last bit must be 0; in 0?1?1, the fourth bit must be 0; in ?1?00, the first bit must be 0. Each contrary bit leaves at most one change, for either value of the other unknown bit.

Finally, for the permutation adfgbce, the labels are
h(adf)=0,
h(dfg)=0,
h(fgb)=1-h(bgf)=0,
h(gbc)=1-h(cbg)=1,
h(bce)=1.
These come respectively from row 10, row 11, row 7, row 7, and row 12. Therefore W(adfgbce)=00011, with exactly one change. This contradicts the supposition. QED.

**Scope.** This is full seven-coordinate closure for coordinate-only reversal-odd labels. General ordered-three-face NORI in dimension seven allows exterior-bit dependence. Occurrences of the same ordered triple can then have different exterior assignments. Extending this table requires compatible face assignments or another justified transport argument. The six-direction monochromatic-facet theorem and this certificate establish transfer to a different omitted-coordinate facet.

**Verification.** Every row was checked sequentially against all 32 binary five-window words satisfying its known entries and having at least two changes. Every forced entry held in all remaining words, and the final word was checked against the accumulated assignments. The proof is the explicit certificate above.
