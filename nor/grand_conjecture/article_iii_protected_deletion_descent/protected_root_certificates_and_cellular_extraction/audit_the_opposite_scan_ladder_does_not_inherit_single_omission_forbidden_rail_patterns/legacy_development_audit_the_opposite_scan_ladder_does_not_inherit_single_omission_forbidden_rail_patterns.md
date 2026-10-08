# Audit: the opposite-scan ladder does not inherit single-omission forbidden rail patterns — preserved pre-item development

## Audit: the opposite-scan ladder does not inherit the single-omission forbidden rail patterns

The exact rung identity of §310 is valid. Its final invocation of the §290 rail-pattern exclusions requires correction.

### Where §290 applies

Root §290 starts with a genuine good deletion witness
\[
O_x
\]
on \(V\setminus\{x\}\). Inserting \(x\) at any gap produces a **full order on \(V\)**. Since the ambient instance is a counterexample, every such insertion is bad.

That full-order obstruction is what excludes:
- a scan pattern \(010\) centered strictly inside the zero phase, because the corresponding insertion duplicates a zero and remains one-change;
- a scan pattern \(101\) centered strictly inside the one phase, by the complementary argument.

### The two-exterior ladder is different

In §§299–310,
\[
O
\]
is an order of
\[
V\setminus\{x,z\}.
\]
Inserting \(x\) into \(O\) produces an order only on
\[
V\setminus\{z\},
\]
which is a proper subinstance. Such an insertion is allowed to be NOR-good; indeed the crossed residue explicitly has the endpoint insertions
\[
xO,\qquad Ox
\]
both good.

Thus a local \(010\) pattern in the \(x\)-scan, or a \(101\) pattern in the \(z\)-scan, does not contradict counterexamplehood. It may simply encode another good deletion witness of a proper subinstance.

Therefore the sentence in §310 asserting the §290 forbidden patterns “for either rail” is unsupported in the doubly-deleted state.

### Unconditional ladder data

What survives without extra hypotheses is exactly:

\[
X_1=0,\quad Z_1=1,\qquad
X_{m-1}=1,\quad Z_{m-1}=0,
\]
\[
R_1=R_m=0,
\]
and for every \(i\),
\[
\boxed{R_{i+1}\oplus R_i=X_i\oplus Z_i}.
\]

The pair-insertion packet at gap \(i\) is still exactly
\[
(X_{i-1},R_i,R_{i+1},Z_{i+1}),
\]
with endpoint clipping.

Any further monotonicity or forbidden-pattern restriction on a rail needs one of:
1. a separate hypothesis that the corresponding exterior coordinate blocks every insertion into \(O\); or
2. an extremal choice among the proper-subinstance good insertions that makes an improving insertion impossible.

### Strategic consequence

Good interior rail patterns should be treated as **useful exits**, not excluded. They create new good deletion witnesses with one of \(x,z\) inserted and the other omitted, precisely the witness class on which the endpoint/protected-root machinery can act.

Hence the crossed-ladder program should split at each rail event:
- a good single insertion gives a new deletion carrier and endpoint-relative descent;
- a genuinely blocking interval permits the codimension-two step-function analysis of §§159–161;
- otherwise the exact rung square remains the correct bookkeeping object.

This correction prevents importing a full-instance obstruction one deletion level too early.
