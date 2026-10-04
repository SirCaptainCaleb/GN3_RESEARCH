# Spanning orders and defect Helly theory

**Summary:** The original two-cover problem is an exact interval-Helly problem on the defect line of a spanning order.

## Statement

For a spanning order, the two-cover condition is exactly the existence of one cut meeting every non-tight defect interval; failure is witnessed by two disjoint defects, and the extreme defects provide canonical coordinates for later topology.

## Body

## Defect intervals and the exact Helly criterion

### Spanning orders and status words

Let \(H\) be a boundary \(3\)-tournament on vertex set \(V\), and let
\[
\pi=(v_1,\ldots,v_n)
\]
be a spanning order. The cases \(n\leq1\) have path-cover number at most one. Throughout the cut formulation assume \(n\geq2\), and interpret the intersection of an empty defect family as the full cut set \(\{1,\ldots,n-1\}\). Write
\[
\epsilon_i(\pi)=
\begin{cases}
1,&(v_i,v_{i+1},v_{i+2})\text{ is tight},\\
0,&(v_i,v_{i+1},v_{i+2})\text{ is non-tight},
\end{cases}
\qquad 1\le i\le n-2.
\]
The word
\[
\epsilon_1(\pi)\cdots \epsilon_{n-2}(\pi)
\]
is the status word of \(\pi\).

The two-cover problem is already visible in one status word. Put a cut between \(v_j\) and \(v_{j+1}\), where \(1\le j\le n-1\). Every consecutive triple wholly contained in either side must be tight if the two inherited blocks are to be tight paths. A non-tight triple centered at status position \(i\) is harmless precisely when the cut separates one of its two adjacent vertex pairs.

It is convenient to encode this in the defect line from [[defect_lines_and_spanning_order_compression_the_defect_line_identity]]. Let the possible cuts be the vertices
\[
1,\ldots,n-1,
\]
and for every non-tight status position \(i\) put the defect edge
\[
I_i=\{i,i+1\}.
\]
Thus the defect family is an interval family on a line.

### The exact Helly theorem

**Theorem 1 (defect-interval Helly criterion).** A spanning order \(\pi\) yields a spanning two-cover by one cut if and only if
\[
\bigcap_{\epsilon_i(\pi)=0} I_i\ne\varnothing.
\]
Equivalently, the defect-line graph has vertex-cover number at most one.

**Proof.** A cut \(j\) leaves a non-tight triple inside one of the two inherited blocks exactly when \(j\notin I_i\). Hence both inherited blocks are tight exactly when \(j\) belongs to every defect interval. This is the asserted intersection condition. The graph formulation is the same statement, because the defect intervals are precisely the edges of the defect line. \(\square\)

The theorem is order-relative. Quantifying over all spanning orders gives the exact existence formulation
\[
\boxed{
\operatorname{pc}(H)\le2
\iff
\exists\pi\text{ such that }\bigcap_{\epsilon_i(\pi)=0}I_i\ne\varnothing.
}
\]

Because intervals on a line are Helly, failure has an especially sharp witness.

**Corollary 2 (separated defect pair).** If \(\pi\) does not yield a two-cover, then there are two non-tight positions \(i<j\) with
\[
I_i\cap I_j=\varnothing.
\]
Equivalently,
\[
j\ge i+2.
\]

Thus every bad spanning order contains two separated defects. There is no need to retain the entire defect set merely to certify failure.

### Reversal and the antipodal defect pair

Let
\[
\pi^{\rm rev}=(v_n,\ldots,v_1).
\]
Boundary antisymmetry gives
\[
\epsilon_i(\pi^{\rm rev})
=
1-\epsilon_{n-1-i}(\pi).
\]
Thus reversal reflects the status positions and complements the colors.

Consequently a counterexample has two simultaneous interval statements. Every spanning order contains two separated non-tight defects, and its reverse contains two separated non-tight defects corresponding to two separated tight positions of the original order. In the Freudenthal language introduced in the next Section, every bad chamber therefore carries a separated defect pair, and the antipodal chamber carries the complementary pair.

This is the exact supported content of the earlier informal phrase that every bad Freudenthal simplex “contains a pair.” No stronger mysterious pair theorem is assumed.

### Extreme defects and switch coordinates

The separated pair can be compressed further by choosing extreme witnesses. When the status word contains both colors, let
\[
a(\pi)=\text{first switch position},
\qquad
b(\pi)=\text{last switch position}.
\]
Equivalently, \(a\) and \(b\) mark the first and last boundaries between monochromatic runs. The reflected terminal coordinate
\[
\bar b(\pi)=m-b(\pi),
\qquad m=n-2,
\]
is chosen so that reversal exchanges \(a\) and \(\bar b\).

These extreme coordinates lose information: they remember only the outermost failure of a one-run description, not the complete defect family. Their virtue is topological. They are the coordinates from which the later rook labels and root vectors are built.

This distinction will remain important throughout the article:

- the defect intervals encode the **exact two-cover condition**;
- extreme switch coordinates are a **compression** designed for topology.

The later topological argument is useful only if its compressed recurrence can ultimately be returned to the exact defect or support formulations.


## Exact inversion-window criterion

### Exact inversion-window criterion

There is a sharper order-relative formulation of the two-cover problem than the extreme-switch compression.

Let
\[
\pi=(v_1,\ldots,v_n),\qquad m=n-2,
\]
with status word \(\epsilon_1,\ldots,\epsilon_m\). Define
\[
p(\pi)=\min\{i:\epsilon_i=0\},\qquad
q(\pi)=\max\{i:\epsilon_i=1\},
\]
using the conventions \(p=m+1\) if there is no zero and \(q=0\) if there is no one.

**Theorem (exact inversion-window criterion).**
\[
\boxed{\operatorname{pc}(H)\le2
\iff
\exists\pi\text{ with }q(\pi)\le p(\pi)+1.}
\]

**Proof.** Suppose first that \(q\le p+1\). Choose an integer cut \(j\) with
\[
q\le j\le p+1.
\]
Then every status wholly inside \(v_1,\ldots,v_j\), namely every \(\epsilon_i\) with \(i\le j-2\), equals \(1\), because \(j-2\le p-1\). Thus
\[
P=(v_1,\ldots,v_j)
\]
is tight. Every status wholly inside \(v_{j+1},\ldots,v_n\), namely every \(\epsilon_i\) with \(i\ge j+1\), equals \(0\), because \(j+1>q\). Boundary antisymmetry therefore makes
\[
Q=(v_n,\ldots,v_{j+1})
\]
tight. Hence \(P\mid Q\) is a spanning two-cover, with the evident empty-side convention at the ends.

Conversely, let \(P\mid Q\) be a spanning cover by at most two tight paths. Concatenate
\[
\pi=(P,Q^{\rm rev})
\]
and let \(j=|P|\). Every status with \(i\le j-2\) is \(1\), while every status with \(i\ge j+1\) is \(0\). Hence \(p\ge j-1\) and \(q\le j\), so \(q\le p+1\). \(\square\)

Thus a counterexample satisfies
\[
q(\pi)-p(\pi)\ge2
\]
for every spanning order. The quantity
\[
\delta(\pi)=q(\pi)-p(\pi)-1
\]
is an exact order-level two-cover deficiency: \(\delta\le0\) is already a certificate.

### Reversal coordinates for the exact obstruction

Put
\[
c(\pi)=m+1-q(\pi).
\]
Reversal-complement gives
\[
p(\pi^{\rm rev})=c(\pi),\qquad
c(\pi^{\rm rev})=p(\pi).
\]
Hence
\[
\psi(\pi)=e_{p(\pi)}-e_{c(\pi)}
\]
is an odd type-\(A\) root label:
\[
\psi(\pi^{\rm rev})=-\psi(\pi).
\]

Moreover
\[
\delta(\pi)=m-\bigl(p(\pi)+c(\pi)\bigr).
\]
Therefore the exact two-cover threshold is the anti-diagonal
\[
p+c\ge m,
\]
while every chamber of a counterexample lies strictly below it:
\[
p+c\le m-1.
\]

This exact inversion root retains substantially more theorem-relevant information than the first/last-switch root. Its tail is the first actual non-tight status, its head is the reflected last actual tight status, and the sum of the two root coordinates measures the exact distance from the two-cover window. It is therefore the natural root for a second pass through the barycentric balance argument.

## Metadata

- ID: spanning_orders_and_defect_helly
- Kind: section
- Version: 5
- Math version: 4
- Audit: unaudited
- Refutation: unrefuted

## Authoring state

- Subsection 1 — crystallized, version 4: Defect intervals and the exact Helly criterion
- Subsection 2 — HOT, version 2: Exact inversion-window criterion
