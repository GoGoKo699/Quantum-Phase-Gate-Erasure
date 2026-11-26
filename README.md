# Quantum Phase Gate Erasure

**Can a quantum program retain an unknown phase gate after some of its probes are lost?** The data arrive after the queries and the loss. The decoder sees which probes were erased and announces success or failure. On success it applies the exact phase gate to the entire data batch, including data entangled with an external reference.

Prepare independent blocks of entangled probes in uniform superpositions over their excitation numbers. An unknown gate call on each probe writes its phase into that superposition. Discard blocks touched by an erasure and combine the intact blocks coherently. The decoder uses the surviving excitation numbers to apply the gate and herald exactness.

## Main results

With $`N`$ parallel queries, any $`t`$ flagged erasures, and $`k`$ delayed data qubits, the smallest worst-case failure probability satisfies

```math
f^*_{N,t,k}=\Theta\!\left(\min\!\left\{1,
  \frac{k}{1+\sqrt{N(N-t)/(t+1)}}\right\}\right).
```

The constants are uniform over the budgets. For one gate and $`t\le N/4`$, this is of order $`\sqrt{t+1}/N`$. Exact success has positive probability precisely when $`k\le N-t`$. In the lossless case the success probability is exactly $`(1-k/(N+1))_+`$.

The bound on failure alone does not resolve how fast success vanishes near the maximum feasible batch size. All claims count one call per physical probe, including discarded probes. The [implementation](science/implementation.md) accounts separately for preparation, coherent processing and the assumed exact known rotations.

| Case | Exact accepted operation |
| --- | --- |
| Ten queries, one arbitrary erased probe, two output gates | Two five-probe blocks achieve $`p=2/3`$ on every erasure pattern. |
| Same budgets with product probes | Every product-probe strategy has $`p\le 84883/131072\approx64.76\%`$ in the worst case, even with joint decoding. |
| General budgets | The intact-block decoder attains the optimal worst-case failure order. |

## Read the science

| Question | Start here |
| --- | --- |
| When do the queries, erasures and data arrival happen? | [Operational model](science/model.md) |
| Why can intact blocks implement the exact joint gate? | [Construction and converse](science/proof.md) |
| How do known gates implement the receiver? | [Circuit and resource account](science/implementation.md) |
| Which ideas come from phase storage and lossy metrology? | [Related work](references/RELATED_WORK.md) |
| How do I reproduce the finite cases? | [Verification](verification/README.md) |

The [science index](science/README.md) connects the results and their limits.

## Learn the result

The educational anchor is John Watrous, *The Theory of Quantum Information* (2018). Start with the [Watrous bridge](learning/WATROUS_BRIDGE.md), follow the [ten-query worked example](learning/WORKED_EXAMPLE.md), or use the [30-milestone map](learning/MILESTONES.md).

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
