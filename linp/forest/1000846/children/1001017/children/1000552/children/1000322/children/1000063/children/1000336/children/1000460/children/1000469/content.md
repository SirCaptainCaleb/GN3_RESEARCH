# A terminal-clean boundary transfer closes a q-cycle

## Statement

In the setting of 5ca3b62fde96, suppose the transfer alternative occurs through terminal y: the deficiency-two path is R=(g_2,...,g_{q-1}) and f is an edge through b_2 and y that is clean relative to R. Then g_2,g_3,...,g_{q-1},e,f is a linear cycle of length q. If moreover f is nonspecial ascending of rank q, then e and f are equal-rank terminal-adjacent ascending edges, and on the (q-1)-edge path g_2,...,g_{q-1},e the edge f has exactly two contacts, b_2 in the first edge and y in the last edge. Thus f realizes equality in the terminal successive-contact separation bound.

## Body

The path R is linear and avoids y,z. The edge e meets R only in x, which lies in g_{q-1}; the transfer edge f meets R only in b_2, which lies in g_2, and meets e in y. Hence the cyclic order g_2,...,g_{q-1},e,f has exactly the required consecutive intersections and no nonconsecutive intersections. It has (q-2)+2=q edges. If f is ascending nonspecial of rank q, 321866bdcbef shows y is terminal for f. Since f is clean relative to R, its only contacts with the path g_2,...,g_{q-1},e are b_2 at the first edge and y at the last; their edge-index separation is q-2, attaining the terminal-contact bound e7315cdd5c63.
