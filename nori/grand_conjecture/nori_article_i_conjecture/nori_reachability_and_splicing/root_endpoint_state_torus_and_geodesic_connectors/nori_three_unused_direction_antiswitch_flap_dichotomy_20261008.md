# Three-direction antipodal flaps force exact alternating seam obstruction

# Three-unused-direction flap dichotomy in ordered-three-face NORI

Fix n>=6, a color-q geodesic P of length m=n-3 from x to y, with direction sequence p=(p_1,...,p_m), and the three unused coordinates W={a,b,c}. Thus the ordered-three-face word inside P consists of m-2>=1 copies of q. For any ordering t=(a,b,c) of W, consider two *full antipodal* geodesics:
H_front: starting at x XOR W, flip a,b,c to reach x, then follow P to y;
H_back: follow P from x to y, then flip c,b,a to finish at y XOR W=bar x.

Let u=c(F_x,(a,b,c)), the color of the ordered missing-coordinate face at x (its exterior coordinates equal x outside W). Since F_y=bar F_x and antipodal reversal reverses coordinate order, the last ordered face of H_back has color 1-u.

Introduce the exact four bridge colors
A(b,c)=color of the (b,c,p_1) window in H_front,
B(c)=color of the (c,p_1,p_2) window in H_front,
C(c)=color of the (p_{m-1},p_m,c) window in H_back,
D(c,b)=color of the (p_m,c,b) window in H_back.
(The displayed dependencies on b,c are justified because ordered-three-face colors ignore the three free coordinate bits, so the removed first missing coordinate does not affect A/B, and the terminal unflipped missing coordinate does not affect C/D.)

The two full color words are EXACTLY
H_front: (u,A(b,c),B(c),q,...,q),
H_back: (q,...,q,C(c),D(c,b),1-u).

**Theorem (forced anti-switch flaps).** If the NORI grand conjecture fails for this coloring, then for EVERY length-(n-3) monochromatic q-geodesic P and EVERY ordering (a,b,c) of the three unused coordinates the following holds:
- if u=q, then (C(c),D(c,b))=(1-q,q), and at least one of A(b,c),B(c) differs from q;
- if u=1-q, then (A(b,c),B(c))=(q,1-q), and at least one of C(c),D(c,b) differs from q.

*Proof.* If u=q, H_back begins with q and ends with 1-q. The complete four-block word q,C,D,1-q has at most one color change precisely when (C,D) is qq, q(1-q), or (1-q)(1-q). Under counterexample all such completions fail, so the sole remaining pair is ((1-q),q). The matching-front outer color and the P interior color are both q; it fails only if at least one of A,B differs from q. If u=1-q, the same argument with the two completions interchanged gives (A,B)=(q,1-q) and a defect in at least one of C,D. All four bridge windows are actual ordered-three-faces, and the only oddness relation used is c(bar F,rev pi)=1-c(F,pi). QED.

**General-dimension consequence.** Any proposed NORI counterexample must exhibit an explicitly prescribed *alternating two-seam obstruction* on one of two opposite three-direction flap completions of every nearly spanning monochromatic core. This is a direct face-local analogue of the one-edge antipodal extension mechanism, now with two unavoidable seam windows. It is not yet a closure theorem: the color on the missing ordered three-face can vary with all six permutations, and the four bridge families do not contradict each other without additional overlapping-core or path-exchange relations.

**Research target.** Derive an exchange or carrier theorem that forces, for at least one such core, one permutation of W whose forced-flap pattern is impossible. Unlike a Q_7 subclass enumeration, this obstruction and its color transport hold for every dimension n>=6.
