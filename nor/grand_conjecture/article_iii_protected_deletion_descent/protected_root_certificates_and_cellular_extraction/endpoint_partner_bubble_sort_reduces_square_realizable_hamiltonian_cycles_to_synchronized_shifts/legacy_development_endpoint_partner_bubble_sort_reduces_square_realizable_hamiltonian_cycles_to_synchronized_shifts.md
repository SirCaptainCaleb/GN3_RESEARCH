# Endpoint partner bubble-sort reduces square-realizable Hamiltonian cycles to synchronized shifts — preserved pre-item development

## Composition

(none yet)

## Development

## Endpoint partner bubble-sort: square lifting reduces injective Hamiltonian partners to a cyclic shift

Consider the endpoint rank-two cycle
rho_i=e_{x_i}-e_{x_{i+1}},
C_i={x_i,a_i},
D_i=e_{a_{i+1}}-e_{a_i},
with i in Z/kZ.

Assume the physical cycle x_0,...,x_{k-1} is Hamiltonian on the coordinate set under consideration and the partner assignment is injective with the same coordinate set. Write
a_i=x_{i+b_i},
where each displacement b_i is represented by the integer in {0,...,k-1}. The endpoint exclusions a_i notin {x_i,x_{i+1}} give
b_i in {2,3,...,k-1}.

Thus the partner assignment is a permutation sigma(i)=i+b_i mod k avoiding i and i+1.

### Lemma 1: every cyclic descent gives a legal nondegenerate square move

Suppose b_i>b_{i+1} in the chosen integer representatives.

The adjacent partner swap
(a_i,a_{i+1}) -> (a_{i+1},a_i)
preserves the endpoint exclusions exactly when
a_{i+1} != x_i
and
a_i != x_{i+2}.

In displacement notation these forbidden equalities are
b_{i+1}=k-1
and
b_i=2.

But b_i>b_{i+1} implies b_i>=3 and b_{i+1}<=k-2. Hence neither forbidden equality occurs. Therefore every strict descent is a genuine four-distinct-coordinate Johnson square, not a degenerate triangle.

After the swap the two local displacements become
b_i'=b_{i+1}+1,
b_{i+1}'=b_i-1.

### Lemma 2: a cyclic descent lowers the quadratic displacement potential

Put
Q=sum_i b_i^2.

For the square move above,
Q'-Q
=(b_{i+1}+1)^2+(b_i-1)^2-b_i^2-b_{i+1}^2
=2(b_{i+1}-b_i)+2.

Because sigma is injective, b_i=b_{i+1}+1 is impossible: it would give
sigma(i)=i+b_i=i+1+b_{i+1}=sigma(i+1).

Hence a strict descent actually satisfies b_i>=b_{i+1}+2, and therefore
Q'-Q<=-2.

So every cyclic descent admits a legal adjacent square commutation that strictly lowers Q.

### Theorem: square-realizable minimal partner assignments are synchronized cyclic shifts

Assume the missing endpoint square-lift theorem in the following precise form: whenever the abstract adjacent partner swap above is a nondegenerate Johnson square, either
1. the swapped partner assignment is realized by legal endpoint/deletion witnesses for the same physical cycle, or
2. the local surgery returns a full-support one-change order or a strictly improved protected witness.

Choose, among witness-realized injective Hamiltonian partner assignments on the fixed physical cycle, one minimizing Q.

If some b_i>b_{i+1}, Lemmas 1-2 and square lifting either solve/improve the instance or produce another realized assignment with smaller Q, contradiction.

Therefore no cyclic descent exists. A finite cyclic sequence of integers with no strict descent is constant. Hence
b_i=r
for every i, for some r in {2,...,k-1}.

Thus every Q-minimal unresolved injective Hamiltonian endpoint cycle has the synchronized form
a_i=x_{i+r}
for one fixed cyclic displacement r.

This is the promised finite partner-alignment reduction. It does NOT force a constant partner coordinate, which is impossible on a Hamiltonian physical cycle. Instead it forces a constant OFFSET.

### Defect relation and sign audit

For a synchronized shift a_i=x_{i+r},
D_i=e_{a_{i+1}}-e_{a_i}
=e_{x_{i+r+1}}-e_{x_{i+r}}
=-rho_{i+r}.

Therefore the partner-defect circulation reuses the original protected-root directions with the OPPOSITE orientation.

This corrects the sign in Subsection 89. With that subsection's stated conventions
rho_i=e_{x_i}-e_{x_{i+1}}
and
D_i=e_{a_{i+1}}-e_{a_i},
its displayed conclusions D_i=rho_{i-1} and D_i=rho_{i+2} should read
D_i=-rho_{i-1}
and
D_i=-rho_{i+2},
respectively.

The geometric conclusion of Subsection 89 survives: no new unoriented root directions occur. The orientation matters, however, for any later circulation or gluing argument.

### Geometric form of the residual obstruction

At the synchronized residue,
C_i={x_i,x_{i+r}},
C_i^+={x_{i+1},x_{i+r}},
C_{i+1}={x_{i+1},x_{i+r+1}}.

So every chronological step is one elementary square of the cyclic chord strip:
first advance the physical endpoint i->i+1, then advance the partner endpoint i+r->i+r+1.

The unresolved endpoint problem has therefore reduced, conditional on square lifting, from an arbitrary partner word to a single integer r and a closed staircase of congruent Johnson squares.

This is substantially stronger than abstract defect telescoping and avoids the false expectation that a Hamiltonian cycle should acquire a constant core.
