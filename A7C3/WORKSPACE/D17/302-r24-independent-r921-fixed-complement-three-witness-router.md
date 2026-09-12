# R921 is R24-independent: three-witness fixed-complement routing is local wall geometry

**Workspace:** D17
**State:** established
**Key:** `r24-independent-r921-fixed-complement-three-witness-router`

**Summary:** R921, `Fixed-Complement Three-Witness Router`, is independent of R24. Once the fixed-complement wall of R912 is available, three distinct deletion labels provide three same-polarity witnesses on each reverse boundary dimer of the complement. The three-witness routing then uses only R3, R523, and the common-crossing/finite seam compiler: pigeonhole on the binary actualization tests yields a same-oriented collision, direct balanced pair, P4/P5, or bidirectional packet. No singleton-deletion rail-size floor is used.

### 1. Input from the repaired wall
Use the R24-independent R912 wall. For three distinct labels y_1,y_2,y_3 in the deletion-Hamiltonian block Omega, the reverse source dimer of Q is tail-signed by all three and the reverse terminal dimer is head-signed by all three.

### 2. Three-witness compiler
Apply the local three-witness mechanism to either boundary dimer. Every selected crossing/marker test is binary. With three witnesses, two share one outcome class; equal opposite polarity gives the R523 interaction/P4, same polarity gives the retained collision packet, and the split case is resolved by the third witness exactly as in the three-witness common-crossing D17 compiler.

The refined output is one of

  P4/P5,
  direct mass-four balanced pair,
  bidirectional same-witness packet.                     (R921.1)

### 3. Dependency repair
All inputs are local wall turns plus R3/R523. Therefore R921 is independent of R24 once R912 is supplied by its repaired proof.