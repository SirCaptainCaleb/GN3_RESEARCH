# Audit simultaneous defect free one change insertion is false

## Metadata

- ID: audit_simultaneous_defect_free_one_change_insertion_is_false
- Parent Section: directed_nor_union_closed_bridge
- Position: 55
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

The local insertion statement proposed after the exact alpha-plus-defect calculus is false. Take a defect-free old order (v1,v2,v3,v4,v5) whose alpha status word is 0,1,1. Add x. On every triangle {x,vi,v{i+1}} mark vi as the defect vertex (type L). Then prepending x is unsafe, and every interior gap before the last is unsafe because the next new triple has its middle vertex marked. The only defect-safe placements are between v4 and v5 and after v5. Choose the orientation scan values s3=alpha(x,v3,v4)=0 and s4=alpha(x,v4,v5)=0. At the last interior gap the old final status 1 is replaced by (s3,1-s4)=(0,1), so the full word becomes 0,1,0,1 and has more than one change. Appending x adds status s4=0 to 0,1,1, again creating a second change. Since alpha orientations and defect marks on distinct triangles are independent in the triangle-orientation-plus-defect encoding, these local data are realizable. Thus one cannot inductively preserve both defect-freeness and at most one alpha change by inserting each new vertex into an arbitrary existing good order. This is only an obstruction to that proof method, not a NOR counterexample; another global order may still work.

## Frontier

- Development version when composed: None
- Development version now: 1
