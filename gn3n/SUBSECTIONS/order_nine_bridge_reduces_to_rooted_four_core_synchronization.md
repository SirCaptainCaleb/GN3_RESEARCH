# Order-nine bridge reduces to rooted four-core synchronization

## Metadata

- ID: order_nine_bridge_reduces_to_rooted_four_core_synchronization
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 32
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

## The order-nine bridge reduces to a six-vertex rooted synchronization problem

The adjacent-window obstruction from [[protected_parabolic_carriers_reduce_the_global_gap_to_adjacent_window_gluing]] admits a stronger common-core reduction.

Let (I) be the order-nine terminal interval. Then (H[I]) has a complementary Hamiltonian (5|4) partition.

**Lemma (Hamiltonian (5|4) core on nine vertices).** Every nine-vertex boundary tournament has a partition
[
I=Asqcup B,qquad |A|=4,quad |B|=5,
]
such that both (H[A]) and (H[B]) are Hamiltonian.

**Proof.** Let (h_5) be the number of Hamiltonian five-subsets of (I). Every six-set has at least four Hamiltonian five-deletions. Counting incidences ((F,S)) with (|F|=5), (|S|=6), (Fsubset S), and (F) Hamiltonian gives
[
4h_5ge 4inom96,
]
hence
[
h_5ge inom96=84.
]

Let (h_4) be the number of Hamiltonian four-subsets. Every five-set has at least three Hamiltonian four-deletions. Counting incidences with a Hamiltonian four-set inside a five-set gives
[
5h_4ge 3inom95=378,
]
so
[
h_4ge 76.
]

The (126=inom94=inom95) complementary (4|5) partitions identify four-sets with complementary five-sets. If no partition had both sides Hamiltonian, the (h_4) good four-sides and the complements of the (h_5) good five-sides would be disjoint classes among only (126) four-sets. But
[
h_4+h_5ge 160>126.
]
Contradiction. In fact there are at least (34) good complementary (5|4) partitions. (square)

Now let (x,y) be the two exterior vertices in the adjacent normalization windows
[
J_-=Icup{x},qquad J_+=Icup{y}.
]
Choose a good core (I=Asqcup B) as above. The prescribed-endpoint extension theorem from [[localextend01]] applied to a tight Hamiltonian triple inside a Hamilton order of (A), with the fourth vertex of (A) as the auxiliary exterior vertex, implies that for each (zin{x,y}) there is a Hamiltonian support on (Acup{z}) with (z) exposed at an endpoint; since all five vertices are needed whenever the produced four-support omits a vertex of (A), the remaining exceptional case is itself a Hamiltonian four-support and can be absorbed by the same (4|5) core. Thus both ten-windows admit rooted repairs using the same Hamiltonian five-side (B) and a Hamiltonian varying side through (A).

The protected gluing problem is therefore no longer a ten-vertex support problem. It reduces to the following bounded ordered synchronization statement on the six-set
[
Acup{x,y}.
]

> **Rooted four-core synchronization.** Given a Hamiltonian four-set (A) and two exterior vertices (x,y), choose rooted Hamiltonian extensions through (Acup{x}) and (Acup{y}) so that the two resulting ten-window repairs are joined inside the depth-(>r) chamber complex.

A stronger but not universal formulation would ask for one Hamilton order of (A) simultaneously extendable by both (x) and (y) at an endpoint; that strengthening is false in general, so the bridge must allow a short reconfiguration of the four-core order. The remaining obstruction has therefore been compressed to a genuine six-vertex ordered problem.
