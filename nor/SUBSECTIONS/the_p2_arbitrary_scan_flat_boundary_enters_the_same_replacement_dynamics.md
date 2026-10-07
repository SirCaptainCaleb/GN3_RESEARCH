# The p=2 arbitrary-scan flat boundary enters the same replacement dynamics

## Metadata

- ID: the_p2_arbitrary_scan_flat_boundary_enters_the_same_replacement_dynamics
- Parent Section: directed_nor_union_closed_bridge
- Position: 218
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Arbitrary-scan boundary lemma for the corrected flat ternary dynamics. Let O have word 00 1^q with q>=2 in a minimum coboundary-flat ternary counterexample, and let x be the omitted coordinate with scan s_i=alpha(x,v_i,v_{i+1}). Failure of prepend forces s_1=1. Failure of insertion after v_1 then forces s_2=1, since otherwise the full word begins 000 and then enters the old 1-run. If s_3=1, replacing v_2 by x gives a monochromatic deletion carrier: flatness on {x,v_1,v_2,v_3} gives alpha(x,v_1,v_3)=s_1 xor w_1 xor s_2=0, hence alpha(v_1,x,v_3)=1, followed by s_3=1 and the untouched old 1-suffix. Appending the new omitted vertex would then give a full order with at most one change, contradiction. Therefore s_3=0. Failure of insertion after v_3 forces s_4=0, because the local word is 0,1,1,s_4,1... and is one-change when s_4=1. Failure of insertion after v_4 forces s_5=0; with s_3=s_4=0 its local word is 0,0,0,1,s_5 followed by only 1s, so s_5=1 would be one-change. Thus every surviving scan begins 11000. Now replace v_5 by x. The flat bridge formula gives the new crossing packet (s_3, 1 xor s_4 xor s_5 xor w_4, s_6)=(0,0,s_6), with the final term omitted when the carrier ends there. Hence the new deletion carrier is one-change. If s_6=1 its run profile is (4,q-2); if s_6=0 it is (5,q-3). For q=2 the packet is truncated and the new carrier is monochromatic, closing NOR. For q=3 the new second run has length at most one, which cannot be perfectly blocked. Thus p=2 is not an exceptional obstruction: it either closes immediately or enters the same protected distance-2/distance-3 replacement dynamics as the p,q>=3 case. By reversal the same holds for q=2.

## Frontier

- Development version when composed: None
- Development version now: 1
