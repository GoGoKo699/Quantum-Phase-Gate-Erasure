# Related work

## Exact storage and gate replication

Sedlák and Ziman give the optimal lossless $`N`$-to-one probabilistic storage and retrieval of an unknown qubit phase gate. Their optimum $`N/(N+1)`$ and uniform charge program are the lossless single-gate benchmark. The coherent charge-shift receiver used here extends that construction to a batch and an arbitrary pure charge distribution. The new storage question is robustness to unknown physical loss positions before the decoder can compress the program. It requires one probe design to serve all patterns. [Sedlák and Ziman, *Phys. Rev. A* **102**, 032618 (2020)](https://doi.org/10.1103/PhysRevA.102.032618)

Pavličko and Ziman analyze a lossless-optimal retrieval device with its queried channels independently replaced by depolarizing or dephasing mixtures. Their successful output can retain phase noise. Here all calls are ideal, the erasures act on the already-queried probes, positions are known and the accepted output is an exact noiseless channel. An algebraic decomposition of noise without access to its realization cannot supply the erasure flag. [Pavličko and Ziman, *Phys. Rev. A* **106**, 052416 (2022)](https://arxiv.org/abs/2211.07079)

Dür, Sekatski and Skotiniotis replicate phase rotations approximately by handling the typical charge sectors of the desired operation. Their full article discusses the extreme-charge coherence of a GHZ state as a limitation on worst-case quality. Sekatski and coauthors extend channel cloning to noisy phase gates with approximate output. Exact application to the whole batch, including any superposition of its extreme charges, is the guarantee used here. [Dür, Sekatski and Skotiniotis, *Phys. Rev. Lett.* **114**, 120503 (2015)](https://arxiv.org/abs/1410.6008) · [Sekatski et al., arXiv:2509.08059](https://arxiv.org/abs/2509.08059)

## Lossy metrology and erasure correction

Phase-estimation work identifies the effect of loss on available number fluctuations. The conditional-variance bound here uses the same underlying leakage of excitation information. The task output is a quantum channel, and the proof must bound the probability of an exact successful branch, rather than a mean estimation error. The proof uses Fourier matching on the data charge range to connect charge concentration to this probability. [Demkowicz-Dobrzański et al., *Phys. Rev. A* **80**, 013825 (2009)](https://doi.org/10.1103/PhysRevA.80.013825)

Covariant Erasure Yield encodes a data qubit supplied before loss into two adjacent charge sectors, then recovers its entire state exactly on success. Its converse uses the erased charges to distinguish the two encoded sectors. Encoding a known superposition in such a code would supply a single program token. Delayed exact application at success approaching one requires a broader charge resource. Here the conditional spread of that resource controls an arbitrary batch of later-supplied data. [Covariant Erasure Yield, model and proof at the inspected revision](https://github.com/GoGoKo699/Covariant-Erasure-Yield/blob/c51e759e502d272381c7694732bfa324955ba395/science/model.md)

The contribution is the minimax failure law for this delayed exact task, the explicit flagged-loss block design, and the same-budget separation from all product probes. The [bibliography](references.bib) lists the starting sources.
