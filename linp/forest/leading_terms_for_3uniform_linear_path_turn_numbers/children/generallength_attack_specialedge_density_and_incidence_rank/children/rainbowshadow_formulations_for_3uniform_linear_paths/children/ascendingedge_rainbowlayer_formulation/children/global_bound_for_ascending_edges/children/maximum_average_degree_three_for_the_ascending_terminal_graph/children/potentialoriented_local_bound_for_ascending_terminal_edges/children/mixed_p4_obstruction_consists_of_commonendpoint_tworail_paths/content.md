# The mixed p=4 obstruction consists of common-endpoint two-rail paths

## Statement

Assume phi(v)=4 and four potential-charged ascending nonspecial edges through v have ranks (3,4,4,4). Let e={x,v,u} be the unique rank-three edge, so phi(x)=2. For any rank-four charged edge f={a,v,b} and any longest four-edge path P_f=(h_1,h_2,h_3,f) ending in f with last vertex v, one has x=h_2∩h_3 and u is a private vertex of h_1. Hence P_f is a four-edge path with last vertices u and v and middle joint x.

## Body

By 2dbfe112a0fe, the entrance x of the rank-three edge e={x,v,u} is the middle joint of every maximum four-edge path ending at v. Therefore for the chosen longest path
P_f=(h_1,h_2,h_3,f)
we have x=h_2∩h_3.

Because f is nonspecial of rank four with unique entrance a, the penultimate intersection is
h_3∩f={a}.
The last vertex v is a terminal vertex of f, so a!=v.

We claim u∈h_1. Suppose not. Consider the sequence
h_1,h_2,e,f.
Its consecutive intersections are:
- h_1∩h_2, inherited from P_f;
- h_2∩e={x}, since x lies in h_2 and e={x,v,u};
- e∩f={v}.

All nonconsecutive pairs are disjoint. Indeed h_1 is disjoint from f and h_2 is disjoint from f because these are nonconsecutive pairs in P_f. The edge h_1 is disjoint from e under the supposition u∉h_1, because x lies only in h_2,h_3 on P_f and v lies only in f. Finally h_2∩f=∅ in P_f. Thus h_1,h_2,e,f is a four-edge linear path ending in f through entrance label v.

This contradicts nonspecialness of f: every longest four-edge path ending in f must enter through its unique entrance a, while v is a terminal.

Hence u∈h_1. Moreover u cannot equal the joint h_1∩h_2, because then e and h_2 would share both u and x, violating linearity. Therefore u is private to h_1 on P_f.

So every rank-four charged edge supplies a longest u-to-v four-edge path whose central joint is the same vertex x.