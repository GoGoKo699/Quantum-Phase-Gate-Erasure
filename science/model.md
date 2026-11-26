# Operational model

A device can call an unknown qubit phase gate now, but the qubits that need the gate arrive later. The probe register can lose physical qubits between these two events. The aim is to apply the gate on an announced subset of runs with perfect conditional accuracy.

## Order of operations

1. Prepare an arbitrary $`N`$-qubit probe state, independent of the unknown phase. The preparation can entangle any of the probe qubits.
2. Apply $`U_\phi=|0\rangle\langle0|+e^{i\phi}|1\rangle\langle1|`$ once on each probe in parallel, using the same fixed unknown $`\phi`$.
3. A subset $`S`$ of $`t`$ probes is erased. The decoder receives its positions as a classical flag. Between interrogation and this erasure there is no gate or compression step. The lost subsystems are traced out and there is no protected stored quantum register.
4. Receive the $`k`$ data qubits and run a known instrument on the data, surviving probes and fresh ancillary systems. The data may be entangled with an inaccessible reference.

The set $`S`$ may be any subset with the stated size. For each such fixed set the guarantee holds uniformly in $`\phi`$. The flag gives the positions only. The receiver has no later call to the unknown gate. Shared classical randomness independent of the unknown phase is allowed.

## Exactness and failure

For every $`\phi`$ and $`S`$, the successful completely positive map on the data must satisfy

```math
\mathcal A_{S,\phi}=p_S(\phi)\,\mathcal U_\phi^{\otimes k},
\qquad \mathcal U_\phi(X)=U_\phi XU_\phi^\dagger .
```

The equality is an equality of linear maps. It ensures exact action on a joint state with a reference as well as success probability independent of the data. An arbitrary failed-data channel is allowed. The optimum is

```math
f^*_{N,t,k}=\inf_{\text{allowed protocols}}
\sup_{|S|=t,\;\phi\in[0,2\pi)} \bigl(1-p_S(\phi)\bigr).
```

The receiver may be specific to the loss pattern. The probe preparation is common to all patterns. The converse allows phase-dependent success probabilities, while the construction has a phase-independent success probability for each pattern.

## Charges and resources

The physical charge of a bit string is its Hamming weight. A full-probe charge sector of weight $`m`$ acquires phase $`e^{im\phi}`$. The target data have charges $`0,\ldots,k`$ and the sector of charge $`\ell`$ must acquire $`e^{i\ell\phi}`$. The decoder may use known coherent gates between these sectors. The model charges all $`N`$ query calls and probe sites. Its guarantee concerns exact abstract known controls. The [circuit account](implementation.md) gives separate preparation, gate and workspace costs.

One can constrain entanglement depth by allowing mixtures of products over blocks of at most $`d`$ probes. A classical label may specify the partition and the state of each block. The depth-constrained lower bound allows the receiver to know that label. At $`d=1`$ this includes unequal local preparations and arbitrary joint decoding.

A reusable protected program would define a different storage task. Likewise, if data could be encoded before the calls, a covariant erasure code could carry the data through the phase operation. Here the data are independent of the storage procedure and are supplied only at retrieval. See [related work](../references/RELATED_WORK.md).
