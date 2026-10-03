# Local one-eighth 0-1-1 extraction with source and terminal conditions

**Summary:** Local one-eighth 0-1-1 extraction with explicit source and terminal conditions.

## Statement

Let (H_j) satisfy
  S_j=sum_v phi(v),  S_j/n_j^+ -> infinity,
  |E(H_j)| >= (43/48)S_j-o(S_j),
and choose maximum endpoint paths as in a57007500001.

Then for each vertex v one may choose a family G_v of ascending nonspecial edges terminal at v such that every f in G_v:
(1) belongs to the common maximum-path switcher family at v supplied by f3588b3a3bc7;
(2) carries at v one selected D+Y certificate from the certificate-count theorem;
(3) is satisfies the source condition at its unique entrance;
(4) is terminal-single on the chosen maximum endpoint paths at both terminals.

Writing p_v=phi(v),
  sum_v (p_v/8-|G_v|)_+ = o(S_j).

Consequently, for every fixed epsilon>0, the total endpoint-potential mass of vertices satisfying
  |G_v| < (1/8-epsilon)p_v
is o(S_j).

Thus the local one-eighth certified 0-1-1 degree survives without any endpoint-intersection premise, and every retained edge also carries the genuine common-reference switcher structure.

## Body

Use the exact four-defect identity of a57007500001:
  6m = sum_v(4p_v-2+beta(p_v))
       -D-eta-2(A-C)-2U.
Since
  sum_v(4p_v-2+beta(p_v)) <= (43/8)S+O(n_+),
the near-equality hypotheses imply
  D=o(S),  eta=o(S),  A-C=o(S),  U=o(S).              (1)

By the endpoint-intersection stability theorem 223efeb00c7b, inactive and aligned vertices carry only o(S) endpoint-potential mass. Bounded-p vertices contribute O(n_+)=o(S).

Fix an active misaligned vertex v of sufficiently large p_v. Apply 614c7d2d181a to its common maximum-path switcher family. Its D+Y counting proof permits an injection of the D_v^case+Y_v units into distinct center-switcher incidences (v,f): a singly occupied certified case contributes its unique switcher; a double uncertified case contributes one of its two switchers; a double certified case contributes both switchers, one for each D/Y unit. Let J_v be the resulting selected switchers. Then
  |J_v|>=p_v/8-eta_v-O(1).                             (2)

Now delete from every J_v each underlying edge that fails either global good condition: the source condition at its unique entrance, or the terminal-single condition at one of its two terminals. Let b_v be the number deleted.

There are exactly A-C failing the source condition ascending edges. Also, if an ascending edge fails the terminal-single condition at one of its two terminal endpoint paths, that terminal incidence has contact multiplicity at least two and therefore contributes at least one unit to D. Hence at most D ascending edges fail terminal-single at some terminal.

An ascending edge has exactly two terminals, so it can occur in center-indexed J_v for at most two centers. Therefore
  sum_v b_v <= 2[(A-C)+D]=o(S).                        (3)

Put G_v=J_v minus the deleted edges on active misaligned large-p vertices and G_v=empty elsewhere. From (2),
  (p_v/8-|G_v|)_+ <= eta_v+O(1)+b_v
on the active misaligned large-p set. Summing and using (1), (3), n_+=o(S), and the o(S) potential mass of the discarded inactive/aligned/bounded-p vertices proves
  sum_v(p_v/8-|G_v|)_+=o(S).

The epsilon consequence follows because every vertex with
  |G_v|<(1/8-epsilon)p_v
contributes at least epsilon p_v to the positive-part sum.

## Metadata

- ID: local_oneeighth_011_extraction_with_source_and_terminal_conditions
- Kind: toolkit
- Version: 3
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Toolkit status: Limbo
