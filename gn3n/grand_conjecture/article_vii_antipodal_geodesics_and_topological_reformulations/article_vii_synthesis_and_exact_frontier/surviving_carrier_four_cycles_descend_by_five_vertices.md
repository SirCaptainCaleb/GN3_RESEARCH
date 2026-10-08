# Surviving carrier four-cycles descend by five vertices

## Composition

(none yet)

## Development

## A surviving carrier four-cycle gives strict hereditary descent by five vertices

Let \(H\) be a boundary tournament with no spanning two-cover. Suppose a protected terminal-pair carrier loop survives all local filling branches, and let
\[
B=\{a,b,c,d\},\qquad Y=B\cup\{z\}
\]
be its five-label support.

By [[a_mutual_terminal_pair_four_cycle_forces_a_hamiltonian_five_support]], \(H[Y]\) is Hamiltonian. By [[surviving_terminal_pair_four_cycles_have_complement_path_cover_at_least_three]], if
\[
R=H-Y,
\]
then
\[
\boxed{\operatorname{pc}(R)\ge3.}
\]
Thus \(R\) is itself a boundary tournament with no spanning two-cover and
\[
|V(R)|=|V(H)|-5.
\]

The stronger overlapping-support theorem [[mutual_terminal_pair_four_cycles_force_four_overlapping_hamiltonian_four_supports]] gives, for every \(w\in B\),
\[
Y-\{w\}\text{ Hamiltonian}.
\]
For a genuinely surviving loop, its complement consequence further gives
\[
\boxed{\operatorname{pc}(R\cup\{w\})\ge3\qquad(w\in B).}
\]
Hence a surviving loop actually carries a five-way hereditary obstruction:
\[
R,\quad R\cup\{a\},\quad R\cup\{b\},\quad R\cup\{c\},\quad R\cup\{d\}
\]
all fail the two-cover conclusion, at orders \(n-5\) and \(n-4\).

### Inductive elimination of the topological loop branch

The project already has the small-order two-cover theorem through order ten. Therefore an induction on order may be initialized at that finite base.

Assume the grand two-cover theorem has been proved for every boundary tournament of order strictly less than \(n\), and let \(H\) have order \(n\). If the Article VII carrier analysis reaches a genuinely surviving terminal-pair \(C_4\), the induced subtournament
\[
R=H-Y
\]
has order \(n-5<n\). The inductive hypothesis gives
\[
\operatorname{pc}(R)\le2,
\]
contradicting the surviving-loop theorem above.

Equivalently, in a minimum-order counterexample above the established finite base, a surviving protected terminal-pair four-cycle is impossible because it canonically deletes five vertices and leaves another counterexample.

This use of order minimality is bounded and explicit: the reduction decreases the order by exactly five and terminates at the already-proved small-order range. It does not invoke any of the old unbounded minimum-counterexample disturbance machinery.

### Frontier consequence

The protected four-label carrier loop is therefore not an independent terminal obstruction in an inductive proof of the grand conjecture. Once the five-label Hamiltonian support and complement-path-cover theorem are retained, the loop branch closes by strict hereditary descent.

The remaining Article VII obligation is consequently the combinatorial/maximal-support branch: produce a two-cover there, or obtain an equally explicit hereditary descent.
