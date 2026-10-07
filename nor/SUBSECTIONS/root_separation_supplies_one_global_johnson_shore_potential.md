# Root separation supplies one global Johnson-shore potential

## Metadata

- ID: root_separation_supplies_one_global_johnson_shore_potential
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 64
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Let V be the finite set of minimum-short-shore protected states after the antipodally closed normalization of root 61. For each state write S for its short shore and r_S for a chosen shore-oriented canonical protected root. Thus r_S=e_a-e_c with a in S and c outside S, and complement-reversal fixes S and r_S.

Apply the finite alternative theorem for vectors in the type-A space W. Exactly one of the following holds:

1. there is a nonzero coefficient vector lambda_S>=0 such that sum_S lambda_S r_S=0;
2. there is a linear functional w in W* such that w(r_S)>0 for every chosen canonical root.

The first case is a positive protected-root dependence and enters the existing root-cycle/hypersimplex extraction theory.

In the second case define the shore potential
Phi(S)=sum_{v in S} w_v.
If r_S=e_a-e_c and the forced Johnson successor is S^+=(S-{a}) union {c}, then
Phi(S^+)-Phi(S)=w_c-w_a=-w(r_S)<0.
Hence one single global linear potential strictly decreases along every canonical shore successor.

This is stronger than having a separately exposed potential at one realized shore. In particular, choose a realized minimum short shore minimizing Phi. Its forced successor S^+ cannot itself be a realized minimum short shore. Therefore every zero-free canonical root system exposes a globally minimal realized shore whose canonical Johnson edge leaves the entire extremal realized family.

Equivalently, if every canonical successor of every minimum short shore were again realized at the same extremal short-phase level, finiteness would force a directed Johnson cycle, hence a positive root dependence. No local rank or ad hoc phase potential is needed.

For closure, choose a Phi-minimal extremal witness and then maximize the threshold-compatible band inside that shore fiber. Any proved repair that stays within the minimum-short-shore family cannot decrease Phi below this state. The terminal protected root nevertheless points toward the strictly lower unrealized shore S^+. Thus the remaining realization theorem can be phrased as an extremal escape statement: at a Phi-minimal, maximal-band state, a fully-curved barrier must either realize the forbidden lower shore, close NOR, or emit enough additional protected roots to contradict the separating functional w.

This gives a common state class and common potential simultaneously: the short-shore family is antipodally closed, while Phi is supplied canonically by separation whenever root cancellation is absent.

## Frontier

- Development version when composed: None
- Development version now: 1
