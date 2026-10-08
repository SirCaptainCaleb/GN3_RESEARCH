# Extremal arbitrary-scan deletion dynamics always close or eject a protected root

## Metadata

- ID: extremal_arbitrary_scan_deletion_dynamics_always_close_or_eject_a_protected_root
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 297
- Row version: 1
- Development version: 1
- Composition version: 2
- Composition stale: False

## Composition

The audited extremal arbitrary-scan deletion dynamics close or eject an actual protected root with all changed boundary windows retained. The flat scan recurrence is no longer an independent closure target; the remaining work is the root's ambient realization and extraction.

## Development

## Extremal arbitrary-scan deletion dynamics always close or eject a protected root

Work in a minimum coboundary-flat alternating ternary counterexample.

Choose among all one-change deletion witnesses, reversals, and global color complements a normalized witness
\[
O,\qquad w(O)=0^p1^q,
\]
lexicographically minimizing
\[
(p,\ q-p).
\]
By §287,
\[
p,q\ge3.
\]

Let \(x\) be the omitted coordinate. Since every insertion of \(x\) would otherwise give a spanning NOR order, \(x\) is an insertion blocker for \(O\).

### Corrected arbitrary-scan replacement applies recursively

The audited arbitrary-scan replacement theorem in ternary §3 applies whenever both phases have length at least three. It produces a genuine one-change deletion witness by replacing one old coordinate with the omitted coordinate on one side of the switch.

Because \(p\) is globally minimal, the first replacement cannot shorten the zero phase. Hence it is forced to the right, with transfer distance
\[
d\in\{2,3\},
\]
and new profile
\[
(p+d,q-d).
\]

Every resulting deletion witness again has both phase lengths at least three by §287. Therefore the corrected replacement theorem remains available at every subsequent state; its former short-phase caveat has disappeared in a minimum counterexample.

### Phase drift cannot persist at the extremal profile

The audited replacement-dynamics theorem (ternary §6) shows that two consecutive replacements have only the outcomes
\[
(d,e)=(2,2),\ (3,3),\ (3,2).
\]

The unequal case \((3,2)\) changes the profile by
\[
(p,q)\mapsto(p+1,q-1).
\]
After normalization by reversal if needed, this strictly decreases \(q-p\) while preserving the lower bound \(p\). This contradicts the chosen lexicographic extremality.

Thus an extremal trajectory must enter one of the two same-profile rank-two recurrences.

### Distance three: antipodal recurrence

The \((3,3)\) recurrence is the exact two-state antipodal backtrack. The audited antipodal theorem (ternary §38) gives:

- a spanning NOR order; or
- a strict phase-imbalance improvement; or
- in the unique caged equality residue, a transverse nonzero protected quotient-root exit.

The first closes NOR; the second contradicts extremality. Hence survival forces a protected-root exit.

### Distance two: directed \(A_2\) recurrence

The \((2,2)\) recurrence is the exact three-state directed \(A_2\) replacement cycle of ternary §6 / Article II §207.

The audited residual scan theorems (ternary §§65–66) cover both possibilities for each residual scan:

- a later \(0\to1\) rise;
- no later rise.

In either case the recurrent \(A_2\) state yields a spanning NOR order or, after a strict boundary-safe enlargement and finite flat combing, a fully-curved protected physical root.

Thus survival again forces a protected-root exit.

### Theorem

For a lexicographically extremal deletion profile in a minimum counterexample,
\[
\boxed{\text{the arbitrary insertion/replacement dynamics cannot recur inside the flat class.}}
\]

Every trajectory either proves NOR or exits through an actual protected root. There is no remaining flat replacement cycle, no short-phase terminal state, and no unbounded scan-wandering branch.

Consequently the arbitrary-scan flat sector is fully routed into the protected-root realization problem. The unresolved global problem is now the interaction and extraction of protected roots; flat deletion dynamics themselves are no longer an independent frontier.
