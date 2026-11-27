# Flagged erasure in parallel marked-set search

[Phase-gate model](model.md) · [Watrous bridge](../learning/WATROUS_BRIDGE.md) · [Marked-set theorem](https://github.com/GoGoKo699/Quantum-Parallel-Marked-Set/blob/main/science/flagged-erasure.md)

Both experiments prepare a probe, apply a parallel layer of diagonal oracle calls, and lose a physical register before the decoder can act. The loss flag gives the port position. The decoder then acts on a reduced state. The finite search experiment adds protected quantum memory and changes the requested output.

| | Delayed phase-gate retrieval | Flagged marked-address search |
| --- | --- | --- |
| Unknown operation | A fixed continuous qubit phase gate applied at each queried probe | A bare sign flip at one unknown address, applied at each queried port |
| Task after loss | Apply the gate to late data with exact announced success, including reference-entangled data | Identify the marked address with certainty, or recover superpositions of the queried states in the coherent variant |
| Stored quantum system | Surviving probes | Surviving ports and a protected register of dimension $`d`$ |
| What exactness constrains | Every accepted contribution lies on one unitary Choi ray | Different classical marks have orthogonal survivor supports. Coherent recovery also fixes the erased port's reduced state across code inputs |

## The same reduction gives different tests

Expand the erased port in its computational basis before taking the partial trace. For a mark $`m`$ and erased port $`i`$, write $`|\psi_{m,a}^{(i)}\rangle`$ for the subnormalized vector of surviving ports and protected memory conditioned on the lost basis address $`a`$. The receiver sees the state

```math
\rho_m^{(i)}=\sum_a |\psi_{m,a}^{(i)}\rangle\langle \psi_{m,a}^{(i)}|.
```

An exact classical receiver must distinguish the supports of these positive operators. For distinct marks $`m,n`$, their Hilbert–Schmidt overlap is

```math
\operatorname{Tr}\bigl(\rho_m^{(i)}\rho_n^{(i)}\bigr)
=\sum_{a,b}\bigl|\langle\psi_{m,a}^{(i)}\mid\psi_{n,b}^{(i)}\rangle\bigr|^2.
```

Every term must vanish. The conditions with $`a=b`$ give moment equations on probabilities. Those with $`a\ne b`$ also constrain how the probe amplitudes are arranged in the protected register. In the [phase-gate converse](proof.md#what-the-erasures-reveal), the analogous hidden basis expansion feeds each component into the successful completely positive map. Positivity forces its accepted Choi operator into the target unitary's rank-one support.

## What protected memory buys

For five addresses, one mark, three simultaneous calls and one arbitrary flagged port loss, [Quantum Parallel Marked Set](https://github.com/GoGoKo699/Quantum-Parallel-Marked-Set/blob/main/science/flagged-erasure.md) proves that dimension one is impossible and gives an explicit dimension-three preparation and receiver. All three calls, including the erased port, count toward the query budget. The protected qutrit survives independently of the queried ports and is accessed at decoding. Whether dimension two suffices for exact classical identification remains open.

The same construction recovers an arbitrary superposition of the five queried states, including a superposition entangled with a reference. That stronger task forces the erased port's marginal to be independent of the input, which yields a dimension-three lower bound. A classical mark output can also be used to apply the now-known reflection to later data. That operation and coherent recovery of the queried-state span have different input and output registers.

The derivation, qutrit preparation, decoder and lower bounds are in the [marked-set theorem](https://github.com/GoGoKo699/Quantum-Parallel-Marked-Set/blob/main/science/flagged-erasure.md). The [exact verifier](https://github.com/GoGoKo699/Quantum-Parallel-Marked-Set/blob/main/verification/check_flagged_erasure.py) checks all 750 cross-mark branch overlaps. Read Watrous §2.1.3 on partial trace, §2.2.2 on Choi representations and §3.1 on state discrimination alongside the [learning route](../learning/WATROUS_BRIDGE.md#compare-the-flagged-search-task).
