# Failed-splice exchange is naturally a bounded clause system, not a graph

## Statement

Proposal: model obstruction-augmented exchange by bounded disjunctive transition clauses rather than by adding ordinary failure edges. A clause records that if one attempted splice fails, boundary antisymmetry and the no-two-cover hypothesis force at least one of a bounded list of reverse cross triples or alternative repartitions. Successful splice edges remain ordinary transitions. The target is an augmenting-clause theorem: every closed family of unresolved clauses either contains a consistent sequence of checked repartitions reaching a two-cover or forces incompatible orientation requirements.

## Body

The certified one-split double-pivot theorem gives the first exact template. Two failed-insertion pivots on the two paths of one deletion cover do not yield a single alternative move; instead they force two clauses C1 and C2, each asserting that at least one of three explicit cross triples is tight. This is precisely the information lost by an ordinary endpoint-to-cut graph. The redesign should therefore preserve the disjunction until another obstruction or deletion state resolves it. A useful next lemma would show that two or three overlapping clauses sharing the omitted label cannot remain simultaneously unresolved without yielding an order-disagreement witness or a checked repartition.