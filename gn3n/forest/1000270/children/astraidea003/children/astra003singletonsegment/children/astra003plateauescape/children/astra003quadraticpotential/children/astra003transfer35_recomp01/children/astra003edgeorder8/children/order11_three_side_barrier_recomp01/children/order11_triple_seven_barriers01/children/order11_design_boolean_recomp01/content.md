# Order-eleven triples force blocked overlap or fourteen Boolean extension families

## Statement

Let H be a hypothetical order-eleven minimum counterexample, let X be any three-set, and put U=V(H)-X. Then either:

(1) there are Hamiltonian four-sets A,B subset U with |A intersection B|=3 such that H[X union A] and H[X union B] are both non-Hamiltonian; or

(2) there is a 14-block 3-(8,4,1) family F of Hamiltonian four-sets in U such that H[X union A] is non-Hamiltonian for every A in F, together with at least fourteen Hamiltonian four-sets C outside F such that H[X union C] is Hamiltonian. Every pair {u,v} subset U lies in at least three such C, and every such C has four distinct members A_T of F, one for each triple T subset C, with A_T intersection C=T. Moreover, for every such C, if D=U-C then D is non-Hamiltonian and for every nonempty proper subset S of D the induced subtournament H[X union C union S] is non-Hamiltonian with path-cover number two.

## Body

Take the fourteen Hamiltonian four-sides supplied by seven balanced 4|4 complements of X from order11_triple_seven_barriers01. Every one has non-Hamiltonian union with X. If two of them intersect in three vertices, outcome (1) holds.

Assume no two of these fourteen four-sets meet in three vertices. Each contains four triples, so their 14*4=56 triples are all distinct. Since U has C(8,3)=56 triples, they exhaust all triples of U and form a 3-(8,4,1) family F.

Let C be any Hamiltonian four-set outside F. For each triple T subset C, let A_T be the unique member of F containing T. The four A_T are distinct: a four-set containing two distinct triples of C would equal C. If H[X union C] were non-Hamiltonian, then C and any A_T would be Hamiltonian four-sets meeting in three vertices whose unions with X are both non-Hamiltonian, contradicting the present branch. Hence every Hamiltonian four-set outside F is Hamiltonian after adjoining X.

Fix a pair {u,v} subset U. By 1000615, among the other six vertices at least six exterior pairs complete {u,v} to Hamiltonian four-sets. In a 3-(8,4,1) family exactly three blocks contain a fixed pair. Therefore at least three Hamiltonian four-sets through {u,v} lie outside F, and all are Hamiltonian after adjoining X. Counting pair incidences gives at least 28*3=84 incidences between pairs of U and such four-sets C. Each C contains six pairs, so there are at least fourteen distinct C. This proves all assertions in (2) up to the final path-cover-two family.

Now fix one such C and put D=U-C. If H[D] were Hamiltonian, a Hamilton path on X union C together with a Hamilton path on D would form a spanning two-cover of H, contradiction. Thus D is non-Hamiltonian. Apply fourset_boolean_pc2_01 to D. Since V(H)-D=X union C, for every nonempty proper subset S of D the induced subtournament H[X union C union S] is non-Hamiltonian with path-cover number two. This completes outcome (2).