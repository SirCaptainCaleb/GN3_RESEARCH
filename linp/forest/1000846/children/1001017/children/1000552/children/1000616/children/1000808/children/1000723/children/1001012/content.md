# Pure rank-five at potential five forces a multi-precursor competitor

## Statement

Assume phi(v)=5 and four potential-charged ascending nonspecial rank-five edges are terminal at v. Fix one as e4 and a five-edge path
  P=(g1,g2,g3,g4,e4)
ending in e4 with physical terminal v.

Let f be one of the other three competitors.

If f meets exactly one precursor path edge among g1,g2,g3,g4, then that edge is either g2 or g4, and the contact vertex is the private vertex of that path edge. If the unique precursor edge is g4, that private vertex is the unique entrance of f.

Consequently at most two of the three competitors can meet exactly one precursor path edge, and therefore at least one competitor meets at least two precursor path edges.

## Body

Suppose f meets exactly one precursor path edge g_j. Together with the final edge e4, f therefore meets exactly two path edges of P. Apply the certified two-contact competitor theorem 0a5cb0d55cbd with p=5. It gives either
  j=4
or
  j<=2.

The terminal-tail blocker lemma for the rank-five edge f forces one of its non-v vertices into the final three precursor edges g2∪g3∪g4. Since f meets exactly one precursor path edge, j cannot be 1. Therefore j∈{2,4}.

If j=2, the contact cannot be either joint of g2: a contact at g1∩g2 would also meet g1, and a contact at g2∩g3 would also meet g3. Hence it is the private vertex of g2.

If j=4, similarly the contact cannot be g3∩g4 because that would also meet g3. It cannot be g4∩e4 because f and e4 already share v and linearity forbids a second common vertex. Hence it is the private vertex of g4.

Finally, in the j=4 case, if the private g4 contact were the opposite terminal of f rather than its entrance, then
  (g1,g2,g3,g4,f)
would be a five-edge linear path ending in the nonspecial rank-five edge f through a terminal rather than its unique entrance. Thus the private g4 contact is the entrance.

Distinct competitors through v have pairwise disjoint non-v pairs, so at most one competitor can use private(g2) and at most one can use private(g4). With three competitors total, at least one meets at least two precursor path edges.
