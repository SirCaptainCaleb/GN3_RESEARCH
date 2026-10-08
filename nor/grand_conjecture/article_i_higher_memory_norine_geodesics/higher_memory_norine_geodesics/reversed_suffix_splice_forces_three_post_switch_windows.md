# Audit: reversed-suffix propagation requires unproved switch polarization

## Composition

(none yet)

## Development

## Audit

The earlier version attempted to propagate a common-tail deletion cycle through a reversed post-switch suffix and claimed q>=3.

That argument depended on the former first-post-switch polarization claim. The latter is unsupported for q>1 because it was obtained after truncating to a proper subset and then incorrectly importing full-counterexample endpoint blocking and bad-cut constraints.

Accordingly the q=2 exclusion and the deeper blocking identities stated in the earlier version are not proved.

The valid conclusion from this line is the full-ground-set singleton-final-run theorem: a common-tail deletion 3-cycle cannot have q=1.

A repair would need a splice using every ambient vertex, or a theorem that reattaches every removed final-run vertex while preserving the one-change structure.
