# Fixed-defect three-side transport descends to a monotone 4|3 corridor

## Statement

In the three-side fixed-defect setup of threeside01, fix z in Z and let Q have order m>=7. The entire left-to-right fixed-z shell transport admits a component-respecting lift one potential level lower: after one strict 5|2 -> 4|3 descent, one can travel from the left shell to the right shell through spanning covers of constant profile (4,m-3,3), every three-side containing z, using only equal-Phi pairwise repartitions. Thus the original deletion singleton reaches this monotone corridor with total Phi drop 6(m-4). No endpoint-coherence or inter-shell common-deletion hypothesis is needed.

## Body

Use the shells W_0,...,W_3, tails T_0,...,T_3, shell graphs Omega_j, and fixed defect z from threeside01. For every fixed-z shell edge {z,c}, the corresponding top state is
C_{j,c}=(W_j-{z,c}) | T_j | (z,c),
of profile (5,m-3,2).

We first record the lower layer inside one shell. By the shell descent-diamond argument (equivalently, directly from independence_number_at_most_two_in_every_boundary_tournament as in fixeddefect_shell_edge_lies_in_a_common_43_descent_diamond), every prescribed edge {z,c} has a strict one-move descendant of profile (4,m-3,3),
D=K | T_j | R,
where K and R partition W_j, |K|=4, |R|=3, both are Hamiltonian, and z belongs to R. Any two such lower states in the same shell are themselves one pairwise-repartition move apart: they have the identical component T_j, while their other two components are two exact 4|3 path covers of the same seven-set W_j. Hence the lower descendants in one shell form a connected equal-Phi layer, and every fixed-z top state has an edge of Phi-drop exactly four into that layer.

It remains to glue the lower layers of consecutive shells without returning to the 5|2 level.

Fix consecutive shells W_j,W_{j+1}. By threeside01, choose their shared fixed-z shell edge {z,c}. Put U=W_j intersect W_{j+1}. Then |U|=6. Let a be the unique vertex of W_j-U and b the unique vertex of W_{j+1}-U, and put B=U-{z,c}, so |B|=4. Since {z,c} is a shell edge in both shells, B union {a}=W_j-{z,c} and B union {b}=W_{j+1}-{z,c} are Hamiltonian five-sets.

Define
A_a={d in B : (B-{d}) union {a} is Hamiltonian},
A_b={d in B : (B-{d}) union {b} is Hamiltonian}.
By independence_number_at_most_two_in_every_boundary_tournament, every five-set has at least three Hamiltonian four-vertex deletions. In B union {a}, only the deletion of a lies outside the four core labels B, so |A_a|>=2. Similarly |A_b|>=2.

If A_a intersects A_b, choose d in the intersection. Then
D_j=((B-{d}) union {a}) | T_j | (z,c,d)
and
D_{j+1}=((B-{d}) union {b}) | T_{j+1} | (z,c,d)
are legal one-move descendants of the shared top states on the two shells. They have the same three-side (z,c,d). Their other two components are two exact two-covers of the same support H-{z,c,d}, so replacing one pair by the other is a single legal pairwise repartition. The two lower states have the same profile (4,m-3,3), hence this inter-shell move preserves Phi.

Suppose instead A_a and A_b are disjoint. Since both have order at least two and B has order four, each has order exactly two and together they partition B. The five-set B union {a} has at least three good deletion labels, but only the two labels in A_a among B are good core deletions. Therefore deletion of a must also be good, so B itself is Hamiltonian. (The same conclusion follows from B union {b}.)

Now the shared top state in shell j has the legal descendant
D_j=B | T_j | (z,c,a),
and the shared top state in shell j+1 has the legal descendant
D_{j+1}=B | T_{j+1} | (z,c,b).
The triples are Hamiltonian automatically. These two lower states share the Hamiltonian four-side B; their other two components are exact two-covers of H-B. Hence they differ by one legal pairwise repartition, again at equal Phi.

Thus in all cases the lower 4|3 layers of consecutive shells are joined by an equal-Phi move. Applying this at the three shell transitions and using the equal-Phi connectivity inside each shell gives a left-to-right corridor of profile (4,m-3,3) whose three-side always contains z. The corridor starts below the shell state associated with {z,q_2} and ends below the shell state associated with {z,q_{m-3}}.

By in_the_deletion_component_and_gives_an_explicit_large_descent, the original singleton lift P|{x}|Q reaches the left top shell state in three moves and then reaches the lower layer by a fourth move. The total potential drop from profile (3,m,1) to profile (4,m-3,3) is
m^2+10-[(m-3)^2+25]=6(m-4).
All subsequent motion through the corridor is Phi-neutral.

Therefore the fixed-defect transport of threeside01 can be carried globally from left to right after a strict descent, without ever climbing back to the 5|2 shell level.