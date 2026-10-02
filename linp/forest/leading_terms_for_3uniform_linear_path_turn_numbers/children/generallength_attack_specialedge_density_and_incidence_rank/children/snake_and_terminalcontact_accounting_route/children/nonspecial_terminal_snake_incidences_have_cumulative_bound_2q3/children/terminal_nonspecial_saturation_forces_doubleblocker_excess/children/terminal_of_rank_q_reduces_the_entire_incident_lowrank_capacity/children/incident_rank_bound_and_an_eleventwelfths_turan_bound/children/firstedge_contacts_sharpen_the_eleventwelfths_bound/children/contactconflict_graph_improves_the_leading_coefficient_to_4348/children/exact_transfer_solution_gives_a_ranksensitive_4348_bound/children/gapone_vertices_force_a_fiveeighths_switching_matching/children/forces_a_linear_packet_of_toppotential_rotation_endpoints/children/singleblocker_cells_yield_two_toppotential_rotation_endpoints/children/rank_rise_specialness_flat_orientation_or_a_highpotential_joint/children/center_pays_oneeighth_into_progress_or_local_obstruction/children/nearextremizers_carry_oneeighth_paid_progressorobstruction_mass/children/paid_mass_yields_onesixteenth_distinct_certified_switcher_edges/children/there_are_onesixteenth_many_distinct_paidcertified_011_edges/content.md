# Near 43/48 there are one-sixteenth many distinct paid-certified 0-1-1 edges

## Statement

Under the 43/48 near-extremal hypotheses, there are at least (1/16-o(1))S distinct ascending nonspecial edges that simultaneously (i) are source-clean on the chosen maximum path at their unique entrance, (ii) have contact multiplicity one on the chosen maximum endpoint path at each of their two terminals, and (iii) carry a paid-cell switching certificate at at least one terminal in the sense of c8d14f7306ab and 9586a4d2317f.

## Body

Start with the distinct certified switcher set E_cert from c8d14f7306ab, for which |E_cert|>=(1/16-o(1))S. By 420e9aea15cc, the number of ascending edges that are not terminal-single at both terminals is at most D=o(S). Hence deleting from E_cert all edges that fail either terminal-single condition removes only o(S) edges. For source cleanliness, in the exact identity of a57007500001, C counts the multiplicity-zero incidences; every such incidence is the unique entrance incidence of an ascending edge, and an ascending edge has at most one such source incidence. Thus C is the number of ascending edges whose chosen source path is clean, so A-C=o(S) means that only o(S) ascending edges fail source cleanliness. Delete these as well. The remaining family still has size (1/16-o(1))S, and every member retains its paid-cell certificate because the cleaning only discards edges, not certificates on surviving edges.