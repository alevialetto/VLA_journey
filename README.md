# VLA Journey

**From control theory to robot foundation models: learning, evaluating and deploying Vision-Language-Action (VLA) models for robot manipulation.**

**Author:** Alessandro Vialetto, MSc student in Robotics Engineering, Politecnico di Milano
**Timeline:** November 2026 to April 2027, then consolidation
**Status:** Phase 1 (Foundations), in progress

---

## Motivation

Vision-Language-Action models (RT-2, OpenVLA, pi0, SmolVLA) are changing how robots are programmed: instead of hand-engineered pipelines, a single model maps camera images and a natural-language instruction directly to robot actions.

Most work on VLAs comes from the machine learning community and focuses on success rates. Much less attention goes to the questions a **control engineer** would ask first:

- How do **inference latency** and **control frequency** affect the behaviour of a VLA running on a real robot?
- How does **action chunking** (predicting several future actions at once) trade off reactivity against smoothness and stability?
- How can we add **safety and robustness** guarantees (limits, filters, failure detection) around a learned policy?

This repository documents a structured path to build the skills needed to work on these questions, ending with a flagship project on a real robot arm.

## Planned research direction

The flagship project (Phase 5) will study VLAs from a control perspective. A working hypothesis:

> *Inference latency and action-chunk size jointly determine the stability and smoothness of a VLA-controlled manipulator, and the best chunk size depends on latency rather than being a fixed hyperparameter.*

Planned methodology:

- **Baselines:** ACT, Diffusion Policy and a zero-shot VLA, compared with a fine-tuned VLA (e.g. SmolVLA).
- **Rigorous evaluation:** multiple seeds, confidence intervals and failure-case analysis, not single best runs.
- **Control metrics** alongside success rate: latency, effective control frequency, trajectory smoothness (jerk) and constraint violations.
- **Real-robot deployment** on a low-cost arm (SO-100 / LeRobot) or a university lab robot, with simulation (LIBERO / ManiSkill) for controlled ablations.

The exact research question will be refined during Phases 3 and 4, ideally together with a thesis supervisor.

## Roadmap

| Phase | Period | Topic | Measurable outcome | Status |
|---|---|---|---|---|
| 0 | Nov 2026 | Setup, Python, NumPy, Git | Simulated joints with a P controller, closed-loop noise analysis | Done |
| 1 | Nov - Dec 2026 | Foundations: PyTorch, Transformer from scratch, ViT, CLIP | Working Transformer and ViT trained from scratch | In progress |
| 2 | Dec 2026 - Jan 2027 | Imitation learning: behavior cloning, ACT, Diffusion Policy (LeRobot) | Policy trained in simulation, success-rate plots | Planned |
| 3 | Jan - Feb 2027 | From VLMs to VLAs: PaliGemma, RT-2, Octo, OpenVLA, LoRA fine-tuning | Reproducible fine-tuning pipeline | Planned |
| 4 | Feb - Mar 2027 | VLAs in depth: pi0, flow matching, SmolVLA, benchmarks, ablations | Results table with ablations (data, chunk size, frozen backbone) | Planned |
| 5 | Mar - Apr 2027 | Flagship project: VLA on a real robot arm from a control perspective | Report, code and demo video | Planned |

## Repository structure

```
00_Setup/               Python basics; simulated robot joints with a P controller
01_Fondamenta/          PyTorch basics, Transformer from scratch, ViT, CLIP
02_Imitation_Learning/  Behavior cloning, ACT, Diffusion Policy
03_Dai_VLM_ai_VLA/      Vision-language models, action tokenization, LoRA fine-tuning
04_VLA_Dettaglio/       pi0, SmolVLA, simulation benchmarks and ablations
05_Progetto_Punta/      Flagship project
Paper_Notes/            Short summaries of the papers I read, in my own words
```

## Principles

- **Everything ends in code:** no tutorial or paper without an implementation in this repo.
- **Measurable results:** every phase closes with numbers, plots or videos.
- **Reproducibility:** each project comes with a README that others can follow to rerun it.
- **Control perspective:** latency, stability, safety and control frequency are treated as first-class concerns.

## Setup

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Development runs on CPU; training runs on Google Colab / Kaggle or cloud GPUs.

## Results

*This section will collect the results of each phase (plots, tables, videos) as they become available.*

## Contact

I am interested in a **Master's thesis on robot learning and VLA models**, especially at the intersection with control.
Feel free to reach out via GitHub or at the Politecnico di Milano.
