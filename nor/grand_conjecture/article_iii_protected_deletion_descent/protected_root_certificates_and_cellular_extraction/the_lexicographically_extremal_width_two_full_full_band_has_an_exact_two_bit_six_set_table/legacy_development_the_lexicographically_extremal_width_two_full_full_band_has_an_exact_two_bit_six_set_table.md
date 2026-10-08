# The lexicographically extremal width-two full-full band has an exact two-bit six-set table — preserved pre-item development

## The lexicographically extremal width-two full-full band has an exact two-bit six-set table

Work in the coboundary-flat alternating ternary sector. Let a lexicographically maximal two-change order contain six consecutive coordinates
\[
(a,b,c,d,e,f)
\]
with local word
\[
0,1,1,0.
\]
By §257 both bounding transitions are fully curved, and lexicographic extremality additionally forces
\[
t:=\alpha(b,c,e)=1,\qquad
u:=\alpha(a,b,e)=1.
\]

The original and full-curvature data are
\[
abc=0,quad bcd=1,quad cde=1,quad def=0,
\]
\[
abd=1,quad acd=0,quad cdf=0,quad cef=1.
\]

Parity on \(\{b,c,d,e\}\) gives
\[
bde=1.
\]
Parity on \(\{a,b,c,e\}\) gives
\[
ace=0,
\]
and parity on \(\{a,b,d,e\}\) gives
\[
ade=1.
\]

Define the two remaining free bits
\[
r:=abf,qquad s:=bcf.
\]

Then every other increasing triple is forced. Parity gives
\[
bdf=1-s,qquad bef=s,
\]
and
\[
acf=adf=r+s,qquad aef=1+r+s
\]
with addition in \(\mathbf F_2\).

Thus the complete increasing-triple table is
\[
\begin{array}{c|cccc}
&abc&abd&abe&abf\\
&0&1&1&r
\end{array}
\]
together with
\[
acd=0, ace=0, acf=r+s, ade=1, adf=r+s, aef=1+r+s,
\]
\[
bcd=1, bce=1, bcf=s, bde=1, bdf=1-s, bef=s,
\]
\[
cde=1, cdf=0, cef=1, def=0.
\]

### Theorem

Up to the fixed exterior collars, a lexicographically extremal width-two full-full band has exactly four possible six-set types, indexed by \((r,s)\in\{0,1\}^2\).

This classification uses only:

- the global two-change lexicographic extremality of §257;
- full curvature at the two band boundaries;
- coboundary flatness.

It does not use the stronger maximal-threshold-band rotations of §221.

### Consequence

Any completion of the width-two branch may now work directly with these four symbolic types. In particular the remaining distinction is purely a distance-four/five chord distinction at the two endpoint collars. No additional internal six-set bit exists.
