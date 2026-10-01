# One-sixteenth of near-extremal potential mass lies on distinct edges with strict rank-ascent certificates

## Statement

Under the 43/48 near-extremal hypotheses of c8d14f7306ab, there is a set E_asc of distinct ascending nonspecial edges with |E_asc| >= (1/16-o(1))S such that for every f in E_asc there exist a terminal center v, p=phi(v), an interior switching cell of the chosen maximum p-edge path P_v containing the unique off-v contact of f, and a host output edge h on P_v for which phi(f)<p<=phi(h). Moreover the standard single-blocker rotation is a p-edge linear path ending in h and containing f. Thus every f in E_asc comes with an explicit strict edge-rank ascent witness f -> h.

## Body

Use the selected center-switcher incidences constructed in c8d14f7306ab. Each selected incidence (v,f) comes from the switching family F_v of b032348c1a8a at an active misaligned center v. Put p=phi(v) and q=q(v). By misalignment q<p, while every f in F_v has edge rank phi(f)<=q; hence phi(f)<p. The selected incidence belongs to an occupied interior cell C_i of the chosen maximum p-edge path P_v. Let h=g_{i+2} be the standard rotation-output edge. The rotation-output theorem 6205fe95ecf8 gives phi(h)>=p, and its displayed standard rotation is a p-edge linear path ending in h that contains f. Therefore phi(f)<p<=phi(h), so this certificate is a strict rank ascent. Finally c8d14f7306ab selects at least (1/8-o(1))S center-switcher incidences and uses that each underlying ascending edge has only two terminal centers to extract at least (1/16-o(1))S distinct underlying switchers. Choose one of the selected incidences for each such underlying edge. The associated output h supplies the asserted strict rank-ascent certificate.
