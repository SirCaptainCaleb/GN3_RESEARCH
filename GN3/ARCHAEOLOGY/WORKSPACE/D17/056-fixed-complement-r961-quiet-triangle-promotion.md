# A quiet source-anchored R961 packet promotes to a physical directed triangle with one certified rail side

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-r961-quiet-triangle-promotion`

**Summary:** In a non-Hamiltonian deletion-Hamiltonian block Omega=X+p, the source-anchored R961-quiet HHH or TTT packet forces its three anchor labels to form a physical tight directed triangle: each pair of puncture paths is an adjacent-slot exchange whose unique double-insertion turn must be bad, so boundary antisymmetry certifies the three cyclic reverse turns. In a smallest-counterexample fixed-complement realization V(H)=Omega disjoint-union Q, deleting this triangle leaves an exact two-cover M|Q; R887/R902 make every triangle-plus-two-exterior five-set Hamiltonian, forcing both M and Q to have at least three vertices. Moreover the anchored packet certifies every restoration turn on the M side and makes the boundary endpoint of M sign every reverse triangle dimer. Thus the R961-quiet half of Critical-Block Complement Absorption enters a strictly specialized directed-triangle absorption problem rather than remaining endpoint-jet bookkeeping.


### 1. Pure critical-block promotion
Let

  Omega=X union {p},   X=(x_1,...,x_k),   k>=4,

be non-Hamiltonian and deletion-Hamiltonian. Retain the accepted exact source-anchored R961 unit `source-anchored-r961-fan` SV304 and assume its quiet alternative.

In HHH the three actual puncture paths are

  P_p   =(x_1,x_2,x_3,...,x_k),
  P_x1  =(x_2,p,x_3,...,x_k),
  P_x2  =(p,x_1,x_3,...,x_k).

Consider the three pairwise double-insertion words

  (x_1,x_2,p,x_3,...,x_k),
  (p,x_1,x_2,x_3,...,x_k),
  (x_2,p,x_1,x_3,...,x_k).

In the first word every consecutive turn is inherited from P_p or P_x1 except `(x_1,x_2,p)`. If this turn were tight, the word would Hamiltonize Omega. Therefore it is bad, and R3 gives

  (p,x_2,x_1) tight.

The second word has unique uncertified turn `(p,x_1,x_2)`, so non-Hamiltonicity and R3 give

  (x_2,x_1,p) tight.

The third word has unique uncertified turn `(x_2,p,x_1)`, so

  (x_1,p,x_2) tight.

Hence with

  Y=(y_0,y_1,y_2)=(p,x_2,x_1),

the three cyclic turns

  (y_0,y_1,y_2), (y_1,y_2,y_0), (y_2,y_0,y_1)

are all tight. The R961 endpoint-return triangle has therefore promoted to a PHYSICAL tight directed triangle in H.

The TTT packet is the exact dual. Writing a=x_{k-1}, b=x_k, its pairwise double-insertion words force

  (p,b,a), (b,a,p), (a,p,b)

all tight, so again Y=(p,b,a) is a physical tight directed triangle.

No R435 output is consumed here: this conclusion belongs only to the fully source-anchored quiet packet.

### 2. The remainder rail is already one-sided signed
Continue HHH and put

  M=(x_3,x_4,...,x_k).

Relative to the cyclic indexing Y=(p,x_2,x_1), the three reverse Y-dimers are

  (x_2,p), (x_1,x_2), (p,x_1).

The displayed puncture paths certify respectively

  (x_2,p,x_3), (x_1,x_2,x_3), (p,x_1,x_3).

Thus the source m_0=x_3 of M TAIL-signs every reverse Y-dimer.

If x_4 exists, the same puncture paths also certify

  (p,x_3,x_4), (x_1,x_3,x_4), (x_2,x_3,x_4).

Equivalently, for EVERY y in Y,

  (y,m_0,m_1) tight,   where m_1=x_4.                 (QT.1)

The TTT dual says that for M=(x_1,...,x_{k-2}), its terminal m_r=x_{k-2} HEAD-signs every reverse Y-dimer, and when m_{r-1} exists,

  (m_{r-1},m_r,y) tight for every y in Y.             (QT.2)

These are literal selected turns inherited from the three puncture paths, not inferred endpoint signs.

### 3. Fixed-complement realization enters directed-triangle absorption
Now place the block in the fixed-complement setting of SV18936:

  V(H)=Omega disjoint_union V(Q),

where Q is a literal Hamilton path and H is a hypothetical smallest counterexample. The triangle Y is a tight trimer. Therefore H-Y cannot be Hamiltonian, since a Hamilton path on H-Y together with Y would two-cover H. On the other hand

  H-Y = M | Q

is a literal two-cover. Hence M|Q is exact.

Because Y is a physical directed triangle, its three ordinary triangle edges form a directed comparison cycle in the R887 line-graph orientation. Thus every five-set Y+{d,e} with distinct exterior d,e is non-edge-orderable and, by accepted R902, Hamiltonian.

This immediately forces

  |M|>=3 and |Q|>=3.                                    (QT.3)

Indeed, if |M|=1, choose an endpoint q of Q. A Hamilton P5 on Y+M+q together with Q-q is a spanning cover by at most two paths. If |M|=2, a Hamilton P5 on Y+M together with Q is a spanning two-cover. Both contradict pc(H)>2; the Q argument is symmetric. In particular the seams in (QT.1) or (QT.2) physically exist in the fixed-complement counterexample setting.

Therefore the quiet R961 branch of Critical-Block Complement Absorption is not merely a common-complement endpoint-fan. It produces the stronger packet:

  - a physical tight directed triangle Y;
  - an exact complementary two-cover M|Q with both rails of order at least three;
  - one distinguished endpoint of M signing all three reverse Y-dimers;
  - every role-correct restoration turn on that same M boundary already tight by (QT.1) or (QT.2).

The existing `directed-triangle-two-rail-absorption` section is an available established but presently uncertified normal-form laboratory for this packet. The next proof target should specialize that triangle analysis using the pre-certified M-side seams rather than restart endpoint-jet transport.

### 4. Strategic consequence and nonclaim
This gives a clean split for the conjectural Critical-Block Complement Absorption theorem:

  (A) explicit common-complement R435 geometry from R961/SV304, or
  (B) the anchored directed-triangle packet above.

Branch (B) has crossed into an older, much more developed absorption interface. A successful general Directed-Triangle Absorption theorem would kill (B) at once and would also consume directed triangles arising from other R435/comparison-cycle reductions.

No spanning two-cover is claimed here, and no conclusion from the uncertified directed-triangle normal form is promoted to canonical status.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R887"
    },
    {
        "relation": "dependency",
        "revision_id": "R902"
    }
]
```
