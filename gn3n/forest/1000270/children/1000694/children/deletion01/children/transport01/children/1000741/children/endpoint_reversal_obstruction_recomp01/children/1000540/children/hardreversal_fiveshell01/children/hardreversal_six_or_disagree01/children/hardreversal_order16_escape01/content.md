# From order sixteen the hard endpoint-reversal residue yields crossing, strict descent, or order disagreement

## Statement

Let H be a minimum counterexample of order n>=16 in the hard endpoint-reversal residue of hardreversal_fiveshell01. Then H exposes at least one of the following: (1) explicit order disagreement supported on a six-vertex slice of the hard residue; (2) a spanning three-cover admitting a strict decrease of the quadratic component-size potential Phi; (3) a component-drop crossing: for a Hamiltonian four-core D and a full two-label path-cover-two square K,K+d,K+e,K+d+e, deleting d or e from a displayed two-cover of the top square produces a three-path cover of a lower state, while some two-cover of that lower state contains an ordinary edge joining two different components of the three-path cover. Thus above order fifteen the universal hard endpoint-reversal branch has no separate Hamiltonian-six residue.

## Body

Choose any four outside labels and apply hardreversal_six_or_disagree01 to the resulting six-set U. If that theorem gives order disagreement, outcome (1) holds. Otherwise U is a proper Hamiltonian six-set and K=H-U is non-Hamiltonian with path-cover number two. Apply ham6goodsquare01: choose endpoint labels d,e of a Hamilton order on U and put D=U-{d,e}. Then D, D+d=U-e, and D+e=U-d are Hamiltonian, while K,K+d,K+e,K+d+e are all non-Hamiltonian with path-cover number two. These are exactly the square hypotheses of ham4squareescape01. Since n>=16, that theorem yields either a component-drop crossing, a strict Phi descent, or order disagreement, giving outcomes (3), (2), or (1) respectively.
