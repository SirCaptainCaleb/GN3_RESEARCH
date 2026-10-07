# Every flat ternary blocking scan has a good replacement on one side of the switch

## Metadata

- ID: every_flat_ternary_blocking_scan_has_a_good_replacement_on_one_side_of_the_switch
- Parent Section: directed_nor_union_closed_bridge
- Position: 205
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development


Let alpha be coboundary-flat and alternating. Let

O=(v_1,...,v_m)

be a one-change ternary deletion carrier with word

0^p 1^q,

where p,q>=3, and let x be an exterior coordinate whose insertion into every gap of O is bad. Write

s_i=alpha(x,v_i,v_{i+1}).

No special blocker-scan form is assumed.

### Step 1: two insertion failures force a monotone five-bit scan core

Insert x immediately after v_p. The affected ternary packet is

(s_{p-1}, 1-s_p, s_{p+1}).

It is surrounded on the left by inherited 0-windows and on the right by inherited 1-windows. Hence this full insertion would be one-change exactly when the displayed packet is nondecreasing.

For binary bits, the triple

(a,1-b,c)

is nondecreasing exactly when the scan triple (a,b,c) is not one of

000,100,110,111? Equivalently, failure of monotonicity of (a,1-b,c) is exactly the condition

a>=b>=c.

Since the insertion is bad,

s_{p-1} >= s_p >= s_{p+1}.

Now insert x after v_{p+2}. The affected packet is

(s_{p+1},1-s_{p+2},s_{p+3}),

again between inherited 0- and 1-phases. Blocking gives

s_{p+1} >= s_{p+2} >= s_{p+3}.

Therefore

s_{p-1} >= s_p >= s_{p+1} >= s_{p+2} >= s_{p+3}.

So the five scan bits straddling the carrier switch are necessarily of the form 1^a0^(5-a).

### Step 2: one of two protected replacements is good

Coboundary flatness gives the replacement bridge formula

B_j=
(
s_{j-2},
1 xor s_{j-1} xor s_j xor w_{j-1},
s_{j+1}
),

for replacing v_j by x.

Case 1: s_{p+1}=1.

The monotone scan core then forces

s_{p-1}=s_p=s_{p+1}=1.

At j=p, since w_{p-1}=0,

B_p=
(
s_{p-2},
1 xor 1 xor 1,
1
)
=
(
s_{p-2},1,1
),

which is nondecreasing. Hence replacing v_p by x produces a genuine one-change deletion carrier.

Case 2: s_{p+1}=0.

The monotone scan core forces

s_{p+1}=s_{p+2}=s_{p+3}=0.

At j=p+3, since w_{p+2}=1,

B_{p+3}
=
(
0,
1 xor 0 xor 0 xor 1,
s_{p+4}
)
=
(
0,0,s_{p+4}
),

which is nondecreasing. Hence replacing v_{p+3} by x produces a genuine one-change deletion carrier.

If the resulting deletion word is monochromatic, appending its omitted coordinate already gives a full order with at most one change, so that case closes immediately.

### Consequence

The special scan 1^(p+1)0^q is unnecessary.

Every fully insertion-blocking scan over a coboundary-flat ternary one-change carrier with p,q>=3 admits a protected one-change replacement on one of the two sides of the switch:

- replace v_p if s_{p+1}=1;
- replace v_{p+3} if s_{p+1}=0.

The remaining global issue is termination: the first replacement shortens the 0-run by two or three, while the second shortens the 1-run by two or three. A closure proof now needs a finite potential or an exchange-cycle obstruction; blocker-scan uniqueness is no longer part of the frontier.


## Frontier

- Development version when composed: None
- Development version now: 1
