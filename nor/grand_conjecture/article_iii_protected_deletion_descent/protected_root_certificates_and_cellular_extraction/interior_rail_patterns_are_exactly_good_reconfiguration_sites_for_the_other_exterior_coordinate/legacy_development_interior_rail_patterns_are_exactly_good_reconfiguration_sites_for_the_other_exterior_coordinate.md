# Interior rail patterns are exactly good reconfiguration sites for the other exterior coordinate — preserved pre-item development

## Composition

(none yet)

## Development

## Interior rail patterns are exactly good reconfiguration sites for the other exterior coordinate

Work in the crossed two-exterior setup with
\[
O=(w_1,\ldots,w_m),\qquad w(O)=0^p1^q,
\]
and define the \(x\)-insertion scan
\[
X_i=\alpha(x,w_i,w_{i+1}).
\]

Insert \(x\) between \(w_i\) and \(w_{i+1}\), with \(2\le i\le m-2\):
\[
H_i=(w_1,\ldots,w_i,x,w_{i+1},\ldots,w_m).
\]

The only new ternary windows are
\[
\alpha(w_{i-1},w_i,x)=X_{i-1},
\]
\[
\alpha(w_i,x,w_{i+1})=1-X_i,
\]
\[
\alpha(x,w_{i+1},w_{i+2})=X_{i+1}.
\]

Thus the exact replacement packet is
\[
\boxed{(X_{i-1},\,1-X_i,\,X_{i+1}).}
\]

### Inside the zero phase

If the insertion gap lies strictly inside the old zero phase, the two old windows being replaced and their immediate target neighborhood all have color \(0\).

Hence \(H_i\) preserves the one-change word exactly when
\[
X_{i-1}=0,\qquad 1-X_i=0,\qquad X_{i+1}=0,
\]
equivalently
\[
\boxed{X_{i-1}X_iX_{i+1}=010.}
\]

### Inside the one phase

If the insertion gap lies strictly inside the old one phase, the target color is \(1\). The insertion is good exactly when
\[
X_{i-1}=1,\qquad 1-X_i=1,\qquad X_{i+1}=1,
\]
equivalently
\[
\boxed{X_{i-1}X_iX_{i+1}=101.}
\]

### Interpretation in the crossed residue

The endpoint placements
\[
xO,\qquad Ox
\]
are already good deletion witnesses omitting \(z\).

Every interior \(010\) of the \(X\)-rail in the zero phase, and every interior \(101\) in the one phase, gives an additional good deletion witness omitting the same coordinate \(z\), now with \(x\) literally inside the carrier.

Since \(z\) is omitted from any such witness, every insertion of \(z\) into it produces a full ambient order and is blocked by counterexamplehood. Therefore these rail patterns are not nuisances: they are certified reconfiguration sites at which the full endpoint/protected-barrier machinery may be restarted with \(x\) frozen at an interior physical location.

This corrects the strategic role of the patterns excluded by §290 in the single-omission setting: one deletion level earlier they are precisely the useful good states.
