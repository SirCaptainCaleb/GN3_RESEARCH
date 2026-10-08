# Six-coordinate ternary counterexamples force opposite-window coherence — preserved pre-item development

## Development

## Six-coordinate ternary counterexamples force opposite-window coherence

Work in coordinate arity \(r=3\) on exactly six coordinates. Suppose, for contradiction, that the directed translation-invariant sector of \(N_4\) has a counterexample.

For any cyclic coordinate order
\[
C=(v_1,\ldots,v_6),
\]
write its cyclic triple-status word as
\[
u_i=h(v_i,v_{i+1},v_{i+2}),
\]
and transition bits
\[
d_i=u_i\oplus u_{i+1},
\]
with indices modulo \(6\).

Because every cut is bad and a linear order keeps four triple statuses, every three consecutive transition bits satisfy
\[
d_i+d_{i+1}+d_{i+2}\ge2. \tag{1}
\]
The cyclic transition weight is even.

### Classification

Condition (1) says that two zero transition bits can never lie at cyclic distance \(1\) or \(2\). Hence there are at most two zeros. Since the number of ones is even, the number of zeros is also even. Therefore every cyclic transition word is of exactly one of the following two forms:

1. \(111111\), of variation \(6\);
2. a rotation of \(110110\), of variation \(4\).

In the second case the two zero transitions are antipodal.

Thus every cyclic order has variation \(4\) or \(6\). Moreover:

- in the variation-\(4\) case, every block of three transition bits has even parity, so
  \[
  u_{i+3}=u_i
  \quad\text{for all }i;
  \]
- in the variation-\(6\) case,
  \[
  u_{i+3}=1-u_i
  \quad\text{for all }i.
  \]

Hence for every cyclic order there is a bit \(\lambda(C)\) such that
\[
u_{i+3}=u_i\oplus\lambda(C)
\qquad\text{for all }i. \tag{2}
\]

Equivalently, for every ordering of the six coordinates
\[
(a,b,c,d,e,f),
\]
the three opposite-window XORs agree:
\[
h(a,b,c)\oplus h(d,e,f)
=
h(b,c,d)\oplus h(e,f,a)
=
h(c,d,e)\oplus h(f,a,b). \tag{3}
\]

Here \(\lambda(C)=0\) is exactly the four-change case and \(\lambda(C)=1\) the six-change alternating case.

### Minimum-counterexample specialization

If the six-coordinate counterexample were minimum and \(C\) were obtained by closing a one-change deletion order as in the four-change extremal-cycle lemma, then \(C\) necessarily has variation \(4\). Therefore \(\lambda(C)=0\), so all three antipodal cyclic triple windows have equal colors.

### Significance

Equation (3) is a linear mod-\(2\) necessary condition on every six-coordinate counterexample. It packages the nonlinear bad-cut condition into a strong opposite-window coherence law, while the minimum-counterexample construction supplies many cycles specifically in the \(\lambda=0\) sector. A remaining closure route is to compare the \(\lambda\)-values under local reorderings until reversal antisymmetry forces an impossible cycle of equalities.
