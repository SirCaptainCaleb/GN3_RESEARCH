# All spanning three-covers of a hypothetical order-eleven minimum counterexample lie in one Astra component

## Statement

Let H be a hypothetical order-eleven minimum counterexample. Then the Astra-003 move graph on spanning three-component tight-path covers of H is connected. More precisely, every such cover lies in the unique component K containing the equitable 5|5|1 surface and the 4|4|3 surface.

## Body


Let K be the universal order-eleven component from 59bfc75bfb10. Thus every spanning 5|5|1 state and every spanning 4|4|3 state belongs to K.

Take an arbitrary spanning three-component cover C of H, and let L be its Astra connected component. Since H is a counterexample, no spanning two-cover exists anywhere, so L contains no two-component state.

Choose a cover C_min in L minimizing

Phi=sum_i |P_i|^2.

Because H has order eleven, the certified Astra descent lemma astra003minsize3 applies: every component of C_min has order at least three.

The three positive component orders therefore sum to eleven with each at least three. Up to decreasing order, the only possibilities are

5|3|3
or
4|4|3.

If C_min has type 4|4|3, then C_min belongs to K by 59bfc75bfb10. Hence L=K.

Suppose instead that C_min has type 5|3|3, say

A|B|C

with |A|=5 and |B|=|C|=3.

The six-set V(B) union V(C) has, by the certified four-of-six theorem, a Hamiltonian five-vertex subset F. Let x be its complementary vertex in this six-set. Then

F | (x)

is an exact 5|1 cover of V(B) union V(C).

Replacing B|C by F|(x) is one legal Astra move, producing the spanning state

A | F | (x)

of type 5|5|1.

By 59bfc75bfb10 every 5|5|1 state belongs to K. Hence again L=K.

Thus every connected component L of the three-cover move graph equals K. Therefore the entire spanning three-cover state graph is connected.

This does not itself prove Astra idea 003, because in a hypothetical counterexample there is still no two-component state to merge into. Its significance is that any terminal no-merge analysis at order eleven may now use the closure of the entire three-cover state space: there are no separate trapped reconfiguration components.
