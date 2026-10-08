# Every spanning compatible monochromatic connector closes across a homogeneous cut — preserved pre-item development

## Composition

(none yet)

## Development

## Every spanning compatible monochromatic connector closes across a homogeneous cut

Work in the coboundary-flat alternating ternary sector and use the fixed switching-normalized tournament. Partition V=U disjoint-union B, with every vertex of B dominating every vertex of U. Suppose U has a coordinate order C=(c_1,...,c_M), M>=2, whose ternary word is monochromatic zero and whose first and last ordered pairs are forward in this fixed representative. Its reversal C^rev has monochromatic word one and backward endpoint pairs. Assume B has a NOR-good coordinate order P=(b_1,...,b_r).

Then V has an explicit spanning NOR-good order. The connector size and the phase lengths of P are unrestricted.

### Uniform interface and insertion formula

For an adjacent B-pair define
d_i=alpha(b_i,b_{i+1},u)=1 xor t(b_i,b_{i+1}),
where u is any U-vertex. Homogeneous dominance makes this independent of u. Here t(v,w)=1 means v dominates w; d is a scan bit, not the tournament edge bit used in some other subsections.

Write C_0=C and C_1=C^rev. Inserting C_eta at an interior gap b_i|b_{i+1} replaces precisely the two old windows of ranks i-1 and i by
d_{i-1}, eta^M, d_{i+1}.
The M equal bits comprise two windows with one B-coordinate and two U-coordinates, together with M-2 internal connector windows. The equal endpoint bits follow from forward endpoint pairs for C_0 and backward endpoint pairs for C_1. All other B windows are unchanged.

### Monochromatic or very short B-word

If P's word is monochromatic beta, append C_beta. The full word is beta^*,d_{r-1},beta^(M-1). If d_{r-1}=beta it is already good. If d_{r-1} differs, instead append C_(1-beta); the word is beta^*,(1-beta)^*, hence good. For r=1 the sole crossing bit is eta, and for r=2 the word begins d_1 then eta^(M-1); either case is good. An empty B needs no insertion.

### One short phase

Normalize a bichromatic P-word as 0^p1^q, p,q>=1. For a word 1^p0^q, apply the same binary-word argument with every displayed bit complemented; both connector orientations remain available.

If p=1, insert C_eta into the first gap b_1|b_2. The resulting word is eta^M,d_2,1^q. Choose eta=d_2. This is good.

If q=1, insert C_eta into the final gap b_(r-1)|b_r. The resulting word is 0^p,d_(r-2),eta^M. Choose eta=d_(r-2). This is good.

### Two neighboring gaps eliminate the parity drop

Assume p,q>=2.

At gap b_p|b_(p+1), the full word is
0^(p-2), d_(p-1), eta^M, d_(p+1), 1^q.
Both connector orientations fail exactly when
d_(p-1)=1 and d_(p+1)=0.
For every other endpoint pair, selecting eta=0 or eta=1 yields a monotone binary word. This criterion remains valid when p=2 and the displayed zero prefix is empty.

At gap b_(p+2)|b_(p+3), the full word is
0^p, d_(p+1), eta^M, d_(p+3), 1^(q-2).
Both orientations fail exactly when
d_(p+1)=1 and d_(p+3)=0.
The criterion remains valid when q=2 and the displayed one suffix is empty.

Simultaneous failure would force d_(p+1)=0 and d_(p+1)=1. Therefore one of the two gaps and one of the two connector orientations gives a spanning good order.

### Consequence for Article IV

In the switching split B -> z -> A -> x, take U=A union {x,z}. Every B-vertex dominates U. Hence constructing a spanning compatible zero connector on U immediately closes NOR, using a good order on B supplied by minimum-counterexample induction.

The parity-drop residue at the central gap is eliminated by the neighboring-gap argument. No reconfiguration of the B-order is required. The argument of Article III §349 is genuinely size independent.

A five-coordinate seed contained in a larger U remains a proper-subinstance object. This theorem requires the actual connector to contain every vertex of U. Individual reachability and pairwise absorption do not establish that hypothesis.

Thus the strategic frontier is collective compatible connector construction, equivalently a cover of A by two compatible zero paths when x,z remain adjacent (§9).

## Elevation: connector adjacency and minimum size
The proof uses only the homogeneous cut, the constant internal connector word, and its endpoint-pair colors. It does not use adjacency of x,z or minimum-shore extremality. It also applies to M=2: the two crossing endpoint windows supply eta^2 and there are no internal connector windows. Thus the theorem is a general homogeneous-cut composition lemma. In the switching split a growth argument may freely reposition x,z while preserving the two endpoint ports.
