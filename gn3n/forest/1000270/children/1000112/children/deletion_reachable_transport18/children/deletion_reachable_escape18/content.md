# Large deletion states reach descent, pc2 transport, neutral support migration, or a positioned reversal

## Statement

Let H be a minimum counterexample of order n>=18 and let H-x=P|Q be any one-vertex deletion two-cover. In the trapped pairwise-repartition component containing the singleton lift, after the universal three strict quadratic-potential descents supplied by bc151d5d2a89 and threesidedescent6, at least one of the following occurs: (1) one further legal pairwise repartition strictly decreases quadratic potential; (2) a reachable Hamiltonian four-side state carries the bounded path-cover-two transport package of four_window_transport15; (3) a reachable Hamiltonian five-side state admits a one-move equal-Phi exchange of one five-side vertex with an endpoint of a long component; (4) in a reachable Hamiltonian five-side state, a five-side vertex participates in a tight triple reversing a displayed edge of a long component.

## Body

By deletion_reachable_transport18, after three strict legal moves the component contains a reachable four-side or five-side state, and either a further strict descent already occurs, the four-side pc2 transport package occurs, or the five-side has a long component R of order at least seven together with a common four-core extending Hamiltonianly to both endpoints of R.

In the first two cases we obtain (1) or (2). In the five-side case, apply five_side_arbitrary_escape01 directly to that reachable five-side and R. Its strict-descent outcome is (1). Its equal-size endpoint/support exchange is a legal pairwise repartition preserving Phi and gives (3). Its final outcome is a tight triple, using a vertex of the five-side, reversing a displayed edge of R, giving (4).

Every cover mentioned before the pc2 transport package is reached by legal pairwise repartitions from the original deletion singleton lift, so the descent and neutral-exchange conclusions are genuinely component-respecting.
