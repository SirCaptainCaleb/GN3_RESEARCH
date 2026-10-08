# Lexicographic two-change descent eliminates every flat band boundary and two width-two chord branches

## Metadata

- ID: lexicographic_two_change_descent_eliminates_every_flat_band_boundary_and_two_width_two_chord_branches
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 257
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

For global words 0^A1^B0^C in the flat alternating sector, a flat first boundary strictly increases A; a flat last boundary preserves A and strictly increases B. Each move retains the two-change class or closes NOR. Lexicographic descent therefore terminates at a full/full band of width at least two. At width two, further boundary-safe surgeries exclude bce=0 and the branch bce=1,abe=0. The surviving chord bits are bce=abe=1, with subsequent endpoint branches addressed by the terminal theorem.

## Development

## All flat boundaries of a global two-change band admit strict run descent

Work in the coboundary-flat alternating ternary sector with a full order of global word
0^A 1^B 0^C, A,B,C>=1.
Use the finite comparison class of all full orders with this word form, and maximize the lexicographic potential (A,B). A one-change output closes NOR.

### Flat first boundary: leading-run gain for every band width

Let (a,b,c,d,e) begin at window rank r=A. The first transition has colors abc=0, bcd=1. If it is flat, abd=0.

Swap c,d. No window before rank r changes. The first two affected statuses are
abd=0, bdc=0.
The third is dce=1-cde.

If B=1, cde=0 and the new affected word is 0,0,1,u followed by unchanged zeros. This is the leading-run descent of §250.

If B>=2, cde=1 and the first three affected statuses are 000. The sole further changed window is cef=u. Every later window is an unchanged continuation of the original one-run followed by the zero suffix.

For B>=3 the exact global word is
0^(A+2), u, 1^(B-3), 0^C.
For B=2 it is
0^(A+2), u, 0^(C-1).
Absent endpoint windows are omitted. Each word is one-change or has one contiguous one-band and a leading zero run strictly longer than A.

Thus a flat first boundary always produces NOR closure or lexicographic improvement in the SAME global two-change class.

### Flat last boundary: one-band gain for every band width

Let j=A+B be the rank of the last one. Write its boundary packet (a,b,c,d), with abc=1, bcd=0.
Flatness gives abd=1.

Swap c,d. The statuses at j,j+1 become
abd=1, bdc=1.
If the next exterior coordinate f exists, the next status is
dcf=1-cdf=1,
because the old suffix is zero. A following status may be an arbitrary u, and every later status is unchanged and zero.

Every earlier window, including the first one of the band, is unchanged. Hence A is preserved, all new ones remain contiguous, and B strictly increases. The output is a one-change order or a lexicographic improvement in the same two-change class.

In particular, if C<=2, there is no subsequent zero beyond the forced new ones. The output is already a spanning one-change order.

### Global normal form

If the instance has a two-change order and NOR has not closed, choose a lexicographically maximum (A,B) in this finite class.

Both boundary tetrahedra of its isolated one-band must be fully curved:
- a flat first boundary increases A;
- a flat last boundary preserves A and increases B.

For B=1, §250 gives leading-run gain in the full/full case, so the globally extremal band has B>=2. Equivalently §254 completes the singleton descent for all curvature types using the same lexicographic potential.

Therefore the entire two-change route reduces by proved finite descent to a full/full band of width at least two. Every applied move retains exactly two changes unless it closes NOR. This supplies a full-word potential and preserves the minimization class.

### Further exact gain for a width-two full/full band

Let its six-coordinate packet (a,b,c,d,e,f) have word 0110, and put
t=alpha(b,c,e), u=alpha(a,b,e).
The two full boundaries give abd=1, acd=0, cdf=0, cef=1.

If t=0, swap d,e. The packet becomes
(a,b,c,e,d,f): 0001.
The first three coordinates are fixed, the last coordinate f is fixed, and only one right crossing window can change. Its value followed by the unchanged zero tail keeps a single one-band. The leading run increases by two, or NOR closes.

If t=1 but u=0, use
(a,b,e,d,c,f).
Its word is again 0001:
abe=0, bed=1-bde=0, edc=1-cde=0, dcf=1.
Here bde=t=1 follows from parity on {b,c,d,e}. The first pair and last coordinate f are fixed, so again only one right crossing bit changes. The output stays in the two-change class and increases A by two, or closes NOR.

Thus a width-two full/full lexicographic extremum additionally satisfies
alpha(b,c,e)=alpha(a,b,e)=1.

These are partial table constraints. The rotations in the separate maximal-threshold-band classification require their own extremal state class and full reconnection verification before further rigid values can be imported.

### Remaining branch

The current genuine two-change obstruction is an extremal full/full band of width at least two. At width two the two specified chord bits are one. Resolving that state requires a boundary-safe full-curvature crossing that retains the global two-change comparison class, or an actual spanning order.
