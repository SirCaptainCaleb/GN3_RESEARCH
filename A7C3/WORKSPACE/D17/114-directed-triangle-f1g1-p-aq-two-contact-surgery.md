# The P | (A union Q) fragmented-B split has four contact-aware two-rail surgeries

**Workspace:** D17
**State:** established
**Key:** `directed-triangle-f1g1-p-aq-two-contact-surgery`

**Summary:** In the R435-quiet v43 P | (A union Q) fragmented-B cell, all four orientations of the two actual B/active contacts admit complete two-rail surgeries. In B_P-P | L-B_L, two opposite Q-order repairs each isolate A, so either successful window gives codimension one by R561; a hard state blocks both ends. In P-B_P | B_L-L, the H2 positive turn c-x-j0 reduces a dimer-isolation repair to the complete remaining j0-to-B_P window, whose success again gives codimension one. In B_P-P | B_L-L, Q transfers seam-free to give (B_P,J)|(B_L,A), after which a short second rail is consumed by R522 and a longer one enters the exact endpoint-transposition/fixed-complement consumer. In P-B_P | L-B_L, a two-turn head exchange gives E1|E2; in H1 an alternate Q order E2^- has one complete B_L attachment window, and simultaneous success yields an actual same-support/common-complement Q reversal with the fixed-complement consumer applied. Thus the second B contact is now used in literal two-rail reconstructions; unresolved outputs are complete contact-coupled blocker windows, not standalone sign packets.


### 1. Setup and the four contact orientations
Retain the exact F1G1 t=3 fragmented-B cell of SV14216 and the P | (A union Q) specialization of SV14802. Put

  P=(j0,j1,m),
  L=(a,b,c,x),
  J=(j0,j1,m,x,c),
  A={a,b}, Q={c,x}.

Work in the R435-quiet literal-order subcell, so the current whole active blocks are literally P and L. Let B_P and B_L be the two nonempty ACTUAL B-fragment paths on the rails meeting P and L respectively, in their actual target-cover orders. No ancestral interval or order statement about either fragment is made. The exact target T has exactly one B/active attachment on each rail, so, up to swapping rail names, there are exactly four orientations:

  (I)   B_P P | L B_L,
  (II)  P B_P | B_L L,
  (III) B_P P | B_L L,
  (IV)  P B_P | L B_L.

Every construction below writes both output rails. Literal B is used only when its whole support is reassembled; otherwise B_P and B_L keep their actual orders.

Recall the fixed ancestry

  (j0,c,x), (j1,j0,c) tight,

and the quiet L->P first-bad alternatives from SV14802:

  H1: (c,x,j0) bad, hence (j0,x,c) tight;
  H2: (c,x,j0) tight and (x,j0,j1) bad, hence (j1,j0,x) tight.

The old G1 seam (j1,m,a) is bad throughout.

### 2. Orientation I: two opposite Q repairs each isolate A
Assume

  T=(B_P,j0,j1,m) | (a,b,c,x,B_L).

First keep the actual Q->B_L attachment and reverse the Q order at the P join. Test

  W_K=(B_P,j0,j1,m,c,x,B_L).

Its complete new P/Q window is exactly

  alpha=(j1,m,c),
  beta =(m,c,x).

Everything before m is inherited from the first target rail and everything from c,x into B_L is inherited from the second target rail. If alpha and beta are tight, then

  W_K | (a,b)

is an exact two-cover of G=H-{u,v}. The isolated dimer A has both Hamilton orders, so accepted R561 Hamilton-extends A by u (or v). Keeping W_K gives an exact two-cover of H-v (respectively H-u). Thus full success is a genuine codimension-two to codimension-one move.

Second keep the literal P/Q join from J and change only the Q-side attachment to B_L. Test

  W_J=(B_P,j0,j1,m,x,c,B_L).

The P/Q turns (j1,m,x),(m,x,c) are inherited from J. Write B_L=(ell0,ell1,...) in its actual order. The complete new Q/B_L window is

  gamma=(x,c,ell0),
  delta=(c,ell0,ell1) if |B_L|>=2.

If every present turn is tight, then W_J|(a,b) is again an exact G-cover with isolated A, and R561 again gives codimension one.

Therefore a surviving Orientation-I cell blocks BOTH complete windows {alpha,beta} and {gamma,delta}. These two windows sit at opposite ends of the same physical Q dimer: W_K selects c->x and preserves the actual L-side B contact, whereas W_J selects x->c and preserves the literal J-side P/Q join. Retain first-bad identities and their R3 reversals if needed; do not replace this paired two-ended Q repair by a generic sign packet.

### 3. Orientation II: H2 turns the second B contact into a dimer-isolation gate
Assume

  T=(j0,j1,m,B_P) | (B_L,a,b,c,x).

In H2 the turn

  (c,x,j0)

is tight. Isolate the ancestral dimer D=(j1,m) and test the complementary rail

  W_2=(B_L,a,b,c,x,j0,B_P).

Write B_P=(p0,p1,...) in its actual order. Apart from the already-positive H2 turn, the complete new junction window after L is

  eta=(x,j0,p0),
  theta=(j0,p0,p1) if |B_P|>=2.

All B_L-to-L turns are inherited from the second target rail. If every present eta/theta turn is tight, then

  W_2 | (j1,m)

is an exact G-cover with an isolated dimer. Accepted R561 extends that dimer by u or v, so the branch moves to an exact singleton-deletion two-cover.

Hence Orientation II in H2 is consumed unless the actual j0-to-B_P window blocks. The resulting blocker is tied simultaneously to the positive H2 L->j0 turn, the actual second B contact, and the retained H2 fork (j1,j0,c),(j1,j0,x). In H1 the first L->j0 turn is already bad, so this particular repair is not claimed to consume that subcell.

### 4. Orientation III: Q transfers seam-free, then the A endpoint gate applies
Assume

  T=(B_P,j0,j1,m) | (B_L,a,b,c,x).

There is an exact seam-free support relocation:

  T_Q=(B_P,j0,j1,m,x,c) | (B_L,a,b)
     =(B_P,J) | (B_L,A).

The first rail uses the inherited B_P->P attachment followed by the literal J turns. The second rail is a literal prefix of the actual target rail B_L L. Thus no new turn is tested. This moves the whole Q block from the L-side rail to the P-side rail and simultaneously changes its selected orientation from c->x to x->c.

Now consume the terminal A block on the second rail. If |B_L|=1, that rail is a tight trimer; probing it by u and v gives codimension one whenever either probe has a Hamilton P4, while if both probes are P4-free accepted R522 gives a Hamilton P5 on the trimer plus {u,v}, closing H with the first rail.

Assume |B_L|>=2 and write the final two actual B_L vertices r,s, so the second rail ends

  ...,r,s,a,b.

Swap only a,b. Its complete new window is

  kappa=(r,s,b),
  xi=(s,b,a).

If both pass, the old and swapped second rails are exact same-support representatives with the identical untouched complement (B_P,J), selecting {a,b} oppositely. Apply the working fixed-complement selected-reversal consumer SV7559 immediately: its directed R548 transport preserves the common support/complement and either reaches full-support R561 or stops at a named wrap shield. If both kappa,xi fail, the SV14216 endpoint argument gives genuine R561 on the four-support {r,s,a,b}; when |B_L|=2 this is the whole second rail and yields codimension one. If exactly one passes, retain the complete one-sided four-support boundary lock on the actual inward B_L edge. No claim is made that a local R561 support on a longer B_L rail eats the rest of B_L.

Thus Orientation III is not left as a raw support transfer: it enters a short-trimer codimension consumer or the exact A-endpoint transposition consumer with the first rail (B_P,J) held fixed.

### 5. Orientation IV: H1 gives an actual common-complement Q reversal after one head exchange
Assume

  T=(j0,j1,m,B_P) | (a,b,c,x,B_L).

Test the two-rail head exchange

  E1=(a,b,j1,m,B_P),
  E2=(j0,c,x,B_L).

The second rail E2 is automatically tight: (j0,c,x) is retained wrap ancestry and the c,x-to-B_L turns are inherited from the target L B_L rail. The complete new window of E1 is exactly

  mu1=(a,b,j1),
  mu2=(b,j1,m).

If both pass, E1|E2 is an exact cover of G.

Now specialize to H1, where (j0,x,c) is tight. Keeping E1 fixed, test the alternate second rail

  E2^-=(j0,x,c,B_L).

Write B_L=(ell0,ell1,...). Its complete new attachment window after the H1 turn is

  nu=(x,c,ell0),
  omega=(c,ell0,ell1) if |B_L|>=2.

If the mu-window and every present nu/omega turn pass, then

  E1 | E2,
  E1 | E2^-

are two exact covers of the SAME residue, with identical support partition and IDENTICAL literal Hamilton complement E1, selecting the physical Q dimer in opposite directions c->x and x->c. This is a genuine current fixed-complement selected reversal, not a graph-intrinsic local sign. Apply SV7559 immediately, yielding finite common-complement transport to full-support R561 or a named wrap shield.

Therefore an unresolved H1 Orientation-IV cell must block either the complete head-exchange window {mu1,mu2} or the complete alternate-Q attachment window {nu,omega}. In H2 the alternate order j0,x,c is unavailable, so a successful head exchange is retained only as an exact support-transfer representative; no false reversal conclusion is drawn.

### 6. Resulting v43 interface
The quiet P | (A union Q) fragmented-B cell now uses BOTH physical B contacts in complete two-rail reconstructions.

- Orientation I has two opposite-Q A-isolation repairs; success of either gives codimension one, so the hard state carries two opposed complete blocker windows.
- Orientation II + H2 has a second-contact dimer-isolation repair; success gives codimension one.
- Orientation III has a seam-free Q support transfer followed immediately by the trimer/A-endpoint consumer with the complementary rail fixed.
- Orientation IV + H1 has a head exchange whose successful alternate Q attachment currentizes an actual same-support/common-complement Q reversal and applies the fixed-complement consumer.

The remaining objects are therefore contact-coupled blocked SURGERIES, not standalone signs. All actual B-fragment orders, both physical B/active attachments, H1/H2 ancestry, and any DF/MX P-side certificate remain retained. No generic R159/R176/R523/R542 payment is used. This section is working exposition and does not claim closure of the other active-support splits or of higher fragmentation.


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
    },
    {
        "relation": "dependency",
        "revision_id": "R561"
    }
]
```
