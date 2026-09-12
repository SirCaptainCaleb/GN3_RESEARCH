# Minimum universal side, saturated ports, and complete-exchange recurrence

**Workspace:** D17
**State:** working
**Key:** `universal-source-saturated-port-recurrence`

**Summary:** The theta-one quiet exit becomes a saturated port; universal crossing versus complete exchange is isolated, Director-v10 source-family targets are stated, and complete exchange reconstructs the quiet double star with its single recurrence.

### 16. Minimum universal side: the theta=1 quiet exit is a saturated port

Choose, among all literal singleton-deletion source covers and all universally crossing vertices on either source rail, a triple

  (p, C_p=A|B, z in A)

for which the offending rail size a=|A| is minimum. Retain the non-Hamilton deletion case of sections 12-13, so

  A=L-z-R

with L,R nonempty, and suppose the common pair-deletion residue W=H-{p,z} admits a theta=1 exact two-cover whose mixed rail has support L union B. Let P_M be that ACTUAL mixed Hamilton order and put

  M=L union B,
  Z={z} union R,
  Omega=Z union {p}.

Section 13 gives the literal exact source

  C_p^new = P_M | (z-R)

of H-p. Since |Z|=|R|+1<|A|=a, no vertex y in Z can be universally crossing on the Z-side relative to this new source: such a y would exhibit a universal-crossing offending rail of size |Z|<a. Hence EVERY y in Z is quiet on that side.

Apply the seam-free deleted-label substitution of `extremal-root-compression` to each such y. It gives an exact H-y cover

  C_y = Q_y | P_M

with V(Q_y)=Omega-{y}. For y=p the new p-source itself supplies Q_p=(z-R) on Omega-{p}=Z. Therefore

  Omega-{y} is Hamiltonian for every y in Omega,

and all these singleton fibers share the same literal Hamilton complement P_M on M.

Omega itself is non-Hamiltonian. Otherwise a Hamilton path on Omega together with P_M would two-cover H. Moreover

  M union {y} is non-Hamiltonian for every y in Omega.

Indeed M+{y} and Omega-{y} are disjoint and partition V(H); the second support is Hamiltonian by the preceding paragraph, so Hamiltonicity of M+{y} would close H. Thus the theta=1 quiet exit is not merely a smaller quiet source. It is a saturated port: one non-Hamiltonian deletion-Hamiltonian universe Omega, with a fixed Hamilton complement M, and EVERY one-vertex extension M+y blocked.

This gives exact terminal endpoint shields on the fixed order P_M=(m_0,...,m_t). Since M+y is non-Hamiltonian for every y in Omega, attaching y to either displayed end of P_M is impossible. Hence for every y in Omega, whenever the displayed turns exist,

  (y,m_0,m_1) is bad,       (m_{t-1},m_t,y) is bad,

so R3 gives

  (m_1,m_0,y) tight,        (y,m_t,m_{t-1}) tight.

Thus every y in Omega simultaneously reverse-shields both terminal dimers of one fixed Hamilton complement. The tested orientations are part of the datum.

Neither M nor any Hamilton puncture Omega-{y} can carry an R561 boundary-reversed Hamilton dimer. Such a dimer on M would Hamilton-extend M by every exterior y, contradicting non-Hamiltonicity of M+y. Such a dimer on Omega-{y} would Hamilton-extend that support by the omitted y and make Omega Hamiltonian.

The source orders that created this port remain available and are not replaced by support-only data: A is the literal bridge L-z-R, while P_M is the actual theta=1 Hamilton rail on L union B. In particular L and B each occur as one contiguous block of P_M, although their internal orders need not agree with the old source orders.

### 17. The saturated port has a universal-crossing / complete-exchange dichotomy

For every y in Omega the cover C_y=(Omega-y)|M is an actual singleton source with the same opposite support M. Fix m in M. By the support characterization of section 8, m is quiet on the M-side relative to C_y exactly when

  M-{m}+{y}

is Hamiltonian. Consequently the saturated port has the exact dichotomy:

(PORT-CROSS) for some y in Omega and m in M, M-m+y is non-Hamiltonian. Then m is a new universal physical source crossing in the saturated source family.

(COMPLETE-EXCHANGE) for every y in Omega and every m in M, M-m+y is Hamiltonian.

The second branch is a genuine all-rows/all-columns replacement reservoir, not merely absence of one obstruction. For each fixed m in M put X_m=M-{m}. Then

  X_m+{r} is Hamiltonian for every r in Omega union {m}.

Indeed r=m gives M itself and r in Omega is exactly the complete-exchange assertion. Thus every codimension-one core X_m of the fixed complement is universally one-vertex Hamilton-extendable by its entire exterior in H. If X_m is non-Hamiltonian, this is precisely the universal-extension hypothesis of the accepted R156/R157 machinery; if X_m is Hamiltonian, the extension reservoir is even stronger, but no endpoint-role consumer is asserted here.

The minimum-size choice also gives a useful size trichotomy for future iteration. Write a'=|Z|<a and m_0=|M|. If m_0<a, then C_p^new has both rails smaller than a and is fully quiet on BOTH sides. If m_0=a, any surviving universal crossing can recur only on the M-side at the same minimum size; this is the critical equal-size recurrence. If m_0>a, any universal crossing remaining in this source has moved to a strictly larger offending rail. In the critical case m_0=a, cardinality gives |B|=|Z|=a', and the old and new H-p support partitions are the exact block rotation

  (L union Z) | B     ->     (L union B) | Z,

with B and Z Hamiltonian and both enlarged supports displayed by actual Hamilton paths. No claim that this rotation itself closes H is made.

This supplies the complete terminal outcome missing from the bare theta=1 source shrink: either the saturated clique exposes a new universal crossing on the fixed-complement side, or it yields the complete-exchange universal-extension reservoir. The unresolved parent theorem is now allowed to terminate in this explicitly finite source-family object rather than in the word `quiet`.

### 18. Revised source-family target after Director v10

The theta=2 taxonomy remains useful diagnostics but is not the parent objective, and no theta=3,4,... shape expansion is needed. Starting from a minimum-side universal source, the desired source-reduction theorem should handle arbitrary fragmentation and have one of three cover-valued conclusions:

  (i) a spanning two-cover of H;
  (ii) an actual source-family repair that reaches a strictly smaller universal offending rail or otherwise improves a specified finite source-family extremal objective;
  (iii) the saturated-port terminal of sections 16-17, followed by a consumer of PORT-CROSS or COMPLETE-EXCHANGE.

The theta=1 construction already reaches (iii) when its smaller source becomes quiet. PORT-CROSS returns to the universal branch with a common fixed complement and a fully certified deletion-Hamiltonian opposite universe. COMPLETE-EXCHANGE gives universal one-vertex extension of every core M-m and therefore a different rigid target. Generic R159/R176 pair birth, isolated P4, or bare R435 mismatch does not consume either terminal.

Status: sections 16-18 are complete internal working deductions from the minimum universal-side choice, theta=1 source currentization, seam-free substitution, section-8 support equivalence, and R3/R561 where cited. They are not independently canonically reviewed and do not yet close Universal Source-Crossing Absorption.


### 19. Complete exchange reconstructs a fully quiet double star and has only one recurrence

Retain the minimum-side saturated port of sections 16-17 in the COMPLETE-EXCHANGE branch. Thus Omega and M partition V(H), Omega is non-Hamiltonian, Omega-y is Hamiltonian for every y in Omega, M is Hamiltonian, M+y is non-Hamiltonian for every y in Omega, and

  M-m+y

is Hamiltonian for every m in M and y in Omega. Put

  k=|Omega|-1,   ell=|M|.

By construction k is the size of the smaller theta=1 rail Z and satisfies k<a, where a was the globally minimum universal-crossing offending-rail size.

Fix any y_0 in Omega. Choose actual Hamilton paths on every support certified above. The following is then a literal complete singleton-cover family of double-star form centered at y_0:

  H-y_0 : (Omega-y_0) | M,
  H-y   : (Omega-y)   | M                    for y in Omega-{y_0},
  H-m   : (Omega-y_0) | (M-m+y_0)           for m in M.

All displayed supports are Hamilton by the saturated-port and complete-exchange hypotheses. The Omega labels form one compatibility clique, M union {y_0} forms the other, and they meet only at y_0. Equivalently this is exactly the literal double star D(y_0; Omega-y_0, M).

More importantly, the CENTRAL source C_{y_0}=(Omega-y_0)|M is quiet at every vertex on both rails. For y in Omega-y_0, the source universe Omega has Hamilton deletion Omega-y. For m in M, complete exchange gives M-m+y_0 Hamilton. By section 8 these are exactly the two quietness statements.

Now apply the quiet two-pivot construction of `extremal-root-compression`, section 6, to this actual double star. Every intermediate double star produced by its one-for-one swaps has the same rail sizes k and ell. If some intermediate source fails the required quiet rebuild, a universal physical source crossing has been encountered. Its offending rail cannot have size k, because k<a and a is globally minimum over all universal-crossing offending rails. Therefore every such failure is a universal crossing on an ell-vertex rail.

If no failure occurs during the complete pivot/swap saturation, section 6 applies verbatim: all k|ell support partitions can be realized at every required singleton deletion. If k!=ell, the larger Hamilton rail contains a contiguous tight subpath of size min(k,ell)+1 whose complement has the opposite saturated size; the section-6 argument gives a spanning two-cover of H. If k=ell, then n=2k+1 and every k-set is Hamiltonian while every (k+1)-set is non-Hamiltonian, namely the uniform middle-layer branch.

Thus COMPLETE-EXCHANGE has the exact global terminal alternative

  spanning two-cover,
  OR uniform middle-layer residue,
  OR a universal source crossing whose offending rail has size ell=|M|.

The same PORT-CROSS output of section 17 is already the third alternative. Hence the two saturated-port branches unify: after a minimum-side theta=1 quiet exit, the only universal recurrence that survives complete source-family currentization is on the fixed-complement M side.

There is a useful immediate corollary. If ell<a, such a recurrence is impossible by global minimality. Hence a theta=1 quiet exit with |M|<a terminates in a spanning two-cover or, only when |M|=|Omega|-1, the uniform middle-layer residue. If ell=a, the only nonclosing recurrence is at the same minimum offending-rail size; if ell>a, it is strictly larger. These equal/larger M-side recurrences, together with arbitrary theta>1 fragmentation, are the remaining source-reduction problem.

No compatibility-edge extremality is used here. The double-star family is constructed directly from the COMPLETE-EXCHANGE Hamilton supports, and the only imported global mechanism is the already proved quiet two-pivot composition.




## References

```json
[
]
```
