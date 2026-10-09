# All rank-two antipodally odd affine edge colorings realize every full direction-color pattern by an odd-odd interleaving lemma

# Rank-two affine antipodally odd edge colorings realize ALL prescribed direction-color words

**Setup.** Let n>=2 and let A be an n x n matrix over F2 with A_ii=0 and A 1=1; the latter says EVERY ROW of A has ODD Hamming weight. Color undirected physical direction-i edges by
   c_i(x)=b_i+(A x)_i,
where the diagonal condition makes c_i(x)=c_i(x+e_i), and the row-odd condition gives c_i(bar x)=1+c_i(x). Assume rank_F2(A)=2.

**THEOREM.** For EVERY target t in F2^n, there is an actual root x in Q_n and a permutation p of all n coordinates such that along the genuine x-rooted FULL antipodal geodesic with direction order p, the unique direction-i edge has prescribed color t_i. In particular choosing t_i identically 0 (or identically 1) gives a MONOCHROMATIC antipodal geodesic. No bound on corank n-2 is needed.

**Step 1 (sharp matrix structure).** The rank-two row space has exactly three nonzero vectors r,s,r+s. Since every row of A is odd and parity is linear, exactly TWO nonzero row-space vectors have odd parity. Name these r,s. Thus every row of A is either r or s, and both occur. Let I={i: row_i(A)=r}, J={j:row_j(A)=s}; these nonempty sets partition [n]. The zero diagonal forces r_i=0 for EVERY i in I and s_j=0 for EVERY j in J; hence supp(r)=P is a nonempty ODD-cardinality subset of J, and supp(s)=Q is a nonempty ODD-cardinality subset of I. In particular r and s have disjoint nonempty supports and are linearly independent as expected.

**Step 2 (two parity registers).** For any initial root x, let alpha=r dot x and beta=s dot x. Since P and Q are disjoint nonempty subsets, alpha,beta can be chosen INDEPENDENTLY as either bit by selecting x on one coordinate of P and one of Q and setting other root bits arbitrarily. For a full direction word p, when direction i in I is traversed, its actual color is
    C_i=b_i+alpha+#(P-directions BEFORE i in p) mod 2.
For a direction j in J,
    C_j=b_j+beta+#(Q-directions BEFORE j in p) mod 2.
Define q_k=b_k+t_k. Achieving C=t is equivalent to making each i in I appear when parity of used P is alpha+q_i, and each j in J appear when parity of used Q is beta+q_j.

**Step 3 (exact odd-odd interleaving lemma).** Let p,q be POSITIVE ODD integers. A word with p occurrences of I and q occurrences of J is said to have statistics a=# I letters with an EVEN number of J predecessors, b=# J letters with an EVEN number of I predecessors. Such a word with prescribed integers 0<=a<=p,0<=b<=q exists IF AND ONLY IF a+b is ODD.

Necessity: write a= sum_I(1+# preceding J) and b=sum_J(1+# preceding I), both modulo two. Every cross-type unordered pair has exactly one of its two letters precede the other, so
  a+b =p+q+pq=1 mod 2
because p,q are odd.

Sufficiency, by induction in steps of TWO on p. For p=1, choose a word consisting of b initial J letters, the unique I, and q-b final J letters. The number b of J letters with even I parity is exactly b, and the unique I contributes a=1 iff b is EVEN, so precisely all pairs with a+b odd are realized. Suppose the assertion holds for p-2, where p>=3 remains odd. If desired a<=p-2, take a realizing word for (p-2,q,a,b) and APPEND two I letters after it. Since q is odd, those I letters see ODD J count and contribute zero to a, while their total count two leaves every J parity unchanged; hence b remains unchanged. If a>=2, take a realizing word for (p-2,q,a-2,b) and PREPEND two I letters. They see zero previous J and contribute two to a; they again leave every J parity unchanged. The ranges a<=p-2 and a>=2 cover every 0<=a<=p for p>=3; parity is unchanged by the +/-2 shift, so the induction applies. QED.

**Step 4 (realize all target bits).** Apply the lemma to the marked coordinates Q subset I and P subset J, whose sizes p=|Q| and q=|P| are odd. Select beta arbitrarily (say beta=0), and let
   bcount = #{j in P : q_j=beta}.
Choose alpha∈F2 so that
   acount=#{i in Q: q_i=alpha}
has opposite parity to bcount, i.e. acount+bcount is odd. Such an alpha always exists, since switching alpha replaces acount by p-acount and p is odd, flipping its parity.
By the lemma, an interleaving of the marked directions can be chosen with precisely acount marked I=Q positions having even used-P parity and bcount marked J=P positions having even used-Q parity. Assign the actual named coordinates having q_i=alpha to the even-P marked I positions, the other Q coordinates to the odd-P positions; similarly, assign named P coordinates with q_j=beta to even-Q marked J positions and the remaining P coordinates to odd-Q positions. This produces a marked-coordinate word satisfying ALL required colors on Q∪P.

Finally insert the unmarked coordinates I\Q and J\P. Each unmarked coordinate affects NEITHER of the two parity registers (it is in neither P nor Q). Because there is at least one marked J=P step, both parities of used-P occur among the gaps of the marked word, and similarly because there is at least one marked I=Q step, both parities of used-Q occur. Insert each unmarked i in I\Q at ANY gap whose used-P parity equals alpha+q_i; insert each unmarked j in J\P at ANY gap whose used-Q parity equals beta+q_j. They may share gaps in any order. Their insertion preserves all marked parity counts. This gives a full direction permutation p satisfying every required edge-color equation. Choose root x with r dot x=alpha and s dot x=beta by Step 2. Every direction is traversed exactly once, so the resulting genuine n-edge path is antipodal and has the full target direction-indexed color word. QED.

**Algorithm and generalization significance.** The proof gives an effective polynomial-time construction: extract the two row classes and disjoint odd sets P,Q; choose alpha,beta and the desired even counts; construct the odd-odd marked interleaving by the two-letter induction; insert unmarked coordinates; choose root from the two parity equations. One can implement this in O(n^2), or O(n) with linked buckets for the interleaving. The proof handles matrices of rank two and corank n-2 for arbitrarily large n, extending the team's rank>=n-1 affine theorem and its functional-graph 2-junta theorem, neither of which covers the general case here. The rank-one case is impossible for n>=2: if all n nonzero odd rows were the same r, diagonal zero would force r_i=0 for every i, contradicting odd weight. Hence rank TWO is the smallest possible rank of an active odd affine edge coloring.

**Exact frontier.** At rank THREE, the parity-odd row space has FOUR possible row types rather than two, yielding a coupled four-class parity walk instead of the present two-register interleaving. Even the arbitrary-target affine surjectivity theorem remains unproved in that case by these arguments. No claim is made here that unrestricted arbitrary antipodally odd (nonaffine) edge coloring or ordered-three-face NORI is solved.
