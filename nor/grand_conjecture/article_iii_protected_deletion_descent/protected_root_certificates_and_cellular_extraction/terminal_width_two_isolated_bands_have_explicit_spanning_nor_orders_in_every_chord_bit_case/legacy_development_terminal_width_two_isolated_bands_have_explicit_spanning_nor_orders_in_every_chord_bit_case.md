# Terminal width-two isolated bands have explicit spanning NOR orders in every chord-bit case — preserved pre-item development

## Development

## A width-two isolated one-band at the global endpoint always closes NOR in the flat alternating sector

Suppose a full order has word
0^A 1^2 0, A>=1,
for a coboundary-flat alternating ternary label.

The final six coordinates (a,b,c,d,e,f) have word 0110. If either band boundary is flat, §257 supplies a strict lexicographic two-change improvement; the explicit flat first-boundary move has output 0^(A+2),u at this endpoint and therefore already closes NOR. The flat last-boundary move also closes at this endpoint.

It remains to handle both boundaries fully curved. Their face values are
abc=0, bcd=1, cde=1, def=0,
abd=1, acd=0, cdf=0, cef=1.
All earlier windows are zero.

Put t=alpha(b,c,e), u=alpha(a,b,e), s=alpha(b,c,f).
Parity on {b,c,d,e} gives bde=t. Parity on {b,c,e,f} gives bef=s.

### Case t=0

The order
(a,b,c,e,d,f)
has word 0001:
abc=0, bce=0, ced=0, edf=1.
It fixes the first pair (a,b), so concatenation after the unchanged zero prefix closes NOR.

### Case t=1 and u=0

Use
(a,b,e,d,c,f).
Its word is 0001:
abe=0, bed=1-bde=0, edc=1-cde=0, dcf=1.
Again the first pair is fixed.

### Case t=u=1 and s=0

Use
(a,b,c,f,e,d).
Its word is 0001:
abc=0, bcf=0, cfe=1-cef=0, fed=1-def=1.
The first pair is fixed.

### Case t=u=s=1

Use the preliminary weave
(a,d,b,c,e,f).
Its internal word is 0111:
adb=1-abd=0,
dbc=bcd=1,
bce=1,
cef=1.

If A=1, this is the entire full order and is NOR-good.

If A>=2, let p be the coordinate immediately before a in the old order. All earlier windows are zero, including pab=0. The preliminary weave retains the first coordinate a, so only the crossing window pad can change on the left.

If alpha(p,a,d)=0, the preliminary weave has a zero prefix followed by ones and closes NOR.

If alpha(p,a,d)=1, replace the final SEVEN coordinates by
(p,a,d,c,f,b,e).
Its five internal statuses are all one:
pad=1,
adc=1-acd=1,
dcf=1-cdf=1,
cfb=bcf=s=1,
fbe=bef=s=1.

The first ordered pair (p,a) is fixed and the packet reaches the global right endpoint. Every earlier zero window is unchanged. Hence this is also a spanning NOR-good order.

### Theorem and scope

All bit cases are exhausted, so every global word 0^A 1^2 0 yields an explicit spanning NOR order. By full reversal and one global color convention, the same holds for 0 1^2 0^A.

Together with §253, the endpoint branches now have:
- singleton bands: closure whenever either exterior run has length at most two;
- width-two bands: closure whenever either exterior run has length one.

The proof applies to arbitrary ambient order through exact frozen prefix pairs. It uses the given terminal endpoint to eliminate exported reconnection windows. Interior full/full bands retain their separate boundary obligations.

### Corollary: all short-phase flat deletion carriers close

Suppose an omitted-x good deletion order has word 0^2 1^q, q>=1.
Prepending x has word either
0^3 1^q,
which is already NOR-good, or
1,0^2,1^q.
In the latter case, full reversal complements and reverses the word, giving
0^q 1^2 0.
The theorem above supplies a spanning NOR order. This uses arbitrary insertion scans.

The same argument for 0^1 1^q uses the terminal B=1 singleton theorem of §253, which requires only alternation.

For a good deletion witness of either one-change direction, full reversal swaps its phase lengths and global color complementation chooses the status convention. Therefore a phase of length at most two can always be placed in the displayed first position.

Consequently, in a coboundary-flat alternating counterexample, every good deletion witness is bichromatic and both its phases have length at least three. A monochromatic deletion witness extends at an endpoint with at most one change.

This discharges the earlier short-phase root-handoff branch by an actual spanning construction. The remaining flat deletion analysis starts at phase length three.
