# Odd Q6 coloring with no good alternating-root geodesic

# Alternating-pole restriction fails in dimension six

Partition six directions into four unmarked directions A and two marked directions M. Define
\[
h(a,b,c)=1 \quad\Longleftrightarrow\quad b\in A\text{ and }\{a,c\}\cap M\ne\varnothing.
\]
This triple label is invariant under reversal. For an ordered three-face F with k exterior coordinates fixed to one, define
\[
\chi(F,\pi)=\begin{cases}
0&k=0,\\
1\oplus h(\pi)&k=1,\\
h(\pi)&k=2,\\
1&k=3.
\end{cases}
\]
Since antipodality sends k to 3-k, reversal leaves h unchanged, and the corresponding displayed values are complementary, this is an antipodal-reversal-odd ordered-face coloring on Q6.

**Theorem.** Every full six-coordinate geodesic whose starting bits alternate in the traversal order has at least two color changes.

**Proof.** Let p=(p1,...,p6) be the traversal order. For starts 010101 and 101010 (in p order), all four windows have exterior-one weights 2 and 1, respectively: between windows the exiting direction pi enters the exterior in flipped state, the entering direction p(i+3) leaves it with the same state. Hence the color word is the h-word of p or its complement. The four-window h-word depends only on the positions occupied by the two M directions. The 15 cases, in increasing marked-position order, are

12:0100, 13:1010, 14:1101, 15:1010, 16:1001;
23:0010, 24:0101, 25:0110, 26:0101;
34:1001, 35:1010, 36:1011;
45:0100, 46:0101, 56:0010.

Each word has two or three color changes. Complementation preserves change count. Thus all alternating-pole geodesics fail. QED.

**Significance.** The established unrestricted Q6 NORI theorem nevertheless guarantees a good geodesic in this coloring. Thus every good full geodesic must visit at least two exterior Hamming-weight layers. The preceding all-dimensional central-layer tournament theorem is strictly conditional; no general argument can restrict to constant-central-weight paths.
