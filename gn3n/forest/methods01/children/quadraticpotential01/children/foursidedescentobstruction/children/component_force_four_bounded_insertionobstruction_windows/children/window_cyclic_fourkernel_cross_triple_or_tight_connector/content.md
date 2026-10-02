# Each long path at a four-vertex quadratic minimum yields a Hamiltonian window, cyclic four-kernel, cross triple, or tight connector

## Statement

Let H be a minimum counterexample and let C=X|P|Q be a spanning three-cover that is Phi-minimal in its pairwise-repartition component, with X=(x_0,x_1,x_2,x_3), |X|=4, and |P|,|Q|>=6. For either R in {P,Q}, let M_R be the displayed middle path obtained by deleting both endpoints of R. Then the two bounded insertion-obstruction windows supplied by insert01 for x_0 and x_3 on M_R force at least one of the following:
(1) a Hamiltonian four-vertex window;
(2) the exceptional cyclic non-Hamiltonian four-kernel, whose every exterior one-vertex extension is Hamiltonian;
(3) a Hamiltonian five-set supported on x_0,x_3 and three consecutive vertices of M_R;
(4) an explicit tight cross triple (x_0,b,x_3) for some vertex b of M_R, after interchanging x_0,x_3 if necessary;
(5) a tight path joining x_0 to x_3 through a nonempty interval of M_R.
Thus each of P and Q independently supplies a Hamiltonian four- or five-set, the cyclic four-kernel, a tight cross triple, or a tight path connecting the same two vertices x_0,x_3.

## Body

Fix R in {P,Q}. By 8086d5becdc1, after deleting the two displayed endpoints of R, the resulting middle path
M_R=(b_1,...,b_t)
has both x_0 and x_3 noninsertable in its displayed order. Apply the failed-insertion normal form in insert01 separately to x_0 and x_3.

Suppose first that at least one obstruction is alternative 1 of insert01. Let z be the corresponding vertex in {x_0,x_3}, and write a,b,c for the three consecutive vertices of M_R in that obstruction window. Alternative 1 gives the three tight triples
(z,b,a), (a,b,c), (c,b,z).

Put K={a,b,c,z}. If H[K] is Hamiltonian, we have outcome (1). Suppose H[K] is non-Hamiltonian. The local classification argument appearing in transport01 applies verbatim here: that argument uses only the three displayed tight triples, boundary antisymmetry, and non-Hamiltonicity of K. It does not use the deletion-cover hypothesis of the surrounding theorem. Those three triples force all remaining reversal pairs on K, yielding exactly the exceptional cyclic non-Hamiltonian four-kernel. The certified small-set conclusion recorded in transport01 then gives that K union {d} is Hamiltonian for every exterior vertex d. This is outcome (2).

It remains to suppose both obstructions are alternative 2 of insert01. Let their obstruction gaps on M_R be
b_i|b_{i+1}
and
b_j|b_{j+1},
and interchange x_0,x_3 if necessary so i<=j. Apply the certified spacing trichotomy 36fccff06d48.

If i=j, the four-set
{x_0,x_3,b_i,b_{i+1}}
is Hamiltonian, giving outcome (1).

If j>=i+2, the sequence
(x_0,b_{i+1},...,b_j,x_3)
is a tight path, giving outcome (5).

If j=i+1, the spacing theorem gives either a Hamiltonian five-set on
{x_0,x_3,b_i,b_{i+1},b_{i+2}},
which is outcome (3), or the explicit tight cross triple
(x_0,b_{i+1},x_3),
which is outcome (4).

These cases exhaust the two alternatives in the failed-insertion normal form and all relative positions of the two alternative-2 obstruction gaps. The argument applies independently to M_P and M_Q, so both long components supply one of the five concrete outputs while sharing the same exterior pair x_0,x_3. ∎