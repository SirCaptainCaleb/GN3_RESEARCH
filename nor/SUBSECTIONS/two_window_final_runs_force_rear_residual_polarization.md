# Two-window final runs force rear residual polarization

## Metadata

- ID: two_window_final_runs_force_rear_residual_polarization
- Parent Section: higher_memory_norine_geodesics
- Position: 48
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

For the stated common-tail configuration with tail word σ^p(1−σ)^2 and three cyclic residual-pair deletion witnesses, the final tail vertex sees the cyclic residual pairs in color 1−σ. A contrary label constructs an explicit monochromatic n−1-vertex path and hence a full NOR order. The resulting rear-cap forks are valid local structure; eliminating the two-window final run still requires a controlled splice from the untouched prefix.

## Development

## The two-window final run forces a rear residual polarization

Work in the directed ternary sector, with
\[
h(z,y,x)=1-h(x,y,z).
\]
Let \(V\) be a minimum counterexample. Suppose
\[
T=(t_1,\ldots,t_m)
\]
has word
\[
\sigma^p(1-\sigma)^2,\qquad p\ge 1,
\]
and \(V\setminus V(T)=\{a,b,c\}\). Assume the three deletion orders
\[
(a,b,T),\qquad (b,c,T),\qquad (c,a,T)
\]
are one-change.

Write
\[
u=t_{m-1},\qquad w=t_m.
\]

From the common-tail rigidity theorem we already have
\[
h(u,w,a)=h(u,w,b)=h(u,w,c)=\sigma,
\]
the cyclic residual triples have color \(1-\sigma\), and
\[
h(a,b,t_1)=h(b,c,t_1)=h(c,a,t_1)=\sigma.
\]

### Proposition
In this configuration,
\[
h(w,a,b)=h(w,b,c)=h(w,c,a)=1-\sigma.
\]

### Proof
Suppose instead that
\[
h(w,a,b)=\sigma.
\]
Consider
\[
P=(u,w,a,b,t_1,\ldots,t_{m-2}).
\]
This path omits only \(c\).

Its first four relevant windows have color \(\sigma\):
\[
h(u,w,a)=\sigma,\qquad
h(w,a,b)=\sigma,\qquad
h(a,b,t_1)=\sigma,\qquad
h(b,t_1,t_2)=\sigma.
\]
All remaining windows lie in the truncated tail
\[
(t_1,\ldots,t_{m-2}).
\]
Because the original tail word is
\[
\sigma^p(1-\sigma)^2,
\]
removing its final two vertices removes exactly the two final \((1-\sigma)\)-windows. Hence every window of
\[
(t_1,\ldots,t_{m-2})
\]
has color \(\sigma\).

Therefore \(P\) is a monochromatic \(\sigma\)-tight path on \(n-1\) vertices. But a counterexample cannot contain a monochromatic tight path on \(n-1\) vertices: the omitted vertex either prepends in color \(\sigma\), giving a spanning monochromatic path, or is blocked, in which case reversal gives a spanning converging tight fork. Contradiction.

Thus
\[
h(w,a,b)=1-\sigma.
\]
Cyclically permuting \(a,b,c\) gives the other two identities. \(\square\)

### Corollary: a forced local tight fork at the rear cap
Reversal gives
\[
h(b,a,w)=h(c,b,w)=h(a,c,w)=\sigma.
\]
Together with
\[
h(u,w,a)=h(u,w,b)=h(u,w,c)=\sigma
\]
and the reversed residual-triple identities, this yields, for example, the color-\(\sigma\) converging fork
\[
(c,b,a,w)
\qquad\text{and}\qquad
(u,w,a)
\]
with center \((a,w)\); cyclic rotations give two analogous forks.

This does not yet exclude a two-window final run. Its value is that the \(q=2\) case is now rigid on both sides of the final tail vertex:
- the terminal pair \((u,w)\) sees every residual vertex in color \(\sigma\);
- the cyclic residual pairs immediately after \(w\) have color \(1-\sigma\);
- the corresponding reversed residual pairs immediately before \(w\) have color \(\sigma\).

Unlike the former suffix-polarization argument, the proof never treats a proper restriction as a counterexample. The truncated tail appears only inside an explicitly constructed \(n-1\)-vertex monochromatic path, and the contradiction comes from the already-proved near-spanning-path closure theorem on the full ambient set.

### Remaining closure target
To eliminate \(q=2\), one must use this rear-cap polarization together with the untouched \(\sigma\)-tight prefix
\[
(t_1,\ldots,t_{m-2})
\]
to force a spanning fork or a one-change order. Any such argument must control the bridge from the prefix's final pair into one of the three forced rear forks.
