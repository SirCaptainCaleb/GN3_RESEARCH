# Active NORI Q5 coloring simultaneously saturates all 24 pentagon inequalities and the 2/5 geodesic density

# Sharp active-NORI five-direction pentagon and good-path density

**Theorem.** Some coordinate-only antipodal-reversal-odd ordered-three-face coloring of Q5 has precisely 48 one-switch and 72 two-switch full direction orders from every physical root, and no monochromatic full order. Thus the universal 2/5 rank-five good-path density and the 4(n-3)/5 mean full-switch bound (at n=5) are jointly sharp even in active NORI. This is a local-method sharpness theorem, not a grand-conjecture counterexample.

**Complete construction.** Give the five directions names 0,...,4. For each increasing triple a<b<c, the following three-bit row specifies the ordered-triple colors h(a,b,c), h(a,c,b), h(b,a,c), in that order:
012 010
013 000
014 010
023 001
024 110
034 110
123 010
124 010
134 111
234 111
Extend h to the three reversed triples by h(c,b,a)=1-h(a,b,c), h(b,c,a)=1-h(a,c,b), h(c,a,b)=1-h(b,a,c). For every actual physical three-face F, set c(F,(a,b,c))=h(a,b,c), regardless of the fixed exterior bits of F. By construction c(bar F,rev pi)=1-c(F,pi) everywhere.

**Exact verification of all cyclic five-window constraints.** For each cyclic direction order p=(p0,...,p4), let w_j=h(p_j,p_(j+1),p_(j+2)), indices mod 5. The following table checks all cyclic orders up to cyclic rotation (p0=0) and reversal (p1<p4); each row lists p and w0...w4:
01234 00101
01243 00101
01324 01101
01342 01001
01423 01011
01432 01011
02134 10101
02143 10100
02314 00101
02413 10010
03124 01001
03214 01001
Every displayed word has EXACTLY ONE cyclic equal adjacent pair, including the final-to-initial comparison. Reversal sends w to its complemented reverse and preserves the number of equal pairs; rotation preserves it too. These 12 cases therefore cover all 24 distinct cyclic orders, and all 120 linear orders through their five rotations.

For any cyclic order, the full ordered Q5-geodesic arising from a rotation reads three consecutive bits of w. Exactly two of the five rotations include the unique equal pair among these three bits, and each has exactly one switch. The other three rotations are alternating (two switches). No rotation is monochromatic. Therefore there are 24·2=48 one-switch full orders, 24·3=72 two-switch full orders, and zero monochromatic ones, at EACH physical root. The mean switches is (48+2·72)/120=8/5=4(5-3)/5.

**Research implication.** Every one of the 24 physical hub pentagons simultaneously attains the minimum one monochromatic comparison. Hence no stronger universal rank-five density follows merely by combining all pentagon inequalities at one fixed hub, even when antipodal-reversal oddness holds. Further progress must genuinely use cross-root/cross-support gluing or longer coherent path geometry. The unrestricted grand conjecture remains open.

**Ambient-dimension elevation (all n>=5).** Fix ANY five-coordinate support S in Q_n, n>=5. Transfer the ten-row h-table to S via an increasing bijection. For every ordered physical three-face with all three free coordinates in S, use h independently of *every* exterior face bit, including coordinates outside S. Complete the coloring on all remaining free-triple types by an arbitrary coordinate-only reversal-odd orientation function (e.g. color 1 if the first direction is less than the last), which independently obeys active NORI oddness. Then on EVERY one of the 2^n physical roots, exactly 48 of the 120 directed geodesic orders supported on S have one switch, exactly 72 have two, and none have zero. Thus sharpness of the rank-five pentagon averaging bound persists inside active NORI in every ambient dimension and every exterior chart for one prescribed support S. This supplies no claim about density or closure of full n-direction geodesics when n>5.
