# Joint snake-incidence and blocker budget

## Statement

Fix a vertex x and let I(x) be the incident edges e with φ(e,x)=φ(e). Let B^-(x) be the nonspecial nonascending edges with unique entrance x. For f∈B^-(x), put w_x(f)=ceil(φ(x)/(φ(f)-1))-1. Then |I(x)|+Σ_{f∈B^-(x)}w_x(f)<=2φ(x)-1.

## Body

Choose a path P of length φ(x) with last vertex x, and let e be its last edge. For every g∈I(x) other than e when e∈I(x), the standard snake-indegree witness argument assigns a distinct vertex of V(P)\e: if such a g avoided V(P)\e, then appending g at x would give a path of length φ(x)+1 ending in g, contradicting φ(g)=φ(g,x)≤φ(x). If e∉I(x), the same argument applies to every g∈I(x), so it gives |I(x)| witnesses rather than |I(x)|-1. For f∈B^-(x), the preceding distortion lemma gives at least w_x(f) vertices of f\{x} lying on P; none lies in e, and these blocker vertices are disjoint for different f by linearity. They are also disjoint from the snake witnesses, because otherwise two distinct edges through x would share another vertex. Since V(P)\e has 2φ(x)-2 vertices, if e∈I(x) then (|I(x)|-1)+Σ_{f∈B^-(x)}w_x(f)≤2φ(x)-2, while if e∉I(x) one has the stronger |I(x)|+Σ_{f∈B^-(x)}w_x(f)≤2φ(x)-2. In either case |I(x)|+Σ_{f∈B^-(x)}w_x(f)≤2φ(x)-1.
