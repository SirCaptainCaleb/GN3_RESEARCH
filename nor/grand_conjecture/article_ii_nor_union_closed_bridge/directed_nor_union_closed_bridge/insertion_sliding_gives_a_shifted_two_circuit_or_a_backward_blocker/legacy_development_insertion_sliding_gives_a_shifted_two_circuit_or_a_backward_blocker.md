# Insertion sliding gives a shifted two-circuit or a backward blocker — preserved pre-item development

## Sliding a missing vertex yields a two-circuit or a backward blocker

Work in ternary arity. Let \(U\) be a front circuit in \(\mathcal F_{\tau,F}\), with
\[
F=(f_1,f_2),\qquad \tau=1-\sigma.
\]
Fix \(x\in U\), and choose a \(\tau\)-tight deletion witness
\[
W_x=(y_1,\ldots,y_k,f_1,f_2)
\]
for \(U\setminus\{x\}\), where \(k=|U|-1\). Put
\[
y_{k+1}=f_1,\qquad y_{k+2}=f_2,
\]
and define the insertion scan
\[
s_i=h(x,y_i,y_{i+1}),\qquad 1\le i\le k+1.
\]

Because \(x\) is blocked at the exposed front of \(W_x\),
\[
s_1=\sigma.
\]
Because the singleton \(\{x\}\) is feasible at the original tail \(F\),
\[
s_{k+1}=h(x,f_1,f_2)=\tau.
\]
Hence some index \(i\le k\) satisfies
\[
s_i=\sigma,\qquad s_{i+1}=\tau.
\]

Set
\[
a=y_i,\qquad b=y_{i+1},\qquad c=y_{i+2}.
\]
Then
\[
h(x,a,b)=\sigma,qquad
h(x,b,c)=\tau,qquad
h(a,b,c)=\tau,
\]
the last identity coming from tightness of \(W_x\).

### Transition lemma
At every such \(\sigma\to\tau\) transition, exactly one of the following two structural outcomes occurs.

1. **Shifted two-circuit.**
   If
   \[
   h(a,x,b)=\sigma,
   \]
   then \(\{a,x\}\) is a two-element minimal infeasible support for the shifted tail \((b,c)\) in color \(\tau\).

2. **Backward blocker.**
   If
   \[
   h(a,x,b)=\tau,
   \]
   then \(i>1\), and with \(p=y_{i-1}\),
   \[
   h(p,a,x)=\sigma.
   \]

### Proof
At the shifted tail \((b,c)\), both singleton supports are \(\tau\)-feasible:
\[
h(x,b,c)=\tau,qquad h(a,b,c)=\tau.
\]
The ordering
\[
(x,a,b,c)
\]
cannot be \(\tau\)-tight because its first triple has color \(\sigma\).

If also \(h(a,x,b)=\sigma\), then the other possible two-support ordering
\[
(a,x,b,c)
\]
also fails at its first triple. Hence both singletons are feasible but the pair is not, so \(\{a,x\}\) is a two-element front circuit at tail \((b,c)\).

Now suppose instead
\[
h(a,x,b)=\tau.
\]
Since also \(h(x,b,c)=\tau\), replacing the local segment
\[
a,b,c
\]
of \(W_x\) by
\[
a,x,b,c
\]
preserves \(\tau\)-tightness from the window beginning at \(a\) onward. If \(i=1\), there is no earlier window, so this replacement would produce a \(\tau\)-tight witness for all of \(U\), contradicting that \(U\) is a front circuit. Thus \(i>1\).

Let \(p=y_{i-1}\). The only new earlier window created by the insertion is
\[
(p,a,x).
\]
All later new windows have color \(\tau\), while all untouched windows of \(W_x\) have color \(\tau\). Therefore infeasibility of \(U\) forces
\[
h(p,a,x)=\sigma.
\]
This is the backward blocker. \(\square\)

### Reversal form
In the backward-blocker case, reversal antisymmetry also gives
\[
h(x,a,p)=\tau.
\]
Thus the obstruction has moved one step backward while simultaneously creating a legal reversed local triple. The four vertices \(p,a,x,b\) satisfy
\[
h(p,a,x)=\sigma,qquad
h(x,a,p)=\tau,qquad
h(a,x,b)=\tau,qquad
h(x,a,b)=\sigma.
\]

### Significance
This is a first local circuit-contraction mechanism for the punctured-Boolean obstruction. Sliding a missing vertex from the blocked front toward its feasible terminal singleton cannot pass from blocking color \(\sigma\) to feasible color \(\tau\) silently. At the transition one either obtains an actual two-element circuit at a shifted tail, or the failure is pushed exactly one window backward.

A closure route can now try to iterate the backward-blocker alternative across suitably chosen deletion witnesses. Termination at a shifted two-circuit would reduce an arbitrary front circuit to the rigid size-two geometry already identified with the two-hole obstruction. The missing step is to show that repeated recentering cannot cycle indefinitely among backward blockers.
