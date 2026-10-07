# Protected switch insertion reduces to one two-bit holonomy class

## Metadata

- ID: protected_switch_insertion_reduces_to_one_two_bit_holonomy_class
- Parent Section: directed_nor_union_closed_bridge
- Position: 196
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development


Work in a minimum coboundary-flat ternary counterexample with a deletion carrier

O=(v_1,...,v_m)

of word 0^p1^q, p,q>=3, and omitted perfect blocker x with scan 1^{p+1}0^q.

Insert x at the deletion-order switch:

F=(v_1,...,v_p,x,v_{p+1},...,v_m).

Put

r=v_{p-3}, a=v_{p-2}, b=v_{p-1}, c=v_p, e=v_{p+1}.

The five consecutive coordinates (a,b,c,x,e) have status pattern

0,1,0.

The two transition tetrahedra

{x,a,b,c}=Q_{p-2},
{x,b,c,e}=Q_{p-1}

are fully curved. The next window is

alpha(x,e,v_{p+2})=1,

so relative to the threshold target with cut immediately after the displayed final 0, F has exactly one defect, namely the middle 1.

Let t be the residual bit of the double-full five-set. In the normalization above,

alpha(a,b,e)=alpha(a,c,e)=alpha(a,x,e)=t.

The preceding deletion tetrahedron {r,a,b,c} has consecutive statuses 0,0 and is therefore flat. Its two cross faces coincide; put

u=alpha(r,a,c)=alpha(r,b,c).

We seek a surgery which preserves the ordered right boundary pair (x,e), so every window from alpha(x,e,v_{p+2}) onward remains unchanged.

### Case u=1

Replace

(a,b,c,x,e)

by

(c,a,b,x,e).

Its three internal statuses are

alpha(c,a,b)=0,
alpha(a,b,x)=1,
alpha(b,x,e)=1.

The first equality is cyclic invariance from alpha(a,b,c)=0. The other two are forced by the two fully-curved tetrahedra.

The immediate left reconnection is

alpha(r,c,a)=1-alpha(r,a,c)=0

because u=1.

Thus every window from this immediate reconnection rightward agrees with the one-change target. The ordered pair (x,e) is unchanged, so the entire matched suffix is protected. Only the next farther-left window, involving the coordinate preceding r, can have changed. Consequently the old defect is removed and at most one defect is exported strictly leftward.

### Case u=0 and t=1

Replace

(a,b,c,x,e)

by

(b,c,a,x,e).

Its internal statuses are

alpha(b,c,a)=0,
alpha(c,a,x)=1,
alpha(a,x,e)=t=1.

The immediate left reconnection is

alpha(r,b,c)=u=0.

Again the ordered right boundary pair (x,e) is unchanged. Hence every window from the immediate left reconnection through the entire right suffix matches the target; at most the single next farther-left window can become defective.

### Residual class

Therefore every protected switch insertion admits a full-support suffix-preserving improvement except possibly when

u=0 and t=0.

In the two resolved classes, either NOR closes outright or the unique threshold defect is transported strictly left while the same ordered suffix pair is protected.

The protected endpoint-surgery problem has thus been reduced to one local two-bit holonomy class, u=t=0.

This reduction uses both outer packets explicitly and does not invoke the audited singleton-shift iteration.


## Frontier

- Development version when composed: None
- Development version now: 1
