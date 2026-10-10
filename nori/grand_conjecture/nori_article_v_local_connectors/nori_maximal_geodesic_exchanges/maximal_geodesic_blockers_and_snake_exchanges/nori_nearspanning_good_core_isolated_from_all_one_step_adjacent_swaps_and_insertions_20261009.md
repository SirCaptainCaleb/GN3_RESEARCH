# All-dimensional simultaneous obstruction to every transposition and insertion of a good near-spanning core

# Every transposition and every insertion of a fixed near-spanning good path can be blocked

**Theorem (all dimensions n>=7).** There exists a legal reversal-odd coordinate-only ordered-three-face coloring of Q_n such that, at EVERY root, P=(1,2,...,n-1) is good with color word 0,1,...,1, while (a) interchanging ANY TWO direction positions in P, adjacent or otherwise, produces a path with at least two color switches, and (b) inserting the missing direction n into P at ANY position produces at least two switches. In dimension n=6 the same holds with (a) restricted to adjacent swaps, by the separate explicit construction in version 1. The result refutes any support-growth rule built from one good-preserving transposition or insertion of this particular core. It leaves other globally good paths available.

**Explicit construction.** Write m=n-1>=6. On each oriented triple of distinct directions in [m], define p(a,b,c)=1 when the permutation (a,b,c) of its increasingly sorted entries has EVEN sign, and 0 when ODD. Reversing a triple toggles p. Obtain h by FLIPPING p on each of the following reversal orbits (each displayed orientation and its reverse):
(1,2,3), (2,1,3), (1,3,4), (1,3,2), (1,2,4), (2,4,3), (1,4,3), (1,2,5), (2,5,4);
(m,2,3), (m-1,2,3), (m-2,m-1,1), (m-2,m-1,2).
These 13 reversal orbits are pairwise distinct for m>=6. Thus h(c,b,a)=1-h(a,b,c). Its consecutive increasing triples (i,i+1,i+2) have h=0 at i=1 and h=1 for 2<=i<=m-2. The core P has exactly one switch.

**Proof: all transpositions.** Let Q_(i,j) be obtained from P by swapping positions 1<=i<j<=m, and let W_t be its t-th ordered-triple color, 1<=t<=m-2. Every triple not meeting a swapped position has its original color (zero at t=1, one at t>=2). We produce three time-ordered windows of colors 0,1,0 or 1,0,1 in every case:

1. If i>=4, W_1=0 and W_2=1. Also W_(i-1)=0: the orientation there is (i-1,j,i) when j=i+1, and (i-1,j,i+1) otherwise. Both have odd sorting parity and meet no exception. Since i-1>=3 this proves 0,1,0.
2. If i=3, for j=4 the first three colors are 0,1,0 by the flipped triples (1,2,4),(2,4,3), followed by the ordinary odd triple (4,3,5). For j=5 they are 0,1,0 by the flips (1,2,5),(2,5,4), followed by (5,4,3). For j>=6 they are 1,0,1: the triples are (1,2,j),(2,j,4),(j,4,5), with unflipped even,odd,even parity.
3. If i=2, j=3 gives first colors 1,0,1 from (1,3,2),(3,2,4),(2,4,5). If j=4, windows 1,2,4 have colors 1,0,1, arising from (1,4,3),(4,3,2),(2,5,6); m>=6 ensures the fourth window exists. If 5<=j<m, W_1=0,W_2=1,W_(j-1)=0: these are (1,j,3),(j,3,4),(j-1,2,j+1). If j=m, W_1=0,W_2=1,W_(m-2)=0, with the last color supplied by the exceptional triple (m-2,m-1,2).
4. If i=1, j=2 produces W_1,W_2,W_3=1,0,1, from (2,1,3),(1,3,4),(3,4,5). For 3<=j<=m-2, W_1=1, W_(j-1)=0, W_j=1: the final two orientations are (j-1,1,j+1) and (1,j+1,j+2), and the first is (3,2,1) when j=3 or (j,2,3) otherwise. If j=m-1 then W_1=0,W_2=1,W_(m-2)=0, using the exceptional (m-1,2,3); the last orientation (m-2,1,m) is odd. If j=m, the same 0,1,0 witness uses exceptional orientations (m,2,3) and (m-2,m-1,1).

All index ranges are valid for m>=6. Each witness is a trio of genuine ordered physical windows.

**Proof: all insertions and physical validity.** Extend h to triples containing n by the independent all-insertions-barred prescription in Item nori_all_dimensions_nearspanning_one_switch_core_all_single_insertions_bad_20261009:
h(n,1,2)=1; h(1,n,2)=1; h(n,2,3)=0;
for 2<=j<=n-3 set h(j-1,j,n)=0,h(j,n,j+1)=1,h(n,j+1,j+2)=0;
and h(n-3,n-2,n)=1,h(n-2,n,n-1)=0,h(n-2,n-1,n)=0.
That Item verifies every insertion has at least two switches. Its triples all involve n, whereas our transposition prescriptions do not. It specifies no reversal pair inconsistently. Fill remaining reversal orbits arbitrarily, enforcing h(c,b,a)=1-h(a,b,c), and color each actual physical ordered face of orientation (a,b,c) by h(a,b,c) independently of exterior bits. This satisfies precisely the active NORI antipodal-reversal axiom. Because the coloring is coordinate-only all statements hold simultaneously at all roots.

**Exact limitation.** This prohibits a good-preserving ONE-transposition or ONE-insertion step from this chosen core. It makes no assertion about single-letter relocation moves, which can be guaranteed in boundary-switch cases by the physical end-rotation surgery. It does not assert P is globally longest among all good paths or that full good paths are absent.

**Check.** Deterministic enumeration confirmed the displayed 13-orbit formula and all transpositions in n=7,...,31; the four-case proof above is uniform in dimension.
