# From Watrous to exact phase-gate retrieval after erasure

An unknown phase is written into a register of probes. Some probes disappear before the data arrive. The receiver knows the lost positions and uses the surviving probes to apply a phase gate to the data. Its success flag certifies the complete gate on the supplied data, including any entanglement with a reference.

The educational anchor is **John Watrous, *The Theory of Quantum Information*, Cambridge University Press (2018)**. Section numbers follow the author's prepublication manuscript, whose preface is dated January 2018. The [author's page](https://cs.uwaterloo.ca/~watrous/TQI/) provides the manuscript and errata. See [front matter](https://cs.uwaterloo.ca/~watrous/TQI/TQI.frontmatter.pdf), [Chapter 1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.1.pdf), and [Chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf).

## Targeted reading

| Concept | Watrous section | Use in this project |
| --- | --- | --- |
| Tensor products, operators and the spectral theorem | §§1.1.1–1.1.3 | Organize the program into Hamming-weight eigenspaces and express a subspace contraction |
| Probability | §1.2.2 | Interpret a distribution of charges and condition on a lost subsystem |
| States, reductions and purifications | §§2.1.2–2.1.3 | Describe the surviving program and the data's inaccessible reference |
| Channels, Choi matrices and Kraus representations | §§2.2.1–2.2.3 | Express the exact accepted operation and control what each Kraus term can do |
| Measurements and outcomes | §§2.3.1–2.3.2 | Interpret the success flag and complete the instrument with a failure branch |

Watrous supplies the operator and channel language. The integer-phase Fourier argument, sampling calculation and intact-block design are developed in the [project's proof](../science/proof.md). The [related work](../references/RELATED_WORK.md) describes the inherited phase-gate storage method and distinguishes the exact delayed-data task from metrology and covariant recovery.

## An exact accepted operation

Watrous writes an adjoint as a star and writes a column vector as an ordinary vector. Here kets denote vectors, and a dagger denotes the adjoint. His Choi convention places the output factor first. The unnormalized Choi operator of a unitary channel is the outer product of the vectorized unitary with itself, so it has rank one. An accepted completely positive operation has Kraus operators $`K_a`$ with $`\sum_a K_a^\dagger K_a\preceq I`$. Its output trace is the probability of the success flag. A failure branch completes the instrument.

For a loss pattern $`S`$ and phase $`\phi`$, the accepted map on the late data equals a scalar $`p_S(\phi)`$ times the channel of $`U_\phi^{\otimes k}`$. Equality is on all operators on the data register. Tensoring both sides with the identity on an external reference extends the equality to entangled inputs. Testing the diagonal action on basis states would leave the relative phase untested.

If an accepted Choi operator is a positive sum with rank one, each nonzero summand has support on that same line. This fact applies to the terms from different decoder Kraus operators. It also applies to any decomposition of a mixed surviving program: whenever a component succeeds, its induced accepted map implements the same gate.

## From charge to a programmable phase

One use of $`U_\phi=\operatorname{diag}(1,e^{i\phi})`$ on an occupied probe contributes a factor $`e^{i\phi}`$. An $`N`$-probe program therefore has phase factor $`e^{im\phi}`$ in each orthogonal component of total Hamming weight $`m`$. Let $`w_m`$ denote the squared norm of that component. Keeping their coherent superposition matters because replacing it with the probability vector would remove the phase.

The late data require factor $`e^{i\ell\phi}`$ on their charge-$`\ell`$ subspace, for each $`\ell`$ from $`0`$ to $`k`$. Fix a retrieval label $`j`$. On data of charge $`\ell`$, take the program component with charge $`j+\ell`$. Its phase factors as

"```math"
e^{i(j+\ell)\phi}=e^{ij\phi}e^{i\ell\phi}.
"```"

When the filter balances the amplitudes across all data charges, the first factor is global on the accepted branch. Measuring $`j`$ then preserves the relative phases between data charges. Each $`j`$ spends at most the smallest population among the required consecutive program charges. The matching retrieval uses that amount, and the Fourier converse shows that any exact retriever has the same limit on a pure program. See the [worked example](WORKED_EXAMPLE.md) for an explicit four-label instrument.

## From a lost subsystem to the resource law

Partial trace can be calculated by expanding the program in a computational basis of the lost probes. The expansion gives a mixture of survivor programs labeled by the lost bit string. The receiver sees the positions only. For the converse the lost string is a mathematical conditioning variable. It gives a sample of the program's original charge and limits the average spread of the remaining charge. The exact filter needs probability spread across consecutive charges, so a small spread forces failure.

The construction takes a complementary route. A uniform superposition over one string of each possible weight provides a flat charge profile within each block. Every affected block can be discarded using the position flags. Intact blocks remain pure and independent across blocks, and their charge distributions convolve. The resulting spread supports enough overlapping charge windows to match the failure lower bound in order.

Follow the [30 milestones](MILESTONES.md) for the dependency order, the [worked example](WORKED_EXAMPLE.md) for a finite run, or the [science index](../science/README.md) for the exact statements and resource accounting.
