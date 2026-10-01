# Every nonblock four-set in a 3-(8,4,1) design has a canonical complementary matching frame

## Statement

Let U be an eight-element set and F a 3-(8,4,1) family of four-subsets of U. For every four-set C not in F, with D=U-C, there is a unique bijection phi:C->D such that (C-{c}) union {phi(c)} is in F for every c in C. Moreover F is closed under complements, so {c} union (D-{phi(c)}) is also in F for every c. Thus every nonblock four-set is surrounded by four canonically matched complementary block pairs.

## Body

For c in C, the triple C-{c} lies in a unique block, necessarily (C-{c})+d_c with d_c in D; set phi(c)=d_c. If phi(c)=phi(c') for distinct c,c', the two corresponding blocks share three vertices, contradicting lambda=1, so phi is a bijection. For complement closure, fix A in F. Every pair of A lies in lambda_2=3 blocks, so besides A the six pairs account for twelve distinct blocks meeting A in exactly two vertices. Each point of A lies in lambda_1=7 blocks, and those twelve blocks account for all 24 incidences of A-points with blocks other than A. The one remaining block is disjoint from A, hence U-A. Apply this to the four blocks indexed by c.
