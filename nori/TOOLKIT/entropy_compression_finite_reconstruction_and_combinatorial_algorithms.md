# Entropy compression: finite reconstruction and combinatorial algorithms

**Summary:** Failures can reveal enough erased data to reconstruct the random input from a shorter history. Prove the decoder and count all histories; then compare against the number of random inputs. This can establish a finite successful construction without a monotone defect count.

## Statement

A randomized construction terminates with positive probability when its unsuccessful random inputs inject into strictly fewer final-state/history pairs. This primer follows Tao's account of Moser's entropy-compression argument, supplies a finite counting lemma and a fully decoded nonrepetitive-word construction, states the Moser–Tardos variable criterion, and lists the reconstruction and incidence obligations for LINP applications.

## Body

# Entropy compression in combinatorics — a primer following Tao

## The idea and sources

Terence Tao's *Moser's entropy compression argument* (5 August 2009) explains a termination method for randomized repair algorithms. A repair can create further defects; a monotone defect count is unnecessary. Instead, record enough information to reconstruct the consumed random choices. A bad configuration reveals information about the overwritten choices, allowing a shorter record. If every long run survived, uniformly random input strings would inject into too few final-state/record pairs, which is impossible. A recursive history can describe the next defect relative to the previous one, rather than name it globally.

Primary explanation:
https://terrytao.wordpress.com/2009/08/05/mosers-entropy-compression-argument/

Additional primary sources consulted:
- Moser and Tardos, *A constructive proof of the general Lovász Local Lemma*: https://arxiv.org/abs/0903.0544, especially Theorem 1.2.
- Esperet and Parreau, *Acyclic edge-coloring using entropy compression*: https://arxiv.org/abs/1206.1535. The constructive record-counting approach applies beyond the clause example in Tao's post.

The finite lemma and worked word construction below are independently supplied proofs. No SAT, MILP, or optimization program was run.

## 1. A finite counting lemma

Fix an instance and deterministic rules for choosing what to repair. Feed the algorithm independent symbols from an alphabet of size q. Let B_T be the length-T input strings on which the algorithm has not yet succeeded after consuming T symbols.

Suppose every such run has an encoding
E_T:B_T -> S_T × R_T
that is injective. S_T includes ALL final-state data needed to decode; R_T is the history. Then
|B_T|≤|S_T||R_T|,
and
Pr(not successful by T)≤|S_T||R_T|/q^T.

Proof. Count the output pairs of an injection and divide by the q^T equally likely inputs.

In particular, if |S_T|≤S and |R_T|≤C T^d α^T with α<q, then the survival probability tends to zero exponentially up to the polynomial factor. There is a finite successful input, and the random procedure succeeds almost surely. If a comparable summable bound holds for all T, its expected number of consumed symbols is finite.

This conclusion concerns the chosen randomized procedure. It does not assert that every possible input terminates or that every legal repair schedule terminates.

An initial random state can be included in the input count, and the final state must still be included in the output count. For variable-length logs, count the possible logs or use a uniquely decodable encoding; an informal “bits per repair” estimate is insufficient. The instance is fixed information shared by encoder and decoder, independent of the random tape.

## 2. The reconstruction obligation

For each step write down:
- the random choices consumed;
- the state entries changed or erased;
- the defect identity and any residual choices not determined by that identity;
- the order of repairs and any recursion/stack information.

Then define the inverse step explicitly. From the new state and log entry, recover the old state AND the fresh random symbols used to obtain the new state. Reverse the steps to reconstruct the complete tape.

A rare bad event is useful because it can determine some erased values. Rarity alone does not provide a decoder. If several old values fit the event, record which one occurred.

In the elementary clause example, a violated clause determines the old values of all its variables. The post-repair values identify the new random symbols. The economical history describes a newly damaged clause among the overlapping possibilities and records the recursion structure. Naming an arbitrary clause independently at every repair would generally lose the desired compression.

The relevant comparison is
random input information consumed > information needed to describe the failure history,
with bounded final-state and initial overhead accounted for.

## 3. A fully specified example: avoiding repeated consecutive blocks

A word is nonrepetitive if it has no consecutive factor XX with X nonempty. Fix a desired length n and alphabet size q.

Start with the empty word. Repeatedly append one uniform random letter. If this creates a square XX at the end, choose its half-length ℓ by a fixed rule, erase the LAST copy X, and record ℓ. If no square occurs, record 0. Stop as soon as the retained word has length n.

Invariant. The retained word is nonrepetitive. Before appending it was nonrepetitive, so every newly created square ends at the new letter. After erasing its last copy, the result is a prefix of the old word and is again nonrepetitive.

Decoder. Suppose the final word after a step and its record ℓ are known.
- If ℓ=0, remove its last letter; that letter is the consumed random input.
- If ℓ>0, the retained word ends in the FIRST copy X of length ℓ. Append that X to recover the word before erasure. Its last letter is the consumed input; removing that letter recovers the previous retained word.

Thus final word plus the sequence of half-lengths reconstructs the whole input tape.

Count. After T steps the retained length is
h_T=T-Σ_(i=1)^T ℓ_i≥0.
Therefore Σℓ_i≤T. The number of nonnegative integer T-tuples with this property is binom(2T,T), an upper bound on the possible logs. For a surviving run h_T<n, the number of possible retained words is at most
S_n=Σ_(h=0)^(n-1) q^h.
Hence
Pr(survival after T)≤S_n binom(2T,T)/q^T.

For q>4 this gives an exponential bound and finite expectation for each fixed n. For q=4, binom(2T,T)/4^T tends to zero, so the same elementary argument still proves existence and almost-sure success. This latter displayed estimate is not summable and does not by itself establish finite expected time.

This example is not an optimal alphabet bound. Its purpose is to show the entire proof: legal erasure, explicit decoder, and exact record count. Notice that the word length need not increase at every step.

## 4. The standard variable-model alternative

When the problem has mutually independent variables and bad events A depending on specified subsets, one may use Moser–Tardos directly. Resample all variables of a currently occurring event, leaving the others unchanged.

If numbers x_A in (0,1) satisfy
Pr(A)≤x_A ∏_(B∈Γ(A))(1-x_B),
where Γ(A) consists of OTHER events sharing variables with A, the expected number of resamplings of A is at most x_A/(1-x_A). The expected total is bounded by the sum of these quantities. A familiar sufficient symmetric condition is e p(d+1)≤1 when every bad event has probability at most p and at most d neighbors.

This theorem avoids having to design a bespoke compression proof when its variable-model assumptions apply. A custom erasure algorithm can use more detailed structure, but it needs its own correctness and history analysis. Permutation entries are not independent variables; the variable-model theorem cannot be applied to them unchanged.

## 5. Designing a useful compression argument

First decide the exact output: a coloring, assignment, path, decomposition, or another finite structure. A successful stopping state must actually have that property.

Choose random decisions with a uniform lower bound on available alternatives, or explicitly analyze their nonuniform distribution. Fix deterministic rules for selecting the next incomplete position and resolving competing defects. In a partial construction, erase only entries whose old values are recoverable from the retained entries and recorded defect.

Bound the number of compatible histories using the actual recursion, erasure lengths, and defect choices. A forest or walk record can be much smaller than an arbitrary sequence of global defect names, but this requires a proof of the record count.

Check that the construction can always take its next prescribed step until success. A dead end is another failure requiring an encoded repair; it cannot simply be omitted. Compare input count with history count and final-state count. State separately whether the conclusion is existence, positive success probability, almost-sure success, or an expected-time bound.

For nonuniform choices, cardinalities alone are insufficient. One may use exact input probabilities, an appropriate entropy inequality with a valid code, or a proved weighted record bound.

## 6. Possible LINP use and limits

Entropy compression is naturally compatible with finite sparse constructions; it does not require dense pattern limits. This makes it a plausible tool for randomized lower-bound constructions or path-building procedures that sometimes undo earlier choices.

For LINP, a candidate is a construction whose failure exposes a specified repeated entrance label, forbidden extra contact, or other reconstructible incidence pattern. One would need to show that:
1. every proposed extension is an edge of the given hypergraph, when constructing a path in a fixed instance;
2. erasing or replacing part of the path preserves all required linearity and distinctness conditions;
3. the failure data determine enough discarded choices to reconstruct them;
4. record growth is strictly smaller than the supply of random extension choices.

These are proposed application requirements, not a proved LINP algorithm. Linearity alone does not give a uniform bound on how many edges meet a high-degree vertex. A global longest-path condition may produce many dependent failures. Randomization does not turn a nonextendible path into an extendible one without a legitimate repair.

Entropy compression may establish termination even when defect counts fluctuate, but it cannot repair an invalid move or recover boundary data that were never recorded. In contrast to flag-algebra averaging, its main output can be an actual successful finite construction, provided the algorithm and decoder have been proved.

## 7. Failure checks

- Forgetting the final object, erased witness information, repair identities, or stack positions in the encoding.
- Assuming that “a failure is unlikely” means its overwritten data are uniquely determined.
- Counting only a preferred class of histories although the algorithm can generate others.
- Reusing an independence theorem after imposing dependent constraints on the random choices.
- Claiming every run terminates from a successful-input counting argument.
- Claiming polynomial expected time from mere existence or a nonsummable survival bound.
- Importing a coloring repair into a path problem without proving its incidence invariants.

A viable proof has three concrete objects: the construction, its inverse decoder, and a strict counting inequality. Those are the pieces to look for.


## Metadata

- ID: entropy_compression_finite_reconstruction_and_combinatorial_algorithms
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
