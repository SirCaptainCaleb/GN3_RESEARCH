# An energy-minimal portal-C4 representative cannot be locally terminal

**Workspace:** D17
**State:** established
**Key:** `universal-one-extension-portal-c4-local-extinction`

**Summary:** Parent extinction theorem for the surviving k>=8 portal-only pair-core C4. Choose an exact H-s two-cover F minimizing the four-cut energy Sigma. Coarsen only by T versus Y and let b_T,b_Y be maximal block counts, e=e_F(T,Y); then b_T+b_Y=2+e and b_T is 1,2,or3. If b_T=1, T has degree one or two. Degree one is the already-current unique-core-crossing branch; degree two gives a literal Hamilton P5 x-T-y. Opposite rim neighbors contradict the forbidden diagonal, while every other pair has Hamilton endpoint replacements S+x,S+y, so R966 exports. If b_T=2, T is one dimer block plus one singleton. When b_Y>=3, an exact Y two-cover must cross inherited Y-components and can be lifted to an actual maximum forest, giving current component-drop geometry. When b_Y=2, both T-blocks are endpoint blocks. Testing the outward turn from the singleton into the free dimer end either gives a one-edge exact-cover surgery strictly lowering Sigma, contradicting minimality, or R3 gives a tight trimer selecting the dimer oppositely, currentized by R4. If b_T=3 and b_Y>=3, the same component-drop export applies. The only rigid b_T=3 case has b_Y=2, so the three T vertices are singleton endpoint blocks attached to an exact Y=A|B cover. If S is non-Hamiltonian, R157 at the three attached residual endpoints gives endpoint-indexed maximum forests. If S is Hamiltonian, any Hamilton order of S is assembled from the singleton s by three successive leaf transfers, yielding an explicit length-three walk from {s}|F to S|A|B. Therefore an output-free Sigma-minimizer does not exist. The portal C4 is locally extinguished: it must hand off to actual/closed maximum-forest dynamics, fixed-complement/high-transition reversal dynamics, current residual component-drop geometry, or a strict lower-energy representative.

### 1. Energy-minimal portal-C4 representative
Retain accepted R927 Arm M in the surviving portal-only pair-core C4 range k>=8. Thus S is universally one-vertex Hamilton-extendable, fix s in S and put

  T=S-{s},
  Y=V(H)-S,

with rim labels a,b,c,d as in the pair-core C4. The four perimeter portal cuts are fixed graph-intrinsically.

Among all literal exact two-covers F of H-s choose one minimizing

  Sigma(F)=tau_ab+tau_bc+tau_cd+tau_da.                 (PE.1)

Such a minimum exists because H is finite.

Forget the six-type refinement temporarily and coarsen F only by the partition

  T | Y.

Let b_T be the number of maximal nonempty T-blocks in the two F-rails, b_Y the corresponding number of Y-blocks, and

  e=e_F(T,Y)

its selected T|Y transition count. Elementary block counting gives

  b_T+b_Y=2+e.                                          (PE.2)

Because |T|=3,

  b_T in {1,2,3}.                                       (PE.3)

We show that every possibility yields a current parent output or contradicts the minimality in (PE.1).

### 2. One T-block is never terminal
Assume b_T=1. The T-block cannot be an entire F-rail because every Arm-M singleton-deletion rail has order k>=8 while |T|=3. Hence its quotient degree is one or two.

#### Degree one
Then e=1 and (PE.2) gives b_Y=2. This is exactly the unique-core-crossing geometry already consumed by SV31933/SV35429. If S is non-Hamiltonian, the fixed residual two-cover exports by universal-extension endpoint surgery to an actual fresh maximum forest. If S is Hamiltonian, SV35429 gives an explicit maximum-forest walk of length at most two from the singleton-rooted representative to the S-rooted representative. Thus this branch is current.

#### Degree two
Let x,y be the two physical Y-neighbors of the T-block. The literal segment

  x - T - y                                             (PE.4)

is a Hamilton P5 on T+{x,y}, exposing x,y as its endpoints.

If x,y are the two opposite rim labels a,c or b,d, (PE.4) Hamiltonizes one of the forbidden pair-core diagonals, contradiction.

In every other case, universal one-extension gives Hamilton endpoint-replacement supports

  S+x,
  S+y.

Therefore accepted R966 applies to (PE.4) with exterior vertex s. Its Hamilton-six-extension branch is a proper Hamilton path and currentizes by R4. Reverse-trimer and proper-cycle outputs currentize by R4 / the movable-break orbit. Its selected-reversal species currentizes by the fixed-complement/high-transition split of SV34757. Hence b_T=1 has no local terminal state at any value of Sigma.

### 3. Two T-blocks: component drop or strict core consolidation
Assume b_T=2. Then T consists of one oriented dimer block and one singleton block. By (PE.2),

  b_Y=e.                                                (PE.5)

#### At least three Y-blocks
If b_Y>=3, choose an exact two-cover

  Y=U|V                                                 (PE.6)

which exists because Y is non-Hamiltonian and proper. Since F[Y] has b_Y>=3 components, U|V must select at least b_Y-2 physical edges joining distinct F[Y]-components. Retain one such edge h.

This component drop is current. If S is Hamiltonian, the maximum forest

  S | U | V                                             (PE.7)

retains h literally. If S is non-Hamiltonian, accepted R157 applies to any endpoint r of U or V. Choose an endpoint not incident with h; this is possible because both residual rails are nontrivial and h has only two endpoints. The R157 graft on S+r deletes only the terminal residual state at r, so the resulting actual maximum forest retains h. Thus b_Y>=3 exports a named residual component-crossing state in current maximum-forest space.

#### Exactly two Y-blocks
Assume b_Y=2. Then e=2, so both T-blocks have quotient degree one.

Write the oriented dimer block as (p,q) and the singleton T-vertex as r. Suppose first that the dimer occurs locally as

  (p,q,y,...)                                           (PE.8)

so p is its free end; the singleton r has its own unique Y-attachment.

Test the outward turn (r,p,q).

If it is tight, delete r's unique Y-attachment and add the edge rp. Exactly as in SV36110, the two path components remain two and the new local rail is

  (r,p,q,y,...).                                        (PE.9)

The deleted T|Y edge has positive four-cut weight: weight two for a rim attachment and weight four for a W attachment. The added T-T edge has weight zero. Hence the new exact H-s cover F' satisfies

  Sigma(F') < Sigma(F),                                 (PE.10)

contradicting the choice of F.

If (r,p,q) is bad, R3 gives the tight trimer

  (q,p,r),                                              (PE.11)

which selects the same physical dimer {p,q} in the opposite direction from F. Restoring s makes {s}|F an actual maximum forest containing p->q, while R4 currentizes the proper trimer (q,p,r) in another actual maximum forest containing q->p. Thus failed descent is a current same-dimer reversal.

If the dimer occurs as (...,y,p,q), use the exact forward dual test (p,q,r): tight gives strict descent by deleting r's attachment and adding qr, while bad gives the reverse-dimer trimer (r,q,p). No path reversal is used.

Therefore b_T=2 is never output-free at a Sigma-minimum.

### 4. Three T-blocks: component drop or a three-leaf crown
Assume b_T=3. Then all three T-vertices are singleton blocks. Equation (PE.2) gives

  b_Y=e-1.                                              (PE.12)

Every singleton T-block has positive quotient degree, so e>=3.

If b_Y>=3, the current component-drop argument of Section 3 applies verbatim: compare F[Y] with an exact Y two-cover and lift one named crossing state to an actual maximum forest using S or R157.

It remains only

  b_Y=2,
  e=3.                                                  (PE.13)

Then every T-singleton has degree exactly one. Deleting T from F therefore gives an exact residual two-cover

  Y=A|B,                                                (PE.14)

and the three T-vertices are three distinct leaf endcaps attached to three endpoints of A|B.

### 5. Non-Hamilton S: the three-leaf crown is an R157 graft fan
Assume S is non-Hamiltonian. Universal one-extension and (PE.14) put us exactly in accepted R157.

For each of the three residual endpoints r_i to which a T-singleton is attached, choose any Hamilton path P_i on S+r_i. R157 says r_i is internal in P_i and gives the actual maximum forest

  P_i | (R_i-r_i) | R_i^opp,                            (PE.15)

where R_i is the residual rail of A|B containing r_i and the opposite residual rail survives literally.

Thus the rigid three-leaf crown produces three endpoint-indexed current universal-extension graft representatives on one fixed exact residual cover. It is a current maximum-forest fan, not a terminal C4 state.

### 6. Hamilton S: the crown has an explicit length-three exchange walk
Assume S is Hamiltonian and choose any Hamilton order

  Q=(q_0,q_1,q_2,q_3)                                   (PE.16)

on S. One q_j is s and the other three are exactly the T-vertices.

Restore s to F:

  F_0={s}|F.                                            (PE.17)

This is an actual maximum spanning three-forest. Also

  F_1=Q|A|B                                             (PE.18)

is an actual maximum forest.

Each T-vertex is a leaf endcap of F. Starting from the singleton component {s}, grow the contiguous Q-subpath one vertex at a time in either direction away from s. At each step, take the next T-vertex t in Q, delete its unique old T|Y attachment, and add the Q-edge joining t to the current Q-subpath endpoint. Deleting the old leaf attachment isolates t without disturbing the Y paths; adding the Q-edge merges t into the current S-subpath. The number of components therefore remains three at every step.

After the three T-vertices have been transferred, the two old residual rails are exactly A and B and the new core rail is Q. Every intermediate core rail is a contiguous subpath of Q, hence tight. Thus

  F_0 -> F_1                                            (PE.19)

is an explicit walk of exactly three local leaf-transfer moves through literal maximum spanning three-forests.

So the Hamilton-S crown is also current exchange geometry.

### 7. Portal-C4 local extinction
Sections 2-6 exhaust b_T=1,2,3. Therefore an exact H-s cover minimizing the four-cut energy Sigma cannot be locally terminal.

Every branch yields at least one of:

1. a current maximum-three-forest representative switch or graft fan;
2. current R435 / proper-cycle / reverse-trimer geometry;
3. fixed-complement or universal high-transition selected-reversal dynamics;
4. a named residual component-drop crossing retained in an actual maximum forest;
5. a strict lower-Sigma exact H-s representative, impossible at the chosen minimum.   (PE.20)

Hence the surviving k>=8 portal-only pair-core C4 has no independent local obstruction class. It is extinguished as a local universal-core object and must hand off to the global maximum-forest / reversal / component-recompletion programs.

This theorem does not by itself close R927 Arm M or O4. It completes Researcher 1's G13 PORTAL-C4 EXTINCTION target at the level requested by the current parent architecture: no output-free portal-C4 representative survives.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R4"
    },
    {
        "relation": "dependency",
        "revision_id": "R157"
    },
    {
        "relation": "dependency",
        "revision_id": "R966"
    }
]
```