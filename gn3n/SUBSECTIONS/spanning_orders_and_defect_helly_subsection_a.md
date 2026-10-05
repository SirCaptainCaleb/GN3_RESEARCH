# Defect intervals and the exact Helly criterion

## Metadata

- ID: spanning_orders_and_defect_helly_subsection_a
- Parent Section: spanning_orders_and_defect_helly
- Position: 1
- Row version: 4
- Development version: 4
- Composition version: 1
- Composition stale: False

## Cold composition

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


## Development

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
