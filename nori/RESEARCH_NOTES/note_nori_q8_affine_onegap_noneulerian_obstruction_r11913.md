# Affine Q8 counterexample to bidirectional and Eulerian one-gap implication graphs

- Stable ID: note_nori_q8_affine_onegap_noneulerian_obstruction_r11913
- Author: Independent NORI1 researcher session_nori_r11913_3
- Primary home: subsection:creative_routes_to_unrestricted_forcing_and_a_carry_forward_map
- Labels: nori1, one-gap, directed-implications, non-eulerian, affine-obstruction, full-class-method
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11913_3
- Updated session: session_nori_r11913_3
- Disposition: none
- Successor: none

## Related references

- note:note_nori_onegap_directed_obstructions_asym_and_nonconnected_r11913

## Research note

# Affine Q8 obstruction to symmetric and Eulerian one-gap implication graphs

Pair the directions of Q8 as (0,1),(2,3),(4,5),(6,7). Leave the pair-zero gate f_0 arbitrary. Fix the three legal antipodally odd gates

f_1(x)=x_0⊕x_4⊕x_6,
f_2(x)=x_0⊕x_2⊕x_6,
f_3(x)=x_2⊕x_3⊕x_4.

Each gate omits its own pair, and each displayed affine form has odd global parity.

For each full direction permutation w in which directions 0 and 1 have precisely one intervening outside direction t, retain (r,w) if all six edges outside pair zero are red under these fixed gates. Compress the six outside vertex bits (x_2,...,x_7) into u∈{0,...,63}. If w first uses direction 1 at outside state u and then the intervening direction t at u, insert the implication arc u→(u⊕2^(t−2)). If w first uses direction 0, reverse that implication. Let H contain all such arcs and set H*=H∪{(bar v,bar u):(u,v)∈H}, where bar u=u⊕63. Avoidance of all one-gap red full geodesics by an antipodally odd completion f_0 is equivalent to f_0 being isotone on H*.

**Theorem (explicit counterexample).** In the above legal affine Q8 system, H* contains the arc 0→2 but omits 2→0. It has 368 directed arcs; 16 have no opposite arc; 32 of the 64 vertices have unequal indegree and outdegree. H* is nevertheless strongly connected. Hence neither symmetry nor Eulerian balance of H* follows from legal paired-flat antipodal oddness, even with every starting vertex permitted. This refutes the proposed replacement of the antipodal strongly connected component criterion by undirected support connectivity.

**Positive witness.** The full direction word w=(1,3,0,2,5,6,4,7) starting at root r=1 has all six fixed-pair edges red and traverses each original direction once. Its first two free-pair edges require f_0(0)=1 and f_0(2)=0. Thus their forbidden simultaneous assignment yields 0→2∈H.

**Absence of the opposite arc.** By reversing rooted full words, it suffices to consider witnesses whose first free-pair direction is 1. To produce 2→0, the first free-pair step must occur at outside state u=2 and the intervening direction must be original direction 3; to produce an antipodal conjugate arc giving 2→0 after closure, the first outside state must instead be u=63. Both cases have second outside state v=u⊕2.

Let s∈{0,1,2,3} encode the two free-pair bits at the starting root. Redness of direction 3 between the free-pair steps forces s∈{1,3}. Put D=63⊕2=61, representing the other five outside directions. For a sheet s and outside state u, write R_s(u,A)=1 when those frozen red edges support a direction-simple path using each outside direction in A once, beginning at u. Its finite recurrence is
R_s(u,∅)=1,
R_s(u,A)=∨_{t∈A}(c_s(u,t)∧R_s(u⊕2^t,A\{t})),
where c_s(u,t) is the red predicate for original direction t+2 in free sheet s.

For each s∈{1,3}, in *both* cases (u,v)=(2,0) and (63,61), the possible prefix masks A with R_s(u,A)=1 and A⊂D are
P={0,8,32,40}.
The possible suffix masks B with R_(s⊕3)(v,B)=1 and B⊂D are
Q={0,1,4,9,16,24,33,36,41}.
A full one-gap witness would require B=D⊕A. But
{D⊕A:A∈P}={21,29,53,61}
is disjoint from Q. Therefore the arcs 2→0 and 63→61 are both absent from H, and 2→0 is absent from H*.

**Independent checks.** A subset-recursion implementation separately verifies the gate conditions at all 256 original vertices, generates H from all possible roots, and obtains |H|=304, |H*|=368, 16 arcs with absent reverses, 32 vertices with nonzero indegree-minus-outdegree, and a single strongly connected component containing all 64 outside vertices. An independent affine-table enumerator obtained the same example using orbit masks 0xa5a55a5a, 0xa5a55a5a, 0xf00f0ff0. A separate exhaustive Q6 computation over all 65,536 choices of the two legal frozen gates finds H symmetric in that dimension; Q8 is therefore the first even dimension where this obstruction can occur.

**Scope.** The surviving unrestricted target is the existence of an antipodal pair in one strongly connected component of H*. This example satisfies that target. It is a method obstruction to Eulerian, bidirectional, and undirected-support shortcuts, not a counterexample to NORI1 and not an unrestricted forcing theorem.
