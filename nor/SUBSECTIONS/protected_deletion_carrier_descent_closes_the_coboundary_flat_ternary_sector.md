# Protected deletion-carrier descent closes the coboundary-flat ternary sector

## Metadata

- ID: protected_deletion_carrier_descent_closes_the_coboundary_flat_ternary_sector
- Parent Section: directed_nor_union_closed_bridge
- Position: 187
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Closure theorem for the coboundary-flat alternating ternary sector. Assume a minimum counterexample exists. Choose any one-change deletion carrier O=(v_1,...,v_m) with word 0^p1^q and omitted coordinate x. By the audited endpoint results p,q>=4, and x is the unique perfect blocker with scan 1^(p+1)0^q. The protected endpoint-surgery theorem forces alpha(v_p,v_1,v_2)=1: otherwise the full order H=(v_p,v_1,...,v_{p-1},x,v_{p+1},...,v_m) is one-change. Since the forced value is 1, delete the first coordinate v_p from H. The resulting order O'=(v_1,...,v_{p-1},x,v_{p+1},...,v_m) spans V\{v_p}. Its word is exactly 0^(p-3)1^(q+3). Indeed w_1,...,w_{p-3}=0; alpha(v_{p-2},v_{p-1},x)=s_{p-2}=1; alpha(v_{p-1},x,v_{p+1})=1 because Q_{p-1} is fully curved and forces alpha(x,v_{p-1},v_{p+1})=w_{p-1}=0; alpha(x,v_{p+1},v_{p+2})=s_{p+1}=1; and all remaining untouched statuses w_{p+1},...,w_{m-2} are 1. Thus O' is another genuine one-change deletion carrier in the SAME minimum counterexample, now omitting v_p, with run lengths (p-3,q+3). Because the full instance is a counterexample, v_p is a perfect insertion blocker for O'. Therefore all audited minimum-counterexample conclusions apply again to O'. In particular both run lengths of every such flat-sector deletion carrier are at least four. Hence p-3>=4. Applying the same protected surgery to O' gives a carrier with first run p-6, then p-9, and so on. Inductively p-3k>=4 for every k, impossible for finite p. Therefore no minimum counterexample exists in the coboundary-flat pure-orientation ternary sector. Equivalently, directed ternary NOR holds whenever delta alpha=0. The proof is a terminating protected descent: each step changes the omitted coordinate but preserves a fully explicit one-change deletion witness, and no cyclic extremality, uncontrolled wrap surgery, or topological extraction is used.

## Frontier

- Development version when composed: None
- Development version now: 1
