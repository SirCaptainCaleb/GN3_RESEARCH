# Audit: isolated Hall blocks do not yet force opposite transfer polarity — preserved pre-item development

## Composition

(none yet)

## Development

## Audit correction

The previous development is withdrawn beyond its per-pair transfer statement.

For one failed concatenation
\[
A=(\ldots,u,v),\qquad B=(a,b,\ldots),
\]
if neither
\[
h(u,v,a),\qquad h(v,a,b)
\]
is tight, reversal antisymmetry gives
\[
h(a,v,u)=h(b,a,v)=1,
\]
so \((b,a,v,u)\) is a Hamiltonian four-path. Hence, absent that four-support, exactly one seam is tight and one of the two endpoint transfers is legal.

What is **not** proved is any relation between the transfer polarities for two different opposite paths. The earlier proof compared
\[
h(a_1,v,u)=h(a_2,v,u)=1
\]
by cyclically rotating one triple; this is invalid. Boundary tournaments distinguish only the reversal pair \((r,s,t)\) and \((t,s,r)\), with the middle vertex fixed.

Thus the claimed opposite-polarity theorem, directed near-balance inequalities, and unconditional potential descent are withdrawn. See [[audit_same_hall_transfer_polarity_is_not_excluded_by_boundary_antisymmetry]] for the independent audit.
