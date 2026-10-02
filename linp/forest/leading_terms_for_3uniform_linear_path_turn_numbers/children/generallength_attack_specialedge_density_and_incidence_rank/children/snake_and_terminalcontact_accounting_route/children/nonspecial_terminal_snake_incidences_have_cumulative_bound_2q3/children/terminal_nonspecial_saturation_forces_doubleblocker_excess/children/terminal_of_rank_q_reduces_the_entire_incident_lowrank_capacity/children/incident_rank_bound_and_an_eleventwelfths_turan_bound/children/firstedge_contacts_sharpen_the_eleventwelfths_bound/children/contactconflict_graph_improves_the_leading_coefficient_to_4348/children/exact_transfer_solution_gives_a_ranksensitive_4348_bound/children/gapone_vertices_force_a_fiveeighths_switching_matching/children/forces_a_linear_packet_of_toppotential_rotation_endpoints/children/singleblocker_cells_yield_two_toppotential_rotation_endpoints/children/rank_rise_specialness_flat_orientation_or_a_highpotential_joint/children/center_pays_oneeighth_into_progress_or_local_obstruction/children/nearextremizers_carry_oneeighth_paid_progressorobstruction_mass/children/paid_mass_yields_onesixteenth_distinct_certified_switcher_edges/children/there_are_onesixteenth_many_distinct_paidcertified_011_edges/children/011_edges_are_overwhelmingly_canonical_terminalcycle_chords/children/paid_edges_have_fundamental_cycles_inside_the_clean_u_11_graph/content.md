# Paid edges have fundamental cycles inside the clean U_11 graph

## Statement

Under the 43/48 near-extremal hypotheses, let J be the terminal graph consisting only of ascending nonspecial hyperedges that are source-clean on the chosen source path and terminal-single on both chosen terminal endpoint paths. Weight each edge of J by its hyperedge rank and choose, in every component of J, a spanning tree of maximum total rank; let F be their union.

Then there is a set E_clean-cyc of distinct paid-certified edges with
  |E_clean-cyc| >= (1/16-o(1))S
such that every e in E_clean-cyc is a nonforest edge of F. Consequently its fundamental cycle C_e is entirely contained in the source-clean U_11 graph J, e has minimum rank on C_e, and at each terminal of e the adjacent cycle edge has rank at least phi(e) and forces e to make an additional blocker contact with every corresponding maximum-rank terminal witness.

Thus a linear-sized family of paid-certified edges has canonical fundamental cycles all of whose edges remain inside the rigid source-clean, doubly-terminal-single ascending class.

## Body

By 7ac951de82f4, the graph J contains a set E_paid of distinct paid-certified edges with
  |E_paid| >= (1/16-o(1))S.                            (1)

The spanning forest F has at most n_+-1 edges in total. Since S/n_+ -> infinity,
  |E_paid intersect F| <= n_+ = o(S).
Delete those edges and set
  E_clean-cyc=E_paid minus F.
Then (1) gives
  |E_clean-cyc| >= (1/16-o(1))S.                      (2)

Fix e in E_clean-cyc. Its fundamental cycle C_e lies wholly in J by construction. If some tree edge g on C_e had rank smaller than e, exchanging g for e would increase the total rank of the spanning tree in that component, contradicting maximality. Hence e is minimum-rank on C_e.

Let g be either of the two cycle neighbors of e, sharing terminal vertex w with e. Then
  phi(g)>=phi(e).
Both hyperedges are nonspecial and w is terminal for both. Apply the certified terminal-adjacency blocker lemma 94c19ac52776 in the direction from a longest g-ending path with last vertex w toward e. If e met that path only in w, appending e would force
  phi(e)>=phi(g)+1,
contrary to phi(e)<=phi(g). Therefore e has an additional contact with that witness path. The same argument applies independently at the other terminal of e.

Because every edge of C_e belongs to J, all cycle edges are ascending, source-clean, and terminal-single at both chosen terminal paths. This gives the strengthened clean-cycle certificate.