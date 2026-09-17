# A rooted canonical cut cannot realize the three-cell quiet residue

**Workspace:** D17
**State:** established
**Key:** `g33-rooted-cut-four-cell-contraction`

**Summary:** For the G33 bad one-hole proposal, choose the canonical cut using the short-active-spoke geometry of SV105144. It may be chosen so that either the omitted B-active spoke s is a singleton J-component, or s lies on a dimer and the chosen cut forest has tau(J)<=1. In the dimer case this follows directly from the literal R540 near-end forms: if the low proposal already has tau<=1 there is nothing to do; if tau=2, the unique bad spectator-side turn contains an X|B edge, and cutting that edge lowers tau to at most one while leaving the s-dimer untouched. The three-cell quiet support-incidence residue of SV105952 is therefore impossible for this rooted cut: a singleton s cannot become internal in F after adding the single missing old seam, while the dimer branch contradicts the forced tau(J)=2. Hence applying the support-incidence reduction to this one rooted cut already yields either a bounded C4/repeated-crossing/R435/local-R3 output or a strict old-source transition descent; outside those outputs the residual incidence geometry is necessarily the four-cell two-old/one-new seam tree. The surviving packet retains the short s-component and rooted old source coordinate, so the previous two-cut symmetry argument is no longer needed to keep the active spoke attached to the live obstruction.


### 1. Setup
Retain the direct G33 packet of SV103129 together with the short-active-component refinement SV105144 and the support-incidence reduction SV105952. Thus

  G=H-{A,C}=X union V(B),
  F=F_1|F_2

is the actual old exact source two-cover, the omitted source spoke s is B-active and internal in F, and the bad low endpoint-cut proposal

  P=P_1|P_2

has exactly one bad consecutive turn eta and

  tau(P)<=2.

Cutting either selected edge inside eta gives one of the two literal spanning tight three-forests from SV103530. We strengthen the choice of cut so that the component D_s containing s is short and the only silent support-incidence residue is impossible.

### 2. Refined choice of the rooted canonical cut
SV105144 lists the literal R540 one-hole positions. Whenever its chosen cut isolates s, take that cut. Then

  D_s=(s).                                                (RC.1)

The only remaining possibility is a near-end spectator cut, where s lies on a dimer. We show that in this case one of the two canonical cuts inside eta may be chosen with

  |D_s|=2,   tau(J)<=1.                                   (RC.2)

Consider first a left cut through L=k_3. The literal proposal has the form

  P_1=(k_0,k_1,k_2,L,b_1,...,b_{m-1}),
  P_2=(s,k_4),

and its unique bad turn is

  eta=(k_2,L,b_1).                                        (RC.3)

The dimer P_2 is disjoint from eta, so either canonical cut leaves D_s=P_2 unchanged. If tau(P)<=1, either cut already gives tau(J)<=1. Suppose tau(P)=2. If k_2=R, then k_0,k_1,k_4 all lie in X, so P_1 has exactly one X|B transition and P_2 has none; hence tau(P)=1, contradiction. Therefore k_2 lies in X. The selected edge k_2 L inside eta is then an X|B transition. Cut that edge. No new transition is created and one transition is deleted, so tau(J)<=1 while the s-dimer survives literally.

The right-cut case is dual. If R=k_1, the proposal is

  P_1=(k_0,s),
  P_2=(b_1,...,b_{m-1},R,k_2,k_3,k_4),

with unique bad turn

  eta=(b_{m-1},R,k_2).                                    (RC.4)

Again the s-dimer is disjoint from eta. If tau(P)<=1, either cut suffices. If tau(P)=2 and k_2=L, then k_0,k_3,k_4 lie in X, so P_1 contributes no transition and P_2 contributes exactly one, again contradicting tau(P)=2. Hence k_2 lies in X, the edge R k_2 is an X|B transition, and cutting it gives tau(J)<=1 without changing D_s.

Thus there is one canonical cut forest J satisfying the exact alternative

  D_s=(s),
  or
  |D_s|=2 and tau(J)<=1.                                  (RC.5)

All old source data retained in SV105144 remain attached to this same J, including the actual old s-B incidence and the free matching copy of s.

### 3. The three-cell quiet residue is impossible for the rooted cut
Apply the support-incidence analysis of SV105952 to this single chosen J.

Suppose first that its acyclic synchronized branch has three cells and no earlier bounded output. Section 6 of SV105952 then says literally that F is obtained from J by adding one old seam o, and forces

  tau(F)=3,   tau(J)=2.                                   (RC.6)

If D_s is a singleton, J has selected degree zero at s. Adding one seam can raise the selected degree of s to at most one. But s is internal in the old source cover F, so d_F(s)=2. Contradiction.

If D_s is a dimer, (RC.5) gives tau(J)<=1, contradicting (RC.6).

Therefore the rooted canonical cut can never realize the one-transition three-cell seam-deletion residue.

### 4. Rooted four-cell contraction
Run Sections 2-8 of SV105952 on this one J. If the support-incidence graph is cyclic, retain its bounded C4 overlap nucleus. If a cell is noncontiguous, retain the repeated-crossing seam pair. If a contiguous cell disagrees in order, retain the exact R435 reversal, reverse trimer, or proper cycle. Outside those outputs the incidence graph is an acyclic three- or four-cell forest and the common cell words are synchronized.

Section 3 is now excluded by Section 3 above. Hence the only synchronized non-output geometry has exactly four cells. Its seam graph is the tree

  O={o_1,o_2},   N={n}.                                   (RC.7)

The two old/new hybrids of SV105952 are each either blocked by one explicit copy-competition or mixed-seam R3 trimer, or are literal exact two-covers. Section 8 of SV105952 shows that if both hybrids are legal then they cannot both fail to lower the old transition count: the nominal all-three-transition residue would Hamiltonize G. Consequently this rooted J yields one of

1. a four-cell cyclic support-overlap nucleus;
2. a repeated-crossing seam pair;
3. an R435 adjacent reversal, reverse trimer, or proper cycle;
4. a copy-competition or mixed-seam R3 trimer; or
5. an exact two-cover T of G with tau(T)<tau(F).

The gain over the unrooted two-cut reduction is not a new terminal consumer. It is that the quiet three-cell alternative is already impossible for one canonically chosen cut whose s-component has order at most two. Thus every surviving non-descent packet stays attached to the omitted B-active spoke, its old source incidence, the free matching copy at s, and the source ancestry from the start; no switch to the other cut is required merely to escape the silent residue.

### 5. Scope
This is a rooted contraction, not G33 extinction. It does not consume the C4, repeated-crossing, R435, or local-R3 outputs. It uses the literal R540 endpoint-cut geometry only through the exact one-hole forms retained by SV105144, plus the support-incidence theorem SV105952. R24, R5, payment, and historical replay are unused.


## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R540"
    }
]
```
