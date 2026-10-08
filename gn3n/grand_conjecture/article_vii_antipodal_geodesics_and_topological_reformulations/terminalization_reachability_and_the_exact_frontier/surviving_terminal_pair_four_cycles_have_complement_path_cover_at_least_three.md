# Surviving terminal-pair four-cycles have complement path-cover at least three

## Composition

(none yet)

## Development

## A surviving terminal-pair four-cycle must have complement path-cover number at least three

Let \(H\) be a boundary tournament with no spanning two-cover. Let
\[
B=\{a,b,c,d\}
\]
and let \(z\notin B\). Suppose the mutual terminal-pair graph before \(z\) contains the cycle
\[
a-b-c-d-a.
\]
Put
\[
Y=B\cup\{z\}.
\]

By [[a_mutual_terminal_pair_four_cycle_forces_a_hamiltonian_five_support]],
\[
H[Y]
\]
is Hamiltonian.

There are now three possibilities for the complement \(H-Y\).

### 1. The complement is Hamiltonian

Then a Hamilton path on \(Y\) together with a Hamilton path on \(H-Y\) gives a spanning two-cover of \(H\), contrary to the standing no-two-cover hypothesis.

### 2. The complement has path-cover number two

Write
\[
H-Y=P\mid Q.
\]
Then
\[
Y\mid P\mid Q
\]
is a spanning three-cover with a distinguished Hamiltonian five-component.

This is exactly the input of the rooted five-component endpoint theory. In particular, after choosing the appropriate distinguished labels when the five-packet arises in the Article VII minimum-hole interface, [[rooted_five_component_endpoint_synchronization_is_a_closed_bounded_theorem]] reduces all four exposed endpoint tests to one of the established bounded outputs:
- a direct endpoint enlargement;
- a Hamiltonian support of order at most six with explicit endpoint/core incidence;
- or a positioned reversing triple.

Thus this branch no longer carries an independent unbounded terminal-pair topology problem; it re-enters the bounded disturbance-conversion interface.

### 3. The complement has path-cover number at least three

This is the only genuinely new complement type for a global terminal-pair four-cycle.

Hence:

> **Global carrier-loop separation.** In a no-two-cover tournament, every mutual terminal-pair \(C_4\) forces a Hamiltonian five-packet \(Y\). If \(\operatorname{pc}(H-Y)\le2\), then either \(H\) already two-covers or the loop enters the closed bounded five-component endpoint-synchronization machinery. A terminal-pair loop that remains genuinely outside the bounded combinatorial interface must satisfy
> \[
> \boxed{\operatorname{pc}(H-Y)\ge3.}
> \]

This strengthens [[a_mutual_four_cycle_with_hamiltonian_complement_already_gives_a_spanning_two_cover]], which treated only the Hamiltonian-complement case. The remaining topological frontier is therefore not an arbitrary protected \(C_4\), but a protected \(C_4\) whose forced Hamiltonian five-packet has genuinely three-path-or-worse complement.
