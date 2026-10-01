# The forced minimum-side cross-end connector yields a positioned Hamiltonian four- or five-window

## Statement

Let H be a minimum counterexample and let H-x=P|Q be a deletion cover whose smaller component P has globally minimum deletion-side order. Write P=(p_0,...,p_r), Q=(q_0,...,q_s). Then, after possibly using the symmetric facing endpoint pair, H has a Hamiltonian set W of order four or five satisfying {p_0,x,q_s} subseteq W and one of the following forms:

(i) W={p_1,p_0,x,q_s,q_{s-1}}; moreover, when (p_0,x,q_s) is tight, W has the Hamilton order (p_1,p_0,x,q_s,q_{s-1});
(ii) W={p_1,p_0,x,q_s};
(iii) W={p_0,x,q_s,q_{s-1}}.

In every case H-W is non-Hamiltonian with path-cover number two, witnessed by the inherited residual paths of P and Q.

## Body

Apply the orientation-clean facing-endpoint theorem 5279c5c777d2 directly to the facing pair p_0,q_s.

If (p_0,x,q_s) is tight, then the endpoint hooks (p_1,p_0,x) and (x,q_s,q_{s-1}) give
(p_1,p_0,x,q_s,q_{s-1})
as a tight Hamilton path. Thus the five-set
S={p_1,p_0,x,q_s,q_{s-1}}
is Hamiltonian, with the displayed order in this subcase.

Otherwise 5279c5c777d2 gives the reverse cross triple
(q_s,x,p_0)
tight. Put
X={p_1,p_0,x,q_s}.

If H[X] is Hamiltonian, use W=X, giving case (ii).

Assume H[X] is non-Hamiltonian and put
S=X union {q_{s-1}}.

If H[S] is Hamiltonian, use W=S, giving case (i). No prescribed Hamilton order on S is asserted in this reverse-cross subcase.

Finally suppose H[S] is non-Hamiltonian. The certified five-set theorem in smallset01 says that a non-Hamiltonian five-set has at most one non-Hamiltonian four-subset. Since X=S-{q_{s-1}} is already non-Hamiltonian, every other four-subset of S is Hamiltonian. In particular
W=S-{p_1}={p_0,x,q_s,q_{s-1}}
is Hamiltonian, giving case (iii).

The complements have inherited two-covers:
for (i), (p_2,...,p_r)|(q_0,...,q_{s-2});
for (ii), (p_2,...,p_r)|(q_0,...,q_{s-1});
for (iii), (p_1,...,p_r)|(q_0,...,q_{s-2}).
Because both original deletion-cover components have order at least three, each displayed residual path is nonempty. In every case W is a proper Hamiltonian set. If H-W were Hamiltonian, Hamilton paths on W and H-W would form a spanning two-cover of H. Hence H-W is non-Hamiltonian; the displayed inherited paths give a two-cover, so its path-cover number is two.

The global minimum-side hypothesis is not needed for this argument; the conclusion follows for every deletion cover whose displayed components have order at least three.
