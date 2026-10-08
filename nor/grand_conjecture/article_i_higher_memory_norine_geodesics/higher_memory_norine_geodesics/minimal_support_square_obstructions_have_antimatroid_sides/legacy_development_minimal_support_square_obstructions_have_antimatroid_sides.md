# Minimal support-square obstructions have antimatroid sides — preserved pre-item development

## Minimal top-missing squares have antimatroid side restrictions

Let
\[
\mathcal F=\mathcal F_{\sigma,S}
\]
be a NOR feasible-support family. Recall that \(\mathcal F\) is accessible.

Suppose \(\mathcal F\) is not union-closed. By the local square reduction, choose a top-missing square
\[
C,\qquad C\cup\{a\},\qquad C\cup\{b\}\in\mathcal F,
\qquad
C\cup\{a,b\}\notin\mathcal F
\tag{1}
\]
with \(|C|\) minimum among all top-missing squares.

### Proposition
Each of the restricted families
\[
\mathcal F|_{C},
\qquad
\mathcal F|_{C\cup\{a\}},
\qquad
\mathcal F|_{C\cup\{b\}}
\]
is union-closed, hence is an antimatroid on its support after discarding elements that occur in no feasible set.

### Proof
Accessibility is inherited by restriction.

Suppose, for example, that
\[
\mathcal F|_{C\cup\{a\}}
\]
were not union-closed. The local square-completion characterization of accessible union closure would then give a top-missing square
\[
D,\quad D\cup\{x\},\quad D\cup\{y\}\in\mathcal F,
\qquad
D\cup\{x,y\}\notin\mathcal F
\]
with
\[
D\cup\{x,y\}\subseteq C\cup\{a\}.
\]
Therefore
\[
|D|\le |C|-1,
\]
contradicting the minimal choice of (1). The \(C\cup\{b\}\) restriction is symmetric, and the restriction to \(C\) follows a fortiori. \(\square\)

### Interpretation
A first failure of union closure in a NOR support family is concentrated in one missing top:
\[
\begin{array}{ccc}
&&C+a+b\quad\text{infeasible}\\
&\nearrow&&\nwarrow\\
C+a&&&&C+b\\
&\nwarrow&&\nearrow\\
&&C.
\end{array}
\]
Everything strictly below either side already has antimatroid support structure.

Thus higher-arity NOR does not first fail by widespread loss of union closure. It first fails by trying to glue two antimatroid side systems across a common antimatroid base.

The remaining obstruction is order-theoretic rather than set-theoretic. Support union closure is perfect on each side, but the witness orders realizing those supports need not synchronize across the missing top.

This gives a refined closure target:

> classify the minimal incompatibility of two tight-path witness languages carried by the antimatroid restrictions on \(C+a\) and \(C+b\), and show that the incompatibility either yields a one-change order or descends to a smaller support square.

This is the natural higher-window replacement for tournament insertion, where the two side witness languages do synchronize and no top-missing square exists.
