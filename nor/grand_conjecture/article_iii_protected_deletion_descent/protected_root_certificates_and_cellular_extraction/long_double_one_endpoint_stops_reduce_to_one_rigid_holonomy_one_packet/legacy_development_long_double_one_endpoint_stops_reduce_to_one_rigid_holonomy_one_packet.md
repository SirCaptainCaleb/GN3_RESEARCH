# Long double-one endpoint stops reduce to one rigid holonomy-one packet — preserved pre-item development

## Composition

(none yet)

## Development

## Long double-one endpoint stops reduce to one rigid six-coordinate pattern

Work in the coboundary-flat alternating ternary sector. Let
O_x=(a,b,c,d,e,f,...)
be a good deletion witness omitting x with word
0^p 1^q,
where p>=4 and q>=1.

Use the endpoint normal form
alpha(x,a,b)=1,
alpha(a,b,c)=0,
alpha(x,a,c)=0,
alpha(x,b,c)=1.

Assume the first two splice bits are both one:
lambda=alpha(a,c,d)=1,
mu=alpha(a,d,e)=1.
The old zero phase also gives
alpha(b,c,d)=alpha(c,d,e)=alpha(d,e,f)=0.

Put
r=alpha(x,c,d),
u=alpha(x,a,e),
t=alpha(a,b,e).

Flat four-face parity gives the following identities.

From {x,a,c,d}:
alpha(x,a,d)=1 xor r.

From {a,c,d,e}:
alpha(a,c,e)=0.

From {a,b,c,e} and {b,c,d,e}:
alpha(a,b,e)=alpha(b,c,e)=alpha(b,d,e)=t.

From {x,a,c,e}:
alpha(x,c,e)=u.

From {x,a,d,e}:
alpha(x,d,e)=r xor u.

From {x,a,b,d}:
alpha(x,b,d)=1 xor r.

These identities produce three explicit SAME-PROFILE deletion witnesses.

### Branch 1: r=0

Delete a and use
O_a'=(b,x,c,d,e,f,...).

Its first two statuses are
alpha(b,x,c)=0,
alpha(x,c,d)=0,
and every status from c,d,e onward is the untouched suffix of O_x.

Hence O_a' has word exactly
0^p 1^q.

Prepending the omitted coordinate a gives first status
alpha(a,b,x)=1,
so O_a' carries the genuine fully-curved endpoint root
a -> c
with cut {a,b}.

### Branch 2: r=1 and u=1

Delete b and use
O_b'=(a,c,x,d,e,f,...).

Its first three statuses are
alpha(a,c,x)=0,
alpha(c,x,d)=0,
alpha(x,d,e)=0.
The remaining suffix from d,e,f onward is untouched.

Thus O_b' again has exact word
0^p 1^q.

Prepending b gives a genuine endpoint root
b -> x
with partner a.

### Branch 3: r=1, u=0, t=0

Delete c and use
O_c'=(a,x,b,d,e,f,...).

Its first three statuses are
alpha(a,x,b)=0,
alpha(x,b,d)=0,
alpha(b,d,e)=0.
Again the rest is the untouched old suffix.

Hence O_c' has exact word
0^p 1^q.

Prepending c gives a genuine endpoint root
c -> b
with partner a.

### Unique residual pattern

Therefore every long stopped branch lambda=mu=1 which avoids all three witness-preserving surgeries must satisfy
r=1,
u=0,
t=1.

Equivalently,
alpha(x,c,d)=1,
alpha(x,a,e)=0,
alpha(a,b,e)=1.

In this residual branch the deletion order
B=(b,x,c,d,e,f,...)
omitting a has word
0,1,0^(p-2),1^q:
it is a one-defect deletion carrier.

Its five-coordinate initial packet
(b,x,c,d,e)
has word 010 and BOTH transition tetrahedra are fully curved.

For the left transition (b,x,c,d):
alpha(b,x,d)=1,
alpha(b,c,d)=0,
so both endpoint repairs fail.

For the right transition (x,c,d,e):
alpha(x,c,e)=0,
alpha(x,d,e)=1,
so both endpoint repairs fail.

### The residual holonomy is forced to one

The five-set holonomy in the normalization of the double-full theorem is
H=alpha(b,x,e).

From the flat identity on {x,a,b,e},
alpha(x,a,b)=1,
alpha(x,a,e)=u=0,
alpha(a,b,e)=t=1,
so
alpha(x,b,e)=0.

By alternation,
H=alpha(b,x,e)=1.

Thus the UNIQUE residual long endpoint pattern is not the obstructed H=0 double-full branch. It is the H=1 branch and therefore admits the unique two-sided monochromatic resolution
(x,b,c,e,d)
of the packet (b,x,c,d,e).

The resolved local word is 111.

### Consequence

The witness-preserving long-stop analysis has now been reduced to one explicit rigid packet:
- every other bit assignment gives a genuine good deletion witness with the SAME phase profile 0^p1^q and an actual endpoint root;
- the sole survivor is a double-full 010 singleton of forced holonomy one.

This does not yet claim that the two-sided resolution closes the global instance, because the reversed right boundary exports outer-window data beyond d,e. But the long branch is no longer an arbitrary lambda=mu=1 family; all remaining freedom is in the right-side reconnection after this forced H=1 resolution.
