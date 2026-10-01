# Carrier-label parity constraint for spanning paths in low-2-rank STS

## Statement

Let S be an STS(v) whose binary block-incidence code has rank v-m with m>=2. By the Assmus/Jungnickel--Tonchev carrier description, label the points by columns h(x) in F_2^m of a parity-check matrix: each nonzero label occurs w times and 0 occurs w-1 times, where v=w2^m-1. If S contains a spanning linear path and J is its joint set, then XOR_{x in J} h(x)=0. Equivalently, the set of carrier classes containing an odd number of joints is a zero-sum subset of F_2^m.

## Body

Let C be the binary span of the block-incidence vectors. For a spanning linear path, the incidence-code constraint gives 1_V+1_J in C. Let H be the m by v parity-check matrix of C supplied by the carrier theorem. Hence H(1_V+1_J)^T=0.

It remains to evaluate H1_V^T, the xor of all carrier columns. Each nonzero vector of F_2^m occurs w times and the zero vector contributes nothing. For m>=2 the xor of all nonzero vectors of F_2^m is 0; multiplying every multiplicity by w does not change this. Thus H1_V^T=0, and therefore H1_J^T=0, i.e. XOR_{x in J}h(x)=0.

For w=1 this recovers the projective hyperplane/vector-sum obstruction. For w>1 it supplies the exact parity projection of any spanning-path joint set to the carrier geometry. The classification of the parity-check columns is Theorem 2.1 of Jungnickel--Tonchev, Counting Steiner triple systems with classical parameters and prescribed rank.
