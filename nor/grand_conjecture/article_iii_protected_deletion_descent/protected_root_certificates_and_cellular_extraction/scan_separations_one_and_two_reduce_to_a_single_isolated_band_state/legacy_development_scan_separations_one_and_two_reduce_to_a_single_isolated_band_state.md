# Scan separations one and two reduce to a single isolated-band state — preserved pre-item development

## Scan separations one and two reduce to a single isolated-band state

Continue with two exterior coordinates x,y which both block all insertions into one long-phase carrier

O=(v_1,...,v_m),
word 0^p1^q,
p,q>=3.

Their five-bit switch cores are nonincreasing step functions. Suppose they are distinct and, after naming, x switches earlier than y.

Root §159 handles separation at least three. Here classify disagreement lengths one and two.

### Separation one

Let i be the unique disagreement index. Then

s_{i-1}^x=s_{i-1}^y=1,
s_i^x=0, s_i^y=1,
s_{i+1}^x=s_{i+1}^y=0,

with endpoint clipping if the core itself begins or ends there.

The pair potential c_j=alpha(x,y,v_j) is constant immediately before and after the disagreement and toggles across i.

Choose the pair orientation whose two internal insertion bits are 01. The exact four-window pair-insertion packet is always

1,0,1,0.

The curvature pattern is

FLAT - FULL - FLAT.

Indeed, in the orientation (A,B,x,y,C,D) with middle bits 01, the neighboring scan equalities give:
- left 10 off-faces 1,0, hence flat;
- middle 01 off-faces 1,0 in the full orientation, hence fully curved;
- right 10 off-faces 1,0, hence flat.

Repair the left flat 10 by its inward last-pair swap. The local four-window word becomes

1,1,0,0.

The symmetric repair on the right gives the mirror constant-block outcome.

When spliced into the untouched old 0^p1^q carrier, this creates at most one isolated monochromatic band bounded by the opposite color. This remains true if i=p-1 or i=p+3: the one additional untouched old window on the near side has the same color as the adjacent 00 or 11 block.

Thus separation one reduces to the standard one-band transport state.

### Separation two

Let the disagreement indices be i,i+1.

The pair potential toggles at both, so the canonical pair orientations at the two gaps alternate.

Exactly one of the two gaps produces packet 1010. The other produces:
- 1011 on one parity; or
- 0010 on the other parity.

If the two disagreement gaps are both interior to the switch region, the 1010 packet has curvature

FLAT - FLAT - FULL

or its mirror

FULL - FLAT - FLAT.

This follows from the fact that one outer neighboring scan pair still disagrees while the other has already rejoined.

Repair an outer flat transition toward the occupied switches. The local variation drops by two, leaving a four-window word with one isolated band, such as 1101 or its reverse/complement analogue.

If the disagreement interval touches an extreme core position p-1 or p+3 and the 1010 packet occurs at that extreme gap, use the OTHER disagreement gap instead. It lies one step inward and its packet is 1011 or 0010. Against the untouched 0-prefix and 1-suffix, either word already gives exactly one isolated monochromatic band and no additional remote disturbance.

Hence separation two also reduces directly to a one-band state.

### Codimension-two conclusion

For two insertion-blocking exterior coordinates on one long-phase carrier:

- identical scan cores: root §157 gives a spanning insertion or explicit new omission;
- separation >=4: root §159 gives a spanning pair insertion;
- separation 3: root §160 gives direct closure or rigid FULL-FLAT-FULL, then a one-band state;
- separation 2: the present theorem gives a one-band state;
- separation 1: the present theorem gives a one-band state.

Therefore EVERY nonclosing interaction of two blocking switch cores is reduced to the already-existing isolated-band / terminal-full-barrier architecture.

No independent codimension-two scan recurrence survives.

The remaining common obstruction is now exactly the same as in the Tucker, endpoint, and one-band Sperner routes: eliminate or realize the exchange encoded by a terminal fully-curved boundary of a finite monotone band transport.
