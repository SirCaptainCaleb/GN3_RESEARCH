# The thirteen-label attachment certificate is not exhaustive even with non-Hamiltonian complement — preserved pre-item development

## The thirteen-label attachment tests are not exhaustive

The conditions in [[a_four_cycle_five_support_has_a_thirteen_label_attachment_certificate]] are sufficient tests. Their simultaneous failure does not follow from the local four-cycle and complementary two-cover hypotheses as an impossibility. Here is a concrete example where every listed attachment and single-label joining test fails, the complement is non-Hamiltonian, and a different repartition gives a spanning two-cover.

### The complementary six-set

Use six exterior labels 0,1,2,3,4,5, with P=(0,1,2), Q=(3,4,5). Define their induced boundary tournament by a strict edge order:
35 < 15 < 02 < 24 < 01 < 34 < 45 < 04 < 13 < 05 < 23 < 14 < 03 < 12 < 25.
Here ij denotes the unordered pair {i,j}, and h(i,j,k)=1 exactly when ij<jk.

P and Q are tight because 01<12 and 34<45. The six-set is nevertheless non-Hamiltonian.

For a reproducible finite certificate, let R(W) be the possible ordered terminal pairs of increasing Hamilton paths on W. Initialize R({i,j}) with (i,j),(j,i). The recurrence is
(v,x) in R(W union {x})
iff some (u,v) in R(W) satisfies uv<vx.
It depends only on W and the terminal pair, so retaining those states is exact.

Applying this recurrence to each five-set gives:
- missing 0: terminal pairs (1,2),(2,5); their final-edge ranks are 14,15, while the possible extension-edge ranks are respectively 3,10.
- missing 1: terminal pairs (0,3),(5,2); ranks 13,15 versus 9,14.
- missing 2: terminal pairs (0,3),(0,4); ranks 13,8 versus 11,4.
- missing 3: terminal pair (2,5); ranks 15 versus 1.
- missing 4: terminal pair (2,5); ranks 15 versus 7.
- missing 5: terminal pair (3,1); ranks 9 versus 2.

Every possible final extension decreases the edge rank. Thus R({0,1,2,3,4,5}) is empty, proving non-Hamiltonicity. This bounded six-vertex computation was also checked directly over all 720 orders.

### The five-support and the blocked attachments

Add S={a,b,c,d,z}. Prescribe the mutual four-cycle before z: for ordered distinct u,v in {a,b,c,d}, set h(u,v,z)=1 on cycle edges ab,bc,cd,da and zero on diagonals.

For every u in {a,b,c,d}, prescribe
h(u,0,1)=h(1,2,u)=0,
h(u,3,4)=h(4,5,u)=0.
Thus no cycle label can be prepended or appended to P or Q.

For every s in {a,b,c,d}, also prescribe
h(z,s,0)=h(z,s,3)=0.
Every rooted four-path R_u supplied by the four-cycle ends in (z,s) for some cycle label s, so no R_u can precede P or Q. Neither can it follow them: its initial cycle label v fails the already prescribed terminal seam h(1,2,v)=0 or h(4,5,v)=0.

Thus all singleton rows and all rooted-path rows of the attachment graphs are empty. The joining orders (P,u,Q) and (Q,u,P) also fail at their first seam for every cycle label u.

### An explicit spanning two-cover

Prescribe the additional tight triples
h(a,0,b)=h(0,b,1)=h(b,1,c)=h(1,c,2)=h(c,2,d)=1,
and h(z,3,4)=1.
The two paths
(a,0,b,1,c,2,d)
and
(z,3,4,5)
are now tight and partition all eleven vertices.

All prescriptions are compatible with boundary antisymmetry. Triples confined to the exterior six-set are already assigned by its edge order. The mutual cycle uses only S. The forbidden singleton attachments have one cycle label and two exterior labels; the blocked rooted-path seam has z, a cycle middle label, and an exterior label. The tight interleaving triples have different reversal orbits from all those prescriptions. In particular h(z,3,4)=1 is independent of the forbidden h(u,3,4)=0 for cycle labels u. Complete every remaining reversal orbit arbitrarily.

The resulting family of boundary tournaments has the stated non-Hamiltonian complement, has the mutual-cycle Hamiltonian five-support, fails every displayed seam test, and has the explicit spanning two-cover.

### Consequence for the frontier

The counterexample does not assert existence of a global no-two-cover tournament. It shows that the local cycle and complementary-path hypotheses alone cannot force one of the thirteen-label attachment tests to pass. Closure must either use additional consequences of the global no-two-cover assumption or allow a repartition that mixes several vertices of an inherited tail into the five-support.

In this example the successful repartition incorporates all three vertices of P into one interleaved path while moving z to Q. The initial prescribed endpoints of the Hamiltonian five-path are not preserved, and no path is reversed.
