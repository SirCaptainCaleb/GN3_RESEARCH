# Pivot the dual route from terminal-pair cuts to defect-span certificates

## Statement

Proposal: use spanning orderings and defect span as the compressed state space for the dual-obstruction route. The used-vertex resource that defeats terminal-pair cut models is automatically encoded by a spanning ordering, and a two-cover exists exactly when some spanning ordering has defect span at most two. Thus a distinct dual theorem should characterize the opposite condition: every spanning ordering has defect span at least three, preferably by a finite certificate whose local witnesses can be altered or canceled by the boundary-tournament relations.

## Body

The ordered-terminal-pair model forgets vertex simplicity and disjoint ownership; the faithful used-set model restores them only at exponential cost. The project already has an exact compression that avoids this defect: a spanning ordering uses every vertex once, and the two-cover question is equivalent to whether its defect centers fit in span at most two. In a minimum counterexample the optimum span is three, and certified results identify such an ordering with a deletion-cover ordering and a canonical central 3- or 5-path state. Therefore the path-cut brainstorm has no independent state-space advantage unless it produces a genuinely dual certificate for minimum defect span three. The missing target is a min-max or cancellation statement for span-three defect witnesses, not another terminal-pair separator.
