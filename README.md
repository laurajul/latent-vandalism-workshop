# Latent Vandalism: The Joy of Productive Damage to Text-to-Image Synthesis Pipelines

**Workshop Materials by Laura Wagner**

🔗 [laurajul.github.io](https://laurajul.github.io/)  
📦 [Workshop Repository](https://github.com/laurajul/latent-vandalism-workshop)

---

## Abstract

Text-to-image models have evolved into sophisticated engines of **template culture** (Grund and Scherffig), systems trained to reproduce standardized aesthetics. Fatigued by the constant flood of polished results and the arms race for images benchmarked on visual coherence, commercial value and consumer-friendliness, this workshop explores once again the charm of **AI weirdness** (Shane) - the failure in generative AI and the epistemic value of **productive damage**.

Drawing inspiration from **glitch studies** (Menkman), we embrace glitches and artifacts as revelatory moments. Through gently violating the consumer-friendly, polished norms meant to please, we surface the model's implicit assumptions about how things are *supposed* to look. Participants will work directly with **Diffusion Transformers (DiT)**, focusing on the role of embeddings in image-text correlation from embedding space to latent space back into pixel space. Through hands-on meddling with the pipeline, we'll systematically damage and reconfigure the semantic substrate that guides image generation, deliberately perturbing inputs to understand this system's sensitivity and dynamics.

This **counterfactual, gently adversarial approach** positions productive damage as a research method. Through **iatrogenic techniques** performed on text-to-image models, we probe the layers of **technological inscription** (Latour) embedded in these systems. Values, design choices, and visual norms inscribed become legible where the system breaks down. By deliberately coaxing the model into failure, we trace the contours of what has been encoded into them.

---

## Workshop Overview



### Productive Damage as Method

Instead of trying to get the "best" results, we're interested in **productive damage**—deliberate interventions that make the system fail in interesting ways. By breaking things carefully, we can:

- **Surface hidden assumptions** about what images "should" look like
- **Reveal the training data's bias** toward certain visual patterns
- **Understand the semantic structure** of embedding space
- **Trace technological inscription**—the values and design choices baked into these systems

As Rosa Menkman argues in glitch studies, glitches aren't just errors—they're **revelatory moments** that expose the normally invisible structures underlying digital systems.

---

## Workshop Structure

### 📓 Introduction & Theory
- **`000_intro.ipynb`** - Workshop introduction, theoretical framework, and conceptual overview

### 🔧 Embedding generation
- **`001_t5_embeddings.ipynb`** - Understanding and extracting T5-XXL embeddings
- **`002_CLIP_embeddings.ipynb`** - Working with CLIP text embeddings
- **`003_CLIP-L_and_G_embeddings.ipynb`** - Comparing CLIP-L and CLIP-G encoders

### 🔨 Vandalism Techniques
- **`004_embedding_manipulation.ipynb`** - Systematic techniques for damaging embeddings (scaling, inversion, mixing, ablation)

### 🚀 Inference & Generation
- **`FLUX_schnell_inference.ipynb`** - Generating images with FLUX-Schnell using damaged embeddings
- **`SD_3.5_inference.ipynb`** - Generating images with Stable Diffusion 3.5 using damaged embeddings

## Task

---

## ☁️ Running on Google Colab

The `notebooks/` folder above is the original setup for a shared university cluster (a shared `venv`
and a shared model folder, everyone with their own workspace, both FLUX-Schnell and SD3.5 Medium).
`notebooks_colab/` is a **FLUX.1-schnell-only** edition adapted for a free **Colab T4 GPU**, condensed
into a single notebook:

- **One model, one notebook**: a personal Google Drive has a 15GB free-tier cap, which doesn't fit
  two full model families the way the cluster's shared filesystem does — so this edition drops SD3.5
  and focuses on FLUX. T5-XXL embeddings, CLIP-L embeddings, embedding vandalism, FLUX inference, and
  the scaling animation are all sections of **one notebook** (`00_complete_workshop.ipynb`) instead of
  seven separate ones, so T5-XXL and CLIP-L are loaded exactly **once** per session and reused by
  every later section — instead of each notebook downloading and saving its own private copy (that
  duplication, ~6GB of T5-XXL alone × 3, was what blew past the 15GB quota in an earlier draft).
- **Precision**: T5-XXL and the FLUX transformer are loaded **4-bit quantized (NF4)**; everywhere the
  cluster version used `bfloat16`, this uses `float16` — the T4 (Turing) has no bfloat16 tensor cores.
- **Shared models, without a shared filesystem**: the workshop organizer runs
  `00_instructor_model_prep.ipynb` once ahead of time to download, quantize, and dedupe everything
  (~13.5GB total) into their own Drive, then shares that folder read-only. Each participant's notebook
  links it into their own Drive as a shortcut and mounts it — the closest Colab equivalent of the
  cluster's shared model folder. Participants' own embeddings/outputs go to their own private Drive
  folder, just like their own cluster workspace.

| Notebook | |
|---|---|
| `00_instructor_model_prep.ipynb` *(organizer runs once, before the workshop)* | runs in Colab |
| `00_instructor_model_prep_local.ipynb` *(same, for non-Colab hardware — see below)* | plain Jupyter notebook |
| `00_complete_workshop.ipynb` *(what participants run)* | runs in Colab |

Loading + quantizing the FLUX transformer on a T4 is tight enough that it can OOM depending on what
else Colab has going on. If `00_instructor_model_prep.ipynb` doesn't get through cleanly,
`00_instructor_model_prep_local.ipynb` does the identical prep on any machine with more GPU headroom
(24GB+) — a lab workstation, a rented instance, whatever's available — and saves locally instead of to
Drive; its last section walks through getting that folder into Drive afterward.

**Organizer setup, once:**
1. Open `00_instructor_model_prep.ipynb`, run all cells (needs a HF token as a Colab
   secret — the notebook explains where). If it OOMs, use `00_instructor_model_prep_local.ipynb` on
   other hardware instead.
2. Share the resulting Drive folder ("Anyone with the link → Viewer"), copy the link.
3. Paste that link as `SHARED_FOLDER_LINK` in the "Colab Setup" section of `00_complete_workshop.ipynb`
   (or just tell participants the link and have them paste it in themselves).

**Participants:** open `00_complete_workshop.ipynb`, run the "Colab Setup" cells at the top, then work
through the sections top to bottom — same content as the cluster version's T5/CLIP/vandalism/FLUX
notebooks, just condensed into one file and running on FLUX-Schnell alone.

---



### JSON Embedding Format

Embeddings are saved with the following structure, so we can peek in:

```json
{
  "prompt": "original text prompt",
  "t5_embeddings": [[...], [...], ...],  // 77 x 4096 or 512 x 4096
  "clip_l_embeddings": [[...], [...], ...],  // 77 x 768
  "clip_l_pooled": [...],  // 768
  "clip_g_embeddings": [[...], [...], ...],  // 77 x 1280 (SD 3.5 only)
  "clip_g_pooled": [...]  // 1280 (SD 3.5 only)
}
```

---


