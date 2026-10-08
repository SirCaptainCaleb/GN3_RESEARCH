# A lexicographic run potential eliminates the final isolated-singleton residue

## Metadata

- ID: a_lexicographic_run_potential_eliminates_the_final_isolated_singleton_residue
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 254
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## A lexicographic run potential eliminates the final isolated-singleton residue

Continue in the coboundary-flat alternating ternary sector and consider a full order with global word
\[
0^A\,1\,0^C,\qquad A,C\ge1.
\]

Root §250 proves that every singleton curvature type except one either closes NOR or produces another global two-change order with strictly larger leading zero run \(A\).

The sole surviving table is the full-left / flat-right, holonomy-one case on five consecutive coordinates
\[
(a,b,c,d,e),
\]
with
\[
abc=0,\quad bcd=1,\quad cde=0,
\]
and
\[
abd=1,\ abe=1,\ acd=0,\ ace=0,\ ade=0,\ bce=1,\ bde=0.
\]

We now eliminate this residue by refining the extremal potential.

### Right endpoint swap

Swap only the final pair:
\[
(a,b,c,d,e)\longmapsto(a,b,c,e,d).
\]

The three internal statuses become
\[
\alpha(a,b,c)=0,
\]
\[
\alpha(b,c,e)=1,
\]
and, by alternation,
\[
\alpha(c,e,d)=1-\alpha(c,d,e)=1.
\]
Thus the local packet changes from
\[
010
\]
to
\[
011.
\]

The ordered left pair \((a,b)\) is unchanged, so every window on the left boundary and farther left is unchanged. Therefore the leading zero run still has length exactly \(A\).

### The exported right windows remain in one band

If there is a next coordinate \(f\), the original global singleton hypothesis gives
\[
\alpha(d,e,f)=0.
\]
After the swap,
\[
\alpha(e,d,f)=1-\alpha(d,e,f)=1.
\]
Hence the new 1-band extends through this crossing window as well.

If a further coordinate \(g\) exists, put
\[
u=\alpha(d,f,g)\in\{0,1\}.
\]
The next window \(\alpha(f,g,h)\), when present, is an untouched old trailing-zero window and therefore equals \(0\).

Consequently the entire changed right packet has the form
\[
0,1,1,1,u,0
\]
with the terminal entries omitted at the endpoint.

For either value of \(u\), all 1s form one contiguous run. Thus the new global word still has at most two changes. If the trailing zero phase disappears, NOR closes immediately. Otherwise the new word is
\[
0^A1^{B'}0^{C'}
\]
with
\[
B'\ge2>1.
\]

### Lexicographic potential

Among all full orders whose word has exactly two changes and whose first and last colors are \(0\), maximize lexicographically
\[
(A,B),
\]
where
\[
0^A1^B0^C
\]
is the word.

The comparison class is finite.

- Every branch handled in §250 either closes NOR or strictly increases \(A\), hence strictly improves \((A,B)\).
- In the sole §250 residual branch, the right endpoint swap above preserves \(A\) and strictly increases \(B\).

Therefore no lexicographically maximal two-change order can have \(B=1\).

### Theorem

In the coboundary-flat alternating ternary sector, a global isolated-singleton order
\[
0^A1\,0^C
\]
cannot be extremal in the two-change class. There is always either:

1. a spanning NOR-good order; or
2. another global two-change order with strictly larger lexicographic potential \((A,B)\).

By reversal/color normalization the same holds for the complementary singleton orientation.

### Carrier consequence

The first five-position equality states of §§241–242 are global isolated-singleton witnesses. Combining §§246,250 with the lexicographic refinement above removes the last singleton residue without leaving the full-order comparison class.

Thus a five-position consecutive-change carrier zero has no terminal singleton obstruction in the coboundary-flat alternating sector: every supporting singleton state admits a terminating full-order improvement to NOR or to a wider/shifted two-change band.

## Frontier

- Development version when composed: None
- Development version now: 1
