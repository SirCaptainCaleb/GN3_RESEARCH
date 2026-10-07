# Exterior vertex absorption into a four change carrier

## Metadata

- ID: exterior_vertex_absorption_into_a_four_change_carrier
- Parent Section: directed_nor_union_closed_bridge
- Position: 38
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Let U be a ternary front circuit at tail F in color tau, let x in U, and let W_x be a tau-tight facet witness for U minus x. The blocked x together with W_x and the maximal sigma-tight core P gives the canonical four-change carrier on V(P) union U. For any exterior y outside U, maximality of P gives h(y,F)=tau. Scan y through W_x by s_i=h(y,w_i,w_{i+1}). Since the final scan value is tau, either y inserts somewhere while preserving tau-tightness, in which case the four-change carrier grows by y without increasing variation; or at the first sigma-to-tau transition one gets a shifted two-circuit if h(a,y,b)=sigma; or insertion succeeds locally but is stopped one window earlier, where h(p,a,y)=sigma. In that last case h(y,a,b)=sigma and reversal of the old tau window h(p,a,b)=tau gives h(b,a,p)=sigma, so p,y,b form a directed triangle in the color-sigma center tournament at a. Thus every failed exterior absorption has a local certificate: a shifted two-circuit or a centered directed triangle. A carrier maximal under variation-preserving absorption therefore forces such a certificate for every exterior vertex.

## Frontier

- Development version when composed: None
- Development version now: 1
