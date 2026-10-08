# The residual full switch transfers the monochromatic connector to the opposite shore — preserved pre-item development

## Composition

(none yet)

## Development

## The residual full switch transfers the monochromatic connector to the opposite shore

Use the switching-normalized shortcut-free split
\[
B\to z\to A\to x,
\]
and a NOR-good order of \(B\) whose unique switch is
\[
\alpha(a,b,c)=0,\qquad \alpha(b,c,d)=1.
\]

Suppose the five-block switch insertion of §346 is in its unique residual state
\[
e_p=1,\qquad e_{p+2}=0.
\]
Since for \(B\)-edges
\[
e=1\oplus t,
\]
this means
\[
t(a,b)=0,\qquad t(c,d)=1.
\]

Assume the switch tetrahedron \(\{a,b,c,d\}\) is fully curved. For a \(0\to1\) full transition its off-faces are
\[
\alpha(a,b,d)=1,\qquad
\alpha(a,c,d)=0.
\]

Put
\[
s=t(b,c).
\]
The four face equations force
\[
t(c,a)=s,\qquad
t(d,b)=s,\qquad
t(d,a)=s.
\]

Hence there are only two cases.

### Case \(s=0\)

The vertices \(b,a,c\) form the directed triangle
\[
b\to a\to c\to b,
\]
and each of \(a,b,c\) dominates \(d\).

Then the six-coordinate order
\[
\boxed{(b,z,x,a,c,d)}
\]
has word
\[
0000.
\]

Indeed:
\[
\alpha(b,z,x)=0
\]
because \(b\to z\to x\) and \(b\to x\);
\[
\alpha(z,x,a)=0
\]
because \(a\) dominates both \(z,x\) while \(z\to x\);
\[
\alpha(x,a,c)=0
\]
because \(a\to c\) and both dominate \(x\);
and
\[
\alpha(a,c,d)=0
\]
is the full-curvature off-face.

### Case \(s=1\)

Now
\[
b\to c\to d\to b
\]
is a directed triangle and \(b,c,d\) all dominate \(a\).

Then
\[
\boxed{(b,z,x,c,d,a)}
\]
again has word
\[
0000.
\]

The first two windows are as above, while
\[
\alpha(x,c,d)=0
\]
because \(c\to d\) and both dominate \(x\), and
\[
\alpha(c,d,a)=0
\]
because \(c\to d\to a\) is transitive.

### Opposite-shore ports

In either case the first exposed pair is
\[
(b,z),
\]
and the last exposed pair is a forward \(B\)-edge.

For every \(u\in A\),
\[
\alpha(u,b,z)=0,
\]
because \(b\to z\to u\) and \(b\to u\).

Likewise, if \(r\to s\) is the final pair of the displayed connector,
\[
\alpha(r,s,u)=0
\]
because both \(r,s\in B\) dominate \(u\).

Thus the six-coordinate block is not merely internally monochromatic: it has color-0-compatible ports on both sides toward the entire opposite shore \(A\). Its reversal is the corresponding color-1 connector.

### Consequence

The unique residual state of the five-block insertion is therefore not terminal when the \(B\)-switch is fully curved. It produces a new monochromatic connector block
\[
\{\text{four switch vertices of }B\}\cup\{x,z\}
\]
whose ports are uniform toward \(A\).

So the shortcut-free split has a genuine **shore-transfer move**:

- an \(A\)-triangle supplies the original five-coordinate connector;
- failure at a full \(B\)-switch converts it into a six-coordinate connector supported on the \(B\)-side;
- the reversed block supplies the opposite color.

This gives an undirected two-shore repair step of exactly the type needed for a Hartman least-unreachable component argument.
