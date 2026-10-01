# Post-43/48 proof rehearsal: paid strict-gap local congestion

## Statement

Suppose the current 43/48 leading coefficient cannot be improved. Then there is a sequence with
  m_j >= (43/48-o(1))S_j.
The exact rank-sensitive theorem a57007500001 forces n_j^+/S_j -> 0, hence S_j/n_j^+ -> infinity. The certified extraction 9fba15f1495c then yields a set Epp of distinct source-clean, doubly-terminal-single, paid-certified ascending nonspecial edges with
  |Epp| >= (1/16-o(1))S_j,
such that every edge has edge rank strictly below both terminal vertex ranks.

Assign each edge of Epp to a terminal of minimum vertex rank. The current end-to-end proof closes if there is a function g(p)=o(p) such that every rank-p vertex receives at most g(p) assigned edges from this class. Indeed 7e6abf77cbc5 then gives |Epp|<=sum_v g(phi(v))=o(S_j), a contradiction.

Thus the first unsupported inference in the current proof organization is exactly the sublinear local congestion bound g(p)=o(p) for minimum-terminal assignments inside the paid-certified source-clean doubly-terminal-single strict-two-terminal-gap class.

## Body

Proof rehearsal.

1. Forcing the large-rank regime.

The exact theorem a57007500001 gives
  6m <= sum_v [4p_v-2+beta(p_v)],
where p_v=phi(v). Its listed small-p values and the formula
  beta(p)=floor((11p-16)/8)  for p>=7
imply, for every positive integer p,
  4p-2+beta(p) <= (43/8)p-27/8.
(The minimum gap is 27/8 at p=1; for p>=7 the gap is at least 4.)
Hence
  6m <= (43/8)S-(27/8)n_+.
Therefore any sequence satisfying
  m >= (43/48-o(1))S
necessarily has n_+/S -> 0, equivalently S/n_+ -> infinity. Thus the large-rank hypothesis used by the near-extremal stability lemmas is automatic in any sequence witnessing saturation of the 43/48 slope.

2. Certified strict-two-terminal-gap extraction.

The load-bearing chain through d287da5967d5, e6137a4bc902, and 619d7583671c is current and certified. In its compressed certified form, 9fba15f1495c gives a set Epp of distinct ascending nonspecial edges with
  |Epp| >= (1/16-o(1))S,
such that every e={x,u,v} in Epp is source-clean at its unique entrance, terminal-single on the chosen maximum endpoint paths at both terminals, paid-certified at at least one terminal, and satisfies
  phi(e)<phi(u),  phi(e)<phi(v).

The factor 1/16 comes from at least (1/8-o(1))S good center-edge incidences followed by quotienting by the underlying edge, which can be selected at no more than its two terminal vertices.

3. Final conditional summation.

Assign each e={x,u,v} in Epp to a terminal of minimum vertex rank, breaking ties arbitrarily. If e is assigned to v and p=phi(v), then
  phi(e)<p
and the other terminal u has phi(u)>=p.

Assume there is a universal function g(p)=o(p) bounding, at every rank-p vertex, the number of assigned edges having exactly these inherited properties. Then
  |Epp| <= sum_v g(phi(v)).
For any epsilon>0 choose P with g(p)<=epsilon p for p>=P and put
  M=max_{1<=p<P}g(p).
Then
  sum_v g(phi(v)) <= M n_+ + epsilon S = o(S)+epsilon S.
Since epsilon is arbitrary,
  sum_v g(phi(v))=o(S),
contradicting |Epp| >= (1/16-o(1))S.

This is precisely the certified reduction 7e6abf77cbc5.

4. First unsupported inference.

The proof now stops at the following local statement:

  There exists g(p)=o(p) such that, for every relevant choice of the maximum endpoint paths, every rank-p vertex v is the minimum-rank terminal of at most g(p) source-clean, doubly-terminal-single, paid-certified ascending nonspecial edges e whose edge rank is strictly below both terminal vertex ranks.

No current certified result proves this. In particular, the newer two-tier packet lemma 59c5795520ff, even if audited successfully, supplies expansion/rank mass for a size-k local family but does not by itself bound k sublinearly in p without a further reuse or packing inequality.

Thus the earlier rehearsal gap at generic center-indexed paid-object congestion has moved strictly downstream. The current first unsupported inference is the sublinear minimum-terminal congestion bound on the paid strict-two-terminal-gap subclass. An O(log p) bound would already suffice; a constant bound is unnecessary.
