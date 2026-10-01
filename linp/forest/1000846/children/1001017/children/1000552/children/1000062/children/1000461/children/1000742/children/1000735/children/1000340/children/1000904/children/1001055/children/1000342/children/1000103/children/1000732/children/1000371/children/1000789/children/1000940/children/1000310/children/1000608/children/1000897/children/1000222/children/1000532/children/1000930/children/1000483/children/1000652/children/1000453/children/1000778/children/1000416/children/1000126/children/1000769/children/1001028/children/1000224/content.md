# Collision count is bounded by rank spread times squared cycle-packing number

## Statement

Let v_0v_1...v_k be a rainbow terminal-pair path of ascending nonspecial edges
E_1,...,E_k
with nondecreasing ranks r_1<=...<=r_k. Let C be the number of color-terminal collision chords on this path, let
D=r_k-r_1,
and let nu be the maximum number of pairwise edge-disjoint linear cycles whose edges all belong to {E_1,...,E_k}.

Then
C <= D(2nu+1)^2.
In particular, if D=0 then C=0, and more generally a path with small rank spread and bounded cycle-packing number is close to strong-rainbow.

## Body

By 31cb29f347a8, every collision chord crosses at least one strict rank jump. Assign each collision to one strict jump that it crosses, for example the leftmost such jump. The number J of strict jumps is at most D because the integer rank rises by at least one at each strict jump.

Fix one strict jump and let M be the number of collision chords assigned to it. All M chords cross that fixed cut, so e4a44a230fe7 supplies at least
ceil((ceil(sqrt(M))-1)/2)
pairwise edge-disjoint linear cycles, all using edges from the parent-edge set {E_1,...,E_k}. By the definition of nu,
ceil((ceil(sqrt(M))-1)/2) <= nu.
Therefore
ceil(sqrt(M)) <= 2nu+1,
and hence
M <= (2nu+1)^2.

Summing this bound over the J<=D strict jumps gives
C <= J(2nu+1)^2 <= D(2nu+1)^2.
When D=0 there are no strict jumps, so C=0.
