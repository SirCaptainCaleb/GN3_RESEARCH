# Terminal potentials of an ascending edge are at most twice its rank minus two

## Statement

Let e={x,u,v} be an ascending nonspecial edge of a finite linear 3-graph, with unique entrance x and edge rank q=φ(e). Then φ(u),φ(v)<=2q-2. Equivalently q>=ceil((φ(u)+2)/2) and q>=ceil((φ(v)+2)/2). This is sharp: the six-edge example 0e0b0a3c7b04 has q=3 and φ(u)=φ(v)=4=2q-2.

## Body

Fix a terminal vertex v of e and put p=φ(v). Suppose for contradiction that p>=2q-1. Choose a p-edge linear path P ending at v. By the long-terminal-path capture lemma 16d45ad1b1b2, P contains the entrance vertex x. By the half-path endpoint-potential lemma 8b1790d79d74, any vertex lying on a p-edge path has endpoint potential at least ceil(p/2). Hence φ(x)>=ceil(p/2)>=q. But e is ascending, so φ(x)=q-1, a contradiction. Thus φ(v)<=2q-2. The same argument applies to the other terminal u. Equality occurs in 0e0b0a3c7b04.