# Every all-equal endpoint probe pair exposes a canonical defect-compression input

## Statement

Let H be a minimum counterexample and let A|B|C be a spanning three-cover with |A|=|B|=|C|=r. Choose arbitrary exact two-covers of H-a_1 and H-a_r for the two displayed endpoints of A. Then the resulting data necessarily expose at least one canonical input accepted by the endpoint-transport / defect-compression bridge: (1) relative-order disagreement with an inherited displayed path; (2) an explicit support crossing consisting of one inherited displayed edge whose endpoints lie in different components of an endpoint deletion cover; or (3) a bounded local obstruction on at most five vertices, namely a reversed inherited edge/path, a reversing triple through an inherited edge, a Hamiltonian five-window, or a doubled reverse barrier. No component-size progression, crossing-count normalization, or detour-length analysis remains.

## Body

Apply 7ae7f3c03f16. Its first outcome is relative-order disagreement, giving (1). Its second outcome is an inherited ordinary edge with endpoints in different components of an endpoint deletion cover, which is exactly the localized support crossing in (2). Its third outcome is a leave-and-return excursion. Under the no-order-disagreement and no-reciprocal-crossing assumptions defining that branch, 0227c4505eec localizes the excursion to a clean detour replacing one inherited edge. The theorem c964a4b8b0dd removes both the detour length and whether the replaced edge is internal or at an endpoint, yielding one of the bounded outcomes in (3). These alternatives exhaust arbitrary choices of the two endpoint deletion covers.
