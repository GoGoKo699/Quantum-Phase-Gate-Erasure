# Finite verification

From the repository root, run the Python standard-library suite:

```sh
python3 -m unittest discover -s verification -v
```

The checks use integers, rational probabilities, and symbolic powers of the unknown phase. They cover:

- Charge-window overlap and its translated-total-variation and concentration bounds, including a gapped profile where the concentration bound is strict.
- The lossless and full-loss endpoints and the range of batch sizes with positive exact success.
- Successful filter action on a joint data and reference superposition. Each branch gives the intended data phases together with one common phase for that branch, and the squared filter amplitudes obey the trace-nonincreasing condition.
- The hypergeometric mean-squared error of the erased-charge estimator and the posterior variance bound on an asymmetric probe profile.
- Every one-site erasure pattern for two five-probe blocks. The joint two-gate success probability is exactly `2/3`. The product-probe success ceiling is `84883/131072`, approximately `0.64760590`.
- Two-site erasures across a small block layout and selected product profiles for the Fourier bound.

See the [proof](../science/proof.md) for the arbitrary-probe converse, the uniform asymptotic bounds, and the Fourier inequality behind the product ceiling.

The [marked-set verifier](https://github.com/GoGoKo699/Quantum-Parallel-Marked-Set/blob/main/verification/check_flagged_erasure.py) checks the qutrit construction and finite converses for the sister task. See [flagged marked-address search](../science/flagged-search.md) for how its exact checks differ from the charge-profile checks above.
