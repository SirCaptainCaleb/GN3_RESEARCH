# Why geodesicity is essential

## Metadata

- ID: lifted_geodesic_graph_and_one_change_orders_subsection_d
- Parent Section: lifted_geodesic_graph_and_one_change_orders
- Position: 4
- Row version: 3
- Development version: 3
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

For any \(s\)-\(t\) walk \(W\), let \(m_v\) be the number of times its projection uses cube coordinate \(v\). Since the projection joins antipodal cube vertices, every \(m_v\) is odd and
\[
|W|=\sum_{v\in V}m_v
=n+2\sum_{v\in V}\frac{m_v-1}{2}.
\]
Thus the geodesics are exactly the walks with \(m_v=1\) for every \(v\).

This is the key constraint behind the analogy with antipodal path theorems. A theorem producing some one-change antipodal walk is insufficient if it allows repeated coordinates; repetition means repeated original vertices. Likewise, an antipodal theorem whose endpoint pair is allowed to vary is insufficient unless its output can be normalized to the distinguished poles \(s,t\). The desired topology must preserve both pole location and zero detour.
