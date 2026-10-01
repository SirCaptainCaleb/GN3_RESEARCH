# Maximum ascending-terminal rank is nondecreasing across a maximum-rank terminal edge

## Statement

For a vertex v incident with at least one ascending edge at which v is terminal, let q(v) be the maximum edge rank among such edges. Let e={x,v,u} be an ascending edge of rank q(v), where x is its unique entrance and u is the other terminal vertex. Then q(u)>=q(v). Consequently, writing Delta(w)=phi(w)-q(w) at active vertices, if phi(u)<phi(v) then Delta(u)<Delta(v). In particular, in any directed graph obtained by choosing at each active vertex v one rank-q(v) ascending edge and directing v to one of its other terminal vertices, q is nondecreasing along every directed edge and is constant on every directed cycle.

## Body

The edge e is ascending and nonspecial, with unique entrance x. Since v is terminal at e and e has three vertices, its third vertex u is also terminal at e. The same edge e is therefore an ascending edge terminal at u. By the definition of q(u) as the maximum rank of an ascending edge terminal at u,
q(u)>=phi(e)=q(v).

Now suppose phi(u)<phi(v). Since q(u)>=q(v),
Delta(u)=phi(u)-q(u)<=phi(u)-q(v)<phi(v)-q(v)=Delta(v).

For the directed-graph statement, every chosen arc v->u satisfies q(u)>=q(v). Along a directed cycle these inequalities return to the starting vertex, so all are equalities and q is constant around the cycle.
