# Every compatible connector decomposes into at most three fully ported shore zero paths — preserved pre-item development

## Development

## Canonical ported shore-block decomposition of arbitrary compatible connectors

Fix the flat normalized split z→A→x and z→x, with α(u,v,w)=t(u,v)+t(v,w)+t(w,u) modulo 2. Let C be any compatible zero connector on R∪{x,z}, R⊆A. Delete x,z from its written order, retaining the maximal contiguous shore blocks P_1,...,P_k that were separated by special coordinates (discard empty blocks).

THEOREM. We have k≤3, and EACH nonempty shore block P_i is a fully ported zero path: it has color zero on each consecutive triple and its first/last ordered pair is forward whenever that pair is defined. In particular, every compatible connector induces an actual ordered, ported cover of its shore by at most three zero paths, even when x,z move independently.

PROOF. Every internal ternary window is inherited from C and has color 0. Let (u,v) be the first pair of one shore block of length≥2. If it is the first pair of C, u→v is its required initial compatible port. Otherwise its immediate predecessor is x or z, and the zero window (s,u,v) gives 0=α(s,u,v)=1−t(u,v), because both special vertices have uniform orientation toward shore (z→shore→x); thus u→v. Similarly, if (u,v) is the final pair of a shore block, either it is the final pair of C, which is compatible, or its successor is x or z, so α(u,v,s)=1−t(u,v)=0, and u→v. Singleton blocks satisfy the port condition vacuously. There are two special coordinates, so at most three maximal shore blocks.

The middle shore block of a separated-special connector is nonempty. If it is a singleton u, the special order must be z,u,x because α(x,u,z)=1 whereas α(z,u,x)=0. Therefore an x-before-z separation forces a middle block of length at least two.

COROLLARY (actual three-path deletion witnesses). In an inclusion-minimal shore A obstructing a spanning compatible connector, every deletion A\{a} has a compatible connector by minimality, and hence an actual fully ported zero-path cover by k≤3 shore blocks. If k=1, §50 immediately closes the original shore via P,x,z,a. If k=2 and one of its paths is a singleton {u}, the forward order of {u,a} and the other path are two disjoint fully ported zero paths covering A, hence close by P,x,z,Q. Consequently, all deletion witnesses in an unresolved minimal obstruction have either exactly two shore blocks EACH of size at least two, or exactly three shore blocks. If x and z are adjacent, there are at most two shore blocks; with the special pair at an end there is only one and closure follows.

This result extracts the ported path certificates directly from deletion-critical compatible connectors. It does not assert coherent selection across deletions or merging of three blocks; these are the remaining augmentation obligations.

EXACT SEPARATED-SPECIAL BRIDGE LAW. If C has separated special coordinates and three nonempty shore blocks, write C=(P,s,Q,t,R), {s,t}={x,z}. Set p=last(P), q=first(Q), q'=last(Q), r=first(R). The two mixed zero windows force q→p and r→q', because for either s∈{x,z} and shore u,v one has α(u,s,v)=t(u,v). Conversely these two directed backward cross-edges are exactly the one-shore-on-each-side mixed-window requirements; remaining mixed windows are governed by the forward exposed ports of the individual blocks (plus the forbidden singleton x,Q,z configuration). This enriches the extracted three-path certificate with two witnessed reverse bridges, a plausible exchange target rather than mere arbitrary path-cover data.
