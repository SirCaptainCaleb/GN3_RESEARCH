# Seven reversal orbits block every missing-direction insertion into a good path and its genuine head rotation

# Seven-orbit simultaneous insertion obstruction for both ends of a physical head rotation

**Theorem (every n>=7).** There exists a legal antipodally reversal-odd physical ordered-three-face coloring of Q_n and a direction-distinct (n-1)-edge geodesic P whose ordered three-face color word is 0,1,...,1, such that BOTH P and its genuine root-shifted head rotation H(P) are good, have color words 0,1,...,1 and 1,...,1,0 respectively, and EVERY single insertion of the missing direction n into EITHER path gives >=2 window-color switches. The property holds at every root, simultaneously. Thus even the exact head rotation, its forced opposite terminal cap, and both complete insertion walls do not, by themselves, yield a support-growth step. This does not assert that P is a globally longest good path or that the full NORI conjecture fails.

**Construction.** Write m=n-1>=6. On an ordered triple (a,b,c) of distinct directions, let p(a,b,c)=1 when (a,b,c) has even permutation parity relative to its increasing sorting, and p=0 for odd parity. In particular p(c,b,a)=1-p(a,b,c). Let E consist of the following SEVEN reversal orbits, represented by
(1,2,3), (m-1,m,1), (1,m,n), (1,n,2), (3,2,n), (m-1,m,n), (m,1,n).
Every orbit contains its displayed triple and its reversed triple. The seven orbits are distinct for m>=6. Define
h(a,b,c)=p(a,b,c) XOR 1[the reversal orbit of (a,b,c) belongs to E].
Then h(c,b,a)=1-h(a,b,c). Give each actual physical ordered three-face F of ordered free-coordinate list (a,b,c) the color h(a,b,c), independent of all fixed exterior bits. This is a legal NORI coloring because the antipodal face with reversed order has the opposite h-value.

Let P=(1,2,...,m) and H=(2,3,...,m,1). The latter is the actual head rotation of P from the root after the first coordinate flip. For P, all increasing consecutive triples have baseline color 1 except (1,2,3), which is flipped to 0. For H the only new terminal window (m-1,m,1) is flipped from 1 to 0. Consequently their words are 0 1^(m-3) and 1^(m-3) 0. (There are m-2 windows each.)

**Insertion proof.** Number insertion slots j=0,1,...,m, where j directions precede the new n. We give increasing-position witnesses of >=2 switches; every mentioned triple is the actual ordered physical face window.

For P:
- j=0,1,2: the FIRST THREE window colors are 1,0,1. At j=0 they are (n,1,2),(1,2,3),(2,3,4); at j=1 they are (1,n,2),(n,2,3),(2,3,4); at j=2 they are (1,2,n),(2,n,3),(n,3,4). The indicated exceptional orbits fix the required colors.
- 3<=j<=m-1: the FIRST window is (1,2,3) of color 0; the SECOND has color 1 (it is (2,3,n) when j=3 and (2,3,4) otherwise); a later window (j,n,j+1) has color 0, by odd sorting parity. This gives 0,1,0.
- j=m: the first windows have colors 0 and 1, and the final (m-1,m,n) is 0 by its exceptional orbit, again 0,1,0.

For H:
- j=0: initial window (n,2,3) has color 0 through exceptional orbit (3,2,n), an interior old (2,3,4) has color 1, and the terminal old (m-1,m,1) has color 0. Witness 0,1,0.
- j=1: initial (2,n,3) has parity-color 0, next (n,3,4) has color 1, and the terminal old window is 0. Witness 0,1,0.
- 2<=j<=m-2: the three consecutive windows surrounding n have colors 1,0,1: the first is the ascending pair of neighboring old directions followed by n, the middle is the first neighboring old direction followed by n followed by the next old direction, and the third is n followed by the next two old directions. For j=m-2, the third is (n,m,1), whose exceptional (1,m,n) reversal orbit flips its parity color from 0 to 1. The other cases have the ordinary 1,0,1 parity pattern.
- j=m-1: an unchanged earlier window has color 1, (m-1,m,n) has exceptional color 0, and (m,n,1) has ordinary parity color 1. Witness 1,0,1.
- j=m: an unchanged earlier window has color 1, the old terminal (m-1,m,1) is 0, and the new terminal (m,1,n) is 1 through its exceptional orbit. Witness 1,0,1.

All slots are covered. Since the coloring is independent of exterior bits, the same certificates work at every root. Direct exhaustive evaluation of the displayed seven-orbit formula independently verified all 2n insertion cases for n=7,8,9,11,25,101.

**Strategic consequence.** A hypothetical dimension-independent support-growth theorem for a globally maximal NORI path must use more than (i) one good core, (ii) its forced good head rotation at a singleton phase, and (iii) their insertion obstruction certificates. It must invoke global maximality beyond this pair, additional root-coupled paths, or a genuinely higher-order exchange/topological invariant. The constructed coloring may still have full good geodesics elsewhere.

**Explicit full-dimensional witness in this same coloring.** In fact the permutation (1,2,4,5,...,n-2,n,3,n-1) has EVERY ordered three-face window of color 1. Consecutive increasing triples have even sorting parity and avoid all seven exceptional orbits; its two terminal non-increasing triples (n-2,n,3) and (n,3,n-1) likewise have even parity and avoid the exceptions. Thus the obstruction construction itself has a monochromatic FULL antipodal geodesic from every root. The obstruction is specifically to local advancement of the pair P,H, not to NORI closure. This explicit family was independently evaluated for n=7,...,199.

**Complete cyclic-rotation refinement.** The m consecutive cyclic ordered triples of the direction cycle (1,2,...,m) have color sequence C=(0,1^(m-3),0,1), because the wraparound triples (m-1,m,1) and (m,1,2) have colors 0 and 1. Every head rotation by r places corresponds to a length-(m-2) cyclic interval of C. EXACTLY TWO of the m cyclic rotations are good: the original starting at direction 1 (word 0,1^(m-3)) and its one-step head rotation starting at 2 (word 1^(m-3),0). Every interval starting at direction 3 contains 1,0,1; every interval starting at directions 4,...,m-1 contains 0,1,0 across the cyclic wrap; the interval starting at m contains 1,0,1. Hence the entire good part of this genuinely root-coupled cyclic-rotation orbit consists exactly of the two already insertion-blocked paths P and H. Even saturating all good cyclic rotations of a fixed near-spanning core supplies no single-insertion support-growth step. (The coloring still has the explicit monochromatic full witness given above.)
