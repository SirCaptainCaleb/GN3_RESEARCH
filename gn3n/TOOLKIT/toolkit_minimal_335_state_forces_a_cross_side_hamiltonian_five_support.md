# A Phi-minimal 3|3|5 state forces a cross-side Hamiltonian five-support

**Summary:** In a Phi-minimal 3|3|5 cover T1|T2|C, the two 3|5 matching-block obstructions can be chosen on the common interior triple (c2,c3,c4). Their two exterior labels w1 in T1 and w2 in T2 then force a Hamiltonian five-set {w1,w2,c2,c3,c4}, whose complement is non-Hamiltonian with path-cover number two.

## Statement

Let H be a minimum counterexample and let T_1|T_2|C be a Phi-minimal spanning three-cover with |T_1|=|T_2|=3 and C=(c_1,c_2,c_3,c_4,c_5). Then there exist w_i in V(T_i), i=1,2, such that each four-set {w_i,c_2,c_3,c_4} is non-Hamiltonian, while the five-set K={w_1,w_2,c_2,c_3,c_4} is Hamiltonian. Consequently H-K is non-Hamiltonian and has path-cover number two.

## Body

Apply toolkit_minimal_35_pair_forces_a_complementary_matching_block_four_set first to T_1|C and then to T_2|C. This gives vertices w_1 in T_1 and w_2 in T_2 such that

F_i={w_i,c_2,c_3,c_4}

is non-Hamiltonian for i=1,2. The three-set

I={c_2,c_3,c_4}

is a tight path, since it is an inherited contiguous subpath of C.

Thus F_1=I union {w_1} and F_2=I union {w_2} are two non-Hamiltonian four-extensions of the same tight three-path I. Apply the controlled two-bad-four-extensions lemma in localextend01. It yields a Hamiltonian five-path on

K=I union {w_1,w_2}={w_1,w_2,c_2,c_3,c_4},

with both endpoints lying in I.

The set K is proper. By minimum-counterexample calculus, H-K has path-cover number at most two. It cannot be Hamiltonian, because a Hamilton path on H-K together with the Hamilton path on K would give a two-cover of H. Hence pc(H-K)=2.

So the two local 3|5 obstructions cannot remain independent: in profile 3|3|5 they synchronize on the common interior triple and force a proper Hamiltonian five-support meeting both 3-sides, with two-coverable complement.

## Metadata

- ID: toolkit_minimal_335_state_forces_a_cross_side_hamiltonian_five_support
- Kind: toolkit
- Version: 2
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
