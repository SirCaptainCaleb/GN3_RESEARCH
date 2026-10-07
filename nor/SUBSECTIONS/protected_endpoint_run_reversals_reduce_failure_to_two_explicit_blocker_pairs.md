# Protected endpoint-run reversals reduce failure to two explicit blocker pairs

## Metadata

- ID: protected_endpoint_run_reversals_reduce_failure_to_two_explicit_blocker_pairs
- Parent Section: directed_nor_union_closed_bridge
- Position: 182
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Protected endpoint-run reversal lemma in the minimum ternary counterexample. Let O=(v1,...,vm) be a one-change deletion order with word 0^p1^q, p,q>=3, and let x be its omitted perfect blocker. Then (x,O) has word 1,0^p,1^q and (O,x) has word 0^p,1^q,0. Reverse the vertex interval supporting the terminal 1-run in (x,O), namely (v_{p+1},...,v_m). Every internal 1-status becomes 0, every earlier 0-status is unchanged, and there is no reconnection at the right endpoint. The only uncontrolled statuses are A=alpha(v_{p-1},v_p,v_m) and B=alpha(v_p,v_m,v_{m-1}). If A=B=0, the full word is 1 followed only by 0s and NOR closes. Hence every counterexample forces (A,B)!=(0,0). Dually, reverse the vertex interval supporting the initial 0-run in (O,x), namely (v_1,...,v_{p+2}). Every internal 0-status becomes 1, the later 1-run is unchanged, and the final endpoint defect remains 0. The only uncontrolled reconnection statuses are C=alpha(v_2,v_1,v_{p+3}) and D=alpha(v_1,v_{p+3},v_{p+4}). If C=D=1, the full word is all 1s followed by the final 0 and NOR closes. Hence every counterexample forces (C,D)!=(1,1). These two blocker pairs are boundary-preserving certificates obtained from the same deletion witness; unlike local singleton bubbling, no additional outer window is silently changed. The next target is to combine coboundary flatness and the perfect-blocker tube to show the two forced blocker pairs cannot coexist, or to vary the deletion witness while keeping one ordered boundary pair fixed.

## Frontier

- Development version when composed: None
- Development version now: 1
