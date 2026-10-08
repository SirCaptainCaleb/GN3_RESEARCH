# The seven-coordinate weave loses two leading zeros: corrected weighted descent — preserved pre-item development

## Composition

(none yet)

## Development

## The seven-coordinate weave loses two leading zeros: corrected weighted descent

Work in the flat alternating sector and compare full orders with word 0^A1^B0^C. The proposed weight 7A+4B in §270 does not cover the seven-coordinate all-one weave: its leading-run loss was undercounted.

Take B=2 and write the six-coordinate band packet (a,b,c,d,e,f), with local word 0110. Assume the forced chords bce=abe=1 and the exact §264 bit s=bcf=1; r=abf is arbitrary. The strong weave (a,d,b,c,e,f) has word 0111 independently of r.

If A=1, no left crossing exists and the weave improves the two-change profile or closes. If A>=2, let p immediately precede a and R=pad. If R=0, the weave preserves A and increases B by one, with the right exterior fixed.

If R=1, the seven-coordinate order
(p,a,d,c,f,b,e)
has word 11111:
pad=1, adc=1, dcf=1, cfb=bcf=1, fbe=bef=1.
Its ordered first pair (p,a) agrees with the old order, so all preceding windows are fixed.

The old seven-coordinate packet (p,a,b,c,d,e,f) has word 00110. Its first window starts at rank A-1, whereas the old leading zeros occupy ranks 1 through A. Thus, for A>=3, the new leading zero length is A-2, not A-1. When its two right reconnection bits are clean, the new one-band width is at least five. Consequently the actual trade is
(A,2) -> (A-2,B'), B'>=5.
For A=2 the unchanged zero prefix is empty and a clean reconnection instead gives a spanning good order.

At the minimum clean width B'=5, the change of 7A+4B is -14+12=-2. Therefore the strict weighted-descent assertion of §270 is unsupported for this surgery.

### Correct alternatives

The lexicographic potential (A+B,A) from §268 does cover the exact seven-coordinate trade: its first component increases by at least one.

A valid scalar alternative for the currently listed clean moves is
Psi=4A+3B.
The gains are:
- flat-left wide-band moves (Delta A,Delta B)=(2,-2) or (3,-3): gains 2 or 3;
- flat-right moves: Delta A=0, Delta B>0;
- the easy width-two 0001 replacements: Delta A>=2, Delta B>=-1, gain at least 5;
- the clean hypothetical switch trade (-1,+2): gain 2;
- the actual seven-coordinate all-one weave (-2,Delta B>=3): gain at least 1.
The singleton moves of §§250,254 also strictly improve this weight whenever they stay in the two-change family: they increase A without decreasing B=1, or preserve A and increase B.

The word clean refers to the actual full window word having at most one nonempty 1-band. It cannot be inferred solely from the displayed internal packet. In particular the §260 left export has a forced second bit equal to one (§263), so the hypothetical all-zero left export is unavailable when that crossing window exists.

Thus (A+B,A), or 4A+3B, supports finite comparison of the proved clean surgeries. No potential here discharges a split-band output. The surviving interior reconnection kernels require an actual surgery returning to the comparison class or a spanning good order.
