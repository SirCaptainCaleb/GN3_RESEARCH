# The quiet R961 triangle carries a bidirectional boundary wall at the remainder rail

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-r961-bidirectional-triangle-wall`

**Summary:** Strengthening the quiet R961 triangle promotion: in the HHH packet the first vertex m0 of the remainder path M tail-signs every reverse directed-triangle dimer directly from the three puncture paths, while any cyclic triangle P4 ending at m0 would extend through the universal m0-m1 seam and Hamiltonize the critical block. Hence every such P4 is forbidden and R3 forces m0 to head-sign every reverse triangle dimer as well. The TTT case is the exact dual at the terminal mr. Thus the quiet critical block contains a physical directed triangle Y and a neighboring remainder endpoint that is simultaneously a head and tail witness on all three reverse Y-dimers. In the fixed-complement smallest-counterexample setting both complementary rails have order at least three by SV19367, so this wall is nondegenerate.


Retain `fixed-complement-r961-quiet-triangle-promotion` SV19367.

### HHH: the first remainder vertex is bidirectional on all reverse triangle dimers
In the HHH packet write

  Y=(p,x_2,x_1),
  M=(m_0,m_1,...)= (x_3,x_4,...).

SV19367 already records the three literal turns

  (x_2,p,m_0), (x_1,x_2,m_0), (p,x_1,m_0),

so m_0 is a TAIL witness on each reverse Y-dimer

  (x_2,p), (x_1,x_2), (p,x_1).

When m_1 exists, the same puncture packet gives

  (y,m_0,m_1) tight for every y in Y.                 (BW.1)

Now fix a cyclic indexing Y=(y_0,y_1,y_2). Suppose for some i the role-correct four-vertex word

  (y_i,y_{i+1},y_{i+2},m_0)

were tight. Appending the inherited remainder M from m_1 onward uses only one new seam, namely

  (y_{i+2},m_0,m_1),

which is tight by (BW.1). The resulting word is a Hamilton path of Omega=Y union M, contradicting that the critical block Omega is non-Hamiltonian. Therefore every such cyclic P4 is forbidden.

Its first two triangle turns are already tight, so the failure is specifically the final turn

  (y_{i+1},y_{i+2},m_0) bad.

Boundary antisymmetry R3 gives

  (m_0,y_{i+2},y_{i+1}) tight.                         (BW.2)

As i runs modulo three, (BW.2) says that m_0 is also a HEAD witness on every reverse Y-dimer. Hence m_0 is simultaneously head- and tail-signed on all three reverse directed-triangle dimers.

### TTT dual
In the TTT packet write

  Y=(p,x_k,x_{k-1}),
  M=(...,m_{r-1},m_r)=(x_1,...,x_{k-2}).

SV19367 directly gives that m_r HEAD-signs every reverse Y-dimer and, when m_{r-1} exists,

  (m_{r-1},m_r,y) tight for every y in Y.              (BW.3)

If a cyclic P4

  (m_r,y_i,y_{i+1},y_{i+2})

were tight, prepend the inherited path M through m_r. The sole new seam is `(m_{r-1},m_r,y_i)`, tight by (BW.3), so Omega would be Hamiltonian. Thus every such P4 is forbidden. Its first mixed turn `(m_r,y_i,y_{i+1})` is therefore bad, and R3 gives

  (y_{i+1},y_i,m_r) tight.

So m_r also TAIL-signs every reverse Y-dimer. The terminal remainder endpoint is bidirectional as claimed.

### Fixed-complement interpretation
In the fixed-complement smallest-counterexample realization of SV19367, both M and the opposite Hamilton rail Q have order at least three. Hence the predecessor/successor seams used above are physically present. The quiet R961 branch therefore yields a nondegenerate packet

  physical directed triangle Y
  + exact complementary two-cover M|Q of H-Y
  + one boundary vertex of M bidirectionally signing every reverse Y-dimer.

This is a stricter target than generic directed-triangle absorption. It should be consumed before exporting the packet as generic R523/R542 signed-dimer currency.

Status: direct working deduction from SV19367 and accepted R3. No spanning two-cover or generic directed-triangle absorption theorem is claimed.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    }
]
```
