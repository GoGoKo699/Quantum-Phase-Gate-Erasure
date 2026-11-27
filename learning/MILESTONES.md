# Project understanding map

These 30 milestones explain how to retain an unknown phase gate across flagged probe losses and apply it exactly to data that arrive later. The [Watrous bridge](WATROUS_BRIDGE.md) identifies the textbook sections and connects them to the project's methods. The [worked example](WORKED_EXAMPLE.md) follows a complete ten-probe experiment. The [science index](../science/README.md) links the proofs, and [flagged marked-address search](../science/flagged-search.md) compares a different receiver built on the same partial trace.

The **11 background/preliminaries milestones** assemble the phase orbit, the loss model, the heralded operation and the necessary probability tools. The **19 narrative/innovation milestones** start with the exact pure-program filter. They build the loss lower bound and the construction before bringing the finite advantage and implementation into the same account.

| Phase | Milestones | Connection |
| --- | --- | --- |
| Background/preliminaries | [M01](#m01-a-phase-gate-query)–[M04](#m04-flagged-loss-and-reduction) | Phase queries, coherent charge and the physical loss channel |
| Background/preliminaries | [M05](#m05-late-data-and-an-external-reference)–[M07](#m07-rank-one-in-the-choi-representation) | The late-input guarantee and the structure of accepted operations |
| Background/preliminaries | [M08](#m08-fourier-coefficients-of-phase-orbits)–[M11](#m11-the-complete-experimental-timeline) | Fourier and probability tools in the complete experimental timeline |
| Narrative/innovation | [M12](#m12-the-charge-resolved-pure-program)–[M16](#m16-the-exact-lossless-optimum) | Optimal exact retrieval from a pure program and the lossless limit |
| Narrative/innovation | [M17](#m17-the-mixed-survivor-program)–[M21](#m21-from-average-to-worst-pattern) | The worst-pattern bound from the charge information in the lost probes |
| Narrative/innovation | [M22](#m22-build-a-uniform-charge-ladder)–[M26](#m26-dense-erasures-and-exact-feasibility) | The intact-block construction, pooled charge and dense-loss regime |
| Narrative/innovation | [M27](#m27-ten-calls-and-two-late-data-qubits)–[M30](#m30-the-complete-loss-and-batch-law) | Finite advantage, implementation and the finished resource account |

## Phase I · Background and preliminaries

### M01 A phase-gate query

**Central question.** What does one interrogation supply?

**Understanding target.** Describe the action of the unknown gate on each basis vector and on a superposition. Identify the common unknown phase shared by all query calls.

**Dependencies.** None within this map.

**Conceptual connection.** The query writes a relative phase into the probe only when the preparation has coherence between distinct charges.

**Source pointers.** Watrous §§2.1.2 and 2.2.1 · [Operational model](../science/model.md).

### M02 Charge of a computational basis string

**Central question.** Why does an occupation count multiply the phase angle?

**Understanding target.** Obtain the total Hamming-weight generator from the tensor power of the gate. Identify both the eigenvalue and its degenerate subspace.

**Dependencies.** [M01](#m01-a-phase-gate-query).

**Conceptual connection.** All basis strings of the same weight receive the same scalar, which is why weight, rather than the string itself, labels the phase harmonics.

**Source pointers.** Watrous §§1.1.1–1.1.3 · [Watrous bridge](WATROUS_BRIDGE.md).

### M03 Relative phases between charge sectors

**Central question.** What does a coherent program retain that a weight histogram loses?

**Understanding target.** Separate a charge distribution from the superposition of sector vectors that realizes it. Explain why measuring the weight during storage would erase the useful relative phases.

**Dependencies.** [M02](#m02-charge-of-a-computational-basis-string).

**Conceptual connection.** The histogram will govern retrieval probabilities even though retrieval requires a coherent state.

**Source pointers.** Watrous §2.1.2 · [Watrous bridge](WATROUS_BRIDGE.md) · [Scientific proof](../science/proof.md).

### M04 Flagged loss and reduction

**Central question.** Which parts of the pre-loss state remain accessible?

**Understanding target.** Distinguish the survivor register from the erased subsystem and apply partial trace to the latter. Identify the erasure positions as the classical side information.

**Dependencies.** [M02](#m02-charge-of-a-computational-basis-string), [M03](#m03-relative-phases-between-charge-sectors).

**Conceptual connection.** Loss acts on physical probes, so an erased carrier can remove coherence even when its location is known.

**Source pointers.** Watrous §2.1.3 · [Operational model](../science/model.md).

### M05 Late data and an external reference

**Central question.** Which input correlations count in a correct gate?

**Understanding target.** Describe data that can arrive already entangled with an inaccessible reference. Formulate gate correctness as a map identity on the complete data register.

**Dependencies.** [M01](#m01-a-phase-gate-query), [M04](#m04-flagged-loss-and-reduction).

**Conceptual connection.** The phase gate must act correctly on off-diagonal operators, which a test of basis populations leaves unconstrained.

**Source pointers.** Watrous §§2.1.2–2.1.3 and 2.2.1 · [Operational model](../science/model.md).

### M06 Success as a quantum instrument

**Central question.** What exactly does the receiver's success flag certify?

**Understanding target.** Read a trace-nonincreasing completely positive map as the accepted branch. Interpret its trace as the success probability and recover the corresponding conditional output.

**Dependencies.** [M05](#m05-late-data-and-an-external-reference).

**Conceptual connection.** A scalar times a unitary channel fixes the conditional gate and makes the probability independent of the input data.

**Source pointers.** Watrous §§2.2.1–2.2.2 and 2.3.1–2.3.2 · [Watrous bridge](WATROUS_BRIDGE.md) · [Operational model](../science/model.md).

### M07 Rank one in the Choi representation

**Central question.** Why must every successful contribution implement the same channel?

**Understanding target.** Use the rank-one Choi operator of a unitary and positivity to localize every term of a successful Kraus decomposition to one line.

**Dependencies.** [M05](#m05-late-data-and-an-external-reference), [M06](#m06-success-as-a-quantum-instrument).

**Conceptual connection.** Averaging positive terms cannot conceal a branch that applies a different channel.

**Source pointers.** Watrous §2.2.2 · [Watrous bridge](WATROUS_BRIDGE.md) · [Scientific proof](../science/proof.md).

### M08 Fourier coefficients of phase orbits

**Central question.** How can a fixed receiver be constrained for every unknown phase?

**Understanding target.** Read the dependence on the unknown angle as a finite Fourier expansion. Use orthogonality to equate two harmonic coefficients and use Parseval's identity to average the squared amplitude.

**Dependencies.** [M02](#m02-charge-of-a-computational-basis-string), [M03](#m03-relative-phases-between-charge-sectors).

**Conceptual connection.** Exactness for the continuous phase forces a relation between program harmonics and data charges.

**Source pointers.** [Watrous bridge](WATROUS_BRIDGE.md) · [Scientific proof](../science/proof.md).

### M09 Local mass and shifted laws

**Central question.** How do profiles expose a bottleneck even at fixed total mass?

**Understanding target.** Evaluate a profile's mass in consecutive charge windows and compare it with its translate using total variation. Use a half-line event to isolate one window.

**Dependencies.** [M03](#m03-relative-phases-between-charge-sectors).

**Conceptual connection.** When the receiver needs several adjacent harmonics at once, a concentration measure is more informative than the dimension of the program alone.

**Source pointers.** Watrous §1.2.2 · [Scientific proof](../science/proof.md).

### M10 Conditional variance and sampling

**Central question.** How can a partial observation constrain the spread of the full charge?

**Understanding target.** Interpret conditional variance as the minimum mean-squared error available from the conditioning variables. Recognize sampling without replacement in a uniformly selected subset of probe indices.

**Dependencies.** [M02](#m02-charge-of-a-computational-basis-string), [M04](#m04-flagged-loss-and-reduction), [M09](#m09-local-mass-and-shifted-laws).

**Conceptual connection.** The lost probe population supplies a hypothetical estimator, which can bound survivor charge fluctuations without modeling a physical measurement.

**Source pointers.** Watrous §1.2.2 · [Scientific proof](../science/proof.md).

### M11 The complete experimental timeline

**Central question.** Where does the unknown gate act, and when may processing depend on the loss flag?

**Understanding target.** Order initial probe preparation, parallel interrogation, flagged erasure, arrival of the data, and retrieval. Identify the optimization over a universal probe preparation and flag-dependent decoders.

**Dependencies.** [M04](#m04-flagged-loss-and-reduction), [M05](#m05-late-data-and-an-external-reference), [M06](#m06-success-as-a-quantum-instrument), [M08](#m08-fourier-coefficients-of-phase-orbits), [M10](#m10-conditional-variance-and-sampling).

**Conceptual connection.** The chronology identifies the protected information as a gate program. There is no opportunity to encode the late data or compress the program between interrogation and loss.

**Source pointers.** [Operational model](../science/model.md) · [Science index](../science/README.md).

## Phase II · Narrative and innovation

### M12 The charge-resolved pure program

**Central question.** Which parts of a pure query resource matter for exact retrieval?

**Understanding target.** Expand a pure program as orthogonal sector vectors with their phase harmonics and squared norms. Separate each known direction within a sector from its phase-dependent coefficient.

**Dependencies.** [M03](#m03-relative-phases-between-charge-sectors), [M08](#m08-fourier-coefficients-of-phase-orbits), [M11](#m11-the-complete-experimental-timeline).

**Conceptual connection.** Even when a sector has large dimension, a fixed pure program occupies one direction there. The proof can therefore derive a scalar probability constraint per sector.

**Source pointers.** [Scientific proof](../science/proof.md) · [Watrous bridge](WATROUS_BRIDGE.md).

### M13 A common amplitude for every data charge

**Central question.** Why do the data sectors compete for consecutive program charges?

**Understanding target.** Use the rank-one branch constraint to require a common scalar amplitude after the desired phase is factored out. Match the Fourier order of this amplitude across all data charges.

**Dependencies.** [M07](#m07-rank-one-in-the-choi-representation), [M08](#m08-fourier-coefficients-of-phase-orbits), [M12](#m12-the-charge-resolved-pure-program).

**Conceptual connection.** In one branch of label j, the program must provide charge j plus each possible data weight.

**Source pointers.** [Scientific proof](../science/proof.md) · [Watrous bridge](WATROUS_BRIDGE.md).

### M14 The overlap bound

**Central question.** What limits the probability paid out by one retrieval label?

**Understanding target.** Apply the Kraus contraction constraint at each charge to bound the common Fourier amplitude by the least available sector population. Sum over the labels using Parseval.

**Dependencies.** [M06](#m06-success-as-a-quantum-instrument), [M12](#m12-the-charge-resolved-pure-program), [M13](#m13-a-common-amplitude-for-every-data-charge).

**Conceptual connection.** The smallest mass in each required window is the bottleneck that any exact receiver must obey.

**Source pointers.** [Scientific proof](../science/proof.md).

### M15 A filter that attains the overlap

**Central question.** How can a fixed decoder realize every allowed label?

**Understanding target.** For each label, select the appropriate program direction conditioned on the data charge and rescale to the same amplitude across charges. Show that the operators can be completed to an instrument.

**Dependencies.** [M12](#m12-the-charge-resolved-pure-program), [M13](#m13-a-common-amplitude-for-every-data-charge), [M14](#m14-the-overlap-bound).

**Conceptual connection.** The accepted label identifies a global program phase. The receiver preserves the data's relative phases while learning the label.

**Source pointers.** [Scientific proof](../science/proof.md) · [Implementation](../science/implementation.md) · [Worked example](WORKED_EXAMPLE.md).

### M16 The exact lossless optimum

**Central question.** What success is possible before there is an erasure penalty?

**Understanding target.** Relate the window-overlap objective to counts of intervals in the profile's superlevel sets. Explain why a uniform charge distribution attains the bound for every full data batch.

**Dependencies.** [M14](#m14-the-overlap-bound), [M15](#m15-a-filter-that-attains-the-overlap).

**Conceptual connection.** The lossless task has an exact baseline against which a physical loss penalty can be measured.

**Source pointers.** [Scientific proof](../science/proof.md) · [Related work](../references/RELATED_WORK.md).

### M17 The mixed survivor program

**Central question.** How does an exact-gate constraint pass through partial trace?

**Understanding target.** Expand the erased subsystem in its computational basis to obtain pure survivor components with angle-independent mixing probabilities. Use Choi positivity to apply exactness separately to their nonzero accepted branches.

**Dependencies.** [M04](#m04-flagged-loss-and-reduction), [M07](#m07-rank-one-in-the-choi-representation), [M12](#m12-the-charge-resolved-pure-program), [M14](#m14-the-overlap-bound).

**Conceptual connection.** The proof can analyze conditional charge distributions even when the actual receiver cannot see which component represents the lost bits. The same expansion gives hidden-address components for finite marked-set discrimination, where supports for different marks must be orthogonal.

**Source pointers.** [Scientific proof](../science/proof.md).

### M18 Failure as missing overlap

**Central question.** How does charge concentration force a heralded failure?

**Understanding target.** Upper bound the full-window success by an endpoint overlap. Connect its complement to total variation of the profile and a charge shift, then to the largest mass inside a data-width window.

**Dependencies.** [M09](#m09-local-mass-and-shifted-laws), [M14](#m14-the-overlap-bound), [M17](#m17-the-mixed-survivor-program).

**Conceptual connection.** A profile supported in too narrow a charge range cannot serve one coherent branch for widely separated data weights.

**Source pointers.** [Scientific proof](../science/proof.md).

### M19 A variance-to-window bound

**Central question.** Why must a narrow profile place substantial mass in a single window?

**Understanding target.** Cover a central interval carrying fixed probability by windows of width equal to the batch charge diameter. Read the lower bound on maximum window mass in terms of the conditional standard deviation.

**Dependencies.** [M10](#m10-conditional-variance-and-sampling), [M18](#m18-failure-as-missing-overlap).

**Conceptual connection.** The variance of the underlying charge law now constrains an operational failure probability.

**Source pointers.** [Scientific proof](../science/proof.md).

### M20 What the erased sample reveals

**Central question.** How much conditional charge spread can an arbitrary probe leave behind?

**Understanding target.** Average the lost locations uniformly for the lower-bound argument. At fixed occupied positions derive the sampling variance of the number of occupied sites among the lost probes.

**Dependencies.** [M10](#m10-conditional-variance-and-sampling), [M17](#m17-the-mixed-survivor-program), [M19](#m19-a-variance-to-window-bound).

**Conceptual connection.** This calculation covers asymmetric and entangled preparations because their computational basis probabilities define the full bit string for the proof.

**Source pointers.** [Scientific proof](../science/proof.md) · [Operational model](../science/model.md).

### M21 From average to worst pattern

**Central question.** Why does a random pattern in the proof bound a worst-case task?

**Understanding target.** Combine the sampling mean-squared error, conditional variance and convexity bounds to lower bound average failure. Use that average to identify the worst-pattern constraint.

**Dependencies.** [M19](#m19-a-variance-to-window-bound), [M20](#m20-what-the-erased-sample-reveals).

**Conceptual connection.** A mathematical average provides a certificate for adversarial flags without requiring the physical losses to be random.

**Source pointers.** [Scientific proof](../science/proof.md) · [Operational model](../science/model.md).

### M22 Build a uniform charge ladder

**Central question.** How can a length-L block occupy every charge with the same weight?

**Understanding target.** Prepare one coherent string per weight by increasing the length of an occupied prefix. Match each string's known preparation amplitude and acquired phase to its ladder charge.

**Dependencies.** [M02](#m02-charge-of-a-computational-basis-string), [M03](#m03-relative-phases-between-charge-sectors), [M12](#m12-the-charge-resolved-pure-program), [M16](#m16-the-exact-lossless-optimum).

**Conceptual connection.** This preparation realizes a broad, flat profile with one phase query per supplied probe.

**Source pointers.** [Implementation](../science/implementation.md) · [Worked example](WORKED_EXAMPLE.md).

### M23 Discard affected blocks

**Central question.** What makes a single preparation useful against every loss pattern?

**Understanding target.** Allocate disjoint independent blocks and discard any block with an erased probe. Count how many whole blocks are guaranteed to survive under the allowed loss budget.

**Dependencies.** [M04](#m04-flagged-loss-and-reduction), [M11](#m11-the-complete-experimental-timeline), [M22](#m22-build-a-uniform-charge-ladder).

**Conceptual connection.** The loss flags locate entire usable programs. The construction collects them without conditioning on their individual charges.

**Source pointers.** [Scientific proof](../science/proof.md) · [Implementation](../science/implementation.md).

### M24 Pooling intact ladders

**Central question.** Why is one collective retrieval useful across several intact blocks?

**Understanding target.** Convolve the independent block charge distributions to obtain the squared norms in each total sector. Describe the simultaneous use of multiple blocks without revealing their separate charges.

**Dependencies.** [M15](#m15-a-filter-that-attains-the-overlap), [M22](#m22-build-a-uniform-charge-ladder), [M23](#m23-discard-affected-blocks).

**Conceptual connection.** A sum of independent uniform charges has a well-behaved profile and lets the receiver exploit the combined width.

**Source pointers.** [Scientific proof](../science/proof.md) · [Implementation](../science/implementation.md).

### M25 From convolution to an attainable failure scale

**Central question.** How many useful charge windows can the intact blocks support?

**Understanding target.** Use unimodality to express the exact overlap loss as the largest batch-width window mass. Connect Fourier anticoncentration of the convolution to the upper bound on this mass.

**Dependencies.** [M08](#m08-fourier-coefficients-of-phase-orbits), [M18](#m18-failure-as-missing-overlap), [M24](#m24-pooling-intact-ladders).

**Conceptual connection.** Pooling balanced blocks makes the probability per charge small. The resulting success matches the sparse-loss converse in order.

**Source pointers.** [Scientific proof](../science/proof.md).

### M26 Dense erasures and exact feasibility

**Central question.** What survives when losses are too extensive for large intact blocks?

**Understanding target.** Use fair single-qubit probes to obtain a binomial charge width. Read the surviving charge range to identify when a joint exact gate has strictly positive success at all.

**Dependencies.** [M16](#m16-the-exact-lossless-optimum), [M18](#m18-failure-as-missing-overlap), [M21](#m21-from-average-to-worst-pattern), [M25](#m25-from-convolution-to-an-attainable-failure-scale).

**Conceptual connection.** The dense-loss construction completes the order bound. The exact feasibility threshold has a different meaning from a constant-order bound on failure.

**Source pointers.** [Operational model](../science/model.md) · [Scientific proof](../science/proof.md).

### M27 Ten calls and two late data qubits

**Central question.** Where does the finite product-probe advantage come from?

**Understanding target.** Trace each retained Fourier label for the two-block example. Calculate the success probability, then apply the product-probe Fourier inequality with unequal local occupations allowed.

**Dependencies.** [M15](#m15-a-filter-that-attains-the-overlap), [M18](#m18-failure-as-missing-overlap), [M22](#m22-build-a-uniform-charge-ladder), [M23](#m23-discard-affected-blocks), [M26](#m26-dense-erasures-and-exact-feasibility).

**Conceptual connection.** The worked separation shows what the entangled preparation buys at the same query count, loss pattern budget and joint gate guarantee.

**Source pointers.** [Worked example](WORKED_EXAMPLE.md) · [Scientific proof](../science/proof.md) · [Verification](../verification/README.md).

### M28 Choose the block size

**Central question.** Which design tradeoff does the loss budget create?

**Understanding target.** Relate the width of one ladder to the number of blocks a loss pattern can spoil. Explain why larger blocks can help at low loss and why the receiver needs a guarantee on how many survive.

**Dependencies.** [M21](#m21-from-average-to-worst-pattern), [M22](#m22-build-a-uniform-charge-ladder), [M23](#m23-discard-affected-blocks), [M24](#m24-pooling-intact-ladders), [M25](#m25-from-convolution-to-an-attainable-failure-scale), [M26](#m26-dense-erasures-and-exact-feasibility).

**Conceptual connection.** The construction balances within-block quantum coherence against independent surviving blocks. Both sources of width enter one query-resource account.

**Source pointers.** [Implementation](../science/implementation.md) · [Scientific proof](../science/proof.md).

### M29 Implementation, attribution and limits

**Central question.** Which claims concern queries, circuits or other phase tasks?

**Understanding target.** Separate the query budget from preparation, decoder rotations, and workspace. Compare delayed exact application with lossless programming, approximate replication, phase estimation and pre-encoded data recovery. In the sister task, distinguish the protected qutrit from the queried ports and compare classical identification with coherent recovery.

**Dependencies.** [M11](#m11-the-complete-experimental-timeline), [M16](#m16-the-exact-lossless-optimum), [M21](#m21-from-average-to-worst-pattern), [M26](#m26-dense-erasures-and-exact-feasibility), [M28](#m28-choose-the-block-size).

**Conceptual connection.** The distinctions identify what the optimal scaling certifies and which assumptions allow its use in a device model.

**Source pointers.** [Implementation](../science/implementation.md) · [Related work](../references/RELATED_WORK.md) · [Flagged marked-address search](../science/flagged-search.md).

### M30 The complete loss and batch law

**Central question.** How do the exact filter, worst-pattern bound and explicit probes form one result?

**Understanding target.** Reconstruct the experiment and its all-regimes failure scale from the earlier milestones. Identify the no-loss endpoint, the strictly positive success region and the finite product-probe separation.

**Dependencies.** [M16](#m16-the-exact-lossless-optimum), [M21](#m21-from-average-to-worst-pattern), [M25](#m25-from-convolution-to-an-attainable-failure-scale), [M26](#m26-dense-erasures-and-exact-feasibility), [M27](#m27-ten-calls-and-two-late-data-qubits), [M28](#m28-choose-the-block-size), [M29](#m29-implementation-attribution-and-limits).

**Conceptual connection.** Program charge spread connects the method and the limitation. Loss narrows the spread that any probe can reliably retain, and intact blocks preserve enough usable spread to match the scaling.

**Source pointers.** [Science index](../science/README.md) · [Operational model](../science/model.md) · [Scientific proof](../science/proof.md) · [Verification](../verification/README.md).
