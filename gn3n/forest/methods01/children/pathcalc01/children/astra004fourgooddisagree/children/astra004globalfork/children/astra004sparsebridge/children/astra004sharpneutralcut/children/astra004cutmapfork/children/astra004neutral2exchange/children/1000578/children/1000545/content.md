# Every sharp-shell longest path exposes explicit transport disturbance

## Statement

Let H be a minimum counterexample in the sharp half-order shell |V(H)|=2lambda+1, let A=(a_0,...,a_{lambda-1}) be any globally longest tight path, put U=V(H)-V(A), and let D={u in U : H[U-{u}] is Hamiltonian}. Then the deletion states around A cannot all be transport-neutral. More precisely, at least one of the following occurs: (i) for some t in D and some endpoint y of A, an exact cover of H-y contains an ordinary edge directly joining U-{t} to A-{y}, or the corresponding endpoint comparison exposes explicit relative-order disagreement; (ii) for some bad label u in U-D, an exact cover of H-u has at least three ordinary edges crossing the cut A | (U-{u}); (iii) some bad-label exact cover with exactly two A | (U-{u}) crossings already exposes explicit ordered disturbance against A; or (iv) two bad labels u,v expose explicit disturbance on H-{u,v}: an inherited three-part crossing, a support-partition crossing between exact covers, or relative-order disagreement. Thus there is no fully neutral longest-path deletion shell in the sharp half-order case.

## Body

Let D be as stated. If |D|>=3, apply astra004threegoodmixed to A. It supplies t in D and one endpoint y of A such that the chosen exact cover of H-y either contains an ordinary edge directly joining the surviving U-side U-{t} to A-{y}, or the endpoint probes expose explicit relative-order disagreement. This is outcome (i).

Assume therefore |D|<=2. By the deletion-sparse branch of astra004globalfork, for every bad label u in U-D, every exact two-cover of H-u has at least two ordinary edges crossing the cut between A and U-{u}. Choose one exact cover C_u for each bad u. If some C_u has at least three such crossings, outcome (ii) holds.

Hence suppose every chosen C_u has exactly two crossings. Apply astra004sharpneutralcut to each C_u. If any one of these equality-two-crossing covers exposes ordered disturbance against A, outcome (iii) holds. Otherwise every bad deletion state lies in the completely order-neutral cut form of astra004sharpneutralcut. The sparse cut-map closure b2fe28397642 then applies and forces explicit disturbance between two bad deletion states in their common double deletion H-{u,v}: either an inherited three-part crossing, a support-partition crossing, or explicit relative-order disagreement. This is outcome (iv).

The four alternatives exhaust the possibilities, so a fully transport-neutral family of deletion states around a globally longest path cannot occur. ∎
