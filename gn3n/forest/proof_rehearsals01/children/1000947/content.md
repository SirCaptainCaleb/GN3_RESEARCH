# Proof rehearsal III — defect-span and spanning-order compression

## Statement

Near-publication rehearsal of the defect-span route. The defect-line identity turns the two-cover theorem into the problem of reducing a spanning order from two independent defect edges to one. Certified normalization identifies the width-three state with a deletion cover and reduces its local geometry to the 101 or 111 central configuration. The 101 fixed-label branch and the universal four-window/five-side branch now both reach, subject to pending second-layer results, a reachable endpoint-edge reversal or endpoint-aligned Hamiltonian 4/5 support. The first unsupported implication is to consume that positioned obstruction into boundary absorption, a two-cover, or defect-line matching number at most one.

## Body


# Defect-span and spanning-order compression

## 1. The proposed proof

Let H be a minimum counterexample to the assertion that every finite 3-uniform boundary tournament has a spanning cover by at most two tight paths. By the certified minimum-counterexample calculus, pc(H)=3.

For a spanning ordering

    pi = (v_1,...,v_n),

call i a defect center when the consecutive triple (v_i,v_{i+1},v_{i+2}) is not tight. The defect line L_pi is the graph on the cuts between consecutive positions, with an edge across the two cuts adjacent to each defect center. The certified identity 1000666 states that the minimum number c(pi) of contiguous tight-path pieces into which pi splits is

    c(pi) = 1 + nu(L_pi),

where nu denotes matching number.

Thus H has a spanning two-cover as soon as we can find a spanning order with

    nu(L_pi) <= 1.

In a minimum counterexample, every optimal spanning order has three path pieces, so the obstruction is exactly one unit larger: the defect line contains a matching of size two. The route seeks to compress those two independent defects into one.

The relevant width-three certificate has a certified normal form. Theorems defectspanisdeletion and defectcanonical35_recomp01 identify a minimum defect-span-three order with an exact one-vertex deletion cover

    H-x = P | Q

written as a spanning order with x inserted between the two tight paths. Hence the defect-span and deletion-cover formulations are not separate problems: they describe the same canonical state.

All results below are certified unless explicitly marked **pending**.

## 2. The canonical central geometry

Around the inserted label x, the minimum width-three order has only two local forms.

In the **101 state**, the middle join through x is tight. The central bridge has order three. This case retains unusually strong provenance: the same omitted label x and the inherited orders of P and Q can be followed under transport.

In the **111 state**, the middle join is defective. Boundary antisymmetry then yields the canonical reversed central five-path. This case retains a positioned five-vertex side and explicit reversal data.

There is also a route-independent bounded-window normalization. Certified theorem 1000006 rules out the isolated three-edge cyclic matching geometry, and 1000458 gives a double-wrap rotation for every deletion singleton lift. The certified cyclic transport theorem then produces a Hamiltonian four-window whose complement has path-cover number two.

Therefore every canonical width-three state enters one of two mathematical continuations:

1. exploit the fixed deletion label in the 101 state; or
2. pass to the universal bounded-window/reversal machinery.

The proof branches here and nowhere earlier.

## 3. The 101 branch: transport one fixed defect label

The special strength of 101 is that the same omitted label survives the transport.

The certified finite-transport theorem defect101_finite_transport01 iterates the local 101 slide. It terminates in one of two states:

- another exact deletion cover H-x=P|Q in which one displayed side has order three; or
- a blocked slide exposing a Hamiltonian four-window with an inherited two-path complement.

The second outcome has already entered the universal bounded-window branch. It remains to understand the three-side outcome.

Certified theorem threeside01 supplies persistent fixed-label transport through four overlapping seven-vertex shells. At least two persistent defect labels can be moved from one end of the long path to the other while preserving the same deletion label. Thus the defect is not merely movable locally; it can be carried across a macroscopic portion of the spanning order.

The strongest continuation is pending audit. Theorems 1000946, 1000950, and 1000951 show respectively that:

- the shell transport remains in the same pairwise-repartition component as the original deletion state;
- every shell transition lies above a 5|2 -> 4|3 strict-descent diamond;
- the lower 4|3 states glue into a left-to-right constant-Phi corridor carrying one persistent label.

The next pending layer, 1000953, reduces failure of synchronized second-layer descent to three degree-four core graphs: 2K2, P4, or K1,3. Those graphs are no longer the strongest endpoint. Pending theorems 1000954-1000956 continue the argument:

- failure of synchronized second-layer descent produces relative-order disagreement between reachable Hamiltonian four-sides in the same fixed-defect component;
- that disagreement yields a literal reversing tight triple on an edge of a reachable four-side;
- internal-edge reversal cases are absorbed into the standard small-window machinery.

Consequently, subject to audit, the entire fixed-label branch reaches exactly one of:

1. synchronized strict second-layer descent;
2. a reversal of an end edge of a reachable Hamiltonian four-side; or
3. a proper endpoint-aligned Hamiltonian four- or five-support with path-cover-two complement.

At a componentwise minimum the first alternative is contradictory. The 101 branch therefore feeds the same positioned bounded obstruction that arises from the universal branch.

## 4. The universal bounded-window branch

The blocked 101 outcome and essentially all of 111 enter the same machinery.

Let W be a Hamiltonian four-set with exact two-path complement P|Q. The certified four-window transport theorem 1000911 says, for n>14, that this state yields one of:

- strict quadratic-potential descent;
- a Hamiltonian four-window at distance one, again with path-cover-two complement;
- an endpoint-aligned Hamiltonian support of order four or five.

Thus a four-window cannot remain an isolated local witness. It either descends or migrates until the bounded support becomes aligned with a displayed endpoint.

The 111 state carries a five-side instead. Certified theorem five_side_arbitrary_escape01 gives the parallel conclusion: a five-side beside a sufficiently long path yields strict Phi-descent, an equal-size endpoint/support exchange, or a tight triple reversing an edge of the displayed path.

These theorems have the same logical purpose. They take a bounded central obstruction and move it toward an endpoint-sensitive configuration. A generic interior reversal or an arbitrary small Hamiltonian set is not the endpoint of the proof; the relevant output is a reversal of a displayed end edge or an endpoint-aligned support with its pc2 complement still attached.

The only finite-order qualification in this branch is the residue n<=14 left by 1000911. Any proof that closes the large-order branch must either treat this residue separately or import a certified small-order argument.

## 5. Convergence of the two branches

After the pending fixed-label refinements, both branches reach the same state:

- a reachable Hamiltonian four-side carrying a reversal of one of its end edges; or
- an endpoint-aligned Hamiltonian support of order four or five with path-cover-two complement.

This is substantially stronger than the unconditional existence of a reversal. Certified theorem 1000164 already gives a genuine reversing tight triple somewhere in every minimum counterexample. What the defect-span route contributes is **placement**: the reversal or small support is tied to a canonical deletion/defect state and, in the 101 branch, to a fixed omitted label and same-component transport history.

The remaining theorem should therefore be stated directly in defect-line language.

**Endpoint compression lemma (open).**  
Let pi be a canonical minimum width-three spanning order arising from an exact deletion cover H-x=P|Q. Suppose a reachable bounded-window state associated with pi contains either

- a reversal of an end edge of its Hamiltonian four-side, or
- an endpoint-aligned Hamiltonian four- or five-support with path-cover-two complement.

Then H has a spanning ordering sigma with

    nu(L_sigma) <= 1.

Equivalently, H has a spanning two-path cover.

No current theorem proves this implication in full generality.

## 6. Why the local obstruction is not already closure

Three points delimit the missing step.

First, an interior reversal cannot simply be read as an endpoint reversal. The order of a tight path is part of the data. Boundary antisymmetry reverses one ordered triple; it does not permit cyclic rotation or reversal of a whole path.

This is not merely a warning. The certified counterexample common_endpoint_barriers_fivewindow_counterexample01 gives arbitrarily long configurations in which common endpoint barrier triples do not produce the Hamiltonian five-window one would obtain by an illicit cyclic reinterpretation. Any valid transport proof must literally move the reversal to the required boundary.

Second, strict Phi-descent is useful only with same-component provenance. A smaller potential state unrelated to the chosen trapped component is not a contradiction. The pending 101 corridor results matter precisely because they certify reachability inside the original deletion component.

Third, neutral migration is not termination. A finite collection of nearby windows can cycle. If the final compression proof uses repeated equal-potential moves, it must provide a well-founded invariant, a no-trapping theorem, or a contradiction from recurrence.

## 7. Relation to the neighboring routes

The quadratic-potential route supplies the extremal meaning of strict descent and rules out small sides at trapped minima. The present route uses that information only to reject the descent outcomes; its own invariant is the defect-line matching number.

The endpoint-transport route is the natural consumer of the positioned outputs above. Once a reversal lies on a displayed component-end edge, the certified endpoint calculus often gives direct absorption, strict descent, or a single neutral transfer. Thus the open lemma above is exactly the defect-span/endpoint-transport interface.

Deletion-cover compatibility can supply additional order disagreement or mixed-support crossing when transport stalls, but generic disagreement is not enough. The defect-line route requires the witness to remain tied to the canonical order.

Longest-path/reversal theory can amplify a reversal into common-core bounded windows. Again, the useful datum is placement and pc2 complement provenance, not witness existence.

## 8. Exact stopping point

The proof is complete through the canonical width-three reduction and both transport branches in the certified core. Subject to audit of 1000954-1000956, the fixed-label branch has already been reduced to the same endpoint-aligned obstruction as the universal four-window branch.

The first unsupported implication is

    reachable endpoint-edge reversal
    or endpoint-aligned Hamiltonian 4/5 support
    => defect-line matching number at most one.

The n<=14 residue of 1000911 remains a separate finite-order obligation for the universal branch.

## 9. Research handoff

The strongest viable next target is the endpoint compression lemma above. A useful proof should retain the displayed deletion label, inherited path order, pc2 complement, and same-component reachability long enough to perform a legal boundary splice.

The principal route not to retry without a new ingredient is another layer of local witness production. The 101 slide, fixed-label shell transport, four-window migration, five-side escape, order disagreement, and generic reversal are all already available. Likewise, the old degree-four shell graphs from 1000953 are superseded, subject to audit, by 1000954-1000956.

The route is now a one-unit compression problem in the literal sense:

    nu(L_pi)=2
    => position one certified obstruction at the boundary
    => nu(L_sigma)<=1.

The first arrow is established. The second is the frontier.
