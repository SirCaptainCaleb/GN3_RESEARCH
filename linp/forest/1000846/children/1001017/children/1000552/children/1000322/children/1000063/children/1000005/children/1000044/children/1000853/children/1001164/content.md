# Class-III systems have no rank-five nonspecial edge

## Statement

Every 12-vertex 5-regular linear triple system has no nonspecial edge of rank five. Consequently, together with the rank-at-least-four reduction and the rank-four exclusion, every Class-III system in the n<=12 strict two-thirds reduction is all-special.

## Body

Let H be a 12-vertex 5-regular linear triple system and suppose, for contradiction, that e={x,y,z} is a nonspecial edge of rank five with unique entrance x; y,z are its terminal vertices.

Each vertex of H has exactly one nonneighbor: its five incident triples contain ten distinct partners among the other eleven vertices. Let
  A=x*, B=y*, C=z*
be the respective unique nonneighbors of x,y,z. These are three distinct vertices outside e. Put U=V(H)\e and let R be the residual hypergraph consisting of the edges of H wholly contained in U.

Every u in U\{A,B,C} is adjacent to each of x,y,z, hence lies in three of the x-,y-,z-stars and has degree 2 in R. Each of A,B,C misses exactly one of x,y,z and lies in the other two stars, hence has degree 3 in R. Thus R has degree multiset
  (3,3,3,2,2,2,2,2,2)
and therefore seven edges.

For v in {y,z}, the four edges through v other than e induce a matching M_v of four pairs on U; M_y leaves B unmatched and M_z leaves C unmatched.

We use the following consequence of nonspeciality repeatedly. If {t,o} is a pair of M_y and R has a three-edge path Q ending at t and avoiding o, then
  Q, {y,t,o}, e
is a five-edge linear path ending in e through entrance y, contradiction. The same holds with z and M_z. Hence every ordered pair arising from M_y or M_z forbids such a residual three-edge precursor.

We also use d9c5b28c09a0: if t is one of A,B,C, o is a degree-two residual vertex, {t,o} is not a residual pair, and there is no three-edge residual path ending at t while avoiding o, then o is adjacent in R to the other two degree-three vertices.

Consider the mates of A in M_y and M_z. They are distinct, since otherwise the two corresponding hyperedges would share A and that common mate.

CASE 1: both mates are degree-three vertices.
Then necessarily M_y pairs A with C and M_z pairs A with B. Hence neither AB nor AC is a residual pair. All three residual edges through A therefore use six degree-two vertices, leaving only four residual edges not through A. But B and C have residual degree three each, giving six B/C incidences among those four edges. At most one of the four edges can contain both B and C, since R is linear; hence the four edges carry at most 2+3=5 such incidences, contradiction.

CASE 2: exactly one mate of A is degree three.
By symmetry suppose M_y pairs A with C, while M_z pairs A with a degree-two vertex r. Then AC is absent from R and Ar is absent from R. Since A has exactly six residual neighbors, it follows that AB is present and r is the only degree-two nonneighbor of A.

By d9c5b28c09a0, r is adjacent to both B and C. Write the residual AB-edge as
  E_AB={A,B,u}.
The three A-edges cover B and the five degree-two vertices other than r.

There are four residual edges not through A. The remaining B/C incidence demand is five: B needs two further incidences and C needs three. Therefore BC must be a residual pair, and among the four non-A edges there is exactly one BC-edge, one further B-edge, and two further C-edges.

The vertex r cannot lie in the BC-edge: if it did, its second residual edge could contain neither A, B nor C, but no all-low residual edge exists in this incidence count. Hence r lies in one B-only edge and one C-only edge.

Write the resulting seven edges, relabeling the five A-neighbor lows, as
  {A,B,u}, {B,C,w}, {C,u,e_0}, {A,w,e_0},
  {A,b,c}, {B,r,b}, {C,r,c}.
Indeed, if there were a three-edge residual path ending at A and avoiding r we would already be done; the absence of such a path forces the three A-pairs against the two r-free non-A edges to cross exactly in this displayed way: the two non-A r-free edges are {B,C,w} and {C,d,e}; an A-edge meeting one must meet the other, otherwise those two edges followed by that A-edge form the required path. Thus their four non-C contact vertices are paired crosswise by two A-edges, and the remaining two low vertices form the third A-edge, giving the displayed normal form.

Now M_z leaves C unmatched and already contains {A,r}. Hence B must be paired to a degree-two residual nonneighbor. In the displayed form the two low nonneighbors of B are e_0 and c.

If M_z pairs B with e_0, then
  {C,r,c}, {A,b,c}, {A,B,u}
is a three-edge residual path ending at B and avoiding e_0.

If M_z pairs B with c, then the four remaining lows are u,w,e_0,b. The two low-low pairs of M_z are forced to be {u,w} and {e_0,b}, because ue_0 and we_0 are residual pairs. But
  {C,r,c}, {A,b,c}, {A,B,u}
is a three-edge residual path ending at u and avoids w. Appending the M_z edge {z,u,w} and then e gives a forbidden five-edge path entering e through z. Thus Case 2 is impossible.

CASE 3: both mates of A are degree-two vertices.
Call them r,s. By d9c5b28c09a0, each of r,s is adjacent in R to both B and C. Since A has two degree-two nonneighbors, it has four degree-two neighbors; together with its six total residual neighbors this forces A to be adjacent to both B and C. Thus AB and AC are residual pairs.

Subcase 3a: BC is not a residual pair.
Then AB and AC occur in two distinct edges
  E_AB={A,B,u}, E_AC={A,C,v}.
The third A-edge is {A,p,q}, and r,s are precisely the two degree-two vertices not adjacent to A.

Because r and s are each adjacent to B and C and have degree two, the remaining four residual edges are
  {B,r,b_r}, {C,r,c_r}, {B,s,b_s}, {C,s,c_s}.
The four symbols b_r,c_r,b_s,c_s are exactly u,v,p,q, each once; moreover b_r,b_s are not u and c_r,c_s are not v by linearity.

If c_r is not u, then
  {C,r,c_r}, {B,r,b_r}, E_AB
is a three-edge path ending at A and avoiding s.
If c_r=u but b_r is not v, then
  {B,r,b_r}, {C,r,u}, E_AC
is such a path, again avoiding s.
The only remaining possibility is c_r=u and b_r=v. Then the four labels force b_s,c_s to be p,q in some order, and
  {C,s,c_s}, {B,s,b_s}, E_AB
is a three-edge path ending at A and avoiding r. In every case one of the two terminal pairs {A,r},{A,s} yields a forbidden terminal entrance into e. Hence Subcase 3a is impossible.

Subcase 3b: all three pairs AB,AC,BC are residual.
There are two ways the three high-high pairs can occur.

First suppose one residual edge is {A,B,C}. The other six residual edges each contain exactly one of A,B,C and two degree-two vertices. Projecting those six edges to their low pairs gives a 2-regular simple graph G on the six degree-two vertices, properly edge-colored by A,B,C, with exactly two edges of each color. Hence G is either C_6 or two disjoint triangles.

Since M_y leaves B unmatched and the high-high pair AC is already residual, M_y pairs A and C to lows and has two low-low pairs. Choose one such low-low pair {t,o}; it is a nonedge of G.

If G is two triangles, t and o lie in different triangles. In the triangle containing o take the unique edge F avoiding o. At t choose an incident edge E whose color differs from the color of F. Then the three residual hyperedges
  F, {A,B,C}, E
form a linear three-edge path ending at t and avoiding o.

If G=C_6, index its vertices cyclically v_0,...,v_5 with t=v_0. A nonneighbor o is at cyclic distance two or three (up to reversal). Let e_i=v_i v_{i+1} and let c_i be its color. For o=v_2, take last edge e_0; among e_3,e_4, both are disjoint from e_0 and avoid o, and since they have different colors at least one has color different from c_0. For o=v_3, if c_4!=c_0 use e_4 and e_0. If c_4=c_0, use e_1 and e_5 unless c_1=c_5; but c_1=c_5 together with c_0=c_4 would force the adjacent edges e_2,e_3 to carry the same third color, impossible. The distance-four case is symmetric. Thus in all cases there are disjoint low edges F,E of distinct colors, with E incident to t and both avoiding o; again
  F, {A,B,C}, E
is a residual three-edge path ending at t and avoiding o. This contradicts the M_y pair {t,o}.

It remains that the three high-high pairs occur in three distinct edges:
  E_AB={A,B,u}, E_AC={A,C,v}, E_BC={B,C,w}.
Each high has one further residual edge F_A,F_B,F_C, and the seventh residual edge T is all-low.

The two low nonneighbors r,s of A are both adjacent to B and C. A low nonneighbor of A adjacent to both B and C can only be w, provided w lies in T, or a common low vertex of F_B and F_C. Therefore both possibilities must occur: w lies in T and
  F_B∩F_C={s}
for one of r,s; the other is w. Write
  F_B={B,s,b}, F_C={C,s,c}.
The remaining two lows p,q form F_A={A,p,q}.

If b!=v, then
  F_B, F_C, E_AC
is a three-edge path ending at A and avoiding w.
If b=v but c!=u, then
  F_C, F_B, E_AB
is such a path, again avoiding w.
Finally, if b=v and c=u, then u and v already have their second residual incidences in F_C and F_B, while w and s are also saturated. Hence p and q must both lie in the all-low edge T in order to reach degree two. But T already contains w, so T={w,p,q}, which shares the two vertices p,q with F_A, contradicting linearity.

Thus the final subcase is impossible.

All possibilities lead to contradiction. Therefore a rank-five nonspecial edge cannot occur in a 12-vertex 5-regular linear triple system.

Together with b9277764ed94 and 09d85d61b8b0, every hypothetical nonspecial edge in Class III is excluded. Hence every Class-III system is all-special.
