# Genuine two-deletion doubles have a fixed mixed polarity and forced first outward shell

## Metadata

- ID: genuine_two_deletion_doubles_have_a_fixed_mixed_polarity_and_forced_first_outward_shell
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 93
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

## Genuine two-deletion doubles have a fixed mixed polarity and a forced first outward shell

Let
\[
J=(x,c_1,\ldots,c_N,y)
\]
be the full determining span of a protected positive reflected span-two double, and suppose
\[
\kappa_2(H[J])=2.
\]

### The endpoint words are necessarily \(011\) on the left and \(001\) on the right

By [[complete_positive_span_two_double_corridor_classification]], the possible reflected endpoint-word pairs are:

1. left \(001\), right \(001\);
2. left \(011\), right \(011\);
3. left \(001\), right \(011\), which is impossible for disjoint determining windows;
4. left \(011\), right \(001\).

In case (1), the canonical corridor two-cover has one component of order two. In case (2), the symmetric component has order two. But [[one_path_complement_bounds_sharpen_the_genuine_double_corridor_profiles]] proves that in a genuine two-deletion instance every corridor component in a two-cover has order at least five. Hence cases (1) and (2) are impossible. Case (3) is already excluded. Therefore every genuine two-deletion reflected double is of the mixed type
\[
\boxed{\text{left }011,\qquad\text{right }001.}
\]

This removes the same-word branches entirely from the \(\kappa_2=2\) frontier.

### The first outward shell

Write the left selected occurrence as the status block
\[
\epsilon_a\epsilon_{a+1}\epsilon_{a+2}=011,
\]
where \(x=v_a\), \(c_1=v_{a+1}\). If there is an immediately preceding ambient-order vertex
\[
z=v_{a-1},
\]
put
\[
\alpha=h(z,x,c_1)=\epsilon_{a-1}.
\]
If \(\alpha=0\), then
\[
\epsilon_{a-1}\epsilon_a\epsilon_{a+1}=001,
\]
so there is already a positive span-two witness beginning one position farther outward than the selected left occurrence. Consequently, in a chamber having no such farther witness at the adjacent outward start,
\[
\boxed{h(z,x,c_1)=1.}
\]

At the right selected occurrence,
\[
\epsilon_b\epsilon_{b+1}\epsilon_{b+2}=001,
\]
and \(y=v_{b+4}\), \(c_N=v_{b+3}\). If there is an immediately following ambient-order vertex
\[
w=v_{b+5},
\]
put
\[
\beta=h(c_N,y,w)=\epsilon_{b+3}.
\]
If \(\beta=1\), then
\[
\epsilon_{b+1}\epsilon_{b+2}\epsilon_{b+3}=011,
\]
which is a positive span-two witness beginning one position farther outward than the selected right occurrence. Hence absence of such a farther witness forces
\[
\boxed{h(c_N,y,w)=0.}
\]

Thus the genuine two-deletion obstruction has the following immediate trichotomy at its first outward shell:

- a farther positive witness already occurs on the left;
- a farther positive witness already occurs on the right;
- or, whenever both neighboring outer vertices exist, the two shell statuses are forced to be
\[
h(z,x,c_1)=1,\qquad h(c_N,y,w)=0.
\]

These constraints concern the existing ambient order and use only the positive language \(\{001,011,0101\}\). They do not assert that the forced safe shell values by themselves give an outward repair. They are intended to be combined with [[outward_buffer_vertices_bypass_the_internal_two_deletion_obstruction]] and [[exterior_assisted_packet_absorption_gives_an_outward_repair]]: once no farther witness is already present, every failed exterior absorption occurs under these fixed shell orientations rather than under arbitrary boundary data.
