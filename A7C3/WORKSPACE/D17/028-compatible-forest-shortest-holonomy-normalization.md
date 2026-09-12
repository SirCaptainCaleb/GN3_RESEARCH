# Shortest comparison holonomy collapses to universal cores or a chord-rigid rim with a three-site exterior defect window

**Workspace:** D17
**State:** established
**Key:** `compatible-forest-shortest-holonomy-normalization`

**Summary:** Choose a shortest directed cycle in the comparison orientation. Star, ordinary-triangle, and ordinary-4-cycle holonomies route respectively to universal one-extension four-cores, five-Hamiltonian directed triangles, and universal Hamilton four-cores. For a shortest ordinary rim Q of length r>=5, every non-rim chord of Q is uniformly SOURCE or SINK relative to all four incident rim edges, not merely every skip-two chord. For any exterior vertex z, each spoke zq_i is LOW, MID, or HIGH relative to the incident rim pair e_{i-1}->e_i; the forbidden fourth state would be a shorter star triangle. Any two MID spokes must lie at cyclic distance at most two, so all MID positions of z lie in one interval of at most three consecutive rim vertices. Consequently, across all cyclic breaks, a source endpoint of a complementary rail yields a rim-expanding SLIDE at every non-LOW spoke, while a terminal endpoint yields one at every non-HIGH spoke. Thus all-break trapping forces source endpoints to be globally LOW and terminal endpoints globally HIGH, creating simultaneous two-ended wall geometry around the entire rim.

### 1. Shortest-holonomy setup
Let H be a hypothetical smallest Strong Level-(1) counterexample and let Gamma=Gamma(H) be the comparison orientation of accepted R887. Assume Gamma is cyclic and choose a shortest directed cycle C. Accepted R887 says C is exactly one of:

1. a local star triangle on three ordinary edges incident with one physical middle vertex;
2. an ordinary triangle on three physical vertices; or
3. for r=|C|>=4, the rim-edge cycle of a simple physical r-cycle Q=(q_0,q_1,...,q_{r-1}), with every cyclic consecutive turn (q_i,q_{i+1},q_{i+2}) tight.

The point of this section is to retain the shortest holonomy itself as the cyclic-branch root rather than charging it as anonymous cycle debt.

### 2. Star holonomy is a universal one-extension four-core
Suppose C is a star triangle. Write its physical support as

  S={v,a,b,c},

with comparison cycle

  va -> vb -> vc -> va,

so equivalently

  (a,v,b), (b,v,c), (c,v,a)                         (SH.1)

are tight. For every physical d outside S, the induced five-set S+d still contains this directed comparison triangle. It is therefore nonintegrable. Accepted R902 gives

  S+d is Hamiltonian for every d outside S.          (SH.2)

Thus a shortest star holonomy is automatically a universal one-vertex Hamilton extension core.

If S itself is Hamiltonian, (SH.2) lands directly in the universal Hamilton four-core setup: S is Hamiltonian and every S+d is Hamiltonian. No further local classification is needed.

Now suppose S is non-Hamiltonian. Then S has no tight Hamilton P4. Apply accepted R516 with the tight trimer (a,v,b) and fourth vertex c. The two same-polarity sign hypotheses required there are forced by P4-freeness. Indeed, if (c,a,v) were tight, then (c,a,v,b) would be a Hamilton P4 using (a,v,b), impossible; hence R3 gives (v,a,c) tight. Likewise if (v,b,c) were tight, then (a,v,b,c) would be a Hamilton P4, so R3 gives (c,b,v) tight. At the same time the star turns (c,v,a) and (b,v,c) make their complete reversals (a,v,c) and (c,v,b) bad. Therefore the R516 alignment bits are exactly 00. Hence

  non-Hamiltonian star support S = the cyclic 00 R516 four-cell.   (SH.3)

Accepted R593 now strengthens (SH.2): for every d outside S there is a Hamilton P5 on S+d in which d occurs one step from an end.

Put Y=V(H)-S. For every d in Y, (SH.2) and accepted R4 imply that Y-d has exact path-cover number two; in particular Y-d is non-Hamiltonian, since a Hamilton Y-d together with a Hamilton S+d would two-cover H. Also Y itself is non-Hamiltonian: if P were a Hamilton path of Y, delete one physical endpoint d of P. The remaining contiguous path P-d Hamiltonizes Y-d, again pairing with S+d to two-cover H. Thus

  Y non-Hamiltonian, and Y-d non-Hamiltonian for every d in Y.   (SH.4)

The small exterior sizes are sharply constrained. Since every set of order at most three is Hamiltonian, (SH.4) first gives |Y|>=5. If |Y|=6, accepted R195 applied to Y says at least four of the six punctures Y-d are Hamiltonian P5 supports, contradicting (SH.4).

Finally suppose |Y|=5 in the non-Hamiltonian-S branch. For each d in Y, use R593 and delete the end vertex s in S adjacent beyond the near-end occurrence of d. This leaves a Hamilton P4 on

  (S-{s}) union {d}.                                  (SH.5)

Thus each of the five d supplies at least one good pair (s,d). Fix s in S and apply R195 to the six-set Y union {s}. At least four of its six five-subsets are Hamiltonian. The deletion of s leaves Y, which is non-Hamiltonian by (SH.4), so for at least four d in Y,

  (Y-{d}) union {s}                                   (SH.6)

is Hamiltonian. Hence for each fixed s at most one d makes (SH.6) fail. Across the four choices of s there are at most four bad complement pairs, whereas (SH.5) supplies at least five good active pairs, one for each d. Choose a pair (s,d) satisfying both (SH.5) and (SH.6). Their supports are disjoint and partition V(H), producing a spanning two-cover, contradiction. Therefore

  star support non-Hamiltonian => |Y|>=7.              (SH.7)

No corresponding |Y|=5 exclusion is asserted here in the Hamiltonian-S branch; that branch is instead handed to the existing universal Hamilton four-core development.

### 3. Ordinary comparison triangle is automatically five-Hamiltonian
Suppose C is the ordinary-triangle case on physical vertices A={a,b,c}. R887 gives the cyclic turns

  (a,b,c), (b,c,a), (c,a,b) tight.                    (SH.8)

For any two distinct exterior vertices d,e, the induced five-set A+{d,e} retains the same directed comparison triangle on the three ordinary triangle edges. It is nonintegrable, so R902 gives

  A+{d,e} is Hamiltonian for every distinct d,e outside A.       (SH.9)

Thus the shortest ordinary-triangle branch lands exactly in the five-Hamiltonian directed-triangle interface already developed elsewhere in D17.

### 4. Ordinary comparison cycles and all-chord rigidity
Suppose C has length r>=4. Write

  e_i={q_i,q_{i+1}},

indices modulo r, so

  e_0 -> e_1 -> ... -> e_{r-1} -> e_0.               (SH.10)

The physical cyclic word Q has every cyclic consecutive turn tight. In particular its support is Hamiltonian, and every cyclic rotation of Q is a Hamilton tight path on the same support.

If r=4, every five-set V(Q)+{d} retains the directed comparison 4-cycle (SH.10), so R902 Hamiltonizes it. Hence the r=4 branch is a Hamiltonian four-core that Hamilton-extends by every exterior vertex.

Now assume r>=5. Let h={q_a,q_b} be ANY non-rim chord of the physical rim, and write d for the forward cyclic distance from a to b, chosen with 2<=d<=r-2. The line-graph vertex h is adjacent to the four rim edges

  e_{a-1}, e_a, e_{b-1}, e_b.                         (SH.11)

Claim: all four comparison arcs between h and the edges in (SH.11) point the same way. Thus exactly one of

  h -> e_{a-1},e_a,e_{b-1},e_b                        (SOURCE(h))

or

  e_{a-1},e_a,e_{b-1},e_b -> h                        (SINK(h))

holds.

Proof. In cyclic order, the four attachment positions split C into directed rim gaps of lengths

  1, d-1, 1, r-d-1.                                   (SH.12)

Every one of these lengths is strictly smaller than r-2. If the four attachment orientations are not all equal, traversing the four attachments cyclically gives an OUT-to-IN transition: for two consecutive attachment vertices f,g in that cyclic list,

  h -> f,    g -> h.

Let ell be the length of the directed C-segment from f to g. By (SH.12), ell<r-2. Hence

  h -> f -> C -> g -> h

is a directed comparison cycle of length ell+2<r, contradicting the choice of C as shortest. This proves all-chord rigidity.       (SH.13)

Thus at every rim vertex q_i the two rim edges e_{i-1}->e_i are consecutive relative to every physical chord whose other endpoint also lies on Q: each such chord lies below BOTH rim edges or above BOTH rim edges. No internal rim chord can occupy the interval between e_{i-1} and e_i.

The old skip-two SOURCE/SINK statement is the special case h={q_{i-1},q_{i+2}}. No parity relation among distinct chord labels is asserted; mixed SOURCE/SINK chord types are possible.

### 5. Exterior spokes have a three-state local alphabet
Fix a physical vertex z outside V(Q), and put

  s_i={z,q_i}.

At q_i the rim pair satisfies e_{i-1}->e_i. The four possible orientations of s_i against this pair reduce to three, because

  e_i -> s_i -> e_{i-1}

would close the directed triangle e_{i-1}->e_i->s_i->e_{i-1}, shorter than r. Hence exactly one of

  LOW_i(z):   s_i -> e_{i-1},e_i,
  MID_i(z):   e_{i-1} -> s_i -> e_i,
  HIGH_i(z):  e_{i-1},e_i -> s_i                       (SH.14)

holds.

Because r>=5, a directed star triangle is itself shorter than C. Therefore at the physical middle z the local tournament on all spokes s_i is acyclic, hence transitive.

### 6. The MID defect set lies in three consecutive rim positions
Let M(z)={i : MID_i(z)}. Take distinct i,j in M(z), and let d be the forward cyclic distance from i to j, 1<=d<=r-1.

If s_i->s_j, then the MID relations give

  s_j -> e_j,
  e_{i-1} -> s_i.

Follow the rim from e_j forward to e_{i-1}. Its length is r-d-1 edges after e_j, so

  s_i -> s_j -> e_j -> e_{j+1} -> ... -> e_{i-1} -> s_i   (SH.15)

is a directed comparison cycle of length r-d+2. Shortestness forces r-d+2>=r, hence d<=2.

If instead s_j->s_i, the symmetric cycle through the forward rim segment from e_i to e_{j-1} has length d+2, so shortestness forces d+2>=r, equivalently r-d<=2. Thus for any two MID positions their cyclic distance in at least one direction is at most two; equivalently their ordinary cyclic separation is at most two.

Since the spoke tournament at z is transitive, the three-point pattern cannot wrap around the rim so as to create a directed spoke triangle. Therefore

  M(z) is contained in one interval of at most three consecutive rim vertices.   (SH.16)

This is a global defect-interval statement forced only by minimal holonomy. Away from a three-site window, every spoke of z is extreme LOW or HIGH.

### 7. Cyclic breaks convert nonextreme exterior endpoints into SLIDEs
Now retain an exact two-covered complement of the Hamilton rim,

  H-V(Q)=U|V,

and orient one complementary rail U=(u_0,u_1,...,u_m). For each i use the cyclic Hamilton break

  Q^(i)=(q_i,q_{i+1},...,q_{i-1}).                     (SH.17)

Consider first the ordered merge seed from terminal q_{i-1} of Q^(i) to source u_0. Its rim-side merge turn is

  (q_{i-2},q_{i-1},u_0).

By (SH.14) this turn is tight exactly when the spoke u_0 q_{i-1} is MID or HIGH. In a counterexample the other merge turn (q_{i-1},u_0,u_1) must then be bad, and the one-bad-hole construction of the SLIDE/DOUBLE section gives the actual maximum-three-forest SLIDE

  (Q^(i),u_0) | U[1,m] | V.                            (SH.18)

Therefore every non-LOW source spoke yields a cyclic break that absorbs the source endpoint u_0 into the rim rail.

Dually consider the seed from terminal u_m to source q_i of Q^(i). Its rim-side turn (u_m,q_i,q_{i+1}) is tight exactly when the spoke u_mq_i is LOW or MID. Hence every non-HIGH terminal spoke gives the SLIDE

  U[0,m-1] | (u_m,Q^(i)) | V.                          (SH.19)

Consequently, if ALL cyclic breaks are DOUBLE for the Q-to-U source family, every u_0-spoke is LOW. If all cyclic breaks are DOUBLE for the U-to-Q terminal family, every u_m-spoke is HIGH. The same statements hold for V.

Moreover in the all-DOUBLE source family, the second bad merge seam reverses by R3 to

  (u_1,u_0,q_i) tight for every i,                     (SH.20)

while an all-DOUBLE terminal family gives

  (q_i,u_m,u_{m-1}) tight for every i.                 (SH.21)

Thus complete cyclic-break trapping does not merely say 'DOUBLE everywhere': it creates a whole-rim two-ended wall. For each reverse rim dimer D_i=(q_{i+1},q_i), both complementary rail sources head-sign D_i and both complementary rail terminals tail-sign D_i.

### 8. Status and the minimal-holonomy extinction target
This section is a cyclic-branch normalization, not closure. It now leaves a much narrower hard object:

- star holonomy: universal one-extension four-core; if non-Hamiltonian, exactly the cyclic 00 R516 cell with exterior order at least seven;
- ordinary triangle: five-Hamiltonian directed-triangle geometry;
- ordinary 4-cycle: universal Hamilton four-core;
- ordinary shortest rim r>=5: every internal chord is globally SOURCE or SINK, every exterior MID defect set lies in at most three consecutive positions, and every complementary endpoint with a nonextreme spoke gives an explicit rim-expanding SLIDE at the corresponding cyclic break.

Hence a rim which traps every cyclic break must push every complementary source into the global LOW sector and every complementary terminal into the global HIGH sector, with the simultaneous wall turns (SH.20)-(SH.21) retained. The next target is to show this all-break wall either admits a multi-cut insertion of the rim into one complementary rail, forces a shorter comparison holonomy, or yields a representative change destroying the chosen minimal obstruction. No additional local DOUBLE subtype is sought.
