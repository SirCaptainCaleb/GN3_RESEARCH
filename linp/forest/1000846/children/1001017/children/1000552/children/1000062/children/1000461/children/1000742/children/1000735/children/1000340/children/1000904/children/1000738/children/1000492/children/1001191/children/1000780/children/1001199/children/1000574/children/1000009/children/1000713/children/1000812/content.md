# Only doubly terminal-single ascending edges can contribute positively to A-X

## Statement

Fix arbitrary maximum endpoint paths P_v at all nonisolated vertices in a finite linear 3-graph, and let X be total excess contact multiplicity. Let U_11 be the number of ascending nonspecial edges e={x,u,v} for which both terminal incidences satisfy mu_u(e)=mu_v(e)=1. Then A-X<=U_11. Moreover, if e has rank q and belongs to U_11, then phi(u),phi(v)<=2q-2. If phi(v)=2q-2, the unique off-v contact of e on P_v must be the entrance x; the opposite terminal u is absent from P_v. The same holds symmetrically at u.

## Body

Decompose A-X edgewise over ascending edges, ignoring excess multiplicity contributed by nonascending edges since it only decreases A-X. An ascending edge contributes one unit to A. If either terminal incidence has multiplicity at least two, then that terminal contributes at least one unit to X, so the net edge contribution is at most zero. Therefore only edges with both terminal multiplicities equal to one can contribute positively, proving A-X<=U_11. Let e={x,u,v} in U_11 have rank q and put p=phi(v). Because v is a terminal of the nonspecial ascending edge e, e cannot be the last edge of a maximum p-edge path ending at v: such a path would make v a longest-path entrance of e. Hence mu_v(e)=1 is an actual single off-v contact on P_v. The corrected singleton-contact lemma 028c2c3f7167 gives p<=2q-2. If p=2q-2, its terminal-only singleton alternative is impossible, so the sole contact is the entrance x. Apply the same argument at u.