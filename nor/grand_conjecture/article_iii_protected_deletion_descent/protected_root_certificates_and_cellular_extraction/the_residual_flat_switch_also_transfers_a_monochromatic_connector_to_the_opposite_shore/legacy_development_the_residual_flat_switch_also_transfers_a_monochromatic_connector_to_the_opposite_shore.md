# The residual flat switch also transfers a monochromatic connector to the opposite shore — preserved pre-item development

## Composition

(none yet)

## Development

## The residual flat switch also transfers a monochromatic connector to the opposite shore

Use the switching-normalized shortcut-free split
\[
B\to z\to A\to x,
\]
with \(x\) a sink, and let a NOR-good \(B\)-order have switch core
\[
(a,b,c,d)
\]
satisfying
\[
\alpha(a,b,c)=0,\qquad \alpha(b,c,d)=1.
\]
Assume the five-block connector insertion is in its unique residual parity state
\[
e_p=1,\qquad e_{p+2}=0.
\]
Since \(e=1\oplus t\) on consecutive \(B\)-edges,
\[
t(a,b)=0,\qquad t(c,d)=1.
\]

Suppose now that the switch tetrahedron is FLAT. For a \(0\to1\) flat transition its off-faces are
\[
\alpha(a,b,d)=0,\qquad \alpha(a,c,d)=1.
\]

Put
\[
s=t(b,c)\in\{0,1\}.
\]
Using
\[
\alpha(r,s,t)=t(r,s)\oplus t(s,t)\oplus t(t,r)
\]
and the four displayed face values gives
\[
t(a,c)=1-s,\qquad
t(b,d)=1-s,\qquad
t(a,d)=s.
\]

Thus there are exactly two flat switch types.

### Case \(s=0\)

The relevant \(B\)-edges are
\[
a\to c,\qquad c\to b,\qquad b\to d,\qquad c\to d.
\]
Hence
\[
(c,b,d)
\]
is a transitive forward triple:
\[
c\to b\to d,\qquad c\to d.
\]

Then the six-coordinate order
\[
\boxed{(a,z,x,c,b,d)}
\]
has word
\[
0000.
\]

Indeed:

- \(\alpha(a,z,x)=0\), since \(a\to z\to x\) and \(a\to x\);
- \(\alpha(z,x,c)=0\), since \(c\) dominates both \(z,x\) while \(z\to x\);
- \(\alpha(x,c,b)=0\), since \(c\to b\) and both dominate \(x\);
- \(\alpha(c,b,d)=0\), since \(c\to b\to d\) and \(c\to d\).

The final exposed pair is \(b\to d\), a forward \(B\)-edge.

### Case \(s=1\)

Now
\[
b\to c,\qquad c\to a,\qquad b\to a,
\]
so
\[
(b,c,a)
\]
is a transitive forward triple.

Then
\[
\boxed{(d,z,x,b,c,a)}
\]
has word
\[
0000.
\]

Again:

- \(\alpha(d,z,x)=0\);
- \(\alpha(z,x,b)=0\);
- \(\alpha(x,b,c)=0\), since \(b\to c\);
- \(\alpha(b,c,a)=0\), since \(b\to c\to a\) and \(b\to a\).

The final exposed pair is \(c\to a\), a forward \(B\)-edge.

### Uniform opposite-shore ports

In both cases the first exposed pair is
\[
(r,z)
\]
for some \(r\in B\), and the last exposed pair is a forward \(B\)-edge.

For every \(u\in A\),
\[
\alpha(u,r,z)=0
\]
because \(r\to z\to u\) and \(r\to u\).

Likewise, for the final forward pair \(q\to q'\) in \(B\),
\[
\alpha(q,q',u)=0
\]
because every \(B\)-vertex dominates every \(A\)-vertex.

Therefore each displayed six-coordinate block has color-0-compatible ports toward the entire shore \(A\). Its reversal is a color-1 connector.

### Theorem

The unique parity-drop residue
\[
(e_p,e_{p+2})=(1,0)
\]
always transfers the monochromatic connector across the shortcut-free split:

- if the \(B\)-switch tetrahedron is fully curved, §353 supplies the six-coordinate opposite-shore connector;
- if it is flat, the constructions above supply one.

Hence the parity-drop state is never a terminal phase-alignment obstruction. It is an exact **shore-transfer state**.

The remaining problem is therefore global termination of repeated shore transfers, not persistence of the local pair \((1,0)\).
