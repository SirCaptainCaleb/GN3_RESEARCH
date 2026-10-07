# Audit: protected-front wedges in exterior absorption

## Metadata

- ID: audit_protected_front_wedges_in_exterior_absorption
- Parent Section: directed_nor_union_closed_bridge
- Position: 41
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Audit correction for exterior absorption. Let a canonical ternary carrier begin (x,w1,w2,...) with h(x,w1,w2)=sigma and with W=(w1,w2,...) tau-tight. For an exterior y, scan s_i=h(y,w_i,w_{i+1}) toward the terminal pair, where the final scan value is tau. At an internal first sigma-to-tau transition, failure to insert y is exactly the previously found dichotomy: a shifted two-circuit or a centered directed triangle. At the protected first transition i=1 there is one additional case because insertion changes the unique blocked carrier window. Writing t=h(w1,y,w2) and u=h(x,w1,y), the enlarged carrier has no extra change unless (u,t,tau)=(tau,sigma,tau). In that exceptional case the color-sigma center tournament at w1 has the transitive wedge y->x->w2 together with y->w2. Thus maximal carrier support forces each unabsorbed exterior vertex to certify one of three types: shifted two-circuit, centered directed triangle, or protected-front transitive wedge. The earlier absorption note omitted the wedge case.

## Frontier

- Development version when composed: None
- Development version now: 1
