# Ternary switch insertion has a unique canonical descent root — preserved pre-item development

## Development

## Ternary switch insertion has a unique canonical descent root

Let a ternary one-change deletion witness have word

0^p 1^q,

and insert the omitted coordinate x at the canonical switch gap, immediately after the p-th old coordinate.

Assume the packet is not clipped by a global endpoint; the clipped cases are easier. The three ternary windows containing x have colors

A,B,C.

The outside window immediately to the left, when present, has old color 0, and the outside window immediately to the right has old color 1.

Since the full instance is a counterexample, the complete local word

0,A,B,C,1

is not monotone nondecreasing. Equivalently the packet ABC contains a 10 descent.

A binary word of length three can contain at most one adjacent 10 descent. The nonmonotone packets are exactly

010, 100, 101, 110.

Hence:

### Theorem

Every ternary canonical switch insertion carries exactly one internal 10 descent and therefore exactly one canonical protected physical root.

More explicitly:

- packets 100 and 101 have the descent A B and the root drops the old coordinate at position p-1 and enters the old coordinate at position p+1;
- packets 010 and 110 have the descent B C and the root drops the old coordinate at position p and enters the old coordinate at position p+2.

Both roots cross the true normalized p-cut of the deletion witness.

### Consequence

In ternary Article III there is no arbitrary choice of canonical root at a minimum-first witness. The witness determines one Johnson successor cut. Thus the finite separation alternative and any Sperner/Brouwer labeling built from canonical switch states may be formulated as an honest single-valued edge field on the realized witness set.

This does not prove that the successor cut is itself realized by a good deletion witness.
