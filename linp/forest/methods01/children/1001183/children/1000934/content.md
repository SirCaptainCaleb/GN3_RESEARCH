# Type-A vertices source only ascending nonspecial edges and have an exact degree decomposition

## Statement

Let v have p=phi(v)>=3 and Type-A local slack
  a(v)=2, b(v)=0.
Let c(v) be the number of ascending nonspecial edges whose unique entrance is v. Then every nonspecial edge whose unique entrance is v is ascending, and
  d_H(v)=2p-1+c(v).

Equivalently, the incident edges at v split exactly into:
- 2p-1 snake-incoming edges (four special and 2p-5 nonspecial terminal edges);
- c(v) ascending nonspecial source edges.
There are no additional nonascending nonspecial source edges.

## Body

Type A gives
  d_D^-(v)=2p-1.
These 2p-1 snake-incoming hyperedges are all distinct incident edges at v.

By the certified local ascending-edge inequality 22362096041e,
  d_H(v)-c(v)<=2p-1.
Since the 2p-1 snake-incoming edges are not counted by c(v), we already have
  d_H(v)-c(v)>=2p-1.
Hence equality holds:
  d_H(v)-c(v)=2p-1.

If a nonspecial edge e had unique entrance v but were nonascending, then it would be incident at v, not snake-incoming there, and not counted by c(v). It would therefore contribute an additional edge to d_H(v)-c(v) beyond the 2p-1 incoming edges, contradicting equality. Thus every nonspecial source edge at v is ascending.

The exact degree decomposition follows.