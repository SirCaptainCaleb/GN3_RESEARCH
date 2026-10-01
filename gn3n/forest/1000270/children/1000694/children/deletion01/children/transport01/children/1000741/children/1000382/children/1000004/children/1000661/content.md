# Every clean all-equal detour reduces to bounded reversal or a Hamiltonian five-window

## Statement

In the clean-detour branch of the all-equal endpoint-probe reduction, the detour's length and position can be discarded. Every such detour forces at least one bounded bridge input: a tight path reversing the replaced inherited edge, an explicit reversing triple through that edge, a Hamiltonian five-set meeting the edge and a detour endpoint, or a doubled reverse barrier on at most five vertices.

## Body

The replaced inherited edge is either internal or is the first/last edge of its inherited displayed path. The internal case is exactly 750799cd88eb. The endpoint case is endpoint_detour_amp. Both conclusions depend only on the replaced edge, at most its two inherited neighbors, one detour endpoint, and in the endpoint case one auxiliary vertex that is either adjacent in the deletion path or the omitted deletion label. Therefore no parameter depending on the length of the exterior detour survives.
