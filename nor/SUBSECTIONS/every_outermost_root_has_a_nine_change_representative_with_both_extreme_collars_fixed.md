# Every outermost root has a nine-change representative with both extreme collars fixed

## Metadata

- ID: every_outermost_root_has_a_nine_change_representative_with_both_extreme_collars_fixed
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 251
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Every outermost root has a nine-change representative with both extreme collars fixed

Let
\[
\pi=(v_1,\ldots,v_n)
\]
be a bad ternary order with first and last change positions
\[
p<q.
\]
Its outermost root is
\[
D(\pi)=e_{v_p}-e_{v_{q+3}}.
\]

We show that, in a minimum counterexample, this same physical root has a witness with uniformly bounded change complexity while preserving the full outside order and the four-coordinate certificates of both extreme changes.

### Long active interval

Assume first
\[
q-p\ge 7.
\]
Freeze the left collar
\[
L=(v_p,v_{p+1},v_{p+2},v_{p+3})
\]
and the right collar
\[
R=(v_q,v_{q+1},v_{q+2},v_{q+3}).
\]
Let
\[
S=\{v_{p+4},\ldots,v_{q-1}\}
\]
be the middle core.

The set \(S\) is proper. By minimum-counterexample induction, the induced ternary instance on \(S\) has a NOR-good order \(g(S)\), whose internal status word has at most one change.

Replace only the middle core:
\[
(v_1,\ldots,v_{p+3})\,
(v_{p+4},\ldots,v_{q-1})\,
(v_q,\ldots,v_n)
\]
by
\[
(v_1,\ldots,v_{p+3})\,
g(S)\,
(v_q,\ldots,v_n).
\]
Call the new full order \(\pi'\).

### The outermost root is unchanged

A ternary window meeting the reordered core can start only at rank \(p+2\) or later and can end only at rank \(q+1\) or earlier.

Therefore:

- every status before rank \(p+2\) is unchanged;
- in particular the two statuses at ranks \(p,p+1\) are unchanged, so the original first change at \(p\) survives and no earlier change is created;
- every status after rank \(q-1\) is unchanged;
- in particular the two statuses at ranks \(q,q+1\) are unchanged, so the original last change at \(q\) survives and no later change is created.

Hence \(p\) and \(q\) remain the first and last changes of \(\pi'\), and
\[
\boxed{D(\pi')=D(\pi).}
\]

The entire prefix before \(v_p\), the entire suffix after \(v_{q+3}\), and both four-coordinate extreme collars are literally fixed.

### Uniform change bound

Between the two frozen extreme changes, the status word splits into five pieces:

1. the fixed left pair \(c_p,c_{p+1}\), containing exactly one change;
2. two left core-crossing statuses;
3. the internal status word of \(g(S)\), containing at most one change;
4. two right core-crossing statuses;
5. the fixed right pair \(c_q,c_{q+1}\), containing exactly one change.

Each two-status crossing piece has at most one internal change. There are four interfaces between the five pieces. Therefore the total number of changes is at most
\[
1+1+1+1+1+4=9.
\]

Thus \(\pi'\) is either NOR-good, closing the problem, or is a bad witness of the SAME outermost root with at most nine changes.

### Short active interval

If \(q-p\le 6\), the status interval from \(p\) through \(q+1\) has at most eight entries, hence at most seven changes already. No replacement is needed.

### Theorem

In a minimum counterexample, every realized outermost root
\[
e_x-e_y
\]
admits a full-order witness with:

- the same outermost root \(e_x-e_y\);
- at most nine ternary changes;
- the same exterior coordinate order outside the original multichange interval;
- the same four-coordinate left and right extreme-change collars.

Therefore every edge of the flag-compatible root cycle of §§244–249 may be represented inside a uniformly bounded-change witness class without changing the physical directed cycle.

### Closure relevance

This is stronger than a bounded disturbance statement because it preserves the exact root used by the topological dependence and preserves both extreme provenance collars. It converts the remaining flag-cycle splice theorem into a finite-band problem: each cycle edge can be worked on by the existing endpoint, singleton, flat-transport, and fully-curved barrier surgeries while its algebraic root and neighboring exterior data remain fixed.

## Frontier

- Development version when composed: None
- Development version now: 1
