# Synchronized five-window families yield endpoint extenders or a linear alternating fan

## Statement

In the setting of 1ee78a15cf10, let m=ceil((h-1)/120). Then one of the following holds. (1) There is a fixed Hamiltonian order R of C union {u} and a set W of at least m exterior vertices, each extending R at the same endpoint. (2) There are fixed distinct a,b in C union {u}, a pivot x outside C union {u}, and sets Y,Z of exterior vertices with |Y|,|Z|>=floor((m+1)/4) such that for every y in Y and z in Z with y!=z, (y,a,x,b,z) is a tight path. Thus the parallel-middle branch contains a complete bipartite family of controlled alternating five-paths of linear side size.

## Body

Apply 1ee78a15cf10. In its endpoint-extender branch there is nothing further to prove. In its parallel-middle branch there are fixed a,b and a set W of order at least m such that (a,w,b) is tight for every w in W. Apply 02316cc0fa9f to this W. With t=floor((|W|+1)/4)>=floor((m+1)/4), obtain a pivot x in W and sets Y,Z subseteq W-{x} of orders at least t such that every distinct cross-pair y in Y, z in Z yields the tight path (y,a,x,b,z). This gives the stated dichotomy.