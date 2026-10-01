# The design branch forces paired deletion covers with a common three-side

## Statement

Let H be a hypothetical order-eleven minimum counterexample, let X be a three-set, and let U=V(H)-X. Assume the design alternative of order11_design_boolean_recomp01. Then there exist distinct a,b in U and disjoint three-sets T,R with U=T disjoint-union R disjoint-union {a,b} such that, writing Y=X union T and S=R union {a,b}: (1) Y union {a} and Y union {b} are Hamiltonian; (2) S is Hamiltonian and its Hamiltonian deletion labels are exactly the three vertices of R, equivalently S-{a} and S-{b} are non-Hamiltonian while S-r is Hamiltonian for every r in R; (3) Y is non-Hamiltonian with path-cover number two; (4) H-a has a two-cover (Y union {b}) | R and H-b has a two-cover (Y union {a}) | R, so these two deletion covers share the same three-vertex side R; (5) no Hamilton path of H[S] has a or b as an endpoint.

## Body

Let E be the family of extendable Hamiltonian four-sets C outside the 3-(8,4,1) family F supplied by the design alternative of order11_design_boolean_recomp01. Thus |E|>=14, every pair of U lies in at least three members of E, and for every C in E its complement U-C is non-Hamiltonian.

First, E contains two members meeting in three vertices. Suppose not. Then each triple of U lies in at most one member of E, so 4|E|<=C(8,3)=56. Hence |E|=14 and every triple lies in exactly one member of E: E itself is a 3-(8,4,1) family. Fix C in E. In such a family every pair lies in exactly three blocks and every vertex lies in exactly seven blocks. Excluding C, the six pairs of C contribute 12 pair-block incidences with the other thirteen blocks. Since no other block meets C in three vertices, exactly twelve other blocks meet C in two vertices. Those twelve contribute all 24 outside point incidences with C, so the thirteenth block is disjoint from C and equals U-C. Then both C and U-C lie in E, impossible because X union C and U-C would be complementary Hamiltonian supports. Hence some C=T union {a}, C'=T union {b} in E satisfy |C intersection C'|=3. Put R=U-(T union {a,b}), Y=X union T, and S=R union {a,b}.

Because C,C' are extendable, Y+a and Y+b are Hamiltonian. Their U-complements are R+b=S-a and R+a=S-b, both non-Hamiltonian. Apply the strengthened theorem 1000858 to the three-set R and exterior labels a,b. It gives that S is Hamiltonian and that its Hamiltonian deletion labels are exactly R: S-r is Hamiltonian for every r in R, whereas S-a and S-b are not.

The disjoint sets Y,S partition V(H). Since S is Hamiltonian, Y cannot be Hamiltonian or H would have a spanning two-cover; minimum-counterexample calculus gives pc(Y)=2. Since R is a three-set it is Hamiltonian, so deleting a gives the two-cover (Y+b)|R and deleting b gives (Y+a)|R. Finally, if a or b were an endpoint of a Hamilton path on S, deleting it would leave a Hamilton path on S-a or S-b, contradiction.
