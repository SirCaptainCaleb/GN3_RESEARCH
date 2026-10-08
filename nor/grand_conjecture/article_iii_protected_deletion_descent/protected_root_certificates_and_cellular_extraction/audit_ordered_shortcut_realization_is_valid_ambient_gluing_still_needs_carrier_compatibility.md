# Audit: ordered shortcut realization is valid; ambient gluing still needs carrier compatibility

## Composition

The ordered physical shortcut is valid. Its existence does not prove relative ambient gluing: the root carrier must preserve its certificates, frozen boundary provenance, and outside order when the shortcut is realized.

## Development

## Audit: the ordered-shortcut theorem is valid, while local opposite-root weaving still needs carrier compatibility

Section §320 proves a genuine and important statement: in the crossed endpoint residue, an explicit fully-curved four-coordinate carrier realizes the ordered root
\[
x\to z.
\]
The calculation is sound.

### Verification of the Type-II packet

With
\[
(A,B;E)=(0,1;0),
\]
tetrahedral parity on
\[
\{x,z,w_1,w_2\}
\]
gives
\[
R_1=0,\qquad R_2=1.
\]
Thus
\[
(w_1,x,z,w_2)
\]
has transition \(01\).

Its off-faces are
\[
\alpha(w_1,x,w_2)=1-A=1,\qquad
\alpha(w_1,z,w_2)=1-B=0.
\]
This is the fully-curved \(01\) pattern. The complete \(K_{2,2}\) barrier square therefore includes the opposite-corner carrier
\[
(x,w_1,w_2,z),
\]
whose physical root is exactly
\[
\boxed{x\to z}.
\]

The right-end Type-I argument is the reversed analogue. Hence the crossed residue really does realize the ordered physical shortcut.

### What this settles

Combining §320 with the earlier endpoint case analysis gives:

> For every desired ordered pair \(x,z\) arising as a certified endpoint-cycle shortcut, there is an actual fully-curved transition carrier with physical root \(x\to z\), unless NOR has already closed.

Thus the **physical shortcut realization problem is solved**.

### What it does not settle automatically

An arbitrary physical shortcut carrier need not share the outside order or ordered-partition carrier of the endpoint witnesses from which the shortcut was requested.

Therefore replacing two consecutive endpoint-cycle edges
\[
x\to y\to z
\]
by the newly realized physical root
\[
x\to z
\]
is valid algebraically in physical root space, but it does not automatically preserve the witness class or the common-carrier provenance needed for a spanning splice.

Likewise, §175 proves only that two opposite root packets on at most five active coordinates admit a one-change weave **on the active set**. Its own conclusion explicitly states that boundary-collar compatibility is still required for a full ambient splice.

Accordingly, the sentence in §286 asserting that a small opposite-root overlap “hence NOR closes” requires an additional common-carrier/outside-order hypothesis unless that provenance is supplied elsewhere.

### Correct frontier after §320

The unresolved issue has moved strictly past shortcut realization.

It is now:

\[
\boxed{\text{upgrade an arbitrary realized physical shortcut to a provenance-compatible shortcut/splice.}}
\]

Equivalently, prove one of:
1. the §320 shortcut can be realized inside the same relative carrier as the two endpoint edges it replaces;
2. the shortcut carrier and endpoint carrier admit a frozen-outside-order exchange;
3. failure of such compatibility yields a strict descent or spanning NOR order.

This is narrower than the previous crossed-ladder problem: the desired root itself now exists explicitly. Only witness compatibility remains.
