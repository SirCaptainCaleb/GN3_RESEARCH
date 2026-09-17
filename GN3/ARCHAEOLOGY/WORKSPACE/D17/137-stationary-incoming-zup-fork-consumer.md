# The incoming B-to-V fork consumes the Z-U-p block word

**Workspace:** D17
**State:** working
**Key:** `stationary-incoming-zup-fork-consumer`

**Summary:** In the quiet c=2,d=1,tau_Z=1 incoming B-to-V survivor, if the other rail has block word Z-U-p, the B terminal has two actual continuations: the current seam into V and the ancestral puncture geometry through p. Replacing retained B by the final-gap puncture K_B changes only (p,b_{k-1},x). If tight, K_B-V and u_X-Z-U give a singleton-deletion two-cover with both rails below 2k. If bad, its reverse together with the Y-p puncture turn gives an R542 two-witness packet on reverse terminal dimer (b_{k-1},p). Thus this entire block word is consumed into threshold closure or R542.

### Setup
Retain the quiet `c=2,d=1,tau_Z=1` stationary survivor after `stationary-one-p-finalgap-consumer`. Up to A/B duality, p is terminal in the A/p block U, the unique A-B seam is incoming from the full retained-order B block into the other A block V, and the one remaining common cross is Z-incident. Write

  B=(b_1,...,b_{k-1}),

let x be the first vertex of V, and retain the exact final-gap puncture on B+p

  K_B=(b_1,...,b_{k-2},p,b_{k-1}).

Write b=b_{k-1}. The stationary source Y-u_Y-z-(Z-z), together with the quiet terminal-puncture theorem on Y+p, gives the exact tight turn

  (u_Y,b,p).

Assume the actual two-cover of W=H-{u_X,u_Y} has block word

  Z - U - p  |  B - V,

with the displayed orientations; the common dual is identical after reversal of the whole argument. Let U_0 denote the A-vertices of the first rail, so U is the path U_0 followed by p. Both U_0 and V are nonempty and partition A.

### The puncture fork at the B terminal
The current seam B-V certifies the complete retained junction at b and x. Replacing the retained B order by K_B changes only one turn before that same selected continuation:

  h=(p,b,x).

Indeed the incoming turn (b_{k-2},p,b) belongs to K_B, the turn after b,x is inherited from the current B-V seam, and every other turn is unchanged.

If h is tight, then

  P_1=K_B - V

is a Hamilton path on B union {p} union V.

On the other current rail, delete its terminal p and prepend the omitted stationary seam label u_X to the retained-order Z block. The ancestral turn (u_X,z,z_2) is tight, while the entire Z-U_0 junction is inherited from the current rail. Hence

  P_2=u_X - Z - U_0

is a Hamilton path on {u_X} union Z union U_0.

The two paths partition H-u_Y. If u=|U_0| and v=|V|, then u+v=k-1 with u,v>=1, and

  |P_1|=k+v <= 2k-1,
  |P_2|=k+u+1 <= 2k-1.

Thus both rails are strictly below the global offending threshold a=2k, contradicting `subminimum-source-saturation`.

### Failure is an exact R542 packet
It remains that h is bad. Boundary antisymmetry gives

  (x,b,p)

tight. Together with the retained puncture turn

  (u_Y,b,p)

this gives two distinct head witnesses x and u_Y on the same tested oriented dimer

  S=(b,p).

The terminal trimer of K_B is

  C=(b_{k-2},p,b),

so S is exactly its reverse terminal boundary dimer. Both witnesses lie outside C. Therefore accepted R542 applies with the actual B-V seam, puncture order, omitted stationary label u_Y, and carrier C all retained.

### Output
Hence the incoming B-to-V stationary survivor with block word

  Z-U-p | B-V

cannot remain a direct-repair obstruction. It yields either

1. an explicit exact singleton cover of H-u_Y whose two rail orders are both <2k, contradiction; or
2. the source-anchored R542 packet on reverse puncture boundary dimer (b_{k-1},p) with witnesses x,u_Y.

No claim is made that the R542 descendant alone closes Arm A. The two other Z-cross block words, U-p | B-V-Z and U-p | Z-B-V, remain separate direct-repair cells.

Status: complete working deduction inside the corrected stationary c=2,d=1,tau_Z=1 quiet cell.
