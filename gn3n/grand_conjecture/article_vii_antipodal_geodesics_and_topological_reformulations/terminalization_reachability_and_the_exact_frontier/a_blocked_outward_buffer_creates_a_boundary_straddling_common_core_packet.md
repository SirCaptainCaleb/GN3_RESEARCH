# Correction: blocked outward buffers give a family of rooted reversers

## Composition

(none yet)

## Development

## Correction: a blocked outward buffer produces a second rooted reverser, but not automatically a common-core packet

Retain the genuine two-deletion mixed double from [[genuine_two_deletion_doubles_have_a_fixed_mixed_polarity_and_forced_first_outward_shell]]:
\[
J=(x,c_1,\ldots,c_N,y),
\]
with left endpoint word \(011\) and right endpoint word \(001\).

Consider the left side and let \(z\) be any ambient-order vertex strictly to the left of \(x\). The selected left \(011\) begins with
\[
h(x,c_1,c_2)=0,
\]
so boundary antisymmetry gives
\[
h(c_2,c_1,x)=1.
\]

Suppose \(z\) is blocked for the left buffer replacement of [[outward_buffer_vertices_bypass_the_internal_two_deletion_obstruction]], i.e.
\[
h(z,c_1,c_2)=0.
\]
Then
\[
h(c_2,c_1,z)=1.
\]
Thus every blocked left buffer vertex \(z\) becomes a second reverser, alongside \(x\), of the same rooted corridor edge \(c_2c_1\). By reverse-complement symmetry the analogous statement holds at the right boundary.

This is a valid and useful boundary-straddling rooted relation. However an earlier draft of this addendum overreached by invoking Lemma 6 of [[endpoint_transport_and_small_support_gluing_two_same_side_extension_vertices]] directly from these two reverse triples. That lemma is proved inside a more specific two-cover/extension setup: its Ramsey argument uses a six-label family of simultaneous extension tests and a two-coverable complement inherited from that setup. Two isolated reverse triples do not by themselves supply those hypotheses. Therefore the common-four-core conclusion cannot be imported here without constructing the required ambient extension family.

### Correct enlarged-window consequence

Combine the rooted reversal observation with [[outward_buffer_vertices_bypass_the_internal_two_deletion_obstruction]].

If both outward sides are nonempty, then either:

1. the two-sided buffer criterion succeeds, giving an outward repair using vertices outside \(J\); or
2. at least one outward side is completely blocked, and every vertex on that side is a common reverser, with the selected exterior endpoint, of one fixed exposed corridor edge.

If the first outward shell already contains a positive word, [[genuine_two_deletion_doubles_have_a_fixed_mixed_polarity_and_forced_first_outward_shell]] instead supplies a strictly farther positive witness.

Hence the surviving no-repair/no-farther-witness branch has a uniform rooted polarization:
\[
h(c_2,c_1,z)=1
\]
for every vertex \(z\) on a blocked left side, or its right-hand mirror. This is stronger than a single failed buffer and is genuinely information involving vertices outside \(J\).

The next structural step must exploit the **family** of common reversers. One legitimate route is to build, from several blocked vertices, the full extension family required by the two-reverse-triples/common-core lemma; another is to combine the common reversers with the assisted-connector tests of [[exterior_assisted_packet_absorption_gives_an_outward_repair]]. What is not legitimate is to infer a Hamiltonian common core from one pair of reverse triples alone.
