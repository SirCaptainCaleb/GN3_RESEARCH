# Three common blocked hooks force a bounded anchor-containing Hamiltonian packet

## Metadata

- ID: three_common_blocked_hooks_force_a_bounded_rooted_hamiltonian_packet
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 101
- Row version: 2
- Development version: 2
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Three common blocked hooks force a bounded anchor-containing Hamiltonian packet

Retain the genuine mixed reflected-double residue
\[
J=(x,c_1,\ldots,c_N,y),\qquad \kappa_2(H[J])=2,
\]
with left endpoint word \(011\). Thus
\[
h(x,c_1,c_2)=0,
\qquad
h(c_2,c_1,x)=1.
\]

Assume the left outward-buffer test is completely blocked, so that for every ambient-order vertex \(z\) strictly to the left of \(x\),
\[
h(z,c_1,c_2)=0.
\]
By boundary antisymmetry,
\[
h(c_2,c_1,z)=1
\]
for every such \(z\), as recorded in [[a_blocked_outward_buffer_creates_a_boundary_straddling_common_core_packet]].

**Lemma (blocked-side three-hook packet).** If the blocked left side contains two distinct exterior vertices \(z_1,z_2\), then there is a Hamiltonian support \(K\) of order four or five such that
\[
\{c_2,c_1\}\subseteq K
\subseteq
\{c_2,c_1,x,z_1,z_2\}.
\]
More precisely, either

1. for some distinct \(s,t\in\{x,z_1,z_2\}\), the four-set
   \[
   \{c_2,c_1,s,t\}
   \]
   is Hamiltonian; or
2. the full five-set
   \[
   \{c_2,c_1,x,z_1,z_2\}
   \]
   is Hamiltonian.

**Proof.** The three vertices
\[
x,z_1,z_2
\]
are common hooks through the ordered anchor pair \((c_2,c_1)\):
\[
h(c_2,c_1,x)=h(c_2,c_1,z_1)=h(c_2,c_1,z_2)=1.
\]
Apply the three-hook consequence in [[localextend01]] with
\[
a=c_2,\qquad w=c_1,\qquad
\{t_1,t_2,t_3\}=\{x,z_1,z_2\}.
\]
That theorem gives exactly the displayed four-set alternative or the five-set alternative. \(\square\)

The right-hand mirror is identical.

### Consequence and limitation

A completely blocked outward side has only two possibilities relevant to the packet problem:

- it contains at most one vertex outside the selected endpoint, so its exterior depth is already bounded; or
- it contains two exterior vertices and therefore supplies a Hamiltonian boundary-straddling packet of order at most five **containing** the exposed corridor edge \(\{c_2,c_1\}\).

If there is also no strictly farther positive witness, [[no_farther_positive_witness_forces_monochromatic_outward_status_rays]] allows \(z_1,z_2\) to be chosen as the first two outward vertices, and
\[
(z_2,z_1,x,c_1)
\]
is itself a tight four-path. Hence the Hamiltonian packet is supported inside a contiguous two-layer exterior guard, not at an arbitrarily remote outside vertex.

The word “anchor-containing” is essential. The three-hook theorem proves Hamiltonicity of the support, but it does **not** prescribe a Hamilton order in which \(c_2c_1\), or either anchor vertex, occurs at a desired endpoint. Therefore this lemma does not supply the rooted attachment required to concatenate the packet to a corridor tail. Any argument that treats support containment as endpoint-rooted Hamiltonicity would repeat the fixed-root error already recorded elsewhere in Article VII.

This repairs the overreach identified in the corrected version of [[a_blocked_outward_buffer_creates_a_boundary_straddling_common_core_packet]]. The conclusion here does **not** invoke Lemma 6 of the same-side-extension section and therefore does not require its six-label simultaneous-extension family or an inherited two-coverable complement.

It also does not yet produce an outward repair. The complement of the four- or five-support need not be Hamiltonian. The next gluing statement must add genuine endpoint control. A viable target is: from the connector-free conditions of [[connector_path_exclusion_for_genuine_two_deletion_packets]] and the known tight guard order, either obtain a Hamilton order of one of these bounded supports with a usable corridor-facing endpoint, or force the failed endpoint choices into reverse junctions on the same bounded two-layer interface.
