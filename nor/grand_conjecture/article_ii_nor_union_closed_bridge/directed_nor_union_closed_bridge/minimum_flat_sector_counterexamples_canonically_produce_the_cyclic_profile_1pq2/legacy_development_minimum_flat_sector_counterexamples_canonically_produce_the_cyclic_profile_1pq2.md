# Minimum flat-sector counterexamples canonically produce the cyclic profile 1,p,q,2 — preserved pre-item development

## Composition

(none yet)

## Development


Assume a minimum ternary counterexample in the coboundary-flat pure-orientation sector.

By the threshold-defect-one theorem there is a full linear order

(x,v_1,...,v_m)

whose ternary word, after complementing colors if necessary, is

1, 0^p, 1^q

with p,q>=2.

Deleting x leaves the one-change carrier

O=(v_1,...,v_m)

with word 0^p1^q. Since the full instance is a counterexample, x cannot be inserted anywhere into O to produce a one-change order. Therefore x has the unique perfect-blocker scan

s_i=alpha(x,v_i,v_{i+1})=1^(p+1)0^q.

In particular,

alpha(x,v_{m-1},v_m)=0.

By cyclic invariance,

alpha(v_{m-1},v_m,x)=0.

Now regard the full coordinate order cyclically. Besides its n-2 linear windows, there are two wrap windows. The first wrap window just computed is 0. Put

r=alpha(v_m,x,v_1)

for the final wrap window.

If r=1, the cyclic status word is

1,0^p,1^q,0,1.

Across the cyclic boundary the final 1 joins the initial 1, so the cyclic word has only two changes. Cutting the cyclic order at either transition gives a spanning linear order with at most one change, contradicting counterexamplehood.

Hence r=0.

Therefore every minimum flat-sector counterexample has a canonical full-support cyclic order with run profile

1,p,q,2.

Moreover:
- the transition from the initial singleton 1-run into the p-run is fully curved, by the perfect-blocker endpoint theorem;
- the transition from the final length-two 0-run into the initial singleton 1-run cannot be fully curved, because the fully-curved 2-to-1 corner theorem would lower cyclic variation from four to two.

Since the sector is coboundary-flat, that wrap 2|1 transition is therefore flat.

Thus a minimum counterexample witness carries a canonical asymmetric four-change carrier: one endpoint barrier is forced full and the opposite 2|1 corner is forced flat.
