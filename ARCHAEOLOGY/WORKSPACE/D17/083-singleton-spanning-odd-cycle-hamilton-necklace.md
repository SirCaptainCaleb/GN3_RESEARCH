# A spanning odd compatibility root is a cyclic common-complement Hamilton-support necklace

**Workspace:** D17
**State:** established
**Key:** `singleton-spanning-odd-cycle-hamilton-necklace`

**Summary:** In the R926 spanning odd-cycle branch, label the root edges e_0,...,e_{2k}. The port universes and singleton rails are explicit: with I_j={e_j,e_{j+2},...,e_{j+2k-2}}, every I_j is Hamiltonian, C_{e_i}=I_{i+1}|I_{i+2}, and Omega_i=V-I_{i+1} is a non-Hamiltonian (k+1)-set whose two incident punctures are Hamiltonian. The supports I_j form one cyclic Johnson orbit I_{j+2}=I_j-e_j+e_{j-1}. Hamilton orders may be chosen coherently, one P_j per I_j, and reused in both singleton rows. Outside R408 every Hamilton order on a fixed I_j has one fixed endpoint pair. The compatibility-neighbor labels e_{i+1} in I_{i+1} and e_{i-1} in I_{i+2} can never be universal endpoints of C_{e_i}, because the adjacent compatible singleton row is an explicit crossing-free witness. Along an exchange I_j=K+e_j to I_{j+2}=K+e_{j-1}, either R435 gives explicit geometry or the common K-order is aligned; in the aligned branch the two inserted labels must occupy the same or adjacent insertion slots, since slot distance at least two would combine the two Hamilton paths into a Hamilton path on the forbidden port universe K+e_j+e_{j-1}. For adjacent singleton rows, deleting their two labels gives a common pair-deletion residue with one literal shared rail; if exactly one exchanged label is an endpoint, the two trims have component counts two and three and give an explicit R159 component drop. Finally, if every coherent P_j has both of its exchange labels e_j,e_{j-3} as endpoints, odd parity forces some singleton row to have opposite-role universal endpoints, hence the R933/reverse-connector branch of the accepted endpoint-universal lock. This is a global monodromy interface, not closure.

### 1. Explicit coordinates for the spanning odd-cycle root
Retain a hypothetical smallest counterexample H and a complete chosen exact singleton-deletion cover family whose accepted R926 rail-incidence root is the spanning odd cycle

  P_0 -e_0- P_1 -e_1- ... -e_{2k}- P_0,

with n=2k+1 physical labels e_0,...,e_{2k}; indices are modulo n. The R926 one-defect coloring determines every port universe explicitly. Define

  I_j={e_j,e_{j+2},...,e_{j+2k-2}}.                    (ON.1)

Then

  Omega_i = {e_{i-1},e_i,e_{i+2},e_{i+4},...,e_{i+2k-2}}
          = V(H)-I_{i+1}.                               (ON.2)

Indeed e_i is the unique monochromatic root edge for the coloring epsilon_{e_i}; starting with value 1 at both endpoints P_i,P_{i+1}, the remaining cycle path alternates, giving exactly (ON.2). Consequently the two rails of the singleton row C_{e_i} are

  Omega_i-{e_i}=I_{i+2},
  Omega_{i+1}-{e_i}=I_{i+1}.                            (ON.3)

After swapping the displayed rail order if desired, write coherently

  C_{e_i}=P_{i+1}|P_{i+2},                              (ON.4)

where P_j is a Hamilton path on I_j. Every I_j is therefore Hamiltonian. Since I_{i+1} is the complement of Omega_i and is Hamiltonian, Omega_i itself is non-Hamiltonian: a Hamilton path on Omega_i together with P_{i+1} would two-cover H. Thus each Omega_i is a non-Hamiltonian (k+1)-set with the two Hamilton punctures Omega_i-e_{i-1}=I_i and Omega_i-e_i=I_{i+2}.

The Hamilton supports form one cyclic Johnson orbit:

  I_{j+2}=I_j-{e_j}+{e_{j-1}}.                          (ON.5)

Because gcd(2,2k+1)=1, repeated +2 visits all n supports.

### 2. Coherent order choice and endpoint rigidity outside R408
Choose once and for all one actual Hamilton order P_j on every I_j and use that same literal path in both singleton rows in which I_j occurs. Equation (ON.4) is then a globally coherent exact cover family.

Suppose a fixed support I_j admits two Hamilton paths P_j,P'_j with different physical endpoint pairs. Keep P_{j+1} fixed in the singleton residue H-e_{j-1}. Both

  P_j|P_{j+1},   P'_j|P_{j+1}

are literal exact two-covers of that same proper residue. Exactness holds because a Hamilton H-e_{j-1} path together with singleton e_{j-1} would close H. A physical vertex lying in the symmetric difference of the endpoint pairs is endpoint in one cover and internal in the other, so accepted R408 applies.

Hence outside explicit R408 output, every Hamilton path on every fixed I_j has one common physical endpoint pair E_j. This is supportwise endpoint rigidity, not literal-order uniqueness.

### 3. The cyclic exchange labels are never universal endpoints in their incident row
Fix row

  C_{e_i}=I_{i+1}|I_{i+2}.

The compatibility-neighbor label e_{i+1} lies in I_{i+1}. It cannot be universal relative to this singleton source. Indeed

  I_{i+3}=I_{i+1}-{e_{i+1}}+{e_i},

so the adjacent compatible singleton row is

  C_{e_{i+1}}=I_{i+2}|I_{i+3}
             =I_{i+2}|((I_{i+1}-{e_{i+1}})+e_i).        (ON.6)

This exact cover of H-e_{i+1} selects no adjacency between I_{i+1}-{e_{i+1}} and I_{i+2}, because those sets lie on different rails. Thus it is an explicit witness to nonuniversality of e_{i+1} in C_{e_i}.

Dually e_{i-1} lies in I_{i+2} and the adjacent row C_{e_{i-1}} is an exact crossing-free witness showing that e_{i-1} cannot be universal relative to C_{e_i}. Therefore the one root-neighbor label carried by each rail is forbidden from serving as that rail's universal endpoint in the accepted endpoint-universal-lock theorem.

### 4. Adjacent Hamilton supports have same-or-adjacent insertion slots outside R435
Consider one Johnson exchange (ON.5). Put

  K=I_j-{e_j}=I_{j+2}-{e_{j-1}},
  a=e_j,  b=e_{j-1}.

Thus P_j is Hamilton on K+a, P_{j+2} is Hamilton on K+b, while

  K+a+b=Omega_{j+1}

is non-Hamiltonian by Section 1. Apply accepted R435 to P_j and P_{j+2}. If the comparison is nonquiet, retain the explicit reversal/reverse-trimer/proper-cycle output. Assume it is quiet. Then the common K-vertices occur in the same linear order in both paths. Write this order as

  K=(x_1,...,x_m),  m=k-1,

and regard a and b as inserted into slots r,s of that common order, where slots 0 and m are the two exterior slots.

If |r-s|>=2, form the word obtained from (x_1,...,x_m) by inserting both a at slot r and b at slot s. Every consecutive triple of this double-insertion word is certified by P_j or P_{j+2}. A triple containing a is one of the unchanged local triples of P_j because the b-slot is at least two slots away; symmetrically for b. A triple containing neither insertion is a consecutive K-triple unbroken by either insertion and hence occurs in both source paths. Therefore the double-insertion word is a Hamilton tight path on K+a+b=Omega_{j+1}, contradiction.

Hence every R435-quiet exchange satisfies

  |r-s|<=1.                                             (ON.7)

This is the all-order near-slot insertion constraint.

### 5. Endpoint-status mismatch on one exchange gives a current pair-deletion component drop
Compare adjacent singleton rows

  C_{e_i}=P_{i+1}|P_{i+2},
  C_{e_{i+1}}=P_{i+2}|P_{i+3}.                          (ON.8)

The active exchanged labels are e_{i+1} in P_{i+1} and e_i in P_{i+3}; the common rail P_{i+2} is literally identical. Delete both e_i,e_{i+1}.

If e_{i+1} is an endpoint of P_{i+1}, trimming it from the first row yields a literal two-cover of

  W=H-{e_i,e_{i+1}}

with common rail P_{i+2}. It is exact because a Hamilton path on W together with the vacuous dimer (e_i,e_{i+1}) would two-cover H. If e_{i+1} is internal, the same trim yields a literal three-cover of W, obtained by splitting P_{i+1}. The identical statements hold for e_i in P_{i+3} using the second row.

Therefore, if exactly one of the two exchanged labels is an endpoint in its source rail, the two trims of (ON.8) give a literal two-cover and a literal three-cover of the SAME pair-deletion residue W, with P_{i+2} retained literally. Accepted R159 applies directly. Retain the two source singleton rows, the common P_{i+2}, both trimmed forests, and the actual selected state of the two-cover joining two components of the three-cover.

Thus a component-drop-quiet exchange must have matching endpoint status: endpoint/endpoint or internal/internal.

### 6. If every support exposes both exchange labels, odd parity forces opposite-role universality
For support I_j, the two labels participating in its two neighboring exchanges are

  e_j  and  e_{j-3}.                                    (ON.9)

Suppose every coherent path P_j has both of these labels as its two physical endpoints. Assume also that the fixed-complement R435 alternatives of the accepted endpoint-universal-lock theorem do not occur.

In row C_{e_i}=P_{i+1}|P_{i+2}, Section 3 says the endpoint e_{i+1} of P_{i+1} is nonuniversal, so the other endpoint e_{i-2} must be universal on that rail. Likewise e_{i-1} is the nonuniversal endpoint of P_{i+2}, so its other endpoint e_{i+2} must be universal.

Define rho_j to be the source/terminal role of e_j in P_j. Since P_j has endpoints e_j and e_{j-3}, the role of e_{j-3} is the opposite of rho_j. If no row has an opposite-role universal pair, the two universal endpoints e_{i-2} and e_{i+2} in C_{e_i} must have the same role. Their roles are respectively opposite(rho_{i+1}) and rho_{i+2}. Hence

  rho_{i+2}=opposite(rho_{i+1})                         (ON.10)

for every i. Thus the binary roles alternate around the cycle. Because the cycle length 2k+1 is odd, (ON.10) is impossible.

Consequently the all-support double-exposed regime necessarily contains a singleton row with opposite-role universal endpoints. By the accepted endpoint-universal-lock theorem, that row enters the exact R933 two-hole seam branch when its role-correct hub turn is tight, or carries the named reverse middle connector when that turn is bad.

### 7. Scope and moonshot target
The spanning odd-cycle exception of R926 is therefore not a free alternating support pattern. It is a cyclic common-complement Hamilton-support exchange orbit with four simultaneous pressures: supportwise endpoint rigidity outside R408, forbidden universality at the exchange labels, same/adjacent insertion slots outside R435, and pair-deletion component drop whenever exchanged endpoint statuses mismatch. If every support exposes both exchange labels, odd parity forces opposite-role absorber geometry.

The unresolved hard residue has genuinely internal exchange labels on some supports, or same/adjacent-slot exchanges whose endpoint statuses match around the whole orbit. The next moonshot consumer should use the common literal rail in (ON.8) to consume an INTERNAL/INTERNAL exchange as a two-sided augmenting-forest event, rather than paying its two three-cover comparisons anonymously. No spanning two-cover is claimed here.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R926"
    },
    {
        "relation": "dependency",
        "revision_id": "R408"
    },
    {
        "relation": "dependency",
        "revision_id": "R435"
    },
    {
        "relation": "dependency",
        "revision_id": "R159"
    },
    {
        "relation": "dependency",
        "revision_id": "R927"
    },
    {
        "relation": "dependency",
        "revision_id": "R933"
    }
]
```
