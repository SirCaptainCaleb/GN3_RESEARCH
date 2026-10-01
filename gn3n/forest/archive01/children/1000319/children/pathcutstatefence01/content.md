# Terminal-pair extension graphs do not have the needed ordinary cut dual

## Statement

The ordered-terminal-pair extension digraph proposed in brainstorm 69a820d63c10 correctly recognizes local tight-path extensions but does not by itself admit an ordinary cut dual for two-path coverability. A directed walk (u_0,u_1)->(u_1,u_2)->... records only the last two vertices and may revisit an earlier vertex, whereas a tight path must be vertex-simple. Likewise two walks covering all vertices exactly once impose a global used-vertex resource constraint not encoded by terminal-pair states. If one augments a state by its used vertex set, the representation becomes exact but exponentially large and its natural cut certificates are global subset-state objects rather than small sets of forbidden continuation triples. Thus any viable min-max theorem on this route needs an additional exchange/matroid-like principle that compresses the used-vertex constraint; ordinary state-graph separator theory is insufficient.

## Body

# Proof

Define the natural extension digraph D whose states are ordered pairs (u,v) of distinct vertices and with an arc

(u,v) -> (v,w)

whenever u,v,w are distinct and (u,v,w) is tight.

Every tight path

(v_1,...,v_k)

does produce the directed state walk

(v_1,v_2) -> (v_2,v_3) -> ... -> (v_{k-1},v_k).

However the converse fails at the level needed for a path-cover min-max theorem. A state walk in D only requires consecutive triples to be tight. Nothing in the state (u,v) records vertices used before u. Thus a later transition can append an earlier vertex and create a repeated-vertex walk. Such a walk is not a tight path under the project definition.

The same issue becomes stronger for two paths. A spanning two-path cover requires two vertex-simple tight paths whose support sets are disjoint and whose union is V(H). In the pair-state digraph this means choosing two walks subject simultaneously to

1. no underlying vertex repeated within either walk;
2. no underlying vertex shared between the walks; and
3. every ambient vertex used by one of the walks.

These are global resource constraints on the entire pair of walks. They are not expressible as ordinary source-target reachability or vertex-disjointness of state vertices, because distinct pair states can share an underlying ambient vertex.

There is an exact finite-state representation: enlarge a state to

(S,u,v),

where S is the set of ambient vertices already used and u,v are the terminal pair. A transition appends w outside S and moves to (S union {w},v,w). A corresponding two-walk state can track two used sets or one global used set plus two terminal pairs. In that expanded state space, spanning two-coverability is an exact reachability problem.

But this exact state space is indexed by subsets of V(H), hence has exponential size. A cut in it is generally a collection of subset-states and does not project automatically to a bounded family of forbidden continuation triples in the original tournament.

Therefore the proposed first attack cannot obtain the desired small dual certificate merely from an ordinary cut in the ordered-pair extension digraph. To make the route theorem-scale, one needs an additional structural theorem that compresses the used-vertex resource constraint—an exchange property, uncrossing principle, matroid-like representation, or another special consequence of boundary antisymmetry.

This is a route fence, not a refutation of the existence of some deeper min-max theorem.
