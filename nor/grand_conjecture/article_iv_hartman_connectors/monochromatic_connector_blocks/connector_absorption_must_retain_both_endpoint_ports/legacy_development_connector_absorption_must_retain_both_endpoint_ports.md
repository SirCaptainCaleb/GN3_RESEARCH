# Connector absorption must retain both endpoint ports — preserved pre-item development

## Composition

(none yet)

## Development

## Connector absorption must retain both endpoint ports

The collective connector state consists of a monochromatic zero order C together with forward first and last ordered tournament pairs. Absorption moves must preserve all three requirements.

### Endpoint absorption has an extra condition

If c_1 -> c_2, then s_1=alpha(a,c_1,c_2)=0 has two possible tournament meanings: a dominates both c_1,c_2, or both c_1,c_2 dominate a. Prepending a gives a compatible connector only in the first case. In the second case the new first pair (a,c_1) is backward.

Similarly, s_(m-1)=0 allows a on either side of the final forward pair. Appending preserves compatibility only when that final pair dominates a.

Consequently failure of compatible absorption does not imply that the insertion scan starts and ends in one. The blocker theorem Article III §360 states a criterion for monochromatic insertion. Its endpoint condition must be strengthened before using it in a maximal compatible-connector argument.

### The no-010 restriction concerns one-runs

For a genuine interior gap 2<=i<=m-2, insertion changes the three windows to (s_(i-1),1-s_i,s_(i+1)) and preserves the endpoint pairs. It succeeds precisely on 010.

Thus absence of 010 excludes isolated internal one-runs. It imposes no lower bound on the length of a zero-run. In particular a distinguished zero at the xz-edge may sit inside 101. The concluding zero-run length assertion in Article IV §5 requires correction.

### Flat boundary data and the repair graph

The flatness calculations at a scan 1-to-0 or 0-to-1 boundary remain valid. A flat boundary supplies a local transition-removal move. To use that move as an edge of the reversible connector complex, prove that its full output remains monochromatic zero, retains both forward endpoint pairs, and retains the specified connector coordinates. These are additional state-preservation obligations.

The useful research state is a pair of disjoint compatible zero paths covering a subset of A, or equivalently the full connector P,x,z,Q. A growth move must increase covered support while preserving the ports; an exchange may preserve support and must belong to an explicitly verified reversible graph. Individual seed absorption alone does not supply the Sperner boundary condition for every such state.
