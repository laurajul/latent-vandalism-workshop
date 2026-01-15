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



### JSON Embedding Format

Embeddings are saved with the following structure:

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

## License

This workshop material is released under [MIT License](LICENSE). Model weights and checkpoints follow their respective licenses (SD 3.5, FLUX-Schnell).

---

## Contact

**Laura Wagner**

- 🌐 Website: [laurajul.github.io](https://laurajul.github.io/)
- 📧 Contact via website or GitHub issues
- 💬 Questions, feedback, and collaborations welcome

---

## Acknowledgments

This workshop builds on:
- The diffusion model research community
- Open source implementations in `diffusers` and `transformers`
- Critical AI studies and glitch aesthetics scholarship

---

