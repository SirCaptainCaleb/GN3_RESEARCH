# Every shortcut-free minimum shore of size at most six has a spanning compatible connector

## Composition

The stated small shores split into two transitive classes and yield spanning compatible connectors. This is a finite base theorem, not a general growth principle or a reason to replace the arbitrary-shore problem by ever-larger checks.

## Development

## Every shortcut-free minimum shore of size at most six has a spanning compatible connector

Use the two-transitive-block connector theorem from the monochromatic-connector section:

> If
> \[
> A=L\sqcup R
> \]
> with \(L,R\) nonempty transitive subtournaments, then ordering \(L\) and \(R\) in dominance order gives
> \[
> L,x,z,R
> \]
> as a compatible monochromatic zero connector on \(A\cup\{x,z\}\).

We apply this to small shores.

### Sizes four and five

Every tournament on at least three vertices contains a transitive triple unless all its triples are cyclic. A four-vertex tournament has at most two cyclic triples, so it contains a transitive triple. The same conclusion for five vertices follows by restricting to any four vertices.

Thus for
\[
|A|=4
\]
choose a transitive triple \(L\); the remaining singleton \(R\) is transitive.

For
\[
|A|=5,
\]
choose a transitive triple \(L\); the remaining two vertices form a transitive \(R\).

Hence every shore of size four or five splits into two nonempty transitive blocks and has a spanning compatible connector.

### Size six

The six-vertex counting theorem in the connector section proves more strongly that every six-vertex tournament contains complementary transitive triples. Hence size six also has a spanning compatible connector.

### Consequence

The size-three shore was already closed explicitly by the five-coordinate connector insertion. Therefore every shortcut-free minimum shore surviving all current connector constructions satisfies
\[
\boxed{|A|\ge 7.}
\]

This lower bound uses only elementary tournament structure and the exact compatible-connector splice theorem. It does not use the earlier, audited-away edgewise triangle-cover claim.
