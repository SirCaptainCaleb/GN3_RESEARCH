# Entrance-side returns with an entrance terminal-path contact have sublinear total mass

## Statement

Let H be a finite linear 3-graph, S=sum_v phi(v), n_+=|{v:phi(v)>0}|, with fixed maximum endpoint paths P_v. At each center v let F_v be a distinct-edge family of ascending nonspecial edges e={x,v,u}, of rank r<min(phi(v),phi(u)), terminal-single on both P_v and P_u. Assume F_v has one common anchor of rank q_v<=phi(v), containing both x,u for every member, with r<=q_v and clean maximum sources.

Let B_v consist of members satisfying the one-sided host-block condition of the rank-spread lemma at this anchor and for which at least one of P_v,P_u has entrance contact x (rather than opposite-terminal contact). Put M=sum_v |B_v|. Then
M <= 6 n_+ + sqrt(36 n_+^2 + 864 n_+ S).
Consequently M=o(S) whenever S/n_+ tends to infinity.

Applied to the selected strict-gap families, this eliminates o(S)-scale entrance-side equal-exchange/order-inversion incidences with at least one entrance contact. Any surviving Omega(S) selected incidence mass must have a terminal-side return or opposite-terminal contacts on both terminal paths. No better leading coefficient is asserted.

## Body

Write p_v=phi(v), and Delta_v=sum_{e in B_v}(q_v-r_e). The rank-spread lemma gives
Delta_v >= |B_v|^2/24-|B_v|/2.

Take the union E of the underlying edges in all B_v. Each edge can have certificates at only its two terminals. At each terminal t, deduplicate edges of E incident with t. Terminal-singleness makes their path contact either the entrance x or the other terminal w. The rotation lemma gives budgets
X_t=sum_{entrance contacts at t}(p_t-r_e) <=12p_t,
U_t=sum_{opposite-terminal contacts at t}(p_t-p_w)_+ <=12p_t.
These are subfamilies of a single contact-drop budget, but the separate coarse bounds suffice.

Charge a certified incidence (v,e) as follows. If its contact at v is x, then q_v-r_e<=p_v-r_e and charge its X_v term. Otherwise its contact is u, and by membership in B_v the contact at u is x. Then
q_v-r_e <= p_v-r_e <= (p_v-p_u)_+ +(p_u-r_e);
charge the U_v term and the X_u term. For a fixed edge and an entrance-contact terminal, that X term is charged at most twice: once by its own certified center, and once by the other center. Each U term is charged at most once. Hence
sum_v Delta_v <= 2 sum_t X_t + sum_t U_t <=36S.
No certificate is transferred; these are numerical charges, not assertions of payment at another terminal.

Summing the quadratic bounds gives
sum_v |B_v|^2 <=864S+12M.
Cauchy-Schwarz over the n_+ possible centers yields
M^2<=n_+(864S+12M).
Solving the quadratic proves the displayed estimate. Since S/n_+ tends to infinity, both n_+/S and sqrt(n_+S)/S vanish.

For the selected families, the original-certificate extraction supplies total center-incidence mass at least S/8-o(S), and its anchor data and two-terminal single contacts are retained. The entrance-side branches of the established trichotomy satisfy the host-block condition, so the estimate removes their incidences with an entrance contact. The remaining disjunction is terminal-side returns or two opposite-terminal contacts; these branches can overlap. The argument does not show either remaining branch has o(S) mass and therefore does not close 43/48.