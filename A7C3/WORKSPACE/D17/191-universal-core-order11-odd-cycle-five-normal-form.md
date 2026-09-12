# An R408-quiet odd donor circuit at order eleven is exactly a five-cycle with two fixed donor endpoints

**Workspace:** D17
**State:** established
**Key:** `universal-core-order11-odd-cycle-five-normal-form`

**Summary:** In the order-eleven universal-core shell SV17264, suppose the chosen shortest donor support-exchange circuit is odd of length at least five and no R408 endpoint/internal discrepancy occurs. SV17264 forces the A-INTERNAL-CIRCUIT regime: the common endpoint set E has two vertices in the fixed three-core A and no circuit label. Since |E|=4 and |Y|=7, the remaining two endpoints must be donor labels outside the circuit, so the circuit omits at least two of the seven donor labels. Therefore its odd length is at most five and hence exactly five. The two off-cycle donor labels are exactly the endpoints of every donor Hamilton P5 in the five exchange covers, while the same two fixed A vertices are the endpoints of every active Hamilton P5. Thus the odd R408-quiet residue is a rigid five-cycle of 5+5 covers with fixed endpoint pairs on both rails.


Retain the order-eleven shell `singleton-universal-core-order11-exchange-shell` SV17264. Thus |X|=4, |Y|=7, a fixed x in X gives A=X-x of order three, and a shortest donor-good cycle

  C=(v_0,v_1,...,v_{m-1},v_0)

supports exact 5+5 covers

  C_i : (A+{v_i,v_{i+1}}) | (Y-{v_i,v_{i+1}})

of H-x.

Assume C is odd with m>=5 and that no physical endpoint/internal discrepancy occurs among the C_i. By SV17264 Section 5 the common physical endpoint set E has size four, and every odd shortest cycle of length at least five is forced into A-INTERNAL-CIRCUIT:

  |E cap A|=2,
  E cap V(C)=empty.                                      (O5.1)

Therefore the other two members of E lie in Y-V(C). In particular

  |Y-V(C)| >= 2.

Since |Y|=7,

  m <= 5.

Together with m>=5 this forces

  m=5.                                                   (O5.2)

Write

  Y-V(C)={r,s}.

Equation (O5.1) and |E|=4 now give

  E cap Y={r,s}.                                        (O5.3)

For every circuit edge {v_i,v_{i+1}}, the donor rail

  Y-{v_i,v_{i+1}}

is a Hamilton five-support in C_i. Its two physical endpoints are precisely the members of E lying on that support. Neither circuit label is in E, while r,s belong to every donor support. Hence EVERY chosen donor Hamilton P5 in the circuit has the SAME physical endpoint pair

  {r,s}.                                                (O5.4)

Likewise every active rail A+{v_i,v_{i+1}} has the same two endpoints E cap A.

Thus the entire odd R408-quiet support-exchange residue is a five-cycle of exact 5+5 covers with fixed endpoint pairs on BOTH rails. Consecutive donor rails differ by exchanging one cycle label across a common four-set but retain endpoints r,s. This is the correct bounded laboratory for further order synchronization: an R435 event is useful explicit geometry, while an R435-quiet comparison gives an adjacent/same-slot insertion constraint on an internal exchanged label. No contradiction from those slot constraints is asserted here.

Status: direct working deduction from SV17264. It does not certify SV17264 and does not itself close the order-eleven universal-core shell.
