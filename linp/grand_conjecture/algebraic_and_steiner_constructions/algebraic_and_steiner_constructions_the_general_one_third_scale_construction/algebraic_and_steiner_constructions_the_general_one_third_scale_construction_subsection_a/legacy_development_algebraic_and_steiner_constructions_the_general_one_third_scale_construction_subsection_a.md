# Proposition 1 — preserved pre-item development

## Development

For every \(\ell\ge2\),
\[
\operatorname{ex}_L(n,P_\ell^{(3)})
\ge
\frac{\ell-1}{3}n-O(\ell^2). \tag{2}
\]

#### Proof
A linear \(3\)-uniform path with \(\ell\) edges has \(2\ell+1\) vertices. Hence every linear triple system on at most \(2\ell\) vertices is \(P_\ell^{(3)}\)-free.

If \(\ell\equiv1\) or \(2\pmod 3\), then
\[
2\ell-1\equiv1\text{ or }3\pmod6.
\]
Take a Steiner triple system on
\[
t=2\ell-1
\]
vertices. It has
\[
\frac{t(t-1)}6
\]
edges, so
\[
\frac{|E|}{t}
=
\frac{t-1}{6}
=
\frac{\ell-1}{3}.
\]

If \(\ell\equiv0\pmod3\), take a maximum partial triple system on
\[
t=2\ell\equiv0\pmod6
\]
vertices. Such a system has
\[
\frac{t(t-2)}6
\]
edges, and again
\[
\frac{|E|}{t}
=
\frac{t-2}{6}
=
\frac{\ell-1}{3}.
\]

Take \(\lfloor n/t\rfloor\) disjoint copies and leave the remaining vertices isolated. The omitted final component costs \(O(\ell^2)\) edges. ∎

To improve the leading coefficient, one needs components with density near or above \(\ell/3\) whose longest path is still shorter than \(\ell\).
