# Exact shortest antipodal window-shift distance: batched-buffer root transport and amplified monochromatic connector density

# Batch exterior-bit transport using a moving outer buffer: antipodal H_i paths of length approximately n

Let n>=5 and let i be a fixed coordinate. For pairwise distinct outer directions u,v different from i, let W_z(u,i,v) denote the ACTUAL physical ordered three-face through z with ordered free directions (u,i,v). The face depends on exterior bits of z only. Let H_i be the genuine physical window-shift graph whose adjacent vertices are consecutive ordered-three-face windows on a four-edge geodesic and whose shared middle pair of directions contains i. Let tau W_z(u,i,v)=W_(bar z)(v,i,u) be the active NORI antipodal-reversal involution, even before a coloring is imposed.

**Lemma 1 (two-step exterior helper AND arbitrary outgoing-bit control).** Suppose u,v,w,k,i are five DISTINCT directions. There is a genuine two-edge H_i walk
  W_z(u,i,v) -- W_*(i,v,k) -- W_(z')(w,i,v)
with the following completely independent physical choices:
(A) the fixed exterior k-bit of the destination is EITHER the same as the initial fixed k-bit OR its complement, at will;
(B) the fixed exterior u-bit of the destination can be chosen ARBITRARILY, independently of (A);
(C) all other coordinates fixed outside the union of old and new free triples, apart from k, preserve their bits.
The new outer w is free at the destination and becomes unconstrained. An analogous two-edge walk
  W_z(u,i,v) -- W_*(k,u,i) -- W_(z')(u,i,w)
replaces the RIGHT outer v by w and can independently toggle helper k and prescribe the destination exterior v-bit.

Proof. For the left replacement, ordered triples (u,i,v) and (i,v,k) are consecutive ordered windows of a four-direction word (u,i,v,k). Similarly (w,i,v) and (i,v,k) are consecutive windows of (w,i,v,k), with the edge traversed backwards. In the physical first face, u is free, allowing any choice of its value in the intermediate face where u is fixed; the middle face makes k free, allowing its fixed value in the second face to be chosen independently. The destination frees w, while the middle face's w-bit agrees with the initial fixed w-bit. The remaining common fixed bits agree, giving two literal four-edge path witnesses by the exact physical-window incidence criterion. The right replacement uses (k,u,i) symmetrically. QED.

**Theorem 2 (short ALL-DIMENSION antipodal window transport).** For EVERY ordered physical three-face v=W_z(a,i,b), there is an EVEN, genuinely physical H_i path from v to tau(v)=W_(bar z)(b,i,a) of length at most
   L_n = 6                                  for n=5 or n=6,
   L_n = n-1                                for odd n>=7,
   L_n = n                                  for even n>=8.
Equivalently, with m=n-3 exterior coordinates, its length is at most 2(2+max{1,ceil((m-2)/2)}).

**Proof (explicit batched swap-and-flip construction).** Let E=[n]\{a,i,b}, |E|=m=n-3>=2. Choose
   s=max{1,ceil((m-2)/2)}
distinct buffer coordinates h_1,...,h_s in E. Let K=E\{h_1,...,h_s} be the remaining helper directions, |K|=m-s>=1. By choice of s,
   |K|=m-s <= s+2.
Perform the following sequence of t=s+2 two-step H_i outer replacements:
   (a,i,b) -> (h_1,i,b) -> (h_2,i,b) -> ... -> (h_s,i,b)
             -> (h_s,i,a) -> (b,i,a).
Every arrow is realized using Lemma 1 with a helper k in K. Thus EACH of the t arrows can independently toggle its chosen helper k, or leave k unchanged. Assign each of the |K| helper directions to a DIFFERENT arrow (possible because |K|<=t), and toggle it exactly once there. For all remaining arrows, use any helper in K without toggling it. The helper pool K stays exterior to every intermediate vertex type, so each k retains its physical fixed-bit identity throughout and ends COMPLEMENTED.

The buffers are treated differently. On the transition (h_j,i,b)->(h_(j+1),i,b), choose the newly fixed outgoing h_j bit to be the complement of its original z-bit; this choice is independent of the helper flip by Lemma 1. On the LAST arrow (h_s,i,a)->(b,i,a), likewise choose the outgoing h_s bit complemented. Each h_j was free throughout its temporary occupation as an outer direction, so its previous fixed value imposes no restriction at the outgoing transition. Therefore ALL buffer coordinates h_1,...,h_s also end complemented. The original a,b, and i are free again in the final face, so their bit values do not affect its physical identity. The final ordered tuple is exactly (b,i,a), with every coordinate exterior to {a,i,b} complemented, hence the final vertex is precisely tau(v). Every elementary arrow uses two certified H_i shift edges; total length is 2(s+2), even.

For m=2,3,4, one may choose s=1, giving six edges. For m>=4, the displayed formula simplifies to n-1 when n is odd, and n when n is even, as stated. QED.

**Theorem 3 (amplified universal monochromatic connector count).** Impose the ACTIVE NORI coloring axiom c(tau u)=1-c(u). Let E0=2^(n-2)(n-1)(n-2)(n-3) be the exact number of distinct physical H_i edges in EACH of the two oriented i-middle edge orbits. Let N_i be the total number of distinct good H_i edges (equal endpoint colors); each is a real monochromatic four-edge path with i among its two middle directions. Then
   N_i >= 2*ceil(E0/L_n).
In fact each of the two oriented edge orbits contains at least ceil(E0/L_n) monochromatic edges.

Proof. Let P be the genuine even H_i path of length L<=L_n given by Theorem 2, connecting v to tau v. Every translate/permutation fixing i sends P to a true even-length physical path whose endpoints remain tau-mates, since geometric automorphisms commute with tau. Opposite endpoint colors on an EVEN-length path imply an ODD, in particular positive, number of equal-color edges (the number of color-changing edges must be odd). Average over the transitive group of all cube-bit translations and all coordinate permutations fixing i. As proved in nori_equivariant_window_shift_short_antipodal_path_many_middle_connectors_20261009, the two oriented i-middle edge orbits each have cardinality E0, and tau interchanges these two edge orbits while preserving good/bad status, so both contain exactly K good edges. If P has m_L,m_R edges of the two types, then
   1 <= E_g[# good edges in gP]
      = (m_L+m_R)K/E0
      = LK/E0 <= L_n*K/E0.
Hence K>=ceil(E0/L_n) and N_i=2K>=2ceil(E0/L_n). QED.

**Concrete gains.** For n=5, (E0,L_n)=(192,6), so N_i>=64 (32 of each orientation). For n=6, (E0,L_n)=(960,6), so N_i>=320 (160 each). For n=7, (E0,L_n)=(3840,6), so N_i>=1280 (640 each). Relative to the prior bound with L≈2n, the asymptotic connector guarantee nearly doubles. No stochastic independence or fictitious face equality is used; every path, step, coordinate flip and orbit edge is physical.

**Closure frontier.** The theorem strengthens the supply and global ubiquity of certified four-edge monochromatic connectors in EVERY coordinate, and provides a linear-length but roughly HALF-AS-LONG genuine antipodal root transport. Still, the good edge selected from different translated paths need not be the same, and a four-edge connector alone does not provide the full monochromatic reversed-two-tail complementary-support intersection or a full one-switch n-geodesic. The missing global compatibility theorem remains open.

**Theorem 4 (SHARP UNIVERSAL GRAPH-DISTANCE THEOREM; strengthening Theorem 2).** The transport upper bound above is EXACT for EVERY physical middle-i window v, without any coloring assumption:
\[
\boxed{d_{H_i}(v,\tau v)=2\max\{3,\lceil (n-1)/2\rceil\}
=\begin{cases}6,&n=5,6,\\n-1,&n\ge7\text{ odd},\\n,&n\ge8\text{ even}.\end{cases}}
\]
In particular no shorter root/window-shift path, including one passing through arbitrary physical hubs and direction orders, can beat the constructed batched-buffer path.

**Proof (combinatorial lower bound independent of all exterior bits).** Every edge of \(H_i\) connects an ordered face having \(i\) in its MIDDLE ordered position to a face having \(i\) at one of its TWO OUTER positions. Indeed if the consecutive triples are \((u,v,w),(v,w,t)\) and \(i\in\{v,w\}\), then \(i\) is middle on exactly one side and outer on the other. Therefore every path between v=W_z(a,i,b) and \(\tau v=W_{\bar z}(b,i,a)\) has EVEN length \(2t\). At the even path vertices its ordered tuples have the form
\[
(A_0,i,B_0),\ (A_1,i,B_1),\ldots,(A_t,i,B_t),
\quad (A_0,B_0)=(a,b),\quad(A_t,B_t)=(b,a).
\]
Each two-edge segment between successive even positions retains at least ONE outer coordinate and therefore changes AT MOST ONE entry in the ordered pair \((A_j,B_j)\). It may also retain BOTH entries while moving only the physical root. The graph on injective ordered pairs in which one entry may change cannot move \((a,b)\) to \((b,a)\) in fewer than THREE transitions: changing a directly to b while b occupies the other slot is forbidden, and similarly in the other direction. Hence \(t\ge3\).

Let \(E=[n]\setminus\{a,i,b\}\), \(m=|E|=n-3\). Every coordinate \(k\in E\) is fixed in the initial physical face at bit \(z_k\), and fixed in the target antipodal physical face at bit \(1-z_k\). Along any actual window-shift EDGE, a coordinate that is fixed in BOTH ordered faces has the SAME physical fixed bit: both windows come from one four-edge geodesic and the coordinate is not traversed. Consequently every \(k\in E\) MUST appear among the free coordinates of AT LEAST ONE window vertex somewhere on the \(2t\)-edge transport path.

We count the number of DISTINCT original E-directions that can thus become free.
(a) At an even vertex the free triple is \((A_j,i,B_j)\). Each original exterior direction \(k\in E\) that ever appears as \(A_j\) or \(B_j\) must be removed from that pair by some later two-edge transition, because the FINAL pair is \((b,a)\). Removing \(k\) uses a transition changing one outer entry. In addition BOTH initially free a and b must each be removed from their initial respective outer slots at least once to reach swapped final positions; these are TWO DISTINCT transitions, also changing at most one entry each. Thus at most \(t-2\) DISTINCT E-directions can ever occur as even-stage outer buffers.
(b) Each ODD window lies between two even stages and has \(i\) in an OUTER position. Its free ordered triple contains i, ONE outer direction retained across those two adjacent even stages, and AT MOST ONE additional helper direction not already free in those even stages. There are exactly t such odd windows, so they can expose AT MOST t further distinct E-directions.
Every one of the m initial exterior coordinates must be exposed as free somewhere; hence
\[
m\le(t-2)+t=2t-2,\quad
t\ge \left\lceil\frac{m+2}{2}\right\rceil
=\left\lceil\frac{n-1}{2}\right\rceil.
\]
Together with \(t\ge3\), every such path has
\[
2t\ge2\max\{3,\lceil(n-1)/2\rceil\}=L_n.
\]
Theorem 2 constructs a path AT that length. Equality follows. QED.

**Optimality significance.** This is the EXACT antipodal distance inside the full physically valid coordinate-i window-shift graph, not merely optimal within the particular batched-buffer algorithm. Consequently the orbit-averaging coefficient \(1/L_n\) in Theorem 3 cannot be improved by shortening an antipodal H_i path; further density improvements require a different averaging argument, multiple simultaneous antipodal transports, or additional global color structure. The sharp metric still does NOT imply a full one-switch antipodal NORI geodesic.
