# Radius-three support expansion has capacity six, and degree-two equality is a sliding-triple system

## Statement

In the order-thirteen mu=6 shell, let Gamma be the graph on deficient seven-supports, adjacent at Johnson distance at most three. Every vertex R with Hamiltonian complement S has at least two Gamma-neighbors, and more precisely the acquired sets Y(R')=R' intersect S cover S, so sum_{R' in N(R)} d_J(R,R')>=6. If deg_Gamma(R)=2, its two neighbors are both at distance three, their acquired triples partition S, and every deletion label in either triple has a fixed-complement exact-cover family, yielding either relative-order disagreement or the certified common-gap geometry. Consequently, any 2-regular component admits a cyclic sliding-triple representation S_i=T_{i-1} disjoint-union T_i in which every three consecutive T-triples are pairwise disjoint, the move R_i to R_{i+1} drops T_{i+1} and gains T_{i-1}, and both T_{i-2} and T_{i+1} are fixed-support Hamiltonian-deletion label triples for R_i.

## Body

# Radius-three support expansion has capacity six, and degree-two equality is a sliding-triple system

Work in the order-thirteen mu=6 shell. A deficient support is a seven-set R whose longest tight path has order six and whose complementary six-set
S=V(H)-R
is Hamiltonian. Let Gamma join two deficient supports when their Johnson distance is at most three.

## Radius-three expansion and neighborhood capacity

Fix a deficient support R and its complement S. For each s in S, take any exact two-cover
H-s=A_s|B_s.
The universal order-thirteen shell makes both components six-vertex paths. Since they contain all seven vertices of R, one component, say A_s, contains at least four vertices of R. Put
R_s=A_s union {s}.

The support R_s is deficient. Indeed A_s is Hamiltonian, while R_s cannot be Hamiltonian because a Hamilton path on R_s together with the path on B_s would be a spanning two-cover of H. Hence R_s has longest-path order exactly six and its complement B_s is Hamiltonian.

Moreover
d_J(R,R_s)=7-|R intersect A_s| in {1,2,3},
and s belongs to R_s intersect S. Thus every s in S occurs in the acquired set of some Gamma-neighbor of R.

For a neighbor R' define
Y(R')=R' intersect S.
Since R and R' both have size seven,
|Y(R')|=d_J(R,R').
The preceding construction gives the covering relation
S subseteq union_{R' in N_Gamma(R)} Y(R'),
and hence
6 <= sum_{R' in N_Gamma(R)} |Y(R')|
  = sum_{R' in N_Gamma(R)} d_J(R,R').

In particular Gamma has minimum degree at least two: every neighbor has distance at most three, so one neighbor cannot carry all six labels. Equivalently, the six deletion labels in S yield at least two distinct radius-three deficient supports.

## Rigidity at degree two

Suppose N_Gamma(R)={R_1,R_2}. The capacity inequality gives
6 <= d_J(R,R_1)+d_J(R,R_2) <= 3+3,
so equality holds throughout. Therefore both neighbors are at distance three, and
Y_i=R_i intersect S
are disjoint three-sets with
S=Y_1 disjoint-union Y_2.

Fix i and s in Y_i. Let H-s=A|B be any exact two-cover, and choose A to be the unique R-heavier component. As above, A union {s} is a deficient neighbor of R containing s. Of the only two neighbors R_1,R_2, exactly R_i contains s because Y_1,Y_2 are disjoint. Hence
A union {s}=R_i,
so every exact cover of H-s has support partition
(R_i-{s}) | S_i,
where S_i=V(H)-R_i.

Thus each triple Y_i is a fixed-complement three-label deletion family. Choose one Hamilton order Q_i on S_i and use it as the fixed complementary path for all three labels. If two varying Hamilton paths on R_i-{s} disagree in relative order on common vertices, path-intersection calculus yields the standard reversed-edge, reversing-triple, or vertex-simple tight-cycle witness. Otherwise the three covers are pairwise compatible and the compatible-triangle theorem places their three omitted labels at one common insertion gap of the varying class.

So degree-two equality is not merely graph-theoretic: it canonically creates two complementary three-label compatibility families.

## Two-regular components are sliding-triple cycles

Now suppose a connected component of Gamma is 2-regular. Since Gamma is finite and simple, write the component cyclically as
R_0,R_1,...,R_{m-1},
and let
S_i=V(H)-R_i.

For the oriented edge R_iR_{i+1}, put
A_i=R_i-R_{i+1},
B_i=R_{i+1}-R_i.
Degree-two equality makes both A_i and B_i three-sets. At R_i, the acquired triples from its two neighbors partition S_i:
S_i=A_{i-1} disjoint-union B_i.                         (1)

Passing from R_i to R_{i+1} removes A_i from the deficient support and adds B_i, so the complementary support changes by the reverse swap:
S_{i+1}=(S_i-B_i) union A_i
       =A_{i-1} disjoint-union A_i.                    (2)

But equality at R_{i+1} also writes
S_{i+1}=A_i disjoint-union B_{i+1}.
Comparing with (2) gives
B_{i+1}=A_{i-1}.                                       (3)

Set
T_i=A_{i-1}.
Then
S_i=T_{i-1} disjoint-union T_i.
Also the move R_i to R_{i+1} drops
A_i=T_{i+1}
and gains
B_i=T_{i-1}.
Because T_{i+1}=A_i lies in R_i while S_i=T_{i-1} disjoint-union T_i, every three consecutive triples
T_{i-1},T_i,T_{i+1}
are pairwise disjoint.

The fixed-support deletion families propagate around the cycle as well. At R_{i-1}, the neighbor R_i acquires T_{i-2}; degree-two rigidity therefore says that for every s in T_{i-2}, every exact cover of H-s has supports
(R_i-{s}) | S_i.
Similarly the neighbor relation through R_{i+1} gives the same conclusion for every s in T_{i+1}. Hence every vertex of
T_{i-2} union T_{i+1}
is a Hamiltonian deletion label of R_i, and the two triples form two synchronized fixed-complement deletion families at R_i.

This is the complete equality geometry: any 2-regular component is a cyclic sliding system of three-sets with local distance-two disjointness and two rigid deletion triangles at every state. In particular a 5-cycle is impossible, since on five cyclic indices every pair of triples has circular distance at most two and would therefore be disjoint, requiring fifteen vertices. The 3- and 4-cycle specializations leave, respectively, four common vertices or one common vertex outside the displayed triples.

Thus radius-three support expansion has total neighborhood capacity at least six, and the extremal degree-two case is forced into an explicit sliding-triple object rather than an arbitrary cycle.
