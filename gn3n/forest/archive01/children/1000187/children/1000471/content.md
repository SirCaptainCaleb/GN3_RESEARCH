# Canonical-bridge descent alone does not rule out trapping

## Statement

Let K be a finite connected component of the pairwise-repartition graph and let Phi be any integer-valued potential on its states. Knowing that a distinguished canonical bridge state C in K has a legal move to a state of smaller Phi does not imply that K contains a two-cover or that K is untrapped. A strictly Phi-decreasing sequence starting at C may terminate at a different Phi-minimal state M in K after the canonical bridge structure has been lost. Consequently, proving only that canonical central-bridge states are not Phi-minimal is insufficient for the no-trapping reduction; one additionally needs either preservation/recovery of the canonical bridge property along descent or a descent/merge theorem applying to every possible terminal state reached from the bridge.

## Body

This is a structural fence on the proposed bridge-minimality mechanism. Finiteness guarantees termination of strict Phi descent, but termination occurs at some minimum of the whole move component, not necessarily at a state retaining the deletion-generated central bridge. Hence the implication 'canonical bridge has strict descent => trapped component impossible' is invalid without a preserved invariant tying every terminal state back to the bridge class. The existing three-side descent theorem is compatible with this: it proves the first descent, not that all later states continue to descend.
