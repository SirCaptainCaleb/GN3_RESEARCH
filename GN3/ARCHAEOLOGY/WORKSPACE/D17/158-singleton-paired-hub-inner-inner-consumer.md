# A double-INNER hub splice always reverses: the four-complement exception is impossible

**Workspace:** D17
**State:** established
**Key:** `singleton-paired-hub-inner-inner-consumer`

**Summary:** Let P=(p0,...,pr) and Q=(q0,...,qs), r,s>=2, be disjoint tight paths and b a further vertex in a system with pc(H)>2. If the inner tail replacement (p0,...,p_{r-2},b,p_{r-1}) and inner head replacement (q1,b,q2,...,qs) are tight, then the cross-hub turn (p_{r-2},b,q2) must be bad. A tight cross seam would give a long path K whose complement is the two endpoint dimers {p_{r-1},pr} and {q0,q1}; four exhaustive R3 tests on those four vertices always produce a spanning two-cover. Thus the double-INNER branch of the paired-hub transfer square never reaches the R813 four-complement exception. Dually the other diagonal always supplies its labelled reverse hub turn as well.

### Standalone inner/inner cross-splice consumer
Let H be a finite Strong Level-(1) boundary tournament with pc(H)>2. Suppose

  V(H)=V(P) disjoint-union V(Q) disjoint-union {b},
  P=(p_0,p_1,...,p_r),
  Q=(q_0,q_1,...,q_s),

with r,s>=2 and P,Q tight. Assume the two INNER endpoint-replacement paths

  R_P=(p_0,...,p_{r-2},b,p_{r-1}),
  L_Q=(q_1,b,q_2,...,q_s)

are tight. Then

  gamma=(p_{r-2},b,q_2)

is bad. Hence by R3 the exact labelled reverse turn

  gamma*=(q_2,b,p_{r-2})

is tight.

### Proof by a four-turn endpoint-dimer decision tree
Assume instead that gamma is tight. Then

  K=(p_0,...,p_{r-2},b,q_2,...,q_s)

is a tight path. Its complement is exactly

  X={a,c,u,v}:={p_{r-1},p_r,q_0,q_1}.

We show directly that H has a spanning two-cover. Test the following four ordered turns in sequence.

1. Test T1=(a,c,u). If T1 is tight, then

  (p_0,...,p_r,u) | (q_1,b,q_2,...,q_s)

is a spanning two-cover: the only new turn on the first rail is T1.

Hence suppose T1 is bad. R3 gives

  (u,c,a) tight.                                           (1)

2. Test T2=(c,u,v). If T2 is tight, then

  (p_0,...,p_{r-2},b,p_{r-1}) | (c,u,v,q_2,...,q_s)

is a spanning two-cover.

Hence suppose T2 is bad. R3 gives

  (v,u,c) tight.                                           (2)

3. Test T3=(a,v,u). If T3 is tight, then by (2)

  (a,v,u,c)

is a tight Hamilton P4 on X, so K|(a,v,u,c) two-covers H.

Hence suppose T3 is bad. R3 gives

  (u,v,a) tight.                                           (3)

4. Finally test T4=(c,a,v). If T4 is tight, then by (1)

  (u,c,a,v)

is a tight Hamilton P4 on X, and K|(u,c,a,v) two-covers H. If T4 is bad, R3 gives

  (v,a,c) tight,

which together with (3) makes

  (u,v,a,c)

a tight Hamilton P4 on X, again yielding K|X as a spanning two-cover.

Every branch contradicts pc(H)>2. Therefore gamma is bad and gamma* is tight.

### Paired-hub consequence
Apply the theorem to the right-P/left-Q diagonal of `singleton-paired-hub-transfer-square`. Its former double-INNER alternative

  tight cross splice + non-Hamiltonian four-complement + R813 fan

cannot occur at all. The exact left-P/right-Q dual is identical. Consequently, outside the already-separated source-relative R435 branches, BOTH opposite-role diagonals of a paired fixed-hub packet always supply their labelled cross-hub reverse turns, regardless of OUTER/INNER type.

This strictly subsumes the R813 exceptional branch of the certified transfer-square theorem. R813 remains valid toolkit mathematics but is unnecessary for this paired-hub diagonal.

### Parent-theorem interpretation
The proof uses only two retained source rails, one transferred vertex b, one inner tail replacement, one inner head replacement, the cross seam, and R3. It is therefore a genuine anchored one-vertex exchange consumer rather than generic Reverse-Ear production. It does not yet consume the resulting pair of diagonal reverse turns into R561 or strict K descent. The fixed-complement radius-two local-ear setting does not automatically provide the reciprocal second-rail INNER replacement used here, so this theorem does not yet subsume that separate ear branch.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    }
]
```
