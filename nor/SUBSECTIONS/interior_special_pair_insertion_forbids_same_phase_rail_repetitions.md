# Interior special-pair insertion forbids same-phase rail repetitions

## Metadata

- ID: interior_special_pair_insertion_forbids_same_phase_rail_repetitions
- Parent Section: monochromatic_connector_blocks
- Position: 36
- Row version: 2
- Development version: 2
- Composition version: 1
- Composition stale: False

## Composition

Interior x,z insertion replaces two old statuses by (1−e_{j−1},0,0,1−e_{j+1}); z,x gives the corresponding middle 1,1 packet. These exact laws produce good orders on U=A∪{x,z}. The claimed rail exclusions require U-counterexamplehood or a further full-instance extension theorem and are not forced by a larger ambient counterexample.

## Development

## Interior special-pair insertion forbids \(11\) in the zero phase and \(00\) in the one phase along each edge-parity rail

Work in the switching-normalized split
\[
B\to z\to A\to x.
\]
Let
\[
O=(a_1,\ldots,a_k)
\]
be a NOR-good shore order with ternary word
\[
c_1\cdots c_{k-2}=0^p1^q,
\]
and let
\[
e_i=1\iff a_i\to a_{i+1}.
\]

Fix an interior gap \(a_j|a_{j+1}\), with \(2\le j\le k-2\).

### Insert \(x,z\)

Replace the gap by
\[
a_j,x,z,a_{j+1}.
\]
The four new windows replacing \(c_{j-1},c_j\) have colors
\[
1-e_{j-1},\quad 0,\quad 0,\quad 1-e_{j+1}.
\]
Indeed the two central windows use the shore signature
\[
\alpha(a,x,z)=\alpha(x,z,a)=0.
\]

If
\[
c_{j-1}=c_j=0,
\]
then the full order remains NOR-good whenever
\[
e_{j-1}=e_{j+1}=1,
\]
because the replacement packet is \(0000\) and every other window is unchanged.

Therefore in a counterexample,
\[
\boxed{c_{j-1}=c_j=0\Longrightarrow (e_{j-1},e_{j+1})\ne(1,1).}
\]

### Insert \(z,x\)

Now replace the same gap by
\[
a_j,z,x,a_{j+1}.
\]
The four new windows are
\[
1-e_{j-1},\quad 1,\quad 1,\quad 1-e_{j+1}.
\]

If
\[
c_{j-1}=c_j=1,
\]
then the full order remains NOR-good whenever
\[
e_{j-1}=e_{j+1}=0,
\]
because the replacement packet is \(1111\).

Hence in a counterexample,
\[
\boxed{c_{j-1}=c_j=1\Longrightarrow (e_{j-1},e_{j+1})\ne(0,0).}
\]

### Rail form

The odd-index and even-index subsequences of the shore-edge word are therefore constrained separately:

- while two consecutive ternary windows lie in the zero phase, neither parity rail may contain adjacent \(11\);
- while two consecutive ternary windows lie in the one phase, neither parity rail may contain adjacent \(00\).

Together with the endpoint laws
\[
e_1=e_2=0,\qquad e_{k-2}=e_{k-1}=1,
\]
every surviving good shore order has two binary rails that must migrate from zero-dominated left boundary data to one-dominated right boundary data without the forbidden same-phase repetitions.

Thus the unresolved switching-split branch is reduced to the finite-width interface where those two rail migrations meet the unique ternary switch.

Elevation audit: the insertion packets are exact and the rail constraints follow if U=A∪{x,z} itself has no NOR-good order. A full-instance counterexample with nonempty B need not forbid a good U-order. The inherited 00/11 endpoint constraints have the same qualification. The calculation does not unconditionally reduce the ambient connector frontier to a finite-width rail interface.
