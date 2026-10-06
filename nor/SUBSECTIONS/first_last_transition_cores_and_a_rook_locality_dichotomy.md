# First--last transition cores and a rook-locality dichotomy

## Metadata

- ID: first_last_transition_cores_and_a_rook_locality_dichotomy
- Parent Section: higher_memory_norine_geodesics
- Position: 29
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development


## First--last transition cores and a rook-locality dichotomy

Fix a coordinate-label arity \(r\ge 2\) and a reversal-antisymmetric directed coloring
\[
h(v_1,\ldots,v_r)\in\{0,1\},
\qquad
h(v_r,\ldots,v_1)=1-h(v_1,\ldots,v_r).
\]
For a permutation
\[
\pi=(v_1,\ldots,v_n),
\]
write
\[
m=n-r+1,\qquad
c_i=h(v_i,\ldots,v_{i+r-1})
\quad(1\le i\le m),
\]
and
\[
d_i=c_i\oplus c_{i+1}
\quad(1\le i<m).
\]

Assume \(\pi\) is bad, so \(\sum_i d_i\ge 2\). Let
\[
p=\min\{i:d_i=1\},
\qquad
q=\max\{i:d_i=1\}.
\]
Then \(p<q\).

Define
\[
A_\pi=(v_1,\ldots,v_p),\qquad
M_\pi=(v_{p+1},\ldots,v_{q+r-1}),\qquad
B_\pi=(v_{q+r},\ldots,v_n).
\]
The initial status run \(c_1,\ldots,c_p\) is constant, the final status run
\(c_{q+1},\ldots,c_m\) is constant, and
\[
|M_\pi|=q+r-p-1=r+(q-p)-1\ge r.
\]
Thus every bad chamber canonically determines a three-block coarsening
\[
A_\pi\mid M_\pi\mid B_\pi
\]
of its coordinate order.

### Transition rook

Define
\[
\rho(\pi)=(v_p,\ v_{q+r}).
\]
If
\[
\pi^{\mathrm{rev}}=(v_n,\ldots,v_1),
\]
then its transition word is the reversal of \(d\). Hence its first and last
transition positions are
\[
p'=m-q,\qquad q'=m-p,
\]
and therefore
\[
\rho(\pi^{\mathrm{rev}})=(v_{q+r},v_p).
\]
So reversal swaps the two rook coordinates exactly. Equivalently,
\[
L(\pi)=e_{v_p}-e_{v_{q+r}}
\]
is a reversal-odd type-\(A\) root.

The whole signed outer support is also antipodal. Put
\[
\varepsilon_\pi(x)=
\begin{cases}
+1,&x\in A_\pi,\\
0,&x\in M_\pi,\\
-1,&x\in B_\pi.
\end{cases}
\]
Then
\[
\varepsilon_{\pi^{\mathrm{rev}}}=-\varepsilon_\pi.
\]

### Adjacent-swap locality

Let \(\pi'\) be obtained from \(\pi\) by swapping positions \(j,j+1\), and
assume both chambers are bad.

Only status coordinates whose \(r\)-windows meet the swapped positions can
change. Hence only
\[
c_i,\qquad j-r+1\le i\le j+1,
\]
can change, after intersecting with the valid range. Therefore only transition
coordinates in
\[
J=[j-r,j+1]\cap\{1,\ldots,m-1\}
\]
can change.

If there is a transition strictly to the left of \(J\), then the first
transition and the first coordinate of \(\rho\) are unchanged. If there is a
transition strictly to the right of \(J\), then the last transition and the
second coordinate of \(\rho\) are unchanged.

Consequently, if an adjacent transposition changes both coordinates of the
transition rook, then neither transition word has a transition outside \(J\).
Thus
\[
q-p\le r+1
\]
for \(\pi\), and likewise for \(\pi'\). Hence
\[
|M_\pi|\le 2r,\qquad |M_{\pi'}|\le 2r.
\]

In particular, every bad chamber with
\[
q-p\ge r+2
\]
has genuine rook locality on every adjacent Coxeter edge incident to it: an
adjacent move can change at most one coordinate of \(\rho\).

There is a parallel set-valued locality statement. If a ground label \(x\) is
not one of the two coordinates being transposed, then \(x\) cannot change
directly from \(A\) to \(B\), or from \(B\) to \(A\), across that edge.

For example, suppose \(x\) keeps position \(t\), lies in \(A_\pi\), and lies
in \(B_{\pi'}\). Then
\[
t\le p,\qquad t\ge q'+r,
\]
where \(q'\) is the last transition of \(\pi'\), so \(p-q'\ge r\). Since the
two transition words agree outside \(J\), this forces \(p,q'\in J\). Hence
\[
j\le q'+r\le t\le p\le j+1,
\]
so \(t\in\{j,j+1\}\), contrary to \(x\) being unswapped. The opposite sign
change is symmetric.

### Structural consequence

A counterexample therefore produces a canonical reversal-antipodal
transition-rook field on permutation chambers with a sharp dichotomy:

- away from chambers whose first-to-last transition span is at most \(r+1\),
  the field has the one-coordinate-at-a-time locality of a rook labeling;
- every failure of that rook locality forces all color changes into a
  transition core containing at most \(2r\) ground coordinates.

This connects the overlap-cut formulation to the chain-level rook
architecture. The remaining obstruction is localized: a Wu--Yang-style
root-chain argument must cross the compressed-core chambers coherently, or a
direct surgery must rule those chambers out in a genuine counterexample.

The statement itself does not close NOR; bounded core size alone is not a
terminating improvement.


## Frontier

- Development version when composed: None
- Development version now: 1
