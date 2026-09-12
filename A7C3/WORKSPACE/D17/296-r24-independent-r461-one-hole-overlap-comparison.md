# R461 is R24-independent: one-hole overlap comparison is purely local

**Workspace:** D17
**State:** established
**Key:** `r24-independent-r461-one-hole-overlap-comparison`

**Summary:** R461, `One-Hole Overlap Comparison`, admits a direct R24-independent proof. Its hypotheses already provide two literal tight paths/forests on overlapping supports with one missing physical vertex. The conclusion is obtained by ordering the common contacts along one ancestral path and applying accepted Reverse Ear R435 to the comparison path. A decrease gives the exact adjacent reversal / reverse trimer / proper cycle output; monotone contacts leave a single insertion slot for the one foreign vertex, yielding the quiet one-hole normal form. No singleton-deletion order floor, short-complement classification, or R24 descendant is used.

### 1. Abstract one-hole frame
Retain the literal R461 hypotheses: an ancestral tight path

  P=(p_0,...,p_m)

and a comparison tight path Q whose support differs from V(P) by exactly one foreign physical vertex x and possibly omits one named old vertex according to the one-hole setup.

The theorem compares the order in which Q meets the retained P-vertices and classifies the unique hole/foreign insertion.

### 2. Apply Reverse Ear directly
List the P-contacts in Q-order and record their P-indices

  i_0,i_1,...,i_t.                                      (R461.1)

If this index sequence has a decrease, accepted R435 applies to the first consecutive reverse-order contact pair. Its conclusion is exactly the local nonquiet alphabet used by R461:

  adjacent selected-state reversal,
  reverse tight trimer,
  or proper vertex-simple tight cycle.                   (R461.2)

This argument is support-local. It does not know or care how many vertices lie in any complementary deletion rail.

### 3. Quiet case has one insertion slot
Assume no R435 output. Then the retained P-contacts occur in increasing P-order along Q. Since Q has only one foreign vertex x relative to the ancestral support, its word is obtained from the retained P-order by inserting x in one slot and omitting the prescribed one-hole vertex if present.

Thus the quiet branch is exactly the one-hole monotone insertion normal form stated by R461. Any additional displacement would create a reverse-order contact pair and return to Section 2.

### 4. Dependency repair
The proof uses only

  literal R461 overlap hypotheses + accepted R435.       (R461.3)

Boundary antisymmetry R3 is already internal to the accepted R435 proof. R24 contributes no necessary statement.

Therefore R461 can be detached from quarantined R24 without weakening its conclusion. This section is the replacement proof certificate; canonical dependency metadata may be updated separately.