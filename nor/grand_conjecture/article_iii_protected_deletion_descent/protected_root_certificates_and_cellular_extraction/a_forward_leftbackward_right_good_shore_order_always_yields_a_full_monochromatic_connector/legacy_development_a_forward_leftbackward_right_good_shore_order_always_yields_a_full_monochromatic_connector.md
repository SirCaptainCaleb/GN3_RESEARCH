# Exact endpoint criterion for a switch-adjacent whole-shore compatible connector — preserved pre-item development

## Composition

(none yet)

## Development

## Exact endpoint criterion for a switch-adjacent whole-shore compatible connector

Audit correction to the previous version.

Continue with §362. Let
\[
O=(a_1,\ldots,a_k)
\]
be a NOR-good order of the minimum shore \(A\), with normalized word
\[
0^p1^q,\qquad p,q\ge1,
\]
and let
\[
e_i=1
\iff
a_i\to a_{i+1}
\]
in the switching-normalized shore tournament.

For
\[
j\in\{p,p+1,p+2\}
\]
define
\[
P_j=(a_1,\ldots,a_j),
\qquad
R_j=(a_k,a_{k-1},\ldots,a_{j+1}),
\]
and
\[
Q_j=P_j,x,z,R_j.
\]

Section §362 correctly proves that the internal ternary word of \(Q_j\) is monochromatic zero precisely when the two splice collars are zero:
\[
e_{j-1}=1,\qquad e_{k-1}=0
\]
with endpoint clipping.

For the **compatible connector** theorem, two additional endpoint-pair conditions are required.

The first ordered pair of \(Q_j\) is the first pair of \(P_j\), hence it is forward exactly when
\[
e_1=1
\]
whenever \(|P_j|\ge2\).

The last ordered pair of \(Q_j\) is
\[
(a_{j+2},a_{j+1}),
\]
the final pair of the reversed suffix \(R_j\). It is forward exactly when
\[
e_{j+1}=0
\]
whenever \(|R_j|\ge2\).

Therefore, in the nondegenerate case,
\[
\boxed{
Q_j\text{ is a compatible monochromatic zero connector}
\iff
e_1=1,\ e_{j-1}=1,\ e_{j+1}=0,\ e_{k-1}=0.
}
\]

The symmetric placement
\[
R_j,x,z,P_j
\]
has the same four compatibility requirements, with the collar roles exchanged.

### Consequence

If
\[
e_1=1,\qquad e_{k-1}=0
\]
and any switch-adjacent two-step edge pair
\[
(e_{p-1},e_{p+1}),\quad
(e_p,e_{p+2}),\quad
(e_{p+1},e_{p+3})
\]
equals
\[
(1,0),
\]
then \(A\cup\{x,z\}\) has a spanning compatible monochromatic connector.

Hence a good shore order with favorable outer endpoint orientation can fail the compatible-connector construction only if the two edge-parity subsequences are locally nondecreasing across the switch:
\[
e_{p-1}=1\Rightarrow e_{p+1}=1,
\]
\[
e_p=1\Rightarrow e_{p+2}=1,
\]
\[
e_{p+1}=1\Rightarrow e_{p+3}=1.
\]

The previous version's stronger claim that favorable outer endpoints alone force a connector is withdrawn.
