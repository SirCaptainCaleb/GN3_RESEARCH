# The two-cover completion rank vanishes in every counterexample

## Statement

If pc(H)>2, then for every ordered pair (u,v) there is no vertex set S containing u,v such that H[S] has a tight path ending (u,v) and H-S is Hamiltonian. Thus the completion rank proposed in ba48cdda95aa has no positive values on any counterexample (and is identically 0 if empty witness families are assigned rank 0).

## Body

Let H be a boundary tournament with pc(H)>2. Suppose an ordered pair (u,v) had a completion-rank witness S as proposed in ba48cdda95aa: H[S] has a tight path P ending (u,v), and H-S is Hamiltonian, with the empty complement allowed.

If H-S is nonempty, P together with a Hamilton path on H-S is a spanning two-path cover of H, contradicting pc(H)>2. If H-S is empty, then P is a Hamilton path of H, contradicting pc(H)>2 even more strongly.

Therefore no ordered pair has any positive completion-rank witness in a counterexample. Equivalently, if one extends the definition by setting the maximum of the empty witness family to 0, then R(u,v)=0 for every ordered pair (u,v).

Hence the proposed orientation by larger R and equal-rank in-neighborhood counting cannot bootstrap toward a two-cover: on every counterexample its state space collapses before the rank argument begins. Any viable terminal-pair lift must rank a genuinely pre-completion notion (for example, a path whose complement has bounded path-cover number or bounded defect), not require a Hamiltonian complement in the definition of the rank itself.
