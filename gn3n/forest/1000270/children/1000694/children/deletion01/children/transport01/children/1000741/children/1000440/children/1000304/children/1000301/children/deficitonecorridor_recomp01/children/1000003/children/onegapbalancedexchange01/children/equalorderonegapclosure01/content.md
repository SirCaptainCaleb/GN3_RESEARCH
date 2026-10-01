# An equal-order one-gap comparison has no neutral insertion residue

## Statement

Let H be a minimum counterexample, let A be a globally longest tight path of order lambda, and let B be another tight path of order lambda whose common vertices with A occur in the same relative order and which agrees with A outside one common-vertex gap. Put O=V(A)-V(B) and E=V(B)-V(A), so |O|=|E|. Then either |E|<=1, in which case the discrepancy-gap support has order at most four when the gap is internal and at most three when it is an endpoint gap, or at least one of the following occurs: (1) H contains a proper Hamiltonian support of order four or five whose complement is non-Hamiltonian with path-cover number two; (2) explicit order disagreement occurs; or (3) an explicit reversed tight triple occurs at one of the at most two splice junctions around a consecutive pair of exterior vertices. Thus an equal-order one-gap comparison of two globally longest paths has no balanced or connector residue.

## Body

Assume |E|>=2 and choose consecutive vertices x,y of the E-block in the displayed order of B. Since x,y lie outside the globally longest path A, the certified longest-path paired-noninsertion theorem 6839f08d0cf8 applies. Its Hamiltonian four- or five-support outcomes give (1), using minimum-counterexample calculus for the complement.

Suppose it gives a direct connector D from x to y through an A-interval. If that interval contains exactly one A-vertex z, then D is a tight cross triple and is handled by the cross-triple paragraph below. Otherwise the interval contains at least two A-vertices. If it contains a vertex of A∩B, then D places such a common vertex strictly between x and y while B does not, yielding order disagreement. Otherwise the interior of D lies in O and is disjoint from B. Replace the edge xy of B by D. All internal triples are tight and only the at most two junction triples can be new. If all existing junction triples were tight, the splice would be a tight path of order at least lambda+2, contradicting maximality of A. Hence a junction is non-tight and boundary antisymmetry gives (3).

Now suppose the paired-noninsertion theorem gives a tight cross triple through z in V(A), including the one-vertex connector case just set aside. If its orientation orders y before x, it disagrees with B. If z lies in A∩B, the three-vertex path through z places z between the consecutive B-vertices x,y although z is not between them in B, again giving order disagreement. The remaining case has z in O and orientation (x,z,y). Replace xy by (x,z,y). If every existing junction were tight, this would be a tight path of order lambda+1, again contradicting maximality. Thus a junction fails and its reverse is tight, giving (3).

These cases exhaust the paired-noninsertion menu. If |E|<=1, equal cardinality gives |O|<=1, so the stated gap-support bounds are immediate.
