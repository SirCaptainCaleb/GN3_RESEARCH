# A singleton support transfer endpointizes unless its endpoint realizations are aligned

## Statement

Let H be a boundary tournament with pc(H)>2. Let X,Y,D and {x} partition V(H), and suppose both
(X union {x}) | Y | D
and
X | (Y union {x}) | D
are spanning three-covers.

If H[X union {x}] has a Hamilton path ending at x and H[Y union {x}] has a Hamilton path beginning at x, then the greedy endpoint-transport theorem produces an explicit tight triple reversing the terminal edge of a displayed Hamilton component. The symmetric conclusion holds when x begins a Hamilton path on X union {x} and ends a Hamilton path on Y union {x}.

Consequently, if no spanning two-cover exists and no displayed component-end reversal is obtainable in this way, then the endpoint realizations of x on the two augmented supports have only the following possibilities:
(1) x is internal in every Hamilton path of H[X union {x}] or in every Hamilton path of H[Y union {x}]; or
(2) every Hamilton path on either augmented support that has x as an endpoint places x on the same side in both supports: only as an initial vertex on both, or only as a terminal vertex on both.

Thus every singleton transfer arising from an equal-Phi near-balanced support comparison is consumed by endpoint transport except for universal internality or a coherent same-end endpoint residue.

## Body

Choose a Hamilton path C on Y union {x} beginning at x, say
C=(x,c_1,...,c_m),
and choose a Hamilton path R_0 on X union {x} ending at x.

Apply a_complementary_path_until_a_reverse_end_hook_appears with the Hamiltonian support X, the displayed complementary path C, unchanged third component D, and c_0=x. Its hypotheses are exactly satisfied: X|C|D is a spanning three-cover, and X union {x} has a Hamilton path whose terminal vertex is x.

Greedily transport the initial segment of C into X as in a_complementary_path_until_a_reverse_end_hook_appears. If every vertex of C transports, then X union V(C)=X union Y union {x} becomes one Hamiltonian path and, together with D, gives a spanning two-cover of H, contrary to pc(H)>2. Therefore transport fails for a first vertex c_{h+1}. At that first failure, a_complementary_path_until_a_reverse_end_hook_appears gives a tight triple
(c_{h+1},c_h,q)
reversing the displayed terminal edge (q,c_h) of the enlarged Hamilton component. Hence opposite endpoint realizations of x force a displayed component-end reversal.

The initial/terminal symmetric case is identical: if x begins a Hamilton path on X union {x} and ends one on Y union {x}, use the symmetric form of a_complementary_path_until_a_reverse_end_hook_appears.

Now suppose neither opposite realization pattern exists. Let E_X and E_Y be the sets of endpoint sides on which x occurs among Hamilton paths of X union {x} and Y union {x}, respectively, where the two sides are initial and terminal. If one of E_X,E_Y is empty, x is internal in every Hamilton path on that augmented support, giving (1). Otherwise both are nonempty. If they contained opposite sides, the preceding argument would apply. Therefore no opposite pair occurs. The only nonempty subsets of {initial,terminal} with no opposite pair across E_X and E_Y are
E_X=E_Y={initial}
or
E_X=E_Y={terminal}.
Indeed, if either set contained both sides and the other were nonempty, an opposite pair would exist. This proves (2).

Finally, support_cut_low_crossing_normal_form01 shows that on an equal-Phi size-gap-one comparison, every one-cut neutral support change is a singleton transfer and one of the two same-path two-cut neutral changes is an internal singleton transfer. The present theorem therefore consumes either singleton-transfer geometry whenever opposite endpoint realizations are available, leaving precisely universal internality or same-end alignment as the low-cut endpoint obstruction.