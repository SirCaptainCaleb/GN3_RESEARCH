# Seven-label equality shells reduce each side to a Hamiltonian-core or synchronized matching-block core

## Statement

Assume the |S|=7 equality case of 50a62b7e1ffb. In a reachable omission state P|Q|(x), write P=A union {t_1,t_2} with A subset S, |A|=3, and t_1,t_2 in T. Put C=A union {x}. Then C cannot be the cyclic non-Hamiltonian four-set. Hence either C is Hamiltonian, in which case for every Hamilton path (a,b,c,d) on C both {a,b,c,t_1,t_2} and {b,c,d,t_1,t_2} are Hamiltonian; or C is a non-Hamiltonian edge-orderable matching-block K4, and each t_i extends C to a non-Hamiltonian five-set satisfying the same extreme-matching and alternating-middle constraints of smallset01.

## Body

# Local dichotomy on one side of the seven-label equality shell

Assume the equality case |S|=7 from 50a62b7e1ffb. Fix a reachable equitable omission state

P|Q|(x),

where x lies in S. Write

P=A union {t_1,t_2},

with A subset S, |A|=3, and t_1,t_2 in T=V(H)-S.

By the equality theorem, in the six-set

R=P union {x}=A union {x,t_1,t_2},

the two bad five-deletions are exactly t_1,t_2. Therefore the two five-sets

C union {t_1},  C union {t_2},

where C=A union {x}, are both non-Hamiltonian.

We classify the four-set C.

## The cyclic non-Hamiltonian four-set is impossible

The certified small-set theorem says that the exceptional cyclic non-Hamiltonian four-vertex configuration is extended to a Hamiltonian five-set by every fifth vertex. Since both C union {t_1} and C union {t_2} are non-Hamiltonian, C cannot be cyclic non-Hamiltonian.

Thus either C is Hamiltonian or C is a non-Hamiltonian edge-orderable four-set. By the four-set classification, in the latter case C has the matching-block form.

## Hamiltonian-core branch

Suppose C is Hamiltonian and choose a Hamilton path

(a,b,c,d)

on C. Since both C union {t_1} and C union {t_2} are non-Hamiltonian, the certified repeated-bad-deletion lemma applies. It gives both

{a,b,c,t_1,t_2}

and

{b,c,d,t_1,t_2}

Hamiltonian.

So a Hamiltonian core forces two explicit cross-exterior Hamiltonian five-sets containing both excluded T-labels.

## Matching-block branch

Suppose C is non-Hamiltonian. As the cyclic case has already been excluded, C is edge-orderable with its three opposite-edge perfect matchings in strict blocks

M_low < M_mid < M_high.

For each i=1,2, the five-set C union {t_i} is non-Hamiltonian. Therefore the certified matching-block extension theorem applies separately to t_1 and t_2. Each t_i has:

- at least one outgoing edge in M_high and no incoming edge there;
- at least one incoming edge in M_low and no outgoing edge there;
- after choosing a common high/low vertex normalization, the two middle matching edges alternate in direction.

Thus both excluded T-labels are simultaneously constrained by one and the same matching-block structure on C.

This yields the promised dichotomy: every side of a seven-label equality-shell omission state has either a Hamiltonian four-core producing controlled cross-exterior five-paths, or a synchronized matching-block four-core controlling both excluded labels.
