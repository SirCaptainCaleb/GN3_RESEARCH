# The nonvacuous disagreement proof can be chosen over a Hamiltonian five-core with pc-two complement extensions

## Statement

Every minimum counterexample H admits one of the following two bounded common-core configurations.

(A) There is a Hamiltonian five-set C and a vertex a outside C such that C+a is Hamiltonian. Writing K=H-(C+a), both K and K+a are non-Hamiltonian of path-cover number two.

(B) There is a Hamiltonian five-set C and distinct vertices a,b outside C such that C+a and C+b are Hamiltonian. Writing K=H-(C+a+b), each of K+a and K+b is non-Hamiltonian of path-cover number two. Moreover the two Hamiltonian six-paths on C+a and C+b may be chosen to exhibit relative-order disagreement on C.

Thus the repaired substantial-disagreement route always carries its order witness together with a fixed Hamiltonian five-core and a one- or two-label family of complementary pc-two states.

## Body

Use the proof of 4cf010e3e5b3.

If its first substantial-disagreement outcome occurs, there is a displayed Hamiltonian five-path W on a set C and a Hamiltonian six-path R on C union {a}. Put K=H-(C union {a}). Since C union {a} is a proper Hamiltonian support in a minimum counterexample, H[K] is non-Hamiltonian with path-cover number two. Since C is also a proper Hamiltonian support, H[K union {a}]=H-C is non-Hamiltonian with path-cover number two. This is (A).

Now consider the adjacent-window side-switch outcome in the all-six-Hamiltonian branch. Use the notation of 4cf010e3e5b3: W_i=(p_i,...,p_{i+4}) and W_{i+1}=(p_{i+1},...,p_{i+5}), and the chosen Hamiltonian six-paths R_i on W_i union {x} and R_{i+1} on W_{i+1} union {x} use opposite insertion sides.

Suppose first R_i uses the right side and R_{i+1} the left side. In R_i, the unique vertex p_i outside the common support C={x,p_{i+1},...,p_{i+4}} occurs at the initial end of the displayed path, because x is inserted only in one of the two rightmost gaps of W_i. Deleting that initial endpoint leaves a tight Hamilton path on C. In R_{i+1}, the unique vertex p_{i+5} outside C occurs at the terminal end, because x is inserted only in one of the two leftmost gaps of W_{i+1}; deleting it likewise leaves a Hamilton path on C. The L-then-R case is symmetric. Hence C is Hamiltonian.

Put a=p_i and b=p_{i+5}. Then C+a and C+b are Hamiltonian, with the chosen six-paths R_i,R_{i+1}; by construction those paths exhibit relative-order disagreement on their common set C. Let K=H-(C union {a,b}). Since C+a is Hamiltonian, its complement K+b is non-Hamiltonian of path-cover number two. Since C+b is Hamiltonian, its complement K+a is non-Hamiltonian of path-cover number two. This is (B).

No claim is made that K itself or K+a+b is non-Hamiltonian in branch (B).