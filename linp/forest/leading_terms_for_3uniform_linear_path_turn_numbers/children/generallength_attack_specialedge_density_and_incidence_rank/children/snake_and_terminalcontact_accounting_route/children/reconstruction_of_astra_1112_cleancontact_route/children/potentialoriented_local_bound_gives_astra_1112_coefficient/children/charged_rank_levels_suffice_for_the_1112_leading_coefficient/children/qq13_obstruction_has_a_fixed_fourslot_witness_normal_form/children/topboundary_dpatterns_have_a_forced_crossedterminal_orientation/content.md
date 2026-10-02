# Top-boundary d-patterns have a forced crossed-terminal orientation

## Statement

Assume q>=4 in the all-visible top-boundary q,(q+1)^3 four-slot normal form, with low entrance x=g_{q-1}∩g_q and occupied high slots among a,b,c,d. If d=g_q∩g_{q+1} is occupied, then d is a high entrance, the low terminal u is absent from the entire left prefix, and the opposite terminal z_d lies on the left, by g_{q-3} whenever b is also occupied. Consequently every occupied triple containing d is crossed: in abd, z_d lies left while z_a,z_b lie right; in bcd, z_d lies left while z_b lies right; in acd, z_d and z_c lie strictly left while z_a lies strictly right.

## Body

A high witness at d is necessarily its unique entrance, so phi(d)=q. If the low terminal u appeared on the left, the path obtained by omitting the first edge and the central edge and splicing through the low edge would have length 2q-3 ending at d, exceeding phi(d); hence u is absent from the left prefix. The right-joint blocker localization then places z_d on the left, either at b or by g_{q-3}; if b itself is occupied the exceptional b-slot is forbidden by linearity. Existing left/right pressure for an occupied a-slot forces z_a into the right suffix, and the conflict-pair lemma for occupied b,d forces z_b right because z_d cannot simultaneously occur in the disjoint right suffix. In the acd pattern the sharper moat bounds force z_d,z_c farther left and z_a farther right. Thus every d-pattern is a crossed-terminal chord system.