# Audit single step residual scans require an unproved propagation lemma — preserved pre-item development

## Composition

(none yet)

## Development

## Audit: single-step residual scans require an unproved propagation lemma

Subsection "Residual A2 scans are single-step functions with same-parity drop ranks" uses the statement that an immediate (0	o1) rise in any residual suffix scan produces a spanning companion weave.

The currently proved companion-weave theorem only establishes this at the first right reconnection of the canonical seven-coordinate weave:
[
s_u(D,E)=0,qquad s_u(E,F)=1
]
closes NOR for the companion order ending in (u).

No theorem presently transports the same seven-coordinate front block to an arbitrary later suffix gap while preserving all intermediate suffix coordinates and the left boundary data. The Article III strategy broadcast explicitly lists this propagation as open.

Therefore the deduction
[
	ext{no }01	ext{ anywhere}quadLongrightarrowquad s_u=1^*0^*
]
is not yet justified.

What is globally proved is weaker but genuine: for every residual coordinate (u), deleting (u) from its companion seven-weave leaves a protected front block of word (0,1,1,1). Inserting (u) at an arbitrary later suffix gap with scan triple
[
s_u(j-1)s_u(j)s_u(j+1)=101
]
creates packet (111) and hence a spanning one-change order. Thus every residual scan is globally (101)-free.

The parity conclusion for hypothetical single-step drop ranks remains valid conditional on the missing propagation lemma, but it should not be used unconditionally.

Current boundary-surgery target: either prove a translated companion weave that excludes arbitrary (01) rises while retaining the whole intervening suffix, or work directly with the weaker (101)-free scans and Klein-four first-return packets.
