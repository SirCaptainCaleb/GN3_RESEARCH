# Every ternary defect-vertex field has a defect-free Hamilton order

## Metadata

- ID: every_ternary_defect_vertex_field_has_a_defect_free_hamilton_order
- Parent Section: directed_nor_union_closed_bridge
- Position: 49
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

For any assignment marking at most one defect vertex on each unordered triple, there exists a Hamilton order with no consecutive triple whose middle vertex is marked. A left-to-right insertion proof propagates any obstruction strictly to the right until insertion succeeds. Applied to ternary NOR, the defect field can always be avoided along some Hamilton order.

## Development

Let d assign to each unordered triple either no marked vertex or one of its three vertices. Then there is a Hamilton order v1,...,vn such that no consecutive triple has its middle vertex marked. Proof is by insertion. Assume v1,...,vm already has this property and insert a new x. If d({x,v1,v2}) is not v1, prepend x. Otherwise d({x,v1,v2})=v1. More generally, suppose d({x,v_k,v_{k+1}})=v_k. Try inserting x between v_k and v_{k+1}. The preceding new triple, when present, is safe because the previous propagation step marked v_{k-1}, not its middle v_k; the middle new triple is safe because its middle is x while the marked vertex is v_k. Thus the only possible failure is the next triple (x,v_{k+1},v_{k+2}), and failure forces d({x,v_{k+1},v_{k+2}})=v_{k+1}. The obstruction therefore marches strictly right. At the last gap there is no next triple, so insertion succeeds. Applying this to the defect field in the triangle-orientation decomposition of ternary NOR gives a Hamilton order on which every consecutive window has epsilon=alpha: none of the middle-vertex defect flips occur. Hence the defect field can never by itself obstruct NOR; the residual problem is the alternating orientation alpha on simplex triangles.
