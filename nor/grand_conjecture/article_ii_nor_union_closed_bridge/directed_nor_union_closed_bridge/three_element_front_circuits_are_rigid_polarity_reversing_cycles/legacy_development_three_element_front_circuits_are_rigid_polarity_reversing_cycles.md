# Three-element front circuits are rigid polarity-reversing cycles — preserved pre-item development

## Three-element front circuits are rigid cyclic obstructions

Work in ternary arity. Let
\[
F=(f_1,f_2),\qquad \tau=1-\sigma,
\]
and let \(U=\{a,b,c\}\) be a front circuit in the opposite-color family \(\mathcal F_{\tau,F}\). Thus every proper subset of \(U\) is \(\tau\)-feasible ending at \(F\), while \(U\) itself is not.

Define a directed relation \(D_F\) on \(U\) by
\[
x\to y
\quad\Longleftrightarrow\quad
h(x,y,f_1)=\tau.
\]

### Theorem
The digraph \(D_F\) is a directed 3-cycle. More precisely, after relabeling,
\[
a\to b,\qquad b\to c,\qquad c\to a,
\]
and the reverse three arcs are absent. Moreover
\[
h(a,b,c)=h(b,c,a)=h(c,a,b)=\sigma,
\]
while the three reversed triples have color \(\tau\).

### Proof
Because every two-element subset of \(U\) is \(\tau\)-feasible ending at \(F\), for each unordered pair \(\{x,y\}\) at least one of
\[
h(x,y,f_1),\qquad h(y,x,f_1)
\]
equals \(\tau\). Hence between each pair, \(D_F\) contains at least one directed edge.

Now fix distinct \(x,y,z\in U\) and suppose
\[
y\to z,
\]
so \(h(y,z,f_1)=\tau\). If also
\[
h(x,y,z)=\tau,
\]
then
\[
(x,y,z,f_1,f_2)
\]
would be a \(\tau\)-tight witness for all of \(U\), contrary to the definition of a front circuit. Therefore
\[
h(x,y,z)=\sigma.
\]
Reversal antisymmetry gives
\[
h(z,y,x)=\tau.
\]
If \(y\to x\), then \(h(y,x,f_1)=\tau\), and
\[
(z,y,x,f_1,f_2)
\]
would again be a \(\tau\)-tight witness for \(U\). Thus \(y\not\to x\).

So every vertex of \(D_F\) has outdegree at most one. But \(D_F\) has at least one directed edge on each of its three unordered pairs, hence at least three directed edges total. The sum of outdegrees is therefore at least three and at most three. Consequently every vertex has outdegree exactly one and every unordered pair carries exactly one direction. The only tournament on three vertices with all outdegrees equal to one is the directed 3-cycle.

Relabel so
\[
a\to b,\quad b\to c,\quad c\to a.
\]
Applying the implication above to \(b\to c\), with remaining vertex \(a\), gives
\[
h(a,b,c)=\sigma.
\]
Cyclically,
\[
h(b,c,a)=h(c,a,b)=\sigma.
\]
Reversal antisymmetry gives color \(\tau\) on the three reversed triples. \(\square\)

### Interpretation
A three-element punctured-Boolean obstruction is therefore completely rigid at its common terminal state:

- the terminal attachment relation to \(f_1\) is a \(\tau\)-colored directed 3-cycle;
- the cyclic triples internal to \(U\) form a \(\sigma\)-colored tight 3-cycle;
- reversing the cyclic order swaps the two colors.

Thus the smallest genuinely higher obstruction is not merely witness incompatibility. It is a polarity-reversing cycle: the same cyclic orientation is \(\tau\) when read through the terminal coordinate \(f_1\), but \(\sigma\) on the internal ternary windows.

### Consequence for closure
For \(|U|=3\), no arbitrary facet synchronization remains to be studied. The obstruction has a unique qualitative form. Any proof excluding three-element front circuits may therefore work directly with this paired-cycle pattern, for example by recentering at one of the three terminal arcs or by splicing the internal \(\sigma\)-cycle against the original maximal \(\sigma\)-tight path beginning at \(F\).

Larger front circuits should be tested for whether every three-vertex contraction or terminal-link minor inherits this cyclic pattern; if so, a circuit-elimination mechanism may reduce the general obstruction to this rigid base case.
