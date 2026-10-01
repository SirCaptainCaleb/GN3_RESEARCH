# A vertex on a linear path has half-path endpoint potential

## Statement

Let P=(e_1,...,e_p) be a p-edge linear path in a linear hypergraph, and let w be any vertex in V(P). Then φ(w)>=ceil(p/2). More precisely, if w lies in exactly one path edge e_i then φ(w)>=max{i,p-i+1}; if w=e_i∩e_{i+1} is a path joint then φ(w)>=max{i,p-i}.

## Body

Because P is linear, the path edges containing w form either one edge or two consecutive edges. If w lies only in e_i, then the prefix (e_1,...,e_i) is an i-edge path that can end at w, since w is not in e_{i-1}; reversing the suffix (e_i,...,e_p) gives a (p-i+1)-edge path ending at w, since w is not in e_{i+1}. Hence φ(w)>=max{i,p-i+1}. If w is the joint e_i∩e_{i+1}, then the prefix (e_1,...,e_i) can end at w and has length i, while the reversed suffix (e_{i+1},...,e_p) can end at w and has length p-i. Thus φ(w)>=max{i,p-i}. Both lower bounds are at least ceil(p/2).
