# An all-break DOUBLE rim emits a cyclic family of fresh retained-path crossing portals

**Workspace:** D17
**State:** established
**Key:** `compatible-forest-rim-double-crossing-fan`

**Summary:** Let Q be a shortest ordinary comparison rim in a smallest counterexample and let U|V be an exact two-cover of its complement. If |U|>=3 and every cyclic break ending at q_i has DOUBLE merge seed q_i->u0, then the two bad merge turns reverse to K_i=(u1,u0,q_i,q_{i-1}). Removing K_i leaves the explicit three-cover R_i|U[2,a]|V. Minimality makes this complement exactly two-coverable, and every exact two-cover must select an actual adjacency joining two of those three named components. Hence all-break DOUBLE produces an r-indexed family of fresh exact crossing portals, not merely r local reverse P4s.

### 1. Setup
Let H be a hypothetical smallest Strong Level-(1) counterexample. Let Q=(q_0,...,q_{r-1}) be the physical rim of a shortest ordinary directed comparison cycle, r>=5, indices modulo r. By the R887 comparison mechanism every cyclic turn (q_{i-1},q_i,q_{i+1}) is tight, so every cyclic break is a Hamilton path on V(Q).

By accepted R4/P601, the complement of Q has an exact two-cover. Fix

  H-V(Q)=U|V,
  U=(u_0,u_1,...,u_a),

with |U|>=3.

For each i take the cyclic break Q_i=(q_{i+1},...,q_i), terminal q_i and predecessor q_{i-1}. Assume the merge seed q_i->u_0 is DOUBLE, so both turns

  (q_{i-1},q_i,u_0),   (q_i,u_0,u_1)

are bad.

### 2. Reverse-P4 carrier at every break
Boundary antisymmetry R3 gives

  (u_0,q_i,q_{i-1}) tight,
  (u_1,u_0,q_i) tight.

Hence

  K_i=(u_1,u_0,q_i,q_{i-1})

is a literal tight P4. It retains the reversed U-source edge, reversed attempted merge state, and reversed Q-terminal edge.

### 3. Named three-cover of the complement
Deleting the adjacent rim vertices q_i,q_{i-1} from the tight cycle leaves the inherited tight path

  R_i=(q_{i+1},...,q_{i-2}).

Since |U|>=3, U_i=U[2,a]=(u_2,...,u_a) is nonempty. Thus

  R_i | U_i | V

is a literal three-path cover of H-V(K_i), with three named nonempty components.

### 4. Every exact complement cover contains a current crossing
K_i is proper. If H-V(K_i) were Hamiltonian, it and K_i would two-cover H. Hence it is non-Hamiltonian; R4/P601 therefore gives pc(H-V(K_i))=2. Choose any exact two-cover T_i of this complement.

T_i must select an actual adjacency whose endpoints lie in two distinct components of R_i|U_i|V. Otherwise each T_i rail would stay inside one named component: the first departure from one component to another would itself be such a selected crossing. Two T_i rails could then cover at most two of the three nonempty components, contradiction.

Therefore every break i supplies a retained selected directed state x_i->y_i joining one of

  R_i--U_i,   R_i--V,   U_i--V.

Retain K_i, the exact T_i, x_i->y_i with its rail position and orientation, and the crossed component pair.

### 5. Cyclic crossing fan
An all-break DOUBLE family therefore yields the cyclic family

  (K_i ; R_i|U_i|V ; T_i ; x_i->y_i),   i in Z/rZ.

This is fresh representative information not present in the native merge windows. The U/V and source/terminal duals are exact. The hypothesis |U|>=3 is deliberate: for |U|=2 the residual U_i is empty, so component count alone does not force a crossing. No claim is made yet that crossing types synchronize between consecutive breaks or already force shorter holonomy.
