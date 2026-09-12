# Orientation I has two complementary isolation surgeries using both B contacts

**Workspace:** D17
**State:** established
**Key:** `directed-triangle-f1g1-orientation1-two-ended-isolation`

**Summary:** In the quiet fragmented-B Orientation I target (B_P,P)|(L,B_L), there are two complementary complete surgeries. Moving x together with the actual B_L tail onto the P-side has exactly one new turn (m,x,ell0); success isolates the literal triangle trimer Y=(a,b,c), so R522 with probes u,v gives codimension one or closure, while failure gives the exact reverse current blocker (ell0,x,m). Dually, moving the entire actual B_P fragment onto the L-side isolates the literal trimer P=(j0,j1,m); its complete new window is (k_{s-1},k_s,a),(k_s,a,b), with the first turn absent when |B_P|=1. Full success again gives codimension one or closure by R522; first failure yields (a,k_s,k_{s-1}) or (b,a,k_s). Hence every surviving Orientation I state carries a genuine two-ended isolation blocker tied to both physical B contacts, rather than merely two local Q windows.

### 1. Exact Orientation-I setup
Retain `directed-triangle-f1g1-p-aq-two-contact-surgery` SV15163 in its quiet Orientation I. Thus on G=H-{u,v} the actual exact target is

  T=(B_P,j0,j1,m) | (a,b,c,x,B_L),

where P=(j0,j1,m), Y=(a,b,c), L=(a,b,c,x), J=(j0,j1,m,x,c), and B_P,B_L are the two nonempty ACTUAL B-fragment paths in their actual target-cover orders. No ancestral order is asserted for either B fragment. The first rail supplies the actual B_P->P attachment, and the second supplies the actual x->B_L attachment.

The purpose here is to use those two contacts in complementary support transfers that leave one literal tight trimer as an entire rail.

### 2. Right-end transfer: x+B_L moves across and isolates Y
Write B_L=(ell0,ell1,...) in its actual order. Test

  T_Y=(B_P,j0,j1,m,x,B_L) | (a,b,c).                 (OI.1)

The complete new-turn ledger of the first rail contains exactly

  chi=(m,x,ell0).                                      (OI.2)

Indeed (j1,m,x) is inherited from the literal old J, while every turn beginning with x,ell0 and continuing down B_L is inherited from the actual target rail (a,b,c,x,B_L). The B_P->P prefix is untouched. Thus no second seam is hidden, including when |B_L|=1.

If chi is tight, (OI.1) is a literal exact two-cover of G whose second rail is the tight trimer Y=(a,b,c). Probe Y by u and v. If Y+u has a Hamilton P4, that P4 together with the first rail of (OI.1) two-covers H-v; similarly a P4 on Y+v gives a two-cover of H-u. If neither extension has a Hamilton P4, accepted R522/P537 gives a Hamilton P5 on Y+{u,v}; together with the first rail this is a spanning two-cover of H. Hence chi-tight gives a strict singleton-deletion improvement or closure.

Therefore every surviving Orientation-I counterexample has chi bad, and R3 gives the exact reverse turn

  (ell0,x,m) tight.                                    (OI.3)

This blocker is tied simultaneously to the actual x->B_L contact and the ancestral/current selected P-Q boundary m->x.

### 3. Left-end transfer: B_P moves across and isolates P
Write B_P=(k0,...,ks) in its actual order. Test

  T_P=(j0,j1,m) | (k0,...,ks,a,b,c,x,B_L).            (OI.4)

Everything after a is inherited from the actual target rail L B_L. The complete new B_P-to-A junction window is

  rho=(k_{s-1},k_s,a)   if |B_P|>=2,
  sigma=(k_s,a,b).                                      (OI.5)

When |B_P|=1 only sigma exists. No other turn changes.

If every present turn in (OI.5) is tight, (OI.4) is a literal exact two-cover of G with isolated tight trimer P=(j0,j1,m). Probe P by u and v. A Hamilton P4 on P+u or P+v gives a two-cover of H-v or H-u respectively; if both extensions are P4-free, accepted R522/P537 gives a Hamilton P5 on P+{u,v}, which together with the other rail of (OI.4) spans H. Thus full success again gives codimension one or closure.

Consequently a surviving state blocks this complete window. Retain the deterministic first-bad reverse:

  rho bad  => (a,k_s,k_{s-1}) tight,                  (OI.6a)

while if rho is absent or tight and sigma is bad,

  sigma bad => (b,a,k_s) tight.                       (OI.6b)

These turns retain the actual terminal B_P vertex, and in (OI.6a) its actual predecessor.

### 4. Two-ended isolation-blocker normal form
Orientation I is therefore stronger than the earlier paired opposite-Q repair ledger. Before any generic R159/R176/R435/R542 payment, either one of the two complete support transfers gives a singleton-deletion improvement / spanning closure, or the same exact target retains BOTH:

  right blocker (ell0,x,m),

and one left blocker from {(a,k_s,k_{s-1}), (b,a,k_s)}.

The right blocker is anchored at the actual B_L source and selected m-x carrier; the left blocker is anchored at the actual B_P terminal and the A source boundary. Both original B/active contacts and both actual B-fragment orders remain part of the state.

No claim is made that these two blockers alone imply R561 or that either propagates through a longer B fragment. The next consumer must use the pair in one complete two-rail reconstruction, ideally reconstructing literal B, isolating another short rail, or currentizing a full-support/common-complement reversal.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R522"
    }
]
```
