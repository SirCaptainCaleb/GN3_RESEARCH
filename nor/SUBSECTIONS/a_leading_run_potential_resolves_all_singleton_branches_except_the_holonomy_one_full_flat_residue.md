# A leading-run potential resolves all singleton branches except the holonomy-one full-flat residue

## Metadata

- ID: a_leading_run_potential_resolves_all_singleton_branches_except_the_holonomy_one_full_flat_residue
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 250
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

In the flat alternating sector, explicit full-order surgeries resolve singleton states with a flat left boundary, a full right boundary, or full-left/flat-right holonomy zero. Every surgery closes NOR or strictly increases the leading zero run while retaining the global two-change class. The prefix-extremal singleton residue has full-left/flat-right type and holonomy one. Subsequent lexicographic band growth handles its improvement; terminal cases have direct spanning constructions.

## Development

## A leading-run potential resolves three singleton curvature types and the zero-holonomy mixed branch

Work with a coboundary-flat alternating ternary label. Fix the global color convention once. Consider a full coordinate order whose entire status word is
0^A 1 0^B, A,B>=1.
Thus it has exactly two changes and one isolated singleton.

Write its five-coordinate packet as (a,b,c,d,e), starting at window rank r=A. The three packet statuses are 0,1,0. Every window outside those ranks is zero.

Let L(pi) be the length of the leading zero run. The comparison class consists of ALL full orders whose word has at most two changes and whose first and last statuses are zero. Orders with at most one change close NOR immediately. Each surgery below either closes NOR or remains in the exactly-two-change comparison class and strictly increases L.

### 1. Flat left boundary

The flat 0->1 tetrahedron (a,b,c,d) has
alpha(a,b,d)=0, alpha(a,c,d)=1.
Swap c,d, giving (a,b,d,c,e).
Its internal word is 0,0,1:
alpha(a,b,d)=0,
alpha(b,d,c)=1-alpha(b,c,d)=0,
alpha(d,c,e)=1-alpha(c,d,e)=1.

Only one further window can change: alpha(c,e,f)=u, where f is the next exterior coordinate. The next window (e,f,g) is unchanged and zero.

Hence the affected word and its first unchanged right window are
0,0,1,u,0,
with the final windows omitted when they reach the global endpoint.
For either u, all new ones form one contiguous run. The leading zero run increases from A to A+1. This proves a legal full-order descent for BOTH flat/flat and flat/full singleton types.

### 2. Fully-curved right boundary

The fully-curved 1->0 tetrahedron (b,c,d,e) has
alpha(b,c,e)=0, alpha(b,d,e)=1.
Swap d,e, giving (a,b,c,e,d).
The packet word is again 0,0,1.

If a next exterior coordinate f exists, the next window has color
alpha(e,d,f)=1-alpha(d,e,f)=1.
The following window alpha(d,f,g)=u may be arbitrary. The next window (f,g,h) is unchanged and zero.

Thus the complete changed packet is
0,0,1,1,u,0,
with absent endpoint windows omitted.
Again the new ones are contiguous, and L increases by one. This covers full/full as well as flat/full.

### 3. Full-left / flat-right, holonomy zero

The only curvature type outside the first two cases is full-left / flat-right. Put t=alpha(a,b,e).
Its local face values are
abc=0, abd=1, acd=0,
bcd=1, bce=1, bde=0, cde=0.

If t=0, use the full-support order
(a,b,e,c,d).
Its internal word is monochromatic zero:
alpha(a,b,e)=0,
alpha(b,e,c)=1-alpha(b,c,e)=0,
alpha(e,c,d)=alpha(c,d,e)=0.

The ordered first pair (a,b) is fixed, so every left crossing window is unchanged. The only right crossing windows are
alpha(c,d,f)=u, alpha(d,f,g)=v.
Every subsequent window is unchanged and zero.

Therefore the new word is a zero prefix followed by u,v and then zeros. For every choice of u,v the ones occupy at most one contiguous run. If any one remains, its first rank is at least r+3, whereas the original one was at r+1. Thus L increases by at least two. If every new bit is zero, the order is monochromatic and NOR closes.

### Extremal consequence

Assume the instance has a two-change full order, and choose among the full orders with word 0^a 1^b 0^c a maximum leading run a. The family is finite.

If this extremal order has b=1, its singleton must have:
- fully-curved left boundary;
- flat right boundary;
- t=alpha(a,b,e)=1.

Every other singleton case gives a spanning NOR order or an order in the SAME comparison class with a strictly larger leading run.

The surviving local increasing-triple table is exactly the t=1 full/flat table of ternary §27:
abc=0, abd=1, abe=1, acd=0, ace=0, ade=0,
bcd=1, bce=1, bde=0, cde=0.

The reversed, color-complemented statement applies to a trailing-run extremum.

### Scope for carrier extraction

Roots §§241-242 show that a five-position C-carrier zero is supported by global isolated-singleton orders. The present result supplies explicit admissible full-order descent for three of their four curvature types and the t=0 mixed branch, with every exterior window accounted for.

The resulting isolated band can have width two or three, and the surgery can leave the original five-position carrier. The valid descent class is the declared global two-change family. A carrier argument must prove the connection to this extremal class, or use the surgeries as actual full-order replacements. The remaining extremal singleton branch is t=1 full-left/flat-right; wider extremal bands remain an additional obligation.
