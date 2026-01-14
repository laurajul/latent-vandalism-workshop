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

This repository contains a series of Jupyter notebooks that guide you through the theory and practice of latent vandalism:

### 📓 Introduction & Theory
- **`000_intro.ipynb`** - Workshop introduction, theoretical framework, and conceptual overview

### 🔧 Technical Foundation
- **`001_t5_embeddings.ipynb`** - Understanding and extracting T5-XXL embeddings
- **`002_CLIP_embeddings.ipynb`** - Working with CLIP text embeddings
- **`003_CLIP-L_and_G_embeddings.ipynb`** - Comparing CLIP-L and CLIP-G encoders

### 🔨 Vandalism Techniques
- **`003_embedding_manipulation.ipynb`** - Systematic techniques for damaging embeddings (scaling, inversion, mixing, ablation)
- **`003_image_to_clip_embeddings.ipynb`** - Using image embeddings instead of text
- **`004_visual_attribute_blending.ipynb`** - Blending visual characteristics across embeddings
- **`005_padding_investigation.ipynb`** - Exploring edge cases and structural assumptions

### 🚀 Inference & Generation
- **`FLUX_schnell_inference.ipynb`** - Generating images with FLUX-Schnell using damaged embeddings
- **`SD_3.5_inference.ipynb`** - Generating images with Stable Diffusion 3.5 using damaged embeddings

### 📊 Supporting Materials
- **`sd35_embedding_diagrams.ipynb`** - Comprehensive diagrams showing pipeline architecture and embedding flow

---

## What You'll Learn

### Technical Skills
- How to extract and save embeddings from T5-XXL, CLIP-L, and CLIP-G encoders
- How to modify the SD 3.5 and FLUX-Schnell pipelines to accept raw embeddings
- Techniques for manipulating embeddings: scaling, inversion, mixing, ablation, interpolation
- Understanding where and how embeddings influence the diffusion process

### Conceptual Insights
- How text-to-image models encode and reproduce aesthetic norms
- The role of different encoders in semantic guidance
- How glitches and failures reveal model assumptions
- Productive damage as a research methodology
- The concept of technological inscription in AI systems

### Creative Possibilities
- Creating images impossible to generate from text prompts alone
- Discovering emergent behaviors in embedding space
- Finding the boundaries of template culture
- Exploring AI weirdness as an aesthetic and epistemic resource

---

## Models Used

- **Stable Diffusion 3.5** - Three text encoders (T5-XXL, CLIP-L, CLIP-G) with MMDiT architecture
- **FLUX-Schnell** - Two text encoders (T5-XXL, CLIP-L) with flow matching (4 steps)

Both models follow the pattern: **Text → Embeddings → Latent Diffusion → Image**

---

## Requirements

### Hardware
- GPU with at least 24GB VRAM recommended (for full SD 3.5)
- Can run FLUX-Schnell on less VRAM with optimizations

### Software
```bash
# Core dependencies
torch >= 2.0.0
diffusers >= 0.30.0
transformers >= 4.40.0
accelerate
safetensors

# Additional tools
jupyter
matplotlib
numpy
pillow
```

### Installation

```bash
# Clone the repository
git clone https://github.com/laurajul/latent-vandalism-workshop.git
cd latent-vandalism-workshop

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook
```

---

## Workshop Philosophy

### Iatrogenic Techniques

We adopt what we call **iatrogenic techniques**—a term borrowed from medicine meaning "caused by treatment itself." Rather than trying to optimize the pipeline, we deliberately introduce perturbations:

- **Scaling embeddings** beyond reasonable ranges
- **Inverting semantic directions** to explore negative space
- **Mixing incompatible concepts** that text prompts can't express
- **Zeroing out encoders** to see what each contributes
- **Creating impossible combinations** that violate training distribution

These interventions are **gently adversarial**—we're not trying to break the system maliciously, but to understand it through carefully designed failures.

### Reading Glitches as Data

Each type of damage produces characteristic failures:

- **Extreme scaling** → Reveals sensitivity thresholds and encoder balance requirements
- **Semantic inversion** → Tests whether semantic directions are truly bidirectional
- **Impossible mixing** → Exposes how models handle semantic conflicts and training data gaps
- **Encoder ablation** → Isolates individual encoder contributions and dependencies
- **Nonsense interpolation** → Reveals non-linear structure of embedding space

As Janelle Shane observes, when AI systems fail, they often fail in **informative ways**. The strange, the broken, the glitched—these aren't just mistakes. They're **windows into the system's implicit knowledge**.

---

## Theoretical Framework

This workshop draws on several theoretical traditions:

### Glitch Studies
- **Menkman, Rosa.** *The Glitch Moment(um)*. Network Notebooks, 2011.
  - Glitches as revelatory moments that expose normally invisible structures
  - Productive failures as aesthetic and epistemic resources

### Template Culture
- **Grund, Katja and Scherffig, Lasse.** Work on template culture and standardized aesthetics in generative AI
  - How models reproduce homogeneous visual languages
  - The political economy of aesthetic standardization

### AI Weirdness
- **Shane, Janelle.** Research on AI failures and unexpected behaviors
  - The epistemic value of AI mistakes
  - How failures reveal system structure

### Science and Technology Studies
- **Latour, Bruno.** "Technology is society made durable." *Sociological Review*, 1990.
  - Technological inscription: How values and choices become embedded in systems
  - Making visible the social and political dimensions of technical artifacts

---

## Usage Notes

### Workflow Overview

1. **Generate embeddings** from text prompts using the encoder notebooks
2. **Save embeddings** as JSON files for inspection and modification
3. **Apply vandalism techniques** to create damaged embeddings
4. **Inject modified embeddings** into the inference pipelines
5. **Analyze the results** to understand what the failures reveal

### Example: Extreme Scaling

```python
# Load saved embeddings
with open('embeddings/sunset.json', 'r') as f:
    emb_data = json.load(f)

# Vandalize: Scale T5 embeddings by 10x
emb_data['t5_embeddings'] = np.array(emb_data['t5_embeddings']) * 10.0

# Keep CLIP embeddings at 0.1x
emb_data['clip_l_embeddings'] = np.array(emb_data['clip_l_embeddings']) * 0.1

# Generate image with damaged embeddings
image = pipeline(
    prompt_embeds=emb_data['t5_embeddings'],
    pooled_prompt_embeds=emb_data['clip_pooled'],
    # ... other parameters
)
```

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

## Contributing

This is an experimental research project exploring productive damage as methodology. Contributions are welcome, especially:

- Novel vandalism techniques
- Interesting failure modes you've discovered
- Theoretical connections to other fields
- Documentation improvements
- Bug fixes and optimizations

Please open an issue or pull request to contribute.

---

## Citation

If you use this workshop or its methods in your research, please cite:

```bibtex
@misc{wagner2025latent,
  title={Latent Vandalism: The Joy of Productive Damage to Text-to-Image Synthesis Pipelines},
  author={Wagner, Laura},
  year={2025},
  howpublished={\url{https://github.com/laurajul/latent-vandalism-workshop}}
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
- Everyone who's ever made something beautifully broken

---

*"The charm of AI weirdness is not just in the strange outputs, but in what those outputs reveal about the system that produced them."*

**Remember:** The goal isn't to make "better" images—it's to understand what "better" means to these systems, and to find creative freedom in the spaces where that definition breaks down.
