# Residual flat drift terminates by reversal minimality

## Metadata

- ID: residual_flat_drift_terminates_by_reversal_minimality
- Parent Section: directed_nor_union_closed_bridge
- Position: 208
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Residual flat drift terminates by reversal-minimality

Continue the setup of §206. Choose, among all one-change deletion carriers in a minimum coboundary-flat ternary counterexample, including reversals and global color complements, one whose normalized first run length
[
p
]
is globally minimum.

Section 206 shows that after a forced right replacement and the forced left replacement which follows it, the run profile either returns to ((p,q)) or undergoes the unique drift
[
(p,q)longmapsto(p+1,q-1).
	ag{1}
]

### Proposition

The drift (1) can occur only finitely many times. In fact along any chain of such two-step drifts it can occur at most
[
q-p
]
times.

### Proof

Because the minimum defining (p) ranges over reversals as well as color complements, every one-change deletion carrier with normalized run lengths
[
(a,b)
]
satisfies
[
age p,qquad bge p.
	ag{2}
]
Indeed the carrier itself gives (age p), while reversing it and complementing colors normalizes the reversed word to (0^b1^a), giving (bge p).

After (k) residual drifts the run profile is
[
(p+k,q-k).
]
Applying (2) to the second run gives
[
q-kge p.
]
Hence
[
kle q-p.
]

If another drift were attempted from the terminal profile with second run (p), it would create a deletion carrier with second run (p-1). Reversal and color complement would then give a normalized deletion carrier with first run (p-1), contradicting the global choice of (p).

Thus residual drift cannot lie on a directed cycle and cannot persist indefinitely. QED.

### Consequence

The only possible recurrent part of the minimum-run flat replacement dynamics consists of the same-profile two-step returns identified in §206:
[
d=e=2
qquad	ext{or}qquad
d=e=3.
]

Therefore termination of the coboundary-flat ternary sector has been reduced to ruling out, or escaping from, same-profile return cycles. No special blocker scan is required.

## Frontier

- Development version when composed: None
- Development version now: 1
