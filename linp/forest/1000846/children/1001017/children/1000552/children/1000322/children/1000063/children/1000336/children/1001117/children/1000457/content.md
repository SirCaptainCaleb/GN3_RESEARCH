# Unsafe clean terminal branches are special or do not drop rank

## Statement

Let e={x,y,z} be an ascending nonspecial edge of rank q, and let P=(p_1,...,p_{q-2}) be an x-ending path avoiding y,z. Let a be an opposite last vertex of p_1. Suppose f_y is an edge through a and y that is clean relative to P, meaning f_y meets V(P) only at a. Then phi(f_y)>=q-1. Moreover there are (q-1)-edge paths ending in f_y with two distinct entrance labels a and y. Consequently either f_y is special or phi(f_y)>=q. The analogous statement holds for a clean z-edge.

## Body

Reverse P and append f_y through a. This gives the (q-1)-edge linear path p_{q-2},...,p_1,f_y ending in f_y and entering f_y through a, so phi(f_y)>=q-1. For the second witness, delete p_1 from P, retain p_2,...,p_{q-2}, append e through x, then append f_y through y. This sequence has (q-3)+2=q-1 edges. It is linear: P avoids y,z; f_y is clean relative to P and its only P-contact a lies in the omitted p_1; e meets the retained P only at the terminal x in p_{q-2}; and e meets f_y at y. Thus it ends in f_y with entrance y. If phi(f_y)=q-1, these are two longest paths ending in f_y with different entrance labels. By the unique-longest-entrance characterization of nonspecial edges, f_y cannot be nonspecial; hence it is special. Otherwise phi(f_y)>=q. The z case is identical.