# A terminal singleton swap gives a Hamiltonian bypass or a paired matching-block endpoint residue

## Statement

Let H be a minimum counterexample. Suppose two spanning three-covers with the same third path D realize the terminal-singleton switch-rectangle outcome of equal_size_block_swap_rectangle01. Thus for distinct vertices x,y there are nonempty tight paths L,R of order at least two such that one cover displays
(L,x) | (y,R) | D,
the other has supports L union {y} and {x} union R together with D, and there is no order disagreement on L or R. Hence the two switched component orders are independently either (L,y) or (y,L), and either (x,R) or (R,x).

If the first switched order is (y,L), then (y,L,x) is a tight path; if the second switched order is (R,x), then (y,R,x) is a tight path. Each such three-block path is a proper Hamiltonian support with non-Hamiltonian path-cover-two complement.

Consequently the only singleton-swap orientation with no such immediate three-block Hamiltonian bypass is
(L,x), (L,y), (y,R), (x,R).
Write (a,b) for the last two vertices of L and (c,d) for the first two vertices of R. Then either one of the four-sets
W_L={a,b,x,y},  W_R={x,y,c,d}
is Hamiltonian, giving a proper Hamiltonian four-support with non-Hamiltonian path-cover-two complement, or both are non-Hamiltonian and form a paired matching-block residue:

- W_L is edge-orderable with opposite-edge matching {ab,xy} as the lowest matching block and the two cross matchings {ax,by},{ay,bx} above it in one of the two possible orders;
- W_R is edge-orderable with opposite-edge matching {cd,xy} as the highest matching block and the two cross matchings {cx,dy},{cy,dx} below it in one of the two possible orders.

Thus an equal-size terminal singleton support swap reduces to a three-block Hamiltonian bypass, a Hamiltonian four-support, or one explicit six-vertex paired matching-block endpoint obstruction sharing the swapped pair {x,y}.

## Body

The no-order-disagreement hypothesis fixes the inherited orders on L and R. Since each switched support contains one singleton and one inherited block, its displayed Hamilton order has exactly one of the two block orders.

Assume first that the switched path on L union {y} is (y,L). The original cover contains the tight path (L,x). Since |L|>=2, every consecutive triple of the concatenation (y,L,x) is inherited either from (y,L) or from (L,x): the only two joins overlap inside the at-least-two-vertex middle block L, so there is no new triple spanning both joins. Hence (y,L,x) is tight. Its complement is covered by the two tight paths R and D. Because H is a minimum counterexample, that complement cannot be Hamiltonian, or it would join the displayed Hamilton path to form a spanning two-cover. Therefore the complement has path-cover number exactly two.

Similarly, if the switched path on {x} union R is (R,x), combine the original path (y,R) with (R,x). Since |R|>=2, (y,R,x) is tight, and its complement L union D is non-Hamiltonian with path-cover number two.

Therefore failure of both immediate bypasses forces the switched orders to be (L,y) and (x,R). Together with the original paths (L,x) and (y,R), the two swapped labels x,y are common right-end extenders of L and common left-end extenders of R.

Let (a,b) be the terminal ordered pair of L and (c,d) the initial ordered pair of R. Tightness of the four displayed paths gives
(a,b,x), (a,b,y), (x,c,d), (y,c,d)
tight.

Consider W_L={a,b,x,y}. If W_L is Hamiltonian, minimum-counterexample calculus gives the claimed non-Hamiltonian path-cover-two complement. Suppose it is non-Hamiltonian. Apply the common-first-pair four-set classification in smallset01 to the tight triples (a,b,x),(a,b,y). It says W_L is edge-orderable and, writing
M_0={ab,xy}, M_1={ax,by}, M_2={ay,bx},
the three opposite-edge perfect matchings occur in strict blocks with either
M_0<M_1<M_2
or
M_0<M_2<M_1.
In particular {ab,xy} is the lowest matching block.

Now consider W_R={x,y,c,d}. If it is Hamiltonian we again obtain a Hamiltonian four-support with non-Hamiltonian path-cover-two complement. Suppose it is non-Hamiltonian. Apply the same small-set classification to the reverse boundary tournament, in which (d,c,x) and (d,c,y) are tight exactly because (x,c,d) and (y,c,d) are tight in H. Non-Hamiltonicity is preserved under this reversal, and reversing the representing edge order returns a representing edge order for the original boundary tournament. Therefore, with
N_0={cd,xy}, N_1={cx,dy}, N_2={cy,dx},
the original W_R edge order has either
N_2<N_1<N_0
or
N_1<N_2<N_0.
Thus {cd,xy} is the highest matching block.

This proves the paired endpoint residue. It is confined to the six vertices {a,b,x,y,c,d}, and every other singleton-swap orientation has already produced a positioned Hamiltonian support with path-cover-two complement.
