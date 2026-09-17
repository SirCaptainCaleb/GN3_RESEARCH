# S9007 — Both-Singleton Sign Degeneracy Guardrail

## Theorem

Let `p` and `t` be distinct vertices of a Level-(1) boundary tournament. Under the standard signed-support convention, the disjoint singleton supports `(p)` and `(t)` always admit a formal balanced opposite-sign labelling.

Indeed, the two-vertex path `(t,p)` is automatically tight because it has no internal turn. Hence `(p)` may be viewed as head-signed by witness `t`, while `(t)` may be viewed as tail-signed by witness `p`.

Consequently, a bare balanced pair whose two supports are both singletons carries no three-vertex turn information by itself. Any theorem that treats such a mass-two floor as productive must use additional retained ancestry, witness structure, payment history, capture data, or another genuine geometric certificate.

## Proof

Take distinct vertices `p,t`.

The ordered path `(t,p)` has only two vertices, so there is no internal triple to test. It is therefore automatically a tight path.

Under the signed-support convention, this same two-vertex path certifies two opposite roles:

- `(p)` is head-signed by exterior witness `t`;
- `(t)` is tail-signed by exterior witness `p`.

The supports are disjoint, and each witness lies outside the singleton support it signs. Thus the two singleton supports form a formal balanced opposite-sign pair.

But the construction used no ordered triple at all. Therefore the bare pair records no internal turn geometry. In particular, merely obtaining a second singleton sign label, or reminting a singleton certificate without additional physical ancestry, cannot by itself constitute new geometric progress. ∎

## Why this is reusable

Singleton floors occur repeatedly at the bottom of signed-support descent arguments. This guardrail prevents a common logical overread: opposite singleton labels are automatically available from a two-vertex path, so the labels alone cannot certify a collision, obstruction, or new turn.

The useful information in a productive mass-two floor must therefore be the **ancestry attached to it**, not the anonymous singleton signs themselves.

## Scope and nonclaims

The theorem does not say that every ancestry-bearing mass-two floor is useless. A singleton floor may remain highly productive when it retains distinct physical witnesses, payment/capture history, source identity, or other certificates.

It says only that the bare two-singleton signed-support label is degenerate and must not be mistaken for independent geometry.

## Provenance

Rescued from the accepted degeneracy theorem historically recorded as `R444`. Corpus mining found `both-singleton floor` in 58 source files with 110 uses and `ancestry-bearing both-singleton floor` in 40 files with 65 uses, making the distinction between the bare label and ancestry-bearing geometry an unusually persistent project-wide guardrail.