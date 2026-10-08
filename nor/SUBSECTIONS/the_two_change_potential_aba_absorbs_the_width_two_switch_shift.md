# The two-change potential (A+B,A) absorbs the width-two switch shift

## Metadata

- ID: the_two_change_potential_aba_absorbs_the_width_two_switch_shift
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 268
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## The potential (A+B,A) is adapted to the full two-change surgery system

Work in the coboundary-flat alternating ternary sector. For a full order with exactly two changes and word
\[
0^A1^B0^C,
\]
define
\[
\Phi=(A+B,A)
\]
with lexicographic order.

Equivalently, the first coordinate minimizes the trailing zero phase C, and the second coordinate then maximizes the leading zero phase.

Choose a two-change order maximizing \(\Phi\).

### Flat right boundary

The exact right-boundary surgery of §257 preserves A and strictly enlarges the 1-band whenever it does not close NOR. Therefore \(A+B\) strictly increases. A \(\Phi\)-maximum has a fully-curved right boundary.

### Flat left boundary

Use the exact formulas of §257.

For \(B\ge3\), the flat-left swap gives either
\[
0^{A+2}1^{B-2}0^{C'}
\]
or
\[
0^{A+3}1^{B-3}0^{C'}
\]
after absorbing the crossing bit. In both cases \(A+B\) is preserved while A strictly increases.

For \(B=2\), every nonclosing output has a strictly larger value of \(A+B\). The singleton case is covered by the explicit §250/§254 surgeries; its residual right endpoint swap increases B with A fixed.

Hence a \(\Phi\)-maximum also has a fully-curved left boundary.

### Width-two chord branches

For a width-two full/full band, the two easy chord branches of §257 have explicit local word 0001 and remain in the global two-change class unless they close NOR. Their leading zero gain implies
\[
(A+B)' > A+B.
\]
Thus the same potential forces
\[
\alpha(b,c,e)=\alpha(a,b,e)=1,
\]
and the exact two-bit table §264 follows.

### The rigid weave

In the exceptional (r,s)=(1,1) type, §266 identifies the rigid six-set and permits the §226 weave.

If its reconnection bit is zero, the profile changes from width two to width at least three with the same leading zero phase, so \(A+B\) increases.

If the bad bit is one and a subsequent double-full resolution returns directly to a clean two-change profile, §260 computes the shift
\[
(A,2)\longmapsto(A-1,4).
\]
For this move,
\[
(A-1)+4=A+3>A+2.
\]
Thus it is also a strict \(\Phi\)-improvement.

### Consequence

The potential \(\Phi=(A+B,A)\) resolves the apparent tradeoff between losing one leading-zero position and gaining two 1-band positions. Every currently proved local surgery that stays inside the global two-change family is either a spanning NOR closure or a strict \(\Phi\)-improvement.

Therefore a \(\Phi\)-maximal counterexample state can survive a width-two repair only by **leaving the two-change class through its exported reconnection kernel**. The remaining obstruction is no longer potential bookkeeping; it is precisely the task of eliminating or monotonically transporting that extra local band until the state returns to the two-change family or closes NOR.

## Frontier

- Development version when composed: None
- Development version now: 1
