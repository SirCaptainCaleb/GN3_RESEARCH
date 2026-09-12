# Hamilton-deletion recurrence compresses to a monochromatic-exchange cover or an endpoint-diverse crossing row

**Workspace:** D17
**State:** working
**Key:** `three-petal-hamilton-deletion-row`

**Summary:** At the R953 three-petal fixed point, in the distinguished-z branch where S=(B+Z)-z is Hamiltonian, the saturated petal C=L+p yields a complete source-label exchange row. If S+y is Hamiltonian for some y in C, then y lies in L and the two Hamilton supports (S+y) and (C-y) give an exact H-z cover with all S|C transitions incident to the single label y, hence tau=1 or 2. If no such y exists, z is universal relative to every source X|(C-y), so every exact H-z cover has S|C transitions incident with at least two distinct C-vertices. Endpoint accessibility of z in X cannot be assumed; a four-vertex boundary-tournament counterexample exists.

### 1. Setup
Retain the normalized R953 three-petal fixed point with

  |L|=|B|=|Z|=k,
  X=B union Z,
  C=L union {p},

where X is Hamiltonian, C is non-Hamiltonian deletion-Hamiltonian, and the historical source head z lies in Z. Retain the p-isolated source

  H-p : X | L

and the source-head conclusion that z is universally crossing on the X-side. Put S=X-{z}. This section treats the HAMILTON-DELETION branch in which S is Hamiltonian. The source-head recurrence gives S union {p} non-Hamiltonian.

For every y in C, deletion-Hamiltonicity of C gives an actual Hamilton path on C-y. Therefore

  H-y : X | (C-y)

is a literal exact singleton-deletion source for every y in C.

### 2. The complete exchange row
For y in C define

  E(y)=1 iff S union {y} is Hamiltonian.

Apply the support characterization of universal crossing from the universal-source-crossing development to the source H-y : X | (C-y). Since z lies in X,

  E(y)=1 iff z is quiet relative to that source,
  E(y)=0 iff z is universally crossing relative to that source.

The source-head recurrence says E(p)=0. Hence every good row label lies in L.

Suppose E(y)=1. Choose actual Hamilton paths P_y on S+y and K_y on C-y. Their supports are disjoint and partition V(H)-{z}, so

  H-z : P_y | K_y

is a literal exact two-cover. The rail K_y lies wholly in C. The rail P_y contains every vertex of S and exactly one C-vertex, namely y. Consequently every selected S|C transition of this cover is incident with y. Since P_y is a path, y has selected degree one or two there. Thus

  tau=1 if y is an endpoint of P_y,
  tau=2 if y is internal in P_y.

In particular, any endpoint-accessible good row entry realizes the tau=1 R508/R511 branch outright. An internal good row entry realizes a tau=2 cover whose possible two crossings are both concentrated on one physical C-label.

### 3. If the row is all zero, every cover has endpoint-diverse crossing
Assume E(y)=0 for every y in C. Equivalently, z is universally crossing relative to every source

  H-y : X | (C-y).

Fix an arbitrary exact two-cover T of H-z. Let D_C(T) be the set of physical vertices c in C incident in T with at least one selected S|C adjacency.

For each y in C, universal crossing relative to the source X | (C-y) says that T selects an adjacency from S to C-y. Therefore D_C(T)-{y} is nonempty for every y in C. This is impossible when D_C(T) is empty or a singleton. Hence

  |D_C(T)| >= 2

for every exact H-z two-cover T.

So the all-zero row is strictly stronger than the scalar lower bound tau>=2: at least two distinct C-labels must physically participate in the crossing system of every target cover. If tau=2 is attained, the two transitions necessarily have distinct C endpoints.

### 4. Endpoint accessibility is not a free theorem
The implication

  X Hamiltonian and X-z Hamiltonian
    => some Hamilton path of X has endpoint z

is false already on four vertices in a boundary tournament. A direct exhaustive check of the 12 reversal-pair bits gives an example with X={0,1,2,3}, z=3, Hamilton paths on X-z including (1,2,0), and Hamilton paths on X including (0,2,3,1), (1,2,3,0), (1,3,0,2), (2,1,3,0), (2,3,0,1), (2,3,1,0), but none beginning or ending at 3. This finite check is only a fence for the endpoint-accessibility shortcut; the row theorem above is symbolic and does not depend on the computation.

### 5. Current consumer target
The Hamilton-deletion branch has therefore split into two cover-valued residues.

(MONOCHROMATIC ROW EXIT) Some y in L Hamilton-extends S. Then H-z has an exact cover with tau at most two and all crossing concentrated at y. If y is endpoint-accessible on S+y, the realized tau=1 machinery applies. If y is always internal, retain the actual Hamilton S+y orders and compare them to a fixed Hamilton order of S; explicit R435 geometry or a clustered insertion cell is the remaining local obstruction.

(ENDPOINT-DIVERSE ROW) Every S+y, y in C, is non-Hamiltonian. Then z is universal across the entire source-label clique C, and every exact H-z cover must use at least two distinct C crossing labels. Any future two-cut consumer should use this endpoint diversity rather than only tau>=2.

Status: complete internal symbolic deductions except for the explicitly labelled four-vertex computational fence. No spanning two-cover is claimed.
