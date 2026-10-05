# Toolkit migration — A five-side no-swap branch forces a two-sided endpoint lock on one long path

Preserved from the retired Toolkit Limbo object [[astra003fivetwosidedlock]]. This Brainstorm is migration evidence, not an accepted Toolkit entry.

## Original metadata

{
    "kind": "toolkit",
    "version": 2,
    "created_at": "2026-09-26T18:20:00.243361+00:00",
    "updated_at": "2026-10-03T15:39:36.649056+00:00",
    "archived_at": "2026-10-03T15:39:36.649056+00:00",
    "original_id": "astra003fivetwosidedlock",
    "audit_status": "unaudited",
    "math_version": 1,
    "toolkit_type": "other",
    "refutation_status": "unrefuted",
    "author_session_ids": [
    ],
    "audited_math_version": null
}

## Simplified statement

A five-side no-swap branch forces a two-sided endpoint lock on one long path

## Statement

Let X|P|Q be a quadratic-potential-minimal trapped three-cover with |X|=5 and |P|,|Q|>=7. Then either an equal-potential support exchange exists as in astra003fiveswapobstruct, or there are x in V(X) and one of the two long paths R=(r_1,...,r_m) such that x cannot be inserted into any position of the displayed order of R. More strongly, writing e_i={r_i,r_{i+1}} and f_i={x,r_i} in the comparison digraph, the four endpoint constraints e_1->f_1, e_2->f_2, f_{m-1}->e_{m-2}, and f_m->e_{m-1} all hold. Hence insert01 supplies a bounded failed-insertion obstruction for x on the full displayed path R.

## Body


By astra003fivethreeendpoints, choose x in V(X), with D=V(X)-{x}, such that D union {e} is Hamiltonian for at least three of the four endpoints of P and Q. Apply astra003fiveswapobstruct to these synchronized endpoints.

If any corresponding support exchange exists, we are in the first alternative. Suppose therefore that none exists. Among at least three endpoints drawn from the two endpoint pairs of P and Q, two belong to the same path. Call that path
R=(r_1,...,r_m), m>=7.
Thus D union {r_1} and D union {r_m} are Hamiltonian, while both
(R-r_1) union {x}
and
(R-r_m) union {x}
are non-Hamiltonian; otherwise the corresponding same-size support exchange would exist.

Let
L=(r_2,...,r_m),  R'=(r_1,...,r_{m-1})
be the inherited endpoint truncations. Since H[V(L) union {x}] and H[V(R') union {x}] are non-Hamiltonian, inserting x into every position of either displayed truncation fails.

We claim that inserting x into every position of the full displayed order R also fails.

- Insertion before r_1 is already the left-end insertion into R', hence fails.
- Insertion after r_m is already the right-end insertion into L, hence fails.
- Insertion between r_1 and r_2 requires, among its tight triples, the left-end triple needed to insert x before r_2 in L. That truncated insertion fails, so the full insertion fails.
- Insertion between r_{m-1} and r_m requires, among its tight triples, the terminal triple needed to insert x after r_{m-1} in R'. That truncated insertion fails, so the full insertion fails.
- Every insertion between r_i and r_{i+1} for 2<=i<=m-2 is an insertion position internal to both endpoint truncations, so it fails there and therefore in R.

Hence x is noninsertable in the full displayed path R.

The failed endpoint insertions also give explicit comparison arcs. Put
e_i={r_i,r_{i+1}}, 1<=i<=m-1,
and f_i={x,r_i}, 1<=i<=m.
Failure of the left-end insertion into R' gives e_1->f_1, and failure of the right-end insertion into R' gives f_{m-1}->e_{m-2}. Failure of the left-end insertion into L gives e_2->f_2, and failure of the right-end insertion into L gives f_m->e_{m-1}. Thus all four stated endpoint constraints hold simultaneously.

Finally, applying the failed-insertion theorem of insert01 to the full path R gives a bounded obstruction involving x and at most four consecutive vertices of R. The point is that this obstruction now sits inside a path carrying simultaneous two-sided endpoint constraints forced by one common five-side displacement.


## Direct premises at migration

[]

## Direct consumers at migration

[]

## Supersession records at migration

[]

## Retained passed-version snapshot at migration

null
