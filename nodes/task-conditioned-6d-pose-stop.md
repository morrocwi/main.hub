# task-conditioned-6d-pose-stop

GENERATED from `graph/repos/` and `graph/nodes.yaml` - do not hand-edit.

- **Repository:** <https://github.com/morrocwi/task-conditioned-6d-pose-stop>
- **Class:** linked
- **Role:** Coverage-qualified stopping for iterative 6D pose refinement: an observable readout goes through a calibrated completion envelope and a task reader to ACT, CONTINUE or HOLD - never a bare pose estimate.
- **Is:** implementation-first research repository (public); a working ACT/CONTINUE/HOLD readout gate: HOLD when no certificate exists, never relabelled; instrumented with real BOP LM-O RGB-D runs, not only synthetic ones
- **Is not:** a claim that quotienting or coverage-qualified stopping is faster or non-inferior in general (several such claims are refuted or unsupported in its own CLAIMS.md); a claim that split-conformal marginal coverage is a deterministic safety guarantee; a claim that any ACT-licensing mechanism in this repository has been shown safe on real sensor data (its own native-sensitivity mechanism was found unsafe on 92.5-100% of real test episodes, reported as a safety finding, not a success)
- **Pinned:** `be2d7f28878d` on `main`, 29 commits after tag `v0.7.0`

## Read in this order

1. [`README.md`](https://github.com/morrocwi/task-conditioned-6d-pose-stop/blob/be2d7f28878df20f00291a944f12fe28a443d79f/README.md)
2. [`CLAIMS.md`](https://github.com/morrocwi/task-conditioned-6d-pose-stop/blob/be2d7f28878df20f00291a944f12fe28a443d79f/CLAIMS.md)
3. [`RESEARCH_QUESTION.md`](https://github.com/morrocwi/task-conditioned-6d-pose-stop/blob/be2d7f28878df20f00291a944f12fe28a443d79f/RESEARCH_QUESTION.md)
4. [`CONTRIBUTING.md`](https://github.com/morrocwi/task-conditioned-6d-pose-stop/blob/be2d7f28878df20f00291a944f12fe28a443d79f/CONTRIBUTING.md)

## Verified edges

- `task-conditioned-6d-pose-stop` **cites-proposal-from** `toledo` - evidence: `task-conditioned-6d-pose-stop` / [`README.md`](https://github.com/morrocwi/task-conditioned-6d-pose-stop/blob/be2d7f28878df20f00291a944f12fe28a443d79f/README.md) contains "Toledo proposal `PROP-DECAY-01`"
- `task-conditioned-6d-pose-stop` **logged-diagnosis-in** `glosa` - evidence: `task-conditioned-6d-pose-stop` / [`README.md`](https://github.com/morrocwi/task-conditioned-6d-pose-stop/blob/be2d7f28878df20f00291a944f12fe28a443d79f/README.md) contains "A diagnosis recorded in glosa"

## Neighbour cards

[[glosa]] · [[toledo]]
