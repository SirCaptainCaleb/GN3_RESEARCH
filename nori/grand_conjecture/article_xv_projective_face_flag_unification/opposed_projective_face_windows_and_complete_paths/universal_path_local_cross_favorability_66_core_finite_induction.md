# Universal path-local cross-favorability: 66-core finite induction

# Universal cross-favorability on a path: 66-core finite induction

**Theorem (all-dimensional, computer-assisted).** For arbitrary binary edge colorings f,g of Q_n whose union direction-interaction graph is contained in a path, there is a root with a full dimension-simple 0*1* geodesic for f and a full dimension-simple 1*0* geodesic for g. No assumptions of affine dependence, antipodal oddness, or root-density bounds are required. The two full direction orders may differ.

**Geometry.** Write u_i=1 if dimension i precedes i+1 in the f-order, and v_i=1 for the g-order. With root bits x and traversed color bits c_i,d_i, for each internal direction
\[
c_i=F_i(x_{i-1}+u_{i-1},x_{i+1}+1-u_i),\qquad
d_i=G_i(x_{i-1}+v_{i-1},x_{i+1}+1-v_i)
\]
over F2. A compatible pair of monotone full paths exists if and only if, on every edge i,i+1,
\[
u_i=1\Rightarrow c_i\le c_{i+1},\quad u_i=0\Rightarrow c_{i+1}\le c_i;
\]
\[
v_i=1\Rightarrow d_i\ge d_{i+1},\quad v_i=0\Rightarrow d_{i+1}\ge d_i.
\]
Sufficiency follows by ordering the two color phases topologically inside their oriented interaction paths, which have no directed cycles.

**Inductive state.** Retain six bits
\[
(a,b,u,v,c,d)=(x_i,x_{i+1},u_i,v_i,c_i,d_i).
\]
For arbitrary next two-input Boolean rules F,G, choose a new starting bit z and next orientation bits u',v', and compute
\[
c'=F(a+u,z+1-u'),\qquad d'=G(a+v,z+1-v').
\]
The successor state is (b,z,u',v',c',d') if both oriented color inequalities hold. There are 64 boundary states and 256 possible interior rule pairs.

**Finite inductive certificate.** The independently preserved file nori_path_induction_66_masks.txt lists 66 explicit masks of these 64 states. A dependency-free Python checker verifies: (i) every one of the 16 paired initial endpoint tables produces a reachable state set containing a listed mask; (ii) the image of every listed mask under each of the 256 interior rules contains another listed mask; (iii) every listed mask meets the successful final state set for every one of the 16 paired terminal endpoint tables. This is 16896 interior-extension checks. By induction, every path length has a compatible final state, proving the theorem.

The SHA256 digest of the 66-mask file is 3c0450114b54eb377ade6e7412b9b5bcd3bb8b8f999bb73b1eeaab59eefb7d4b. An independent full saturation produces 3191 reachable boundary-state sets, of which these 66 are inclusion-minimal. Direct geodesic dynamic programming agreed with the orientation method in 128792 separate comparisons, including all path-local coloring pairs in dimensions two and three. The finite induction is machine checked; no short conceptual classification of the 66 masks is presently claimed.

**Cyclic constant-site corollary.** If two cyclic-local colorings have a direction j whose color is constant in each coloring, fixing bit j leaves two path-local colorings. Apply the theorem to the necessary fibers, then insert j at the beginning or end of the two monotone geodesics according to its color pair: (0,1) first in both; (1,0) last in both; (0,0) first in f and last in g; (1,1) last in f and first in g. Choosing the fiber before or after the bit toggle ensures a common root. Hence any such cyclic-local pair is cross-favorable. The previously proved pendant-tree lifting and free-bridge equivalence then give the corresponding all-dimensional NORI1 closure class.

The unrestricted cyclic pair problem and NORI1 remain open.

## Eight-prototype refinement of the 66-mask induction

The preceding 66-mask certificate admits a much smaller representation. Identify its 64 boundary states with six-bit integers s (in bit order a,b,u,v,c,d). For a state-set mask M and a six-bit translation k, let
\[
\boxed{\tau_k(M)=\sum_{s:\,M_s=1}2^{s\mathbin{\mathrm{xor}}k}.}
\]
Thus tau_k permutes the 64 states by independently flipping any selection of their six bits.

The entire inductive certificate is the union of translation orbits of just **eight prototype masks**:
\[
\begin{array}{ll}
P_1=\mathtt{000000000000ffff},&
P_2=\mathtt{000000003c3cc3c3},\\
P_3=\mathtt{000033cc0000cc33},&
P_4=\mathtt{0140314cc143fd7f},\\
P_5=\mathtt{03c0300cc0030c30},&
P_6=\mathtt{11441144dd77dd77},\\
P_7=\mathtt{1414d7d71414d7d7},&
P_8=\mathtt{5555555555555555}.
\end{array}
\]
Their respective orbit sizes under k in F2^6 are 4,4,4,32,4,8,8,2, totaling **66 distinct masks**. Four orbit types are affine codimension-two state constraints, one is a half-cube, and the remaining three are more flexible nonlinear state conditions.

**Eight-prototype certificate theorem.** Generate the 66 masks by all tau_k(P_i). With the six-bit transition map defined above, the generated family satisfies:
(1) every first-direction reachable mask contains a generated mask;
(2) for each generated mask and each of 256 interior paired color tables, its successor mask contains a generated mask;
(3) every generated mask intersects every terminal-success mask.

An independent standalone Python verifier, **nori_path_8_prototype_induction.py**, contains all eight hexadecimal constants, generates the 66 masks by XOR translation, and directly checks the three properties with no external data files or dependencies. Output: PASS, 66 inductive cores, 16896 extension checks, all initial and terminal tables. SHA256 of the verified Python file:
\[
\mathtt{7ed6dbc8034dae69f4c644b44b8f0df72c904e43f340fcd87d5ce7dfb9a2edc8}.
\]

This eight-prototype presentation supersedes the need for a 66-line externally stored list as a proof certificate. The translation closure is a convenient description of the masks; **it is not assumed that each individual transition commutes with every translation**. Instead the verifier checks the full generated family for closure. A conceptual derivation of the eight shapes, in particular their nonlinear orbit types, remains an attractive further step.

## Constructive linear-time witness extraction and linear forests

**Theorem (constructive version).** The path-local pair theorem is algorithmic: from the local Boolean edge-color tables F_i,G_i on a path of n dimensions, one can construct a common starting root x and two full dimension-simple monotone geodesic orders in **O(n)** time and space.

*Proof.* Maintain for each of the 64 six-bit boundary states either no predecessor or one predecessor state witnessing reachability. The initialization, eight possible successors per state per interior direction, and terminal test are given by the transfer equations above. The verified eight-prototype invariant guarantees that some terminal state succeeds for every input sequence. Store predecessor pointers at each position, requiring O(64n) memory. Backtrack from a successful terminal state to recover all root bits x_i, f-orientation bits u_i, g-orientation bits v_i, and traversed edge colors c_i,d_i.

Build the directed path with edge i−(i+1) oriented according to u_i. Its inequalities exclude directed arrows from the f-one phase into the f-zero phase, so topologically sort the induced f-zero subgraph and then the induced f-one subgraph. This gives the required f-geodesic. Similarly topologically order the g-one subgraph first and the g-zero subgraph last using the v-orientations. Each topological sorting step is linear in n and traverses each dimension once. The result is a constructive pair of monotone full geodesics starting at the same recovered root. QED.

**Independent implementation.** The self-contained Python program nori_path_constructive_solver.py implements this procedure and independently evaluates each reconstructed path against the original edge-color truth tables. It passed 720 independent witness checks, including random dimension-100 path-local pairs. Its SHA256 is 13afaeaddb9b57a6795631fe7651338c755be00681423127572eb60fd45b75a3. These tests audit the constructor; the all-input guarantee is supplied by the eight-prototype induction.

**Corollary (linear forests).** The same cross-favorability assertion and constructive linear-time algorithm hold when the union direction-interaction graph is a *disjoint union of paths*, rather than a single path. Apply the path theorem independently to each connected component and concatenate the component paths, taking all f-zero phases before all f-one phases, and all g-one phases before all g-zero phases. Edge colors in separate components are independent of the other component bits, so each component can be traversed without disturbing the other. The starting roots concatenate to give one common root. Each direction is traversed once.

The theorem therefore settles all binary coloring pairs with union interaction graph a linear forest, in arbitrary dimension and with unrelated nonlinear local functions. A minimal cross-root obstruction must contain either an interaction cycle or a vertex of degree at least three in the union graph.

## Boundary-fiber obstruction to a stronger path induction

The universal path-pair theorem cannot be strengthened by prescribing either endpoint starting bit. In Q4 with path directions 0,1,2,3, encode endpoint one-input color truth tables by two-bit integers and internal two-input tables by four-bit integers, indexing the latter by left+2*right. Take f local truth tables (2,10,12,2), and g tables (2,5,3,2). Direct geodesic reachability from every root gives

A0(f) intersect A1(g) = {0000, 0010, 0100, 0110}

with written bit order x3 x2 x1 x0. Thus every common root has x0=x3=0. There is no common root on either face x0=1 or x3=1, nor with x0+x3=1. Yet the unconditioned cross-root theorem succeeds at four roots.

This finite example refutes the stronger endpoint-prescribed claim without challenging the path theorem. It shows why a cyclic proof cannot simply impose a prescribed endpoint parity on the 66-core induction: adding the closing interaction edge requires a richer boundary relation or a change in the witness orders. The root set was independently checked over every permutation of the four directions and every starting root.
