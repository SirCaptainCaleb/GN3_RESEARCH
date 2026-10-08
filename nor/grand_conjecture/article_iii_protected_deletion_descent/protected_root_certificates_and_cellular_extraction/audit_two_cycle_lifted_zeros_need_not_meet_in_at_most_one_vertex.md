# Audit: two-cycle lifted zeros need not meet in at most one vertex

## Composition

(none yet)

## Development

## Audit: the two-cycle lifted-zero dichotomy does not imply a one-vertex intersection bound

This audits §188.

The main dichotomy of §188 is valid:

A support-minimal honest lifted zero is either
1. one side-balanced directed simple physical cycle; or
2. the union of two directed simple physical cycles with opposite nonzero side imbalances.

The proof by positive cycle decomposition and support minimality is sound.

However the stated intersection bound for case 2 is not justified.

Let the two cycles be C_+ and C_- with physical vertex sets A and B. Section 188 argues that the target dimension gives at most n+1 distinct lifted labels, and then writes
|A|+|B| <= n+1
because each simple cycle has |A| and |B| edges.

This step is valid only if the two cycle edge sets are disjoint.

Support minimality says that the support of the lifted dependence is exactly
E(C_+) union E(C_-).
It does NOT say the two edge sets are disjoint.

If the cycles share a directed edge or a longer directed path, that shared lifted label appears once in the support with coefficient equal to the sum of the two cycle-flow coefficients. The number of distinct labels is then

|E(C_+) union E(C_-)|
=
|A|+|B|-|E(C_+) cap E(C_-)|,

which may be at most n+1 even when |A cap B| is much larger than one.

Thus the conclusions

- full-support two-cycle zeros are vertex-disjoint or meet in exactly one vertex;
- the only remaining geometry is disjoint cycles or a figure eight

are not established.

A theta-type union with a common directed path is not excluded by the §188 dimension count.

### Correct live statement

The valid structural reduction is:

Every support-minimal honest lifted zero consists of one balanced simple cycle or the union of two oppositely imbalanced simple directed cycles, possibly with overlapping directed paths.

Further reduction requires using overlap geometry and support minimality, not only target dimension.

A useful next invariant is the common directed-path structure. If C_+ and C_- share a maximal directed path P from u to v, then deleting P from each cycle leaves two distinct directed v-to-u return paths. Their union gives a third physical cycle with the reverse orientation on one return path. Side imbalances of these three cycles are linearly related. This should be exploited to show that a long common path either yields a balanced subcycle or permits a support-reducing cycle recombination.
