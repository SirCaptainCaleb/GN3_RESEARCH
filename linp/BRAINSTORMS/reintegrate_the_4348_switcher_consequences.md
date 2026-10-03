# Reintegrate the 43/48 switcher consequences

Reconstruct the dependency chain and terminology for the two route-local near-equality consequences formerly published in Toolkit Limbo, then integrate any surviving mathematics into the 43/48 route.

These two results are route-local consequences of the 43/48 near-equality machinery rather than broadly reusable infrastructure. Their old bodies also cite legacy research IDs that are no longer present in the live corpus, so they are preserved here for reintegration rather than promoted or treated as current standalone Toolkit claims.

=== Local one-eighth extraction ===
Statement:\nLet (H_j) satisfy
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

Body:
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

=== Host-order lower bound for low-cost switcher states ===
Statement:\nLet H be a finite linear 3-graph on n vertices and let v be an active misaligned vertex with p=phi(v). Suppose v is low-defect and its switcher-family source-potential mass is within o(p^2) of the generic 185/512 p^2 floor, in the asymptotic regime p->infinity.

Then
  n >= (127/56-o(1))p.

More explicitly, if U_v is the terminal-retained part of a switcher family and k=|U_v|, then
  n >= 2p+1+k.
Hence any estimate k>=(15/56-epsilon)p gives
  n >= (127/56-epsilon)p+1.

Therefore for every fixed epsilon>0, a sequence with
  n <= (127/56-epsilon)p
cannot realize the locally cheap post-43/48 switcher state at a vertex v with p=phi(v); such a center must instead pay a fixed positive quadratic gain in switcher-source potential over the generic 185/512 floor.

Body:
Let P be the chosen maximum p-edge path ending at v. A linear 3-uniform p-edge path has exactly
  |V(P)|=2p+1
vertices.

Every terminal-retained switcher e={x,v,u} has its unique entrance x omitted from P by definition. Distinct switchers through v have distinct entrances: two distinct hyperedges already share v, so sharing an entrance x would violate linearity. Thus the k terminal-retained switchers supply k distinct vertices outside V(P). Consequently
  n>=|V(P)|+k=2p+1+k.                                  (1)

Now assume the local switcher-source mass is within o(p^2) of the generic 185/512 p^2 floor. By 1bab77ec4e49,
  k >= (15/56-o(1))p.                                  (2)
Substituting (2) into (1),
  n >= 2p+1+(15/56-o(1))p
    = (127/56-o(1))p.

For the final contrapositive, fix epsilon>0. If n<=(127/56-epsilon)p for all sufficiently large p, then (1) implies
  k <= (15/56-epsilon)p+O(1).
Since the total switcher-family size is (5/8-o(1))p at a low-defect center, this places k a fixed positive fraction below the three-sevenths threshold of 1bab77ec4e49. That theorem then gives a fixed positive quadratic source-potential gain over 185/512 p^2.
