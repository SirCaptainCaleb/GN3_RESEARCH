# A non-Hamiltonian five-set has either a complete pc2 punctured cube or one Hamiltonian singleton exception

**Summary:** A non-Hamiltonian five-set gives a complete pc2 punctured cube, or one unique Hamiltonian singleton whose complementary non-Hamiltonian K4 carries the full codimension-four structure package.

## Statement

Let H be a minimum counterexample and let F be a non-Hamiltonian five-vertex set. Put K=H-F. Then exactly one of the following holds. (1) For every nonempty proper subset S of F, K union S is non-Hamiltonian with path-cover number two. (2) There is a unique vertex d0 in F such that F-{d0} is non-Hamiltonian and K union {d0} is Hamiltonian; for every other nonempty proper subset S of F, K union S is non-Hamiltonian with path-cover number two. In outcome (2), the proper Hamiltonian set K union {d0} has the non-Hamiltonian four-set F-{d0} as its complement, so the full codimension-four Hamiltonian-side structure theorem codim4_01 applies to this exceptional state. Thus the 30 nonempty proper extension states of K form either a complete pc2 punctured five-cube, or a pc2 punctured cube with one uniquely identified Hamiltonian singleton exception carrying the complete codimension-four complement structure.

## Body

By nonham_five_punctured_pc2_cube02, every extension K union S with 2<=|S|<=4 is non-Hamiltonian with path-cover number two, and at least four singleton extensions K+d are non-Hamiltonian with path-cover number two. The five-vertex small-set theorem gives at most one label d0 for which F-{d0} is non-Hamiltonian. If there is no such label, all five singleton extensions are pc2 and (1) holds.

Otherwise d0 is unique. The proper induced subtournament K+{d0} has path-cover number at most two by minimum-counterexample minimality. If it is non-Hamiltonian, it has path-cover number exactly two, so again all 30 nonempty proper extension states are pc2 and (1) holds. If it is Hamiltonian, then it is the unique singleton state not pc2, while all other 29 states are pc2 by the punctured-cube theorem, giving (2). Uniqueness of the exceptional singleton follows from uniqueness of the non-Hamiltonian four-deletion.

In outcome (2), K+{d0} and F-{d0} are complementary proper induced sets, the former Hamiltonian and the latter a non-Hamiltonian four-set. Therefore the hypotheses of codim4_01 hold with Hamiltonian side K+{d0} and four-vertex complement F-{d0}; every certified structural consequence in that codimension-four package is available at the unique exceptional singleton state.

## Metadata

- ID: nonham_five_pc2_cube_exact01
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
