# Human-proof replacement program for computational evidence

## Statement

Replace LINP's finite computational evidence, where mathematically worthwhile, by exact human arguments. Prioritize open structural conjectures and symmetric finite families; do not spend proof effort reproducing finite evidence whose intended conjecture has already been refuted.

## Body

Current triage of the pending computational-evidence corpus.

Humanized:
- 07a2a6d38eb9, order 4 portion: fd0820036003 gives a complete human classification of the four reduced Latin squares of order 4 and an explicit maximum-length P_5 in each TD(3,4).

Obsolete as support for the intended general conjecture:
- 37868c0561ad supports nullity_R(N)<=s, but 133243b355da gives a certified infinite human counterexample family.
- d2fa3947be65 supports fixed minimum-degree-four elimination of ascending nonspecial edges, but d6649d981b43 / 7564e287447b gives a certified infinite counterexample family.
- c0fd7d75893c supports a pointwise compensated terminal-degree bound a(v)<=3+h(v), but d5e0ab668a51 gives unbounded common-last-vertex ascending degree even with h(v)=0.
- 0bca0e3ad00b and f08a56b7e2cf support the unrestricted at-most-three ascending terminal-degree conjecture, but 58ae15cf5657 / 830b0775567f gives a certified counterexample with four. The structured three-center portion of b3941a078b4b remains useful as a sharpness family for global-density conjectures.

Genuinely open human-proof targets:
- 66cfc745df48 -> potential-oriented local bound 50b6278b9537. The certified rank localization a7b7670e955a and central-window packing 6959dc2c0376 reduce any four-edge counterexample to a narrow near-top-rank regime; a43332068faf further isolates tail-terminal or splice-blocked branches once certified.
- 957adb1bf082 -> maximum-rank nonspecial-edge degree conjecture 73679d821853. Existing opposite-end degree shortcuts are false, but clean entrance replacements and fixed-edge rotations remain available.
- d9ee4adc37d3 -> dense-core all-special conjecture 020f694f8767. Equality at the 2/3 threshold is a genuine obstruction; the target uses strict minimum degree above 2ell/3.
- 8910294f9e62 -> exact six-block deletion threshold in cyclic STS(13). Edge transitivity gives only the weaker general lower bound ceil(13/3)=5, so one additional structural argument is needed.
- 07a2a6d38eb9, order 5 portion, and 3c00d375433a, order 6: seek direct Latin-square/rainbow-path arguments rather than enumeration.
- e202b7528571: seek symbolic paths in the additive G0 lifts, ideally a uniform finite-field construction rather than separate q=2,4,8 witnesses.

The highest-value first target is 66cfc745df48 because a human proof of its underlying conjecture immediately feeds the exact 2/3 upper-bound route. The easiest finite target after order 4 appears to be the order-5 Latin-square case, but it still needs a self-contained classification or structural argument.
