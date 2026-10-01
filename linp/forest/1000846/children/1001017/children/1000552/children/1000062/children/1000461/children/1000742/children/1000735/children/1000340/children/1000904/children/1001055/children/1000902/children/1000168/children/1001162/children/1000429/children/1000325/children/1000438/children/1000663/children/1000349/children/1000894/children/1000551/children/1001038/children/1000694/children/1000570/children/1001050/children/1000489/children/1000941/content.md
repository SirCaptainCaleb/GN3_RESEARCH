# Opposite singleton-contact types have rank sum p plus three only with a superlevel output

## Statement


Let P=(g_1,...,g_p) be a maximum p-edge path with last vertex v. Let e and f be distinct selected ascending nonspecial edges terminal at v, neither equal to g_p, each having exactly one off-v contact with V(P)\g_p.

Assume the contact of one edge is its unique entrance and the contact of the other edge is its opposite terminal. Then
  phi(e)+phi(f) >= p+3.

Moreover, if
  phi(e)+phi(f)=p+3,
then one of the standard rotation-output edges associated with the two selected contacts has all three vertices of vertex rank at least p.

Consequently, in any selected family in which no such superlevel rotation output is allowed, every opposite-type pair satisfies
  phi(e)+phi(f) >= p+4.


## Body


If the two contact intervals are disjoint, e9fc907b07c9 gives the stronger bound
  phi(e)+phi(f)>=p+4.

If the contact intervals overlap, 6bea6cbb3741 gives
  phi(e)+phi(f)>=p+3.
That lemma also classifies equality. In each equality configuration, because both incidences are selected by the D+Y injection, a nearby standard rotation-output edge lies entirely in
  V_p={w:phi(w)>=p}.

This proves both assertions.
