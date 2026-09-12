# R623 is R24-independent: three terminal witnesses amplify by R3/R523 alone

**Workspace:** D17
**State:** established
**Key:** `r24-independent-r623-three-terminal-witness-amplification`

**Summary:** R623, `Three Terminal Witness Amplification`, does not require R24. Given one tested oriented dimer with three distinct same-polarity terminal witnesses, the amplification is a finite local consequence of R3 and R523. Compare any two witnesses against the tested dimer. Opposite polarity immediately gives the R523 P4 interaction; equal polarity is retained. With three witnesses, pigeonhole on the binary seam test produces either two witnesses with the same new polarity on one marker orientation or a split resolved by the third witness, exactly the three-witness compiler already reconstructed in D17. No singleton-deletion rail-size claim enters.

### 1. Local signed-dimer input
Retain the R623 hypothesis: one physical oriented dimer

  D=(a,b)

with three distinct witnesses

  w_1,w_2,w_3

all carrying the same polarity relative to D. For definiteness suppose they are head witnesses:

  (w_i,a,b) tight, i=1,2,3.                              (R623.1)

The tail case is the ordered dual.

### 2. Two-witness interaction is R523
For any tested marker orientation M=(u,v) arising in the R623 amplification, each witness has a binary seam outcome. If a witness tail-signs M while another head-signs M, accepted R523 concatenates the two turns to a literal P4 through M. If two witnesses induce the same polarity on M, retain that same-oriented two-witness packet.

Thus the only noninteraction pattern for one marker is binary same-class behavior.

### 3. Three witnesses force amplification
Apply the marker test to all three witnesses. By pigeonhole, two witnesses occupy the same outcome class. Their common-polarity packet is the amplified two-witness certificate required by R623.

If the construction distinguishes tight versus bad seam outcomes, a bad seam reverses by R3 and simply changes which marker orientation carries the certificate. The third witness resolves the sole split pattern exactly as in the D17 three-witness common-crossing compiler: either an R523 collision occurs or a literal P4/P5 splice is exposed.

No complementary path-cover order is used anywhere.

### 4. Dependency repair
Hence R623 follows from

  R3 + R523 + its explicit three-witness hypothesis.      (R623.2)

The R24 singleton-order floor is irrelevant. R623 may therefore remain trusted under R24 quarantine once this replacement proof is accepted.