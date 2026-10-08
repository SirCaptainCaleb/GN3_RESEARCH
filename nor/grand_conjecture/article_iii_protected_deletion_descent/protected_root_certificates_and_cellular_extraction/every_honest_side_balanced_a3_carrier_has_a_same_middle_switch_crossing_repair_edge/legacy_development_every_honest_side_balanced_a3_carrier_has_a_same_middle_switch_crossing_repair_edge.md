# Every honest side-balanced A3 carrier has a same-middle switch-crossing repair edge — preserved pre-item development

## Composition

(none yet)

## Development

Let an honest side-lifted switch-prism zero be supported in one exact ternary A3 Coxeter block B of four consecutive coordinates. Because its lifted scalar coordinate is side-balanced, the support contains both pre-switch and post-switch internal labels. Therefore the switch lies between the two internal ternary-window ranks of B.

Normalize the target to 0 on the pre side and 1 on the post side.

Take any pre-side violating internal label. Its chamber order on B is necessarily
(u,m,v,z),
where the first internal window (u,m,v) is the selected violation and m is its tracked middle coordinate. Hence
alpha(u,m,v)=1.

Perform the genuine adjacent transposition m<->v:
(u,m,v,z) -> (u,v,m,z).

The first new internal window is
(u,v,m),
whose color is 0 by alternation. It therefore matches the pre-switch target.

Put
q=alpha(m,v,z),
the color of the OLD second internal window. The new second internal window is
(v,m,z),
whose color is 1-q by alternation.

There are exactly two cases.

1. q=0.
Before the swap, the first internal window is a pre defect and the second internal window has color 0 against post target 1, so it is also a defect. Thus the old central defect pattern is 11.
After the swap, the first new window has color 0 on the pre side and the second has color 1 on the post side. Both are matched. The central defect pattern becomes 00. Hence the swap removes two central threshold defects. Only the two exterior windows of the adjacent transposition remain to be audited, exactly as in the established controlled-repair framework.

2. q=1.
Before the swap, the selected first window is the only central defect. After the swap, the first window is matched, while the second new window has color 0 on the post side and is therefore a violation. The SAME physical middle coordinate m has moved from the pre internal rank to the post internal rank. Thus the edge carries the exact complementary signed-middle pair
+m, -m.
The signed-middle Tucker edge theorem applies and gives the canonical switch-crossing repair event.

The argument is completely local to the actual adjacent edge and never changes the tracked middle coordinate. It therefore repairs the gap identified in the alternate-middle A3 audit.

The post-side version is the reversal of the same calculation.

Consequently every side-balanced honest lifted zero supported in one exact A3 block contains a controlled local repair edge: choose any label from either side and apply the corresponding middle-across-switch swap. No classification into two-cycles, triangles, four-cycles, or crossed-diagonal residues is required for carrier-to-local-event extraction.

This does NOT by itself close the full instance: in the q=0 branch the two exterior windows may export up to two defects, and in the complementary branch the established Tucker repair still hands outer-window compatibility to the transport machinery. But the A3 TOPOLOGICAL extraction problem is complete at the cell level. Any remaining obstruction after a forced lifted zero lies in gluing/termination of the exported boundary defects, not in A3 root-circuit algebra.
