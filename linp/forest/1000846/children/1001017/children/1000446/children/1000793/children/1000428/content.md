# Ascending sources are exactly the one-step incidence rank defects

## Statement

Let H be a finite linear 3-graph and let v be a vertex with endpoint potential phi(v)=p. For every incident hyperedge e,
  phi(e)<=p+1.
Furthermore,
  phi(e)=p+1
if and only if e is nonspecial ascending and v is its unique entrance.

Equivalently, every special incidence and every nonspecial terminal or nonascending-entrance incidence satisfies phi(e)<=phi(v); the only incidence with phi(e)>phi(v) is an ascending entrance, and then the gap is exactly one.

## Body

Let e be incident with v and write q=phi(e).

If e is special, then every vertex of e is a snake terminal, hence v is the last vertex of some q-edge path ending in e. Therefore phi(v)>=q.

If e is nonspecial with unique entrance x and two terminals, then at each terminal w one has phi(w)>=q, while at the entrance x deleting e from a longest q-edge path gives phi(x)>=q-1.

Thus at any incidence q<=phi(v)+1. Equality q=phi(v)+1 can occur only when v is the unique entrance of a nonspecial edge, and then phi(v)=q-1, exactly the definition of ascending. Conversely, if e is ascending with entrance v then q=phi(v)+1 by definition.
