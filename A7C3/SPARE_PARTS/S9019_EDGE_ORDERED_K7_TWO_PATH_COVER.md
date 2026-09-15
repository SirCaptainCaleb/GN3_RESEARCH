# S9019 — Every Edge-Ordered K7 Has a Two-Path Increasing Cover

## Theorem

Let K_7 have any strict total order on its 21 ordinary edges. Then its seven vertices can be partitioned into at most two vertex-disjoint increasing paths. Equivalently, no edge ordering of K_7 has increasing path-cover number at least three.

## Proof

Index the 21 ordinary edges of K_7 lexicographically as e_0,...,e_20. For each 0<=i<j<=20 introduce one Boolean variable X_{ij}, interpreted as “e_i precedes e_j in the edge order”. Since exactly one of e_i<e_j and e_j<e_i holds, one bit per unordered edge-pair is enough; there are C(21,2)=210 variables.

TOTAL-ORDER CLAUSES. For every i<j<k add
  (not X_{ij}) OR (not X_{jk}) OR X_{ik},
  X_{ij} OR X_{jk} OR (not X_{ik}).
These are exactly the two clauses excluding the two directed 3-cycles on {e_i,e_j,e_k}. There are 2*C(21,3)=2660 such clauses. A tournament on the 21 edge-objects with no directed triangle is transitive, so these clauses are equivalent to the existence of one strict total edge order realizing all X_{ij}.

TWO-PATH-COVER CLAUSES. Take every ordered vertex permutation pi=(v_0,...,v_6) and every cut c in {1,...,6}. This represents the two oriented vertex paths P=(v_0,...,v_{c-1}) and Q=(v_c,...,v_6). For a path W=(w_0,...,w_s), write f_t={w_t,w_{t+1}}. The path is increasing exactly when every consecutive comparison f_t<f_{t+1} holds, t=0,...,s-2; a singleton or dimer contributes no comparison. For each (pi,c), collect all comparison literals required simultaneously by P and Q and add the single clause which is the disjunction of their negations. Thus the clause says that this particular ordered two-path cover is not increasing on both rails.

Every spanning cover by two increasing paths occurs among these permutation/cut representations after orienting each rail increasingly and ordering the two rails. A Hamilton increasing path also yields one of these two-path covers by splitting off its first vertex as a singleton, so forbidding all represented two-path covers forbids covers by at most two paths. Conversely, a satisfying assignment of all cover-forbidding clauses represents a strict edge order with no spanning increasing two-path cover.

After exact deduplication, the cover family contributes 12,600 distinct clauses: 7,560 clauses of length three and 5,040 clauses of length four. Together with the 2,660 transitivity clauses, the final CNF has 210 variables and 15,260 clauses. Sorting literals in each clause by variable and sorting clauses lexicographically, the DIMACS-style text “lit ... lit 0” joined by newlines has SHA-256 `625270abc73035479584b613d96049c50cf10f22eb8e4bf565928f96e246c9eb`.

A deterministic watched-literal DPLL verifier performs unit propagation to closure, then branches on the unassigned variable of highest total literal occurrence, ties by lowest variable index, trying the majority-occurrence polarity first. On the full unsymmetrized CNF it terminates UNSAT after 355 recursive search nodes, maximum branch depth 24, with no satisfying leaf. Independently, the same 210 comparison bits were encoded as a binary MILP with the 15,260 transitivity and cover constraints; SciPy 1.17 `scipy.optimize.milp` with HiGHS reports infeasible. No vertex or edge-order symmetry assumption is used. Therefore no strict edge ordering of K_7 can avoid every spanning cover by at most two increasing paths.

## Why this is reusable

An exact finite base theorem for increasing path-cover problems. It is completely independent of minimum-counterexample structure and can be used whenever a seven-vertex edge-ordered residue appears.

## Scope and nonclaims

The theorem is specific to seven vertices. It does not classify extremal edge orders or address K8 and larger orders.

## Provenance

Rescued from accepted archived result `R971`. The archived result contains the complete verifier implementation and independent MILP formulation.
