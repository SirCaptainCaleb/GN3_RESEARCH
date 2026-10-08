# Four-root directed cycles admit a two-stage middle-swap descent

## Composition

(none yet)

## Development

## Four-root directed cycles admit a two-stage middle-swap descent

Work in the pure alternating ternary sector inside one ordered-partition carrier cell.

Let a support-minimal positive dependence have four roots. For type-A roots this is a simple directed four-cycle
rho1=e_a-e_b,
rho2=e_b-e_c,
rho3=e_c-e_d,
rho4=e_d-e_a,
on S={a,b,c,d}.

As in the earlier two- and three-root analyses, all four physical coordinates lie in one tied carrier block, and the middle coordinates of every certified 10 packet lie in that same tied block. Hence the middle swaps below stay inside the carrier cell.

Take a chamber carrying rho=e_a-e_b on a certified 10 packet
(a,u,v,b),
and write a surrounding segment as
...,T,R,a,u,v,b,S1,Z,...

Swap u,v. The central colors become 0,1.

The only new 10 transitions that can be created in the affected neighborhood have physical endpoint pairs
{T,v}, {R,u}, {v,S1}, {u,Z}.
Every one avoids a,b.

Therefore an affected replacement root can remain in the A3 subsystem on S only if its two endpoints are exactly the complementary pair {c,d}. Since c and d each occur once in the coordinate order, at most one of these four pairs can equal {c,d}.

So after the first swap there are three possibilities:
1. a new 10 root has an endpoint outside S; then it gives a root transverse to the four-cycle span and supplies the same local carrier deformation used in the three-root theorem;
2. the only S-internal replacement has orientation d->c; together with the witnessed c->d root elsewhere in the same cell this gives the removable opposite-pair case;
3. the only essential recycle is a single forward c->d root.

All other 10 transitions are unchanged, so the total number N10 of 10 transitions never increases.

Now assume case 3. The recycled c->d packet can occur in exactly one of four overlap positions:

A. endpoints {R,u}, packet (R,a,v,u);
B. endpoints {T,v}, packet (T,R,a,v);
C. endpoints {v,S1}, packet (v,u,b,S1);
D. endpoints {u,Z}, packet (u,b,S1,Z).

In A and B, a is trapped as one of the two middle/nearby original coordinates while b lies on the same external side beyond the packet. In C and D the symmetric statement holds with b.

Perform the middle swap of this recycled c->d packet. Every newly affected transition root avoids c,d and pairs one packet-middle coordinate with one exterior coordinate. In cases A and B, every possible pair containing a has its other endpoint outside S, and every other possible pair already contains an endpoint outside S. In cases C and D the same holds with b.

Hence after the SECOND swap no newly created affected 10 root can have both endpoints in S.

Therefore the second swap either exposes a transverse root, giving the local carrier deformation, or genuinely deletes the recycled 10 transition without creating another S-internal one.

Thus every one or two middle-swap stages either resolve the four-root dependence locally or strictly decrease N10.

Iterating is finite. If local resolution never occurs, eventually N10=0. A binary linear word with no 10 occurrence has the form 0^r1^s, allowing either run to be empty, so the terminal chamber is a spanning NOR-good order. Contradiction.

Therefore every support-minimal four-root positive dependence of actual protected ternary window-slide roots in one carrier cell is locally removable.

Together with the earlier support-two and support-three theorems, any essential local carrier zero in the pure ternary protected-root construction must have support at least five.

The geometric mechanism is useful in its own right: a four-cycle root may recycle once to the complementary edge of the A3 cycle, but the overlap created by that first recycle prevents a second in-subsystem recycle.
