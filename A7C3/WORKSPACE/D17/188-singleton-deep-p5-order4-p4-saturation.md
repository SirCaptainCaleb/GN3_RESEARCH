# Every surviving order-four donor terminal contains at least two cyclic R700 P4 cells

**Workspace:** D17
**State:** established
**Key:** `singleton-deep-p5-order4-p4-saturation`

**Summary:** At |B|=4 the source and terminal tests of SV16734 use the same five R700 applications to cyclic trimers K_i=(a_i,a_{i+1},a_{i+2}) with probes b1,b2. Let P be the set of indices whose R700 application takes the P4 branch. If i is not in P, DUAL-CP plus donor failure gives the left inward sign (b2,b1,a_i) and, through the terminal test indexed i+1, the right inward sign (a_{i+2},b2,b1). Hence label a_j is bidirectionally signed on the common reverse middle dimer whenever j and j-2 are both outside P. By SV16865, any adjacent pair of bidirectionally signed cycle labels Hamiltonizes its donor support. Therefore the bidirectionally signed set must be independent in C5 and has size at most two. In particular |P|>=2. Thus an order-four survivor requires at least two distinct specifically supported cyclic R700 P4 cells; the no-P4 and single-P4 patterns are impossible.


Retain SV16734 and SV16865 and write B=(b_0,b_1,b_2,b_3), C_5=(a_0,...,a_4) cyclically.

For i modulo 5 let T_i denote the single accepted R700 application to K_i=(a_i,a_{i+1},a_{i+2}) with probes b_1,b_2. At order four, the source test indexed i in SV16734 is T_i. The terminal test indexed j uses K'_j=(a_{j-1},a_j,a_{j+1}), so K'_j=K_{j-1}; hence the terminal family is the same five R700 tests, cyclically relabelled.

Let P={i : T_i takes the R700 P4 branch}.

If i is not in P, T_i is DUAL-CP. The source donor failure gives (b_2,b_1,a_i) tight. The same T_i is the terminal test with j=i+1, whose failed donor gives (a_{i+2},b_2,b_1) tight. Therefore a label a_j is both head- and tail-signed on the common oriented reverse middle dimer (b_2,b_1) whenever j notin P and j-2 notin P.

Let G={j : j notin P and j-2 notin P}. If G contained adjacent indices r,r+1, then x=a_r,y=a_{r+1} would satisfy both orientations of the coincident-dimer stars. The proof of SV16865 applies verbatim to this single cycle edge: it constructs (x,b_2,b_1,y) and (y,b_2,b_1,x), uses donor non-Hamiltonicity to force the four b_3 endpoint turns, and then one R3 pivot on {x,b_3,y} Hamiltonizes (B-b_0)+{x,y}. This closes H with the already Hamiltonian complementary active support. Hence G is an independent set in C_5, so |G|<=2.

If |P|=1, say P={h}, the condition defining G excludes only h and h+2, leaving |G|=3, contradiction. Therefore |P|>=2.

Thus every surviving |B|=4 donor terminal contains at least two distinct cyclic trimer indices i for which K_i plus one of {b_1,b_2} supports a labelled Hamilton P4. More precisely G must be independent in C_5. This is a finite P4-saturation obstruction, not closure and not an assertion about endpoint positions of those P4 orders.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R700"
    }
]
```
