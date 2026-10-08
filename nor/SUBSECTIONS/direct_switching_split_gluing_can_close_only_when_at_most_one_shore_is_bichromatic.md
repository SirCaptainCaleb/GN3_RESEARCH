# Direct switching-split gluing can close only when at most one shore is bichromatic

## Metadata

- ID: direct_switching_split_gluing_can_close_only_when_at_most_one_shore_is_bichromatic
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 335
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Direct switching-split gluing can close only when at most one shore is bichromatic

Use the exact endpoint-state composition law of §333. In the switching-normalized split
\[
B\to z\to A\to x,
\]
choose NOR-good shore orders with internal ternary words \(c_B,c_A\). The resulting full word is
\[
W=
c_B,\ \epsilon_R(B),\ 0,\ \epsilon_L(A),\ c_A,\ \epsilon_R(A),
\]
with the usual endpoint clipping.

Write \(\operatorname{chg}(w)\) for the number of adjacent changes in a binary word.

### Internal changes survive every contiguous gluing

The word \(c_B\) occurs as a contiguous subword of \(W\), and so does \(c_A\). Therefore
\[
\operatorname{chg}(W)
\ge
\operatorname{chg}(c_B)+\operatorname{chg}(c_A).
\]

Consequently, if both shore orders are genuinely bichromatic NOR orders,
\[
\operatorname{chg}(c_B)=\operatorname{chg}(c_A)=1,
\]
then
\[
\boxed{\operatorname{chg}(W)\ge2.}
\]
No choice of endpoint switching parities can repair this, because the two internal shore switches are already distinct physical window boundaries.

The companion composition
\[
A,x,B,z
\]
has the same obstruction.

### Exact structural consequence

A direct contiguous composition across a shortcut-free switching split can yield a spanning NOR order only if at least one chosen shore order is monochromatic.

If exactly one shore is bichromatic, its unique internal switch must be the unique global switch, so every boundary bit and every bit of the other shore must agree with the appropriate constant side. If both shores are monochromatic, the remaining question is the finite boundary-bit word supplied by §333.

Thus the phase-alignment problem of §331 is not merely an endpoint-parity choice. When both shores possess only bichromatic witnesses, direct block concatenation is impossible in principle.

### Implication for recursive closure

Any induction on shortcut-free switching splits must do one of the following before final gluing:

1. produce a monochromatic witness on one shore;
2. absorb one shore's internal switch into a further recursive split/refinement;
3. interleave or splice the two shore witnesses so their internal switches cease to survive as two distinct global boundaries;
4. exit through a protected shortcut/root.

This sharply identifies the role for a Hartman-style least-unreachable argument: the reachable state must record whether a shore switch has been **absorbed**, not merely the two endpoint parity ports.

In particular, a finite-state recursion whose state space contains only
\[
(\epsilon_L,\epsilon_R)
\]
is insufficient. One additional switch-status variable is logically necessary.

## Frontier

- Development version when composed: None
- Development version now: 1
