# Reversing a minimum first phase compresses a long double-full endpoint band to a one-or-two-window deletion defect

## Metadata

- ID: reversing_a_minimum_first_phase_compresses_a_long_double_full_endpoint_band_to_a_one_or_two_window_deletion_defect
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 174
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Reversing a minimum first phase compresses a long double-full endpoint band to a one-or-two-window deletion defect

Continue with root §172. Let

O=(v_1,...,v_m)

be a globally minimum-first one-change deletion witness with word

0^p 1^q,

normalized under reversal and color complement, and assume p>=4.

Since reversal/complement exchanges the two run lengths, global minimality gives

q>=p>=4.

Let x be the omitted coordinate. Prepending x gives the endpoint-defect full order

F=(x,v_1,...,v_m)

with word

1,0^p,1^q.

Root §172 shows that both boundaries of the isolated 0^p band are fully curved, but the calculation below only uses the word structure.

### Reverse the whole zero-phase coordinate interval

The p zero windows of O are supported by the p+2 coordinate interval

Z=(v_1,...,v_{p+2}).

Reverse exactly Z, keeping x and the remaining suffix fixed:

F^R=
(x,
 v_{p+2},v_{p+1},...,v_1,
 v_{p+3},v_{p+4},...).

Every ternary window wholly internal to Z is the reversal of an old 0-window, hence has color 1.

Put

L=alpha(x,v_{p+2},v_{p+1}),

gamma=alpha(v_2,v_1,v_{p+3}),

delta=alpha(v_1,v_{p+3},v_{p+4}).

Because q>=4, all these windows exist and at least two unchanged 1-windows remain to the right.

The exact new full word is

L, 1^p, gamma, delta, 1^(q-2).

Indeed:
- L is the unique new left crossing window;
- the next p windows are reversed internal zero-phase windows, hence all 1;
- gamma and delta are the two new right crossing windows;
- every later window is an unchanged old 1-window.

### Immediate closure criterion

If

(gamma,delta)=(1,1),

then F^R has word

L,1,1,...,1,

which has at most one change regardless of L. Hence NOR closes.

Therefore in a counterexample

(gamma,delta)!=(1,1).

### Delete the original omitted coordinate

Remove x from F^R. The resulting order on V minus {x} is

O^R=
(v_{p+2},...,v_1,v_{p+3},v_{p+4},...),

with exact word

1^p, gamma, delta, 1^(q-2).

Since (gamma,delta)!=(1,1), this is a near-good deletion order whose entire defect is confined to the two displayed crossing bits.

More precisely:
- 00 gives one isolated 0-run of length two;
- 01 gives one isolated 0-window;
- 10 gives one isolated 0-window.

Thus every unresolved state produced by reversing the arbitrarily long minimum first phase has exactly two changes and an isolated bad band of length one or two.

### Compression theorem

A globally minimum-first deletion witness with p>=4 admits the following dichotomy:

1. reversing its first-phase coordinate interval gives a full-support one-change order and closes NOR; or
2. the same reversal gives, after deleting x, an order with a single isolated defect band of length at most two.

The reduction is independent of p and q after the reversal: all long-range complexity is compressed into the two physical bits gamma,delta.

Together with the double-full boundary theorem §172, this converts the arbitrary-scan long endpoint obstruction into a bounded isolated-band extraction problem without assuming a perfect blocker scan.

No claim is made here that every length-one/two isolated defect is already repairable to a good deletion witness; that is the remaining local task.

## Frontier

- Development version when composed: None
- Development version now: 1
