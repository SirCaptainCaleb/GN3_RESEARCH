# Three-block singleton faces reduce shortcut realization to two one-sided cases

## Composition

(none yet)

## Development

## Three-block singleton faces reduce shortcut realization to two one-sided cases

Assume a minimum counterexample. Fix distinct coordinates (x,z) and put
[
W=Vsetminus{x,z}.
]
Choose any NOR-good order
[
O=(w_1,ldots,w_m)
]
of the proper subinstance on (W).

Consider the full three-block witness
[
Pi=x,O,z.
]

### Monochromatic middle

If (O) is monochromatic of color (c), then (Pi) differs from that constant word only in its new first and last ternary windows.

Because (Pi) is a full order in a counterexample, it must have at least two changes. Therefore both endpoint bits equal (1-c). Hence the first change is at the left endpoint and the last change is at the right endpoint.

Thus
[
oxed{D(Pi)=e_x-e_z.}
]

So a monochromatic doubly-deleted carrier realizes the desired shortcut (x	o z) directly.

### One-change middle

Normalize
[
w(O)=0^p1^q,
qquad p,qge1.
]
Let
[
L=alpha(x,w_1,w_2),qquad
R=alpha(w_{m-1},w_m,z).
]
Then the full status word is exactly
[
L, 0^p1^q, R.
]

Let (ell) and (r) be the first and last physical coordinates of the unique switch tetrahedron of (O), as in §285.

There are four endpoint-bit cases.

1. (L=0,R=1).  
   The whole word is (0^*1^*), so (Pi) is NOR-good. This is impossible in a counterexample.

2. (L=1,R=0).  
   The word has three changes: left endpoint, middle switch, right endpoint. Hence
   [
   oxed{D(Pi)=e_x-e_z.}
   ]
   The desired shortcut is realized directly.

3. (L=1,R=1).  
   The only changes are the left endpoint and the middle switch. Therefore
   [
   oxed{D(Pi)=e_x-e_r.}
   ]

4. (L=0,R=0).  
   The only changes are the middle switch and the right endpoint. Therefore
   [
   oxed{D(Pi)=e_ell-e_z.}
   ]

### Theorem

For every ordered pair (x,z) and every good doubly-deleted carrier (O), the three-block witness (xOz) has exactly one of the following outcomes:

- spanning NOR closure;
- direct outermost shortcut (x	o z);
- left one-sided root (x	o r), where (r) is the far endpoint of the unique switch of (O);
- right one-sided root (ell	o z), where (ell) is the near endpoint of that switch.

Moreover, if (O) is monochromatic, only the direct-shortcut outcome is possible.

### Closure relevance

The certified-shortcut problem of §291 no longer requires arbitrary full-order search. For the rank-two junction shortcut (x	o z), choose a good order of the doubly-deleted middle (Vsetminus{x,z}) and inspect only its two endpoint insertion bits.

Failure to realize (x	o z) is forced into one of two one-sided configurations attached to the unique middle switch. Thus the missing shortcut theorem reduces recursively to controlling one switch endpoint of a proper ((n-2))-coordinate NOR witness.
