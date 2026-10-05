# Lemma 1

## Metadata

- ID: snake_accounting_and_the_4348_equality_problem_the_fixed_entrance_bound_subsection_a
- Parent Section: snake_accounting_and_the_4348_equality_problem_the_fixed_entrance_bound
- Position: 1
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Cold composition

Let \(h\) be an ascending edge of edge rank \(q\ge4\), and let \(v\) be terminal at \(h\). Then
\[
\bigl|\{f\ni v:\phi(f)\le q\}\bigr|
\le
\left\lfloor\frac{11q-5}{8}\right\rfloor . \tag{1}
\]

#### Proof
Choose a \(q\)-edge path
\[
P=(g_1,\ldots,g_q)
\]
with last edge \(g_q=h\) and last vertex \(v\). Let
\[
x=g_{q-1}\cap h.
\]
Since \(h\) is ascending, \(\phi(x)=q-1\). Put
\[
W=V(P)\setminus h.
\]
For every edge \(f\ne h\) containing \(v\) with \(\phi(f)\le q\), define
\[
C_f=(f\setminus\{v\})\cap W.
\]
If \(C_f=\varnothing\), then a final segment of \(P\) followed by \(f\) gives a path longer than \(\phi(f)\). Thus \(C_f\ne\varnothing\). Linearity implies that the sets \(C_f\) are pairwise disjoint, and each has size one or two.

Write
\[
z_i=g_i\cap g_{i+1}\qquad(1\le i\le q-1),
\]
write \(g_1=\{a_1,b_1,z_1\}\), and for \(2\le i\le q-1\) let \(b_i\) be the private vertex of \(g_i\). The vertices
\[
a_1,\quad b_1,\quad b_{q-2},\quad z_{q-2}
\]
cannot occur as singleton sets \(C_f\): in each case replacing an initial or final segment of \(P\) by \(f\) gives a \(q\)-edge path with last vertex \(x\), contradicting \(\phi(x)=q-1\).

After these exclusions, the possible singleton positions occur in
\[
B_1=\{z_1\},
\qquad
B_i=\{b_i,z_i\}\quad(2\le i\le q-3),
\]
together with \(b_{q-1}\). A singleton in the forward position of \(B_i\) excludes specified singleton positions two steps later, because otherwise the two corresponding edges splice with \(P\) to produce a \(q\)-edge path ending at \(x\). Recording whether \(B_{i-1}\) and \(B_i\) contain a singleton gives the four-state recurrence
\[
00\to00:0,\quad 00\to01:2,\quad
01\to10:0,\quad 01\to11:1,
\]
\[
10\to00:0,\quad 10\to01:1,\quad
11\to10:0.
\]
After four steps every finite state value increases by \(3\). Hence the number \(s\) of singleton sets satisfies
\[
s\le
\left\lceil\frac{3q-8}{4}\right\rceil . \tag{2}
\]

Let \(d\) be the number of sets \(C_f\) of size two and let \(u\) be the number of unused vertices of \(W\). Since \(|W|=2q-2\),
\[
s+2d+u=2q-2.
\]
Therefore
\[
\bigl|\{f\ni v:\phi(f)\le q\}\bigr|
=
1+s+d
\le
q+\left\lfloor\frac{s}{2}\right\rfloor
\le
\left\lfloor\frac{11q-5}{8}\right\rfloor .
\]
For \(q=2,3\) the corresponding bounds are \(1,2\). ∎

Define
\[
\gamma(1)=0,\quad \gamma(2)=1,\quad \gamma(3)=2,
\qquad
\gamma(q)=\left\lfloor\frac{11q-5}{8}\right\rfloor\quad(q\ge4).
\]

## Development

Let \(h\) be an ascending edge of edge rank \(q\ge4\), and let \(v\) be terminal at \(h\). Then
\[
\bigl|\{f\ni v:\phi(f)\le q\}\bigr|
\le
\left\lfloor\frac{11q-5}{8}\right\rfloor . \tag{1}
\]

#### Proof
Choose a \(q\)-edge path
\[
P=(g_1,\ldots,g_q)
\]
with last edge \(g_q=h\) and last vertex \(v\). Let
\[
x=g_{q-1}\cap h.
\]
Since \(h\) is ascending, \(\phi(x)=q-1\). Put
\[
W=V(P)\setminus h.
\]
For every edge \(f\ne h\) containing \(v\) with \(\phi(f)\le q\), define
\[
C_f=(f\setminus\{v\})\cap W.
\]
If \(C_f=\varnothing\), then a final segment of \(P\) followed by \(f\) gives a path longer than \(\phi(f)\). Thus \(C_f\ne\varnothing\). Linearity implies that the sets \(C_f\) are pairwise disjoint, and each has size one or two.

Write
\[
z_i=g_i\cap g_{i+1}\qquad(1\le i\le q-1),
\]
write \(g_1=\{a_1,b_1,z_1\}\), and for \(2\le i\le q-1\) let \(b_i\) be the private vertex of \(g_i\). The vertices
\[
a_1,\quad b_1,\quad b_{q-2},\quad z_{q-2}
\]
cannot occur as singleton sets \(C_f\): in each case replacing an initial or final segment of \(P\) by \(f\) gives a \(q\)-edge path with last vertex \(x\), contradicting \(\phi(x)=q-1\).

After these exclusions, the possible singleton positions occur in
\[
B_1=\{z_1\},
\qquad
B_i=\{b_i,z_i\}\quad(2\le i\le q-3),
\]
together with \(b_{q-1}\). A singleton in the forward position of \(B_i\) excludes specified singleton positions two steps later, because otherwise the two corresponding edges splice with \(P\) to produce a \(q\)-edge path ending at \(x\). Recording whether \(B_{i-1}\) and \(B_i\) contain a singleton gives the four-state recurrence
\[
00\to00:0,\quad 00\to01:2,\quad
01\to10:0,\quad 01\to11:1,
\]
\[
10\to00:0,\quad 10\to01:1,\quad
11\to10:0.
\]
After four steps every finite state value increases by \(3\). Hence the number \(s\) of singleton sets satisfies
\[
s\le
\left\lceil\frac{3q-8}{4}\right\rceil . \tag{2}
\]

Let \(d\) be the number of sets \(C_f\) of size two and let \(u\) be the number of unused vertices of \(W\). Since \(|W|=2q-2\),
\[
s+2d+u=2q-2.
\]
Therefore
\[
\bigl|\{f\ni v:\phi(f)\le q\}\bigr|
=
1+s+d
\le
q+\left\lfloor\frac{s}{2}\right\rfloor
\le
\left\lfloor\frac{11q-5}{8}\right\rfloor .
\]
For \(q=2,3\) the corresponding bounds are \(1,2\). ∎

Define
\[
\gamma(1)=0,\quad \gamma(2)=1,\quad \gamma(3)=2,
\qquad
\gamma(q)=\left\lfloor\frac{11q-5}{8}\right\rfloor\quad(q\ge4).
\]
