# Two-lemma induction scheme for the dense-core all-special conjecture

## Statement

For ell>=4 define k_ell=floor(2ell/3)+1.

Suppose the following two statements hold for every ell.

EAR-TO-PROGRESS(ell):
Let H be P_ell-free with delta(H)>=k_ell. Let e be nonspecial of rank q<=ell-1 and P a q-edge path ending in e. If some v in V(P) has at least
  k_ell-floor(2(q+1)/3)
incident edges not contained in V(P),
then either
(i) e is actually special; or
(ii) H contains a nonspecial edge f with phi(f)>q; or
(iii) q=ell-1 and V(P)=V(H).

SPANNING-TOP(ell):
Every P_ell-free linear 3-graph H on exactly 2ell-1 vertices with delta(H)>=k_ell is all-special.

Then the dense-core all-special conjecture holds for every ell.

Moreover, by e6d318739fde, EAR-TO-PROGRESS is invoked only with exactly the amount of external attachment guaranteed inductively; no stronger ambient density statement is needed. Thus the grand conjecture reduces inductively to converting a quantitatively forced family of clean ears/one-contact chords into rank progress, plus the spanning top-rank base geometry.

## Body

Proceed by induction on ell. The small base ell=4 is already proved by 4218a20eafe9.

Assume the dense-core all-special conjecture for all smaller forbidden lengths and suppose H is a counterexample at ell, chosen with |V(H)| minimum. Choose a nonspecial edge e of maximum possible rank q, and a q-edge path P ending in e.

By e6d318739fde, either:
(A) P contains a vertex v with
d_H(v)-d_{H[V(P)]}(v)>=k_ell-floor(2(q+1)/3),
so in particular v has at least that many external incident edges; or
(B) q=ell-1 and P spans H, so |V(H)|=2ell-1.

In case (B), SPANNING-TOP(ell) contradicts the existence of e.

In case (A), apply EAR-TO-PROGRESS(ell). Alternative (i) contradicts the choice of e as nonspecial. Alternative (ii) contradicts maximality of q among nonspecial edges. Alternative (iii) is incompatible with case (A), except that it returns us to the spanning top-rank case already handled by SPANNING-TOP.

Thus no counterexample exists, completing the induction.

The significance is that all global induction bookkeeping is now finished. The only missing mathematics lies in two local geometric statements: external-ear rank progress, and the spanning top-rank core.
