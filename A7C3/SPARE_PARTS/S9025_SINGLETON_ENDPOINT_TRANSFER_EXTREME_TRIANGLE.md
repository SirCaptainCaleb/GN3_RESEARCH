# S9025 — Singleton Endpoint Transfer Forces an Extreme Carrier-Triangle Edge

## Theorem

Let G be a finite edge-ordered complete graph with pc_inc(G)>2. A SOURCE TRANSFER for singleton pair {x,y} at carrier neighbor v means there are literal spanning three-covers A | (y,v,b_2,...,b_m) | {x} and A | (x,v,b_2,...,b_m) | {y}, with the obvious order-two interpretation when no b_2 exists. Then lambda(vx)<lambda(xy) and lambda(vy)<lambda(xy), so xy is the unique maximum edge of triangle {x,y,v}. Dually, a TERMINAL TRANSFER at carrier neighbor w means there are literal spanning three-covers A | (...,w,y) | {x} and A | (...,w,x) | {y}; then lambda(xy)<lambda(wx) and lambda(xy)<lambda(wy), so xy is the unique minimum edge of {x,y,w}. If the same unordered singleton pair {x,y} occurs in both a source transfer with carrier v and a terminal transfer with carrier w, where v,w are distinct from x,y, then lambda(vx),lambda(vy) < lambda(xy) < lambda(wx),lambda(wy). Consequently both (v,x,y,w) and (v,y,x,w) are increasing Hamilton P4 orders.

## Proof

For the source transfer, retain literal covers A | (y,v,b_2,...,b_m) | {x} and A | (x,v,b_2,...,b_m) | {y}. Since the second rail in each cover is increasing, lambda(yv)<lambda(vb_2) and lambda(xv)<lambda(vb_2) when b_2 exists; only the first edge matters below. If lambda(xy)<lambda(yv), then (x,y,v,b_2,...,b_m) is increasing, and together with A it two-covers G. If lambda(xy)<lambda(xv), then (y,x,v,b_2,...,b_m) is increasing and again A gives a two-cover. In a graph with pc_inc(G)>2 both conclusions are impossible. Hence lambda(xy)>lambda(yv) and lambda(xy)>lambda(xv), so xy is the unique maximum edge of {x,y,v}. The order-two carrier case is identical with the tail after v absent.

For the terminal transfer, retain A | (...,v,y) | {x} and A | (...,v,x) | {y}. If lambda(vy)<lambda(xy), appending x to the first rail gives (...,v,y,x), while if lambda(vx)<lambda(xy), appending y to the second gives (...,v,x,y). Either would two-cover G with A. Therefore pc_inc(G)>2 forces lambda(xy)<lambda(vy) and lambda(xy)<lambda(vx), making xy the unique minimum edge of the carrier triangle.

Now suppose the same singleton pair {x,y} appears in a source transfer with carrier v and a terminal transfer with carrier w. The source conclusion gives lambda(vx)<lambda(xy) and lambda(vy)<lambda(xy). The terminal conclusion gives lambda(xy)<lambda(wx) and lambda(xy)<lambda(wy). Hence lambda(vx)<lambda(xy)<lambda(yw), so (v,x,y,w) is increasing; and lambda(vy)<lambda(xy)<lambda(xw), so (v,y,x,w) is increasing. These are two explicit Hamilton P4 orders on {v,x,y,w}. No synchronization of the underlying transfer covers is needed beyond the graph-intrinsic edge inequalities.

## Why this is reusable

Repeated singleton transfers turn failed two-cover closures into sharp edge-order information: the singleton edge is forced to be the unique maximum or minimum of a carrier triangle, and opposite polarities compile directly to two increasing P4 orders.

## Scope and nonclaims

The theorem does not force a repeated transfer to occur and does not by itself absorb the resulting P4 complement.

## Provenance

Rescued from accepted archived result `R992`.
