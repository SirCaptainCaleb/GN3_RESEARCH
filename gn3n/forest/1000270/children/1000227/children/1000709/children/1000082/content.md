# One-defect transfers are alternating Hamiltonian-deletion moves

## Statement

Let H be a minimum counterexample and let V(H)=R disjoint-union S with d(R)=1 and d(S)=0. If v in R is a Hamiltonian deletion of R, then transferring v gives a new D=1 state (R-{v}) | (S union {v}), with R-{v} Hamiltonian and S union {v} deficient. At a minimum deficient-support state |R|=delta=mu+1, two such transfers return to deficient-support size delta; a nontrivial two-step move is exactly a one-for-one support swap v<->w where w != v is a Hamiltonian deletion of S union {v}. Thus two-step trapping at minimum size is equivalent to every S union {v}, for v a good deletion of R, having v as its unique Hamiltonian deletion.

## Body

# One-defect transfers are alternating Hamiltonian-deletion moves

Let H be a minimum counterexample. For a vertex set T write

d(T)=|T|-L(T),

where L(T) is the maximum tight-path order in H[T]. Suppose

V(H)=R disjoint-union S,

with

d(R)=1, d(S)=0.

Call v in R a good deletion of R if R-{v} is Hamiltonian.

## Transfer lemma

For every good deletion v of R, the transferred partition

(R-{v}) | (S union {v})

again has total deficit one, and its deficient side is S union {v}.

Indeed R-{v} is Hamiltonian by definition. The set S union {v} contains the Hamiltonian set S, so its deficit is at most one. It cannot be Hamiltonian, because then the two Hamiltonian sets R-{v} and S union {v} would partition V(H), giving a spanning two-cover of H. Hence

d(S union {v})=1.

Thus every Hamiltonian deletion of the deficient side gives a legal D=1 move, and every such move flips the side carrying the defect.

## Two-step dynamics at minimum deficient-support size

Let delta be the minimum possible size of a deficient support in a D=1 state. By the one-defect/deletion-cover equivalence, delta=mu+1, where mu is the global minimum smaller side of a deletion two-cover.

Now take a delta-minimal state R|S with d(R)=1, d(S)=0 and |R|=delta. Let v be a good deletion of R. After transferring v, the state is

(R-{v}) | (S union {v}),

where R-{v} is Hamiltonian and S union {v} is deficient.

Let w be any good deletion of S union {v}. Transferring w back gives

((R-{v}) union {w}) | ((S union {v})-{w}).

The second support is Hamiltonian, and the first is deficient. Its size is

|R|-1+1=delta.

If w=v, this is the original support partition. If w!=v, it is a genuine one-for-one support swap

v <-> w

between R and S, producing a different delta-minimal D=1 state.

Consequently a delta-minimal state has no nontrivial two-transfer neighbor exactly when, for every good deletion v of R, the enlarged opposite support S union {v} has v as its unique good deletion.

This is the exact local trapping condition for the single-vertex-transfer version of the one-defect route.

## Relation to the known fences

For small deficient supports, the synchronized-omission theorem supplies several choices of v. However the double-frozen construction and the one-vertex-replacement counterexamples show that uniqueness of v on the opposite enlarged support is locally consistent; it cannot be ruled out using the two enlarged supports separately.

Therefore any proof that excludes a trapped minimum D=1 state must eventually use mixed triples between the two supports, a larger exchange shell, or another global consequence of pc(H)>2. The transfer formulation identifies precisely where such information has to enter.
