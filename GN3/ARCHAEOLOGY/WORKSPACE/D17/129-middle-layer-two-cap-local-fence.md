# The local two-cap package does not close the near-maximal branch at k=7

**Workspace:** D17
**State:** limitation
**Key:** `middle-layer-two-cap-local-fence`

**Summary:** A verified ten-vertex boundary assignment at k=7 satisfies the complete h/t star signs, rigid endpoint pairs on all three residual-pair 7-supports, every left/right cap terminal normal form, the common ordinary two-cap label conclusion, and Hamiltonicity of every one-vertex deletion of the target U_r, while U_r itself is non-Hamiltonian. Thus no all-k proof may use only this local cap/critical-block data; the P-relative active-side or same-residue cover coupling is genuinely additional information.

### Exact finite fence for pure two-cap amalgamation

This section is a computational limitation, not a proof of the near-maximal branch. It shows that the local data isolated in `middle-layer-nearmax-outer-terminal` and `middle-layer-common-two-cap-label` do not by themselves imply the desired cap union when k=7.

Use vertices 0,...,9 with

  O={0,1,2,3,4},  R={5,6,7},  h=8,  t=9,

and take the common ordinary cap label r=5. Encode a boundary tournament by one bit for each complete-reversal pair of ordered triples, using the lexicographically smaller representative and ordering the 360 representatives lexicographically. Bit 1 means the canonical orientation is tight. The following 360-bit assignment, packed as hexadecimal, is a reproducible satisfying certificate:

  fd81dd01a0a0a02ea0bd027408000006004275d0628a2920f510420101c00f43dfeef0111110003492005540fc

Direct enumeration verifies all of the following.

1. COMPLETE STAR SIGNS. For every x in O and every y in O union R distinct from x, both (h,x,y) and (y,x,t) are tight.

2. RIGID RESIDUAL-PAIR SUPPORTS. Each O+a+b, {a,b} subset R, has Hamilton paths and every Hamilton path has endpoint pair exactly {a,b}. In fact each has exactly two Hamilton orders:
   Z_56: (5,4,3,0,2,1,6) and (6,4,3,0,2,1,5);
   Z_57: (5,4,3,0,2,1,7) and (7,4,3,0,2,1,5);
   Z_67: (6,4,3,0,2,1,7) and (7,4,3,0,2,1,6).

3. ALL SIX CAP TERMINAL NORMAL FORMS. For X_v=O+h+v every Hamilton path is of the near-maximal left TYPE A/B form, and for Y_v=O+t+v every Hamilton path is of the right TYPE A_R/B_R form. For v=5 the exceptional forms do not occur: every X_5 Hamilton path ends at 5 with h first or second, and every Y_5 Hamilton path starts at 5 with t last or penultimate. Counts of Hamilton orders are X_5:4, Y_5:5, X_6:4, Y_6:7, X_7:4, Y_7:7, with zero violations of the stated terminal forms.

4. FULL LOCAL CRITICAL-BLOCK PUNCTURES. Put U_5=O+{h,t,5}. U_5 has no Hamilton path, but every U_5-d is Hamiltonian. The Hamilton-order counts after deleting d=0,1,2,3,4,5,8,9 are respectively 12,9,7,12,9,29,5,4.

Thus the complete stars, all three rigid residual-pair supports, all six cap terminal restrictions, the common ordinary cap label, and even deletion-Hamiltonicity of the target U_r can coexist with U_r non-Hamiltonian at k=7. The k=6 local package is infeasible, but that is a small-order phenomenon and cannot be elevated to an all-k theorem.

CONSEQUENCE. Any general near-maximal closure must spend information not present in this ten-vertex local package. The live candidates are precisely the P-relative support-wide activity and the same-residue exchange covers with forced complementary endpoints. Pure local two-cap amalgamation is therefore fenced.

Status: verified finite limitation certificate; not canonical mathematics until independently reviewed.
