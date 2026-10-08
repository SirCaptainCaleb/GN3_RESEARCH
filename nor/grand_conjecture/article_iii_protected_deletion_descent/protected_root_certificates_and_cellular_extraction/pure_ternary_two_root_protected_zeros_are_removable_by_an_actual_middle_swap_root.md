# Pure ternary two-root protected zeros are removable by an actual middle-swap root

## Composition

(none yet)

## Development

## Pure ternary two-root protected zeros are locally removable by a middle swap

Work in the pure alternating ternary sector and in a minimum counterexample.

Suppose one carrier cell contains a two-term protected-root zero supported by opposite ACTUAL window-slide roots
rho=e_a-e_d
and
-rho=e_d-e_a.

Let the chamber carrying rho contain the certified 10 packet

(a,b,c,d),

so
alpha(a,b,c)=1,
alpha(b,c,d)=0.

Because the opposite root occurs in another refinement of the same ordered-partition cell, a and d lie in one common tied block. Since b,c lie between them in this refinement, b,c lie in that same tied block as well.

Therefore swapping the two middle coordinates b,c is an allowed chamber edge inside the SAME carrier cell.

Let pi* be the adjacent chamber with local packet

(a,c,b,d).

### The middle swap destroys the antipodal root direction

Alternation gives

alpha(a,c,b)=0,
alpha(c,b,d)=1.

Thus the local packet changes from 10 to 01.

The unique ternary window-slide vector with endpoints a,d in pi* is still e_a-e_d, but it is no longer carried by a 10 descent.

Also e_d-e_a cannot occur as a window-slide root in pi*: the relative order of a and d was not reversed by the middle swap.

Hence pi* carries no 10 certificate parallel to rho.

### Counterexamplehood supplies an independent actual root

The full order pi* is still an order of the ambient counterexample, so its ternary word has at least two changes and therefore contains some actual 10 descent.

Let
sigma=e_u-e_v
be the physical window-slide root of any such descent.

By the preceding paragraph,
sigma is neither rho nor -rho.

Type-A roots are parallel only when they have the same unordered endpoint pair. Therefore sigma is linearly independent of rho.

Crucially, sigma is an ACTUAL protected window-slide root from a genuine chamber of the same carrier cell. No omitted-coordinate exchange label or formal auxiliary direction is introduced.

### Zero-free local blow-up

In the physical root space W, the segment from rho to sigma avoids the origin because sigma is not a negative scalar multiple of rho.

Likewise the segment from sigma to -rho avoids the origin because sigma is not a positive scalar multiple of rho.

Hence the broken path

rho -> sigma -> -rho

lies entirely in W minus {0}.

Since the three chamber states lie in one convex permutahedral cell, a local subdivision/blow-up of the cell may route the PL protected-root map through the sigma-labeled chamber, replacing the straight antipodal interpolation that crossed zero.

On the reversal-mate cell perform the mirrored modification. The free-cell pairing lemma preserves equivariance.

### Theorem

Every isolated two-root protected Radon zero in one carrier cell is locally removable in the pure alternating ternary sector.

Therefore an essential zero of the protected actual-root carrier cannot have support size two. After inert zeros are removed by the common-halfspace blow-up, every essential local cancellation must involve at least three nonparallel actual window-slide roots.

### Relation to the earlier audit

This repairs the conceptual defect in the old pair-order desingularization attempt: the intermediate vector sigma belongs to the SAME actual window-slide root system as rho and -rho.

No dictionary between omitted-coordinate replacement roots and protected slide roots is needed.

### Scope

The key step uses alternation under the middle transposition:
10 -> 01.

It is not asserted for a general reversal-odd ternary label.

For pure ternary orientation, the previously isolated five/six-coordinate certificate-persistence problem is therefore unnecessary for TWO-TERM zeros. Those bounded-support analyses remain relevant for three-or-more-root cancellations and for boundary-safe combinatorial surgery.
