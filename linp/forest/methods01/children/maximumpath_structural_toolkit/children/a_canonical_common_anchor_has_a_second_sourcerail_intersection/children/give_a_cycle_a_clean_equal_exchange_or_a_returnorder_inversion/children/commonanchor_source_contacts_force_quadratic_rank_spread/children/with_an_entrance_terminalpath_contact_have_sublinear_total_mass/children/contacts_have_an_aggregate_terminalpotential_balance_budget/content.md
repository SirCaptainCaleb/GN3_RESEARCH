# Two-opposite-terminal contacts have an aggregate terminal-potential balance budget

## Statement

In the fixed maximum-path setting, let E be a set of distinct ascending nonspecial strict-gap edges e={x,u,v}, terminal-single at both terminals, with the contact at u equal to v and the contact at v equal to u. Then
sum_{e in E}|phi(u)-phi(v)|<=12S.
For certificate-centered incidences supported on E, each edge occurring at at most two centers, the number having |phi(u)-phi(v)|>=epsilon phi(center) is o(S) for every fixed epsilon>0, whenever S/n_+ tends to infinity. Thus the two-opposite-terminal-contact residual is asymptotically balanced in terminal potentials in the incidence-count sense.

## Body

At terminal v each edge has path contact u. Sum the rotation contact-drop bound over all terminals, with E deduplicated at each terminal. Each edge contributes exactly (p_v-p_u)_+ +(p_u-p_v)_+=|p_v-p_u|. Hence the first bound is 12S. Center-incidence multiplicity at most two gives a total absolute-difference budget at most 24S over certificate-centered incidences.

The same one-contact families have degree <=2p_v+1: their non-v contacts are distinct vertices on a p_v-edge linear path. Thus centers of potential <=K support at most (2K+1)n_+ incidences. Among centers of potential >K, every epsilon-imbalanced incidence contributes at least epsilon K to the absolute-difference budget, so there are at most 24S/(epsilon K). The total bad count is at most (2K+1)n_++24S/(epsilon K). Taking K approximately sqrt(S/n_+) proves o(S) for fixed epsilon. The conclusion concerns incidence counts, not total endpoint-potential mass, and does not bound edge-rank deficits p-r.