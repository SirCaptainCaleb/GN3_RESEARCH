# The 4|4|3 plateau has complete pair reachability on its three-side

## Statement

Let K be a connected Astra-003 component consisting of 4|4|3 states on eleven vertices, and let D be the family of three-side supports occurring in K. Then every vertex occurs in D, and indeed every pair of vertices occurs together in some member of D. Moreover each occurring pair has D-codegree at least three, so |D|>=55.

## Body

# Complete pair reachability on a 4|4|3 plateau

Let K be a connected Astra-003 component all of whose states have component orders 4,4,3. Let D be the family of three-vertex supports of the order-three component.

We first record the local exchange supply. In a state

X|P|Q,

with |X|=3 and |P|=|Q|=4, fix x in X. Consider the five-set P union {x}. The four-set P is Hamiltonian.

If P union {x} is non-Hamiltonian, the certified five-set theorem says at most one of its four-subsets is non-Hamiltonian, so at least three vertices p in P satisfy (P-p) union {x} Hamiltonian. If P union {x} is Hamiltonian, at most three four-subsets are non-Hamiltonian, so at least one such p exists. Thus for every x there is at least one legal one-for-one exchange with P, and likewise at least one with Q. Therefore, for every X in D and x in X, at least two vertices y outside X satisfy X-x+y in D.

## Every vertex occurs

Assume a vertex z belongs to no support in D. Choose a state X|P|Q with z in P and write

X={x_1,x_2,x_3},  B=P-{z}.

The set B has order three and is Hamiltonian. For every i, the four-set B union {x_i} must be non-Hamiltonian; otherwise swapping z with x_i would put z on the new three-side.

Apply the certified bad-extension-pair theorem to the tight three-path B and the three exterior vertices x_1,x_2,x_3. Its bad-pair graph is triangle-free, so some pair, say x_1,x_2, has

B union {x_1,x_2}

Hamiltonian. Repartition X|P as this five-path together with the residual two-set {z,x_3}. This is a legal 5|2 split on the same seven vertices.

Now take an endpoint r of the Hamilton five-path. Removing r leaves a tight four-path, while {z,x_3,r} has order three and is Hamiltonian. Repartitioning the 5|2 pair once more gives a 4|3 split whose new three-side contains z. This state lies in the same Astra component, contradiction.

Hence every vertex occurs on a reachable three-side.

## Every pair occurs

Assume a pair {z,w} never occurs together in D. Choose a state

X|P|Q,  X={z,x_1,x_2},

and assume w in P. Put B=P-{w}, a Hamiltonian three-set.

For i=1,2, the four-set B union {x_i} must be non-Hamiltonian; otherwise the one-for-one swap x_i <-> w produces a three-side containing z,w.

The certified two-bad-four-extensions lemma applied to B and exterior vertices x_1,x_2 gives a Hamiltonian five-set

B union {x_1,x_2}.

Its complement inside X union P is the two-set {z,w}. Thus one legal repartition gives a 5|2 split with two-side {z,w}. Transfer an endpoint r of the five-path to that two-side. The residual four vertices remain a tight path and {z,w,r} is a Hamiltonian three-set. Hence a second legal repartition produces a 4|3 split whose three-side contains z,w, contradiction.

Therefore the two-shadow of D is K_11.

Finally, the coordinate-wise exchange supply gives at least two alternate third vertices for every pair already occurring in a support. Including the original third vertex, every pair has D-codegree at least three. Hence

3|D| >= 3*C(11,2),

so

|D|>=55.