# A singleton switching shore has exactly one exceptional endpoint-state type — preserved pre-item development

## A singleton switching shore has exactly one exceptional endpoint-state type

Assume a protected-shortcut-free switching split with minimum shore
\[
A=\{u\}.
\]
In switching-normalized form,
\[
B\to z\to u\to x,
\]
with every \(B\)-vertex also pointing to \(u\).

Let \(P_B\) be a NOR-good order of \(B\), made directed by switching bits, with internal ternary word \(c\) and endpoint parities
\[
(\epsilon_L,\epsilon_R).
\]

There are two canonical full block orders.

### Order I: \(P_B,z,u,x\)

The last three separator windows are
\[
\alpha(b_{r-1},b_r,z)=\epsilon_R,\qquad
\alpha(b_r,z,u)=0,\qquad
\alpha(z,u,x)=0,
\]
with clipping when \(|B|<2\).

Hence the full word is
\[
\boxed{c,\epsilon_R,0,0.}
\]

### Order II: \(u,x,P_B,z\)

Using the companion split of §333, the full word is
\[
\boxed{0,\epsilon_L,c,\epsilon_R}
\]
up to the same endpoint clipping.

Now classify the genuinely bichromatic case.

### If \(c=0^p1^q\)

Order I always has at least two changes because \(c\) already changes \(0\to1\) and the final \(00\) forces a later \(1\to0\).

Order II has at most one change exactly when
\[
\epsilon_L=0,\qquad \epsilon_R=1.
\]
Indeed then
\[
0,0,0^p1^q,1
\]
has one change. Any other port value creates an additional boundary change.

By the reversal involution §336, reversing \(P_B\) preserves the \(0\to1\) phase direction and transforms
\[
(\epsilon_L,\epsilon_R)
\mapsto
(1-\epsilon_R,1-\epsilon_L).
\]
The condition \((0,1)\) is fixed by this involution. Hence reversal creates no additional closing case.

Therefore a \(0\to1\) bichromatic shore closes by direct singleton-split composition iff
\[
\boxed{(\epsilon_L,\epsilon_R)=(0,1).}
\]

### If \(c=1^p0^q\)

Order I is NOR-good whenever
\[
\epsilon_R=0.
\]
If \(\epsilon_R=1\), reverse the shore. The reversed order has the same \(1\to0\) phase direction and new right parity
\[
\epsilon_R'=1-\epsilon_L.
\]
Hence the reversed Order I closes whenever \(\epsilon_L=1\).

Thus the only nonclosing port pair is
\[
(\epsilon_L,\epsilon_R)=(0,1).
\]

So for a \(1\to0\) bichromatic shore, direct singleton-split composition closes iff
\[
\boxed{(\epsilon_L,\epsilon_R)\ne(0,1).}
\]

### Monochromatic shore

If \(c\) is monochromatic, one of the two orientations supplied by §336 makes Order I have at most one change regardless of the original endpoint ports. Hence a monochromatic \(B\)-shore always closes.

### Exact singleton-shore residue

The only direct-composition failures are therefore the two complementary endpoint-state types
\[
\boxed{
\begin{array}{c|c}
\text{shore phase direction}&(\epsilon_L,\epsilon_R)\\ \hline
0\to1&\ne(0,1)\\
1\to0&(0,1)
\end{array}}
\]

Equivalently, the port pair \((0,1)\) selects exactly one of the two possible phase directions.

This turns the minimum-shore \(|A|=1\) branch into a finite local state obstruction. Any further Hartman-style reachability argument needs only show that the exceptional phase/port combination cannot persist under changing the good \(B\)-order, or that persistence forces a protected shortcut.
