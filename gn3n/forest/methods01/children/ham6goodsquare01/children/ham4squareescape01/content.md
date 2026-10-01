# A Hamiltonian four-core two-label square yields a cross-component edge, descent, or order disagreement above order fifteen

## Statement

Let H be a minimum counterexample of order n>=16. Let D be a Hamiltonian four-vertex set and let d,e be distinct vertices outside D. Put K=H-(D union {d,e}). Assume K, K+d, K+e, and K+d+e are all non-Hamiltonian with path-cover number two, and D+d, D+e, and D+d+e are Hamiltonian whenever those supports occur as specified below; in particular assume D+d and D+e are Hamiltonian. Let F=P|Q be any two-cover of K+d+e. Then at least one of the following holds: (1) deleting d or e from F produces a three-path cover of the corresponding lower square state, and some two-cover of that lower state contains an ordinary edge joining two different components of that three-path cover; (2) the spanning three-cover D|P|Q admits a legal pairwise repartition with strictly smaller quadratic potential; (3) H contains order disagreement between two tight paths. For n=15 the same conclusion holds except possibly when d,e are endpoints of one component of F of order five and the other component has order six.

## Body

# Proof

Choose a Hamilton tight ordering of D and regard C=D|P|Q as a spanning three-cover of H.

Suppose first that d is internal in its component of F. Deleting d from that displayed path splits it into two nonempty tight subpaths; together with the other component of F this gives a three-path cover R of K+e. By hypothesis K+e has a two-cover T. Since T has fewer components than R, the component-drop lemma in coversurg01 gives an ordinary edge of T whose endpoints lie in two different components of R. This is outcome (1). The same argument applies if e is internal.

Hence assume d and e are displayed endpoints of their F-components. Neither can be a singleton component: if, for example, {d} were a component, the other component would be a Hamilton path on K+e, contradicting non-Hamiltonicity of K+e. Thus deleting d or e from its component leaves a nonempty tight path.

Let d lie in an F-component of order p. Since D+d is Hamiltonian, repartitioning D together with that component as (D+d) and the component with d deleted is legal. The affected component orders change from (4,p) to (5,p-1), so

Delta Phi = [25+(p-1)^2]-[16+p^2]=10-2p.

If p>=6 this is negative, giving outcome (2). Therefore, if no strict descent occurs, the component containing d has order at most five. The same holds for e.

If d and e lie in different components of F, then both component orders are at most five, whereas their sum is n-4>=12, impossible for n>=16. Thus in the no-descent branch they lie in the same component, say P, of order p<=5. Put q=|Q|. Since 4+p+q=n, we have q=n-4-p>=7 when n>=16.

Apply the certified theorem a25b748fb338 to the spanning three-cover D|Q|P, using a Hamilton ordering of D and the q-path Q. Because q>=7, that theorem yields either a legal strict decrease of Phi, which is outcome (2), or explicit order disagreement, outcome (3). This proves the result for n>=16.

When n=15, the same argument works unless the no-descent same-component branch has p=5 and q=6. If p<=4 then q>=7 and a25b748fb338 applies; if p>=6 the direct endpoint move already strictly decreases Phi; and if d,e lie in different components then their orders sum to eleven, so one has order at least six and again gives the direct descent. Thus only profile 4|5|6 remains. ∎
