# Alternating exchange graph for path forests

## Statement

Given a three-path cover P|Q|R, build an auxiliary bipartite graph whose left vertices are path endpoints and whose right vertices are internal cut positions; an edge records a certified splice that moves an endpoint across a cut while preserving three paths. Conjecture an augmenting-path theorem: if no two components can be merged, every maximal alternating exchange walk eventually creates two distinct splices into the same component, and their symmetric difference yields a legal merge. Equivalently, a merge-free three-cover should force a finite Hall-type deficiency certificate that can be ruled out by boundary antisymmetry.

## Body

Why it might matter globally:
This recasts repeated path surgery as augmenting-path combinatorics, potentially turning many ad hoc crossing configurations into one global exchange theorem. It is structurally different from both support reconfiguration and defect-span minimization.

Plausible first attack:
Restrict first to three paths with all orders at least four. Define only endpoint-to-single-cut splices whose new consecutive triples are explicitly checkable. Derive the exact Hall obstruction for absence of an augmenting walk of length at most three, then translate that obstruction into a pattern of forced reversed triples. Check whether the forced pattern already creates a direct two-component merge.