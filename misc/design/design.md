# Design specification

Visual standards for figures, tables, and documents.
Version 0.6 — revised against three reference figures and the paper's LaTeX source.

Values marked **measured** were sampled from the reference figures or read directly from
`arxiv_version.tex` and are not proposals.

---

## 1. The look in one paragraph

Pale tinted fills, tight hatch textures, and fine black outlines on a white ground. Every
piece of information that is a *category* gets a rounded pill with a colored border and a
matching tint fill; legends use the same rounded frame, so the figure has one corner
language throughout. Color is assigned by meaning, not by series index — a base model is
always Coral, an adapter type is always SlateGray. Figures are set in condensed Noto Sans,
bold nearly everywhere and small — weight and a narrow cut carry the emphasis so the
strokes never have to. The document around them is
Latin Modern, two-column, with color reserved for links and figures. Grid is faint dashed
grey and sits behind everything.

---

## 2. Palette

Ten colors, all CSS named colors, so every value has a canonical name usable directly in
CSS, matplotlib, and LaTeX.

| Name | Hex | Group | Role |
|---|---|---|---|
| Coral | `#FF7F50` | Warm | Primary category color; base models; mid-high ordinal; URLs |
| Crimson | `#DC143C` | Warm | High ordinal; alerts, deviations; citations |
| Maroon | `#800000` | Warm | **Text only** — axis labels, numeric emphasis, line numbers |
| RosyBrown | `#BC8F8F` | Warm | Low-mid ordinal; muted secondary; code comments |
| BlueViolet | `#8A2BE2` | Cool | Top of ordinal ramp; internal links; code keywords |
| SlateGray | `#708090` | Cool neutral | Type/class labels; the "structural metadata" color |
| Silver | `#C0C0C0` | Neutral | Gridlines, tag pills, lowest ordinal band |
| DarkGrey | `#A9A9A9` | Neutral | Captions, de-emphasized text |
| Gainsboro | `#DCDCDC` | Neutral | Row separators, hairline rules |
| Bisque | `#FFE4C4` | Neutral | Reserved — see below |

**On Maroon.** It appears in all three reference figures and never once encodes data. It
is the color of axis titles, numeric fields, and listing line numbers. Keep it that way:
Maroon is a *text* color, and at 10.95:1 on white it is the only palette color safe at any
size.

**On Bisque.** It appears in no reference figure and is not defined in the LaTeX preamble.
Either drop it or give it one job — page tint or table-header fill.

**On SlateGray.** Not in the original list but present in the reference table carrying both
`TI` and `LORA` badges, and defined in the preamble. A full member.

**On SteelBlue `#4682B4`.** Defined in the LaTeX preamble but never used in the document.
Either an eleventh member with no assigned role, or dead code to remove.

---

## 3. The tint system

This is the mechanic underneath every fill. **Measured** from the reference bars and
badges: one base color produces three values by alpha compositing over white.

| Layer | Alpha | Purpose | Example (BlueViolet) |
|---|---|---|---|
| Fill | **0.20** | Body of a bar, interior of a pill | `#E8D5F9` |
| Hatch / mid | **0.50** | Hatch strokes, secondary emphasis | `#C495F0` |
| Stroke / text | **1.00** | Pill border, hatch color, label text | `#8A2BE2` |

| Base | Fill 0.20 | Hatch 0.50 | Stroke 1.00 |
|---|---|---|---|
| Coral | `#FFE5DC` | `#FFBFA8` | `#FF7F50` |
| Crimson | `#F8D0D8` | `#EE8A9E` | `#DC143C` |
| BlueViolet | `#E8D5F9` | `#C495F0` | `#8A2BE2` |
| RosyBrown | `#F2E9E9` | `#DEC7C7` | `#BC8F8F` |
| SlateGray | `#E2E6E9` | `#B8C0C8` | `#708090` |
| Silver | `#F2F2F2` | `#E0E0E0` | `#C0C0C0` |
| Maroon | `#E5CCCC` | `#BF8080` | `#800000` |

Composite over white is `0.2·C + 0.8·255` per channel. Recompute rather than reusing these
hex values if a figure sits on a tinted background.

---

## 4. Two type systems

The figures and the document use different families, deliberately.

| | Family | Where |
|---|---|---|
| Figures | **Noto Sans Condensed** | everything inside a plotted image |
| Document body | **Latin Modern Roman** (`lmodern`, T1, `microtype`) | running text |
| Document headings | **Latin Modern Sans** (`\sffamily`) | title, sections, declarations |
| Code listings | Typewriter, `\scriptsize\bfseries` | `lstlisting` blocks |

Both sans faces are neutral grotesques, so a Noto Sans figure sitting in a Latin Modern
document reads as intentional rather than mismatched. It is still a mismatch — see the open
questions.

### The weight rule

Below 10 pt, bold. Small type loses stroke weight before it loses size, so weight
compensates. In practice all figure text is bold, and regular weight is reserved for
document body copy.

Weight is paired with a **condensed cut**. Bold at small sizes widens the apparent color of
a line of text; condensing pulls it back so labels stay dense and short without crowding the
plot. The font stack asks for `Noto Sans Condensed`, then `Noto Sans SemiCondensed`, then
plain `Noto Sans`, with `font.stretch: "condensed"` as the selector. If no condensed cut is
installed, matplotlib silently falls back to the normal width and the type reads a step
looser than intended — check the render rather than assuming.

### Figure type scale

Sizes below are for a **single-column** figure (84.6 mm), the common case. Scale up by
about a third for a full-width `figure*`.

| Element | Size | Weight | Color |
|---|---|---|---|
| Figure title | 9 pt | Bold | Near-black |
| Axis title | 8.5 pt | Bold | Maroon `#800000` |
| Tick label | 6.5 pt | Bold | Near-black |
| Legend title | 6 pt | Bold | Near-black |
| Legend entry | 5.5 pt | Bold | Series color |
| Badge / pill text | 6 pt | Bold | Badge color |
| Annotation | 6 pt | Bold | Crimson |

These are small numbers. They work because every one of them is bold and condensed — the
same label at regular weight and normal width would be unreadable at 5.5 pt. This is the
one place the weight rule earns its keep.

Sentence case everywhere except badge text, where the source string wins (`SD 1.5`,
`SDXL 1.0`, `LORA`, `TI`).

---

## 5. Information fields (badges)

The rounded pill is the signature element.

- **Fill** — base color at alpha 0.20
- **Border** — base color at full strength, 1.0 pt
- **Text** — base color at full strength, bold condensed, 6 pt
- **Corner radius** — generous; roughly half the pill height
- **Padding** — 0.35 em

### Color is assigned by field, not by row

A column's header takes the same color as the badges beneath it.

| Field | Color | Examples |
|---|---|---|
| Base model | Coral | `SD 1.5`, `SDXL 1.0` |
| Base model (exception) | BlueViolet | `Pony` — a distinct lineage, not a version |
| Adapter / artifact type | SlateGray | `TI`, `LORA` |
| Count, magnitude | Maroon text on Coral 0.20 fill | `594,253` |
| Free-form tags | Silver border, DarkGrey text | `anime`, `photorealistic` |
| Name | No badge, near-black bold | — |

Tags are deliberately the quietest: many per row, low information each. Never let a tag
pill compete with a base-model pill.

Rows are divided by Gainsboro `#DCDCDC` hairlines, not by boxes or zebra fill.

---

## 6. Figures

### 6.1 Ordinal series (**measured**)

For ranked or severity-graded categories, low to high:

```
Silver #C0C0C0  →  RosyBrown #BC8F8F  →  Coral #FF7F50  →  Crimson #DC143C  →  BlueViolet #8A2BE2
```

The ramp climbs in saturation and ends on the only cool color, which is why the top band
reads as the top band. Use for any ordered scale up to five levels.

### 6.2 Categorical series

```
1. Coral       #FF7F50
2. BlueViolet  #8A2BE2
3. Maroon      #800000   (fill/stroke use only)
4. RosyBrown   #BC8F8F
5. SlateGray   #708090
6. Crimson     #DC143C
```

Above six, stop adding colors — switch to small multiples, direct labeling, or
"top 5 + other."

### 6.3 Hatch

Every filled area gets a hatch. Patterns are **tight**: five repetitions of the character,
drawn at 0.7 pt. Five repeats give a dense weave that still resolves at column width;
denser than that fills in and reads as a flat block at 300 dpi.

| Position | Pattern | matplotlib |
|---|---|---|
| 1 | Diagonal, rising | `/////` |
| 2 | Diagonal, falling | `\\\\\` |
| 3 | Cross | `xxxxx` |
| 4 | Dots | `.....` |
| 5 | Plus | `+++++` |
| 6 | Circles | `ooooo` |

Hatch is drawn in the **series color**; the outline stays black. `hatch.linewidth: 0.7`,
kept just under the bar outline so the texture never competes with the edge.

Assign a distinct pattern per series rather than reusing one. The reference figure uses a
single `/` throughout, which makes hatch decorative. Varying it turns hatch into a second
encoding channel, which matters because Coral, Crimson, RosyBrown, and Maroon converge
under red-green color vision deficiency (§8).

### 6.4 Chart furniture

| Element | Value |
|---|---|
| Figure background | White |
| Bar/area outline | Black, 1.0 pt |
| Axis spines | Black, 1.1 pt; left and bottom only |
| Tick marks | Black, 1.0 pt, 2.5 pt long, 1.5 pt pad |
| Gridlines | Silver `#C0C0C0`, dashed, 0.7 pt, alpha 0.7, behind data |
| Grid axis | Whichever is *not* the categorical axis; vertical dashed separators when the x-axis has groups |
| Line series | 1.6 pt, markers 4 pt, distinct marker shape per series |
| Event marker | Black dashed vertical line, 1.2 pt, above the grid |
| Annotation | Crimson bold |

Axis labels sit 2 pt off the spine (`axes.labelpad`), tick labels 1.5 pt
(`xtick.major.pad`). Rotated tick labels need `rotation_mode="anchor"` alongside
`ha="right"`, or matplotlib rotates the label about its centre and leaves a wedge of dead
space between the text and the axis that no padding setting will close:

```python
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
```

Outlines are fine rather than heavy. The black edge is there to separate a tinted fill from
its neighbor, not to draw attention, and at 1.0 pt it does that without turning a stacked
bar into a grid of boxes. Keep a consistent order of weight — hatch 0.7, grid 0.7, outline
1.0, spine 1.1 — so nothing outweighs the data.

### 6.5 Legend

White fill, black border 1.0 pt, **rounded corners**, full opacity, tight padding. The
radius matches the badge radius, so pills and legend share one corner language.

In matplotlib this needs `legend.fancybox: True` plus an explicit boxstyle on the frame —
`rounding_size` is measured in font-size units, so at a 6 pt legend the default 0.2 is
invisible. Use `rounding_size=0.6, pad=0.30` and scale with the legend's font size.

Padding is tight so the box stays small: `labelspacing 0.2`, `handletextpad 0.4`,
`handlelength 1.5`. Condensed bold entries can sit this close without running together.

**The two paddings add.** `legend.borderpad` insets the contents from the frame, and the
boxstyle's own `pad` then grows the frame outward again — set both and you get the gap
twice. Set `legend.borderpad: 0.0` and control the inset solely through the boxstyle
`pad`, which is the one the rounded corner is measured against. `pad=0.30` with
`rounding_size=0.6` is snug without crowding; `pad=0.20` starts to touch the descenders.

**The frame must not touch the axis.** The boxstyle `pad` grows the frame outward from
where matplotlib placed it, and `legend.borderaxespad` offsets it inward from the axes
corner — the two work in opposite directions and cancel. At the previous `borderaxespad
0.3` against `pad 0.30` they cancelled exactly, which is why the frame sat welded to the
y-axis spine. Set `borderaxespad` to roughly the boxstyle `pad` **plus** the inset you
actually want, so `1.6` for a visible float. The legend should read as sitting inside the
plot area, not as a panel bolted to its edge.

Give the legend room to float by adding headroom rather than letting it overlap bars:
`ax.set_ylim(0, data_max * 1.3)` for a five-entry legend in a corner.

Bold title in near-black. Each entry bold and set in its own series color, so the legend
needs no lookup. Order entries to match the visual stacking order — top of the stack first.
Include sample size inside the box as a final line (`n images = 40,621,133`) rather than in
the caption.

### 6.6 Sizes and export (**measured**)

The paper is `\documentclass[11pt, svgnames, twocolumn]{article}` with
`\usepackage[margin=0.85in, top=1.1in, bottom=1in]{geometry}` on letter paper. That fixes
the real target widths:

| Target | Width | Notes |
|---|---|---|
| `\columnwidth` | **84.6 mm** (3.33 in) | single-column figure |
| `\textwidth` | **172.7 mm** (6.80 in) | `figure*`, spanning both columns |
| `0.85\textwidth` | 146.8 mm (5.78 in) | the house default for `figure*` |
| `0.47–0.48\textwidth` | 81–83 mm | side-by-side minipages, as in Figures 3 and 4 |
| Slide | 254 × 143 mm (16:9) | 200 dpi |

Every figure in the paper is a `figure*`. Widths in use are `\textwidth` (Figures 1, 8, 9),
`0.88\textwidth` (Figure 2), and `0.85\textwidth` (Figures 5, 6, 7) — so 0.85 is the
working default and full bleed is the exception for dense grids and Sankey diagrams.

Export vector (PDF) for plots, PNG at 300 dpi for image grids. Never upscale a raster
export. Build figures at their final width rather than scaling in `\includegraphics`, or
the type scale in §4 stops being true.

---

## 7. Document (LaTeX)

### 7.1 Layout (**measured**)

```latex
\documentclass[11pt, svgnames, twocolumn]{article}
\usepackage[margin=0.85in, top=1.1in, bottom=1in]{geometry}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{microtype}
```

Two columns, 84.6 mm each, 3.5 mm gutter. Title block is full width via
`\twocolumn[...]`. Running header carries the acceptance notice with a 0.4 pt rule; footer
carries the page number.

### 7.2 Headings (**measured**)

Set in Latin Modern Sans, ragged right rather than justified, so the sans headings sit
against the justified serif body as a clear second voice.

| Level | Command | Face | Size (11 pt class) |
|---|---|---|---|
| Title | `\sffamily\LARGE\bfseries` | LM Sans bold | 17.3 pt |
| `\section` | `\sffamily\large\bfseries\raggedright` | LM Sans bold | 12 pt |
| `\subsection` | `\sffamily\normalsize\bfseries\raggedright` | LM Sans bold | 11 pt |
| `\subsubsection` | `\sffamily\normalsize\itshape\raggedright` | LM Sans italic | 11 pt |
| Body | default | LM Roman | 11 pt |

**Headings are black.** This is worth stating because it contradicts the obvious move of
coloring them Maroon. In the document, color is spent on links, citations, and figures;
the heading hierarchy is carried by family, weight, and alignment instead. Keep it.

### 7.3 Color in running text (**measured**)

```latex
\PassOptionsToPackage{colorlinks=true,
  linkcolor=blueviolet, citecolor=crimson,
  urlcolor=coral, filecolor=crimson}{hyperref}
```

| Element | Color |
|---|---|
| Internal link (cross-reference) | BlueViolet |
| Citation | Crimson |
| URL | Coral |
| File link | Crimson |
| Content warning | `red!60!black` |

Citations are the most frequent colored element in the body, which is why they get Crimson
rather than Coral — at 4.99:1 Crimson is readable at body size, and Coral at 2.50:1 is not.
Coral is confined to URLs, which are typically set in a mono face at a larger relative
x-height.

### 7.4 Code listings (**measured**)

| Element | Style |
|---|---|
| Base | `\ttfamily\scriptsize\bfseries` |
| Keywords | BlueViolet bold |
| Strings | BlueViolet |
| Line numbers | Maroon bold, `\ttfamily\scriptsize`, left, 4 pt sep |
| Comments | RosyBrown |
| Digits | Coral (via `literate`) |
| Caption position | Bottom |

Coloring every digit Coral is unusual and effective here, because the listings are JSON
metadata where the numbers are the payload. Treat it as specific to data-structure
listings, not as a general code style.

### 7.5 Markdown and HTML

No LaTeX equivalent exists for these, so this section is a **proposal**, aligned to §7.2's
principle that headings carry hierarchy without color:

| Level | Color | Weight |
|---|---|---|
| H1–H4 | Near-black `#1A1A1A` | Bold, descending size |
| Body | Near-black `#1A1A1A` | Regular, 1.5 line height |
| Caption | DarkGrey `#A9A9A9` | Regular, 9 pt |
| Link | BlueViolet, underlined | Regular |
| Rule | Gainsboro `#DCDCDC` | 0.5 pt |
| Inline key term | Badge treatment, SlateGray | Bold |
| Callout | Coral 0.20 fill, Coral 3 pt left border | — |

---

## 8. Contrast reference

WCAG ratio against white. Normal text needs 4.5, large text (18 pt, or 14 pt bold) needs
3.0, graphical elements need 3.0.

| Color | on White | Text use |
|---|---|---|
| Maroon | 10.95 | Any text ✓ |
| BlueViolet | 5.96 | Any text ✓ |
| Crimson | 4.99 | Body text ✓ |
| SlateGray | 4.76 | Body text ✓ |
| RosyBrown | 2.81 | No text |
| Coral | 2.50 | No text; below 3.0 even as a graphic |
| DarkGrey | 2.35 | Fails AA — captions only, by exception |
| Silver | 1.82 | Structure only |
| Gainsboro | 1.35 | Rules only |
| Bisque | 1.22 | Fill only |

Consequences:

1. **Coral badge text at 8 pt fails AA.** Legible in practice because it is bold and short,
   but if a document must pass, darken badge text to `#E2622F` (3.2:1) while keeping border
   and fill at true Coral. The badge still reads as Coral.
2. **Coral URLs** inherit the same problem in §7.3. Same fix if needed.
3. **Silver tag text** is why tags use DarkGrey text inside a Silver border — and even
   DarkGrey is a deliberate de-emphasis, not an accessible choice.

Pairs too close to distinguish as adjacent series (ratio < 1.6): Coral/DarkGrey (1.06),
Coral/RosyBrown (1.13), BlueViolet/Crimson (1.19), RosyBrown/DarkGrey (1.20),
Silver/DarkGrey (1.29), Coral/Silver (1.37), RosyBrown/Silver (1.55). The ordinal ramp
avoids all of these except RosyBrown/Silver, which is why levels 1 and 2 need different
hatch patterns.

---

## 9. Implementation

### matplotlib

```python
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.colors import to_rgb
from cycler import cycler

C = {
    "coral": "#FF7F50", "crimson": "#DC143C", "maroon": "#800000",
    "rosybrown": "#BC8F8F", "blueviolet": "#8A2BE2", "slategray": "#708090",
    "bisque": "#FFE4C4", "silver": "#C0C0C0", "darkgrey": "#A9A9A9",
    "gainsboro": "#DCDCDC", "ink": "#000000",
}

SERIES  = [C["coral"], C["blueviolet"], C["maroon"],
           C["rosybrown"], C["slategray"], C["crimson"]]
ORDINAL = [C["silver"], C["rosybrown"], C["coral"], C["crimson"], C["blueviolet"]]
HATCH   = ["/////", "\\\\\\\\\\", "xxxxx", ".....", "+++++", "ooooo"]

# Figure widths in inches, from the paper's geometry
COLUMN_W   = 3.331   # \columnwidth   =  84.6 mm
TEXT_W     = 6.800   # \textwidth     = 172.7 mm
DEFAULT_W  = 5.780   # 0.85\textwidth = 146.8 mm


def tint(color, alpha=0.20):
    """Composite a palette color over white."""
    return tuple(alpha * c + (1 - alpha) for c in to_rgb(color))


mpl.rcParams.update({
    # type: condensed bold, small
    "font.family":        "sans-serif",
    "font.sans-serif":    ["Noto Sans Condensed", "Noto Sans SemiCondensed",
                           "Noto Sans", "DejaVu Sans", "Noto Sans CJK JP"],
    "font.stretch":       "condensed",
    "font.weight":        "bold",
    "axes.labelweight":   "bold",
    "axes.titleweight":   "bold",
    "axes.labelcolor":    C["maroon"],
    "axes.labelsize":     8.5,
    "axes.labelpad":      2,
    "axes.titlesize":     9,
    "axes.titlecolor":    C["ink"],
    "xtick.labelsize":    6.5,
    "ytick.labelsize":    6.5,

    # strokes: fine, and ordered hatch < grid < outline < spine
    "axes.edgecolor":     C["ink"],
    "axes.linewidth":     1.1,
    "grid.color":         C["silver"],
    "grid.linestyle":     "--",
    "grid.linewidth":     0.7,
    "grid.alpha":         0.7,
    "hatch.linewidth":    0.7,
    "lines.linewidth":    1.6,
    "lines.markersize":   4,
    "xtick.color":        C["ink"],
    "ytick.color":        C["ink"],
    "xtick.major.width":  1.0,
    "ytick.major.width":  1.0,
    "xtick.major.size":   2.5,
    "ytick.major.size":   2.5,
    "xtick.major.pad":    1.5,
    "ytick.major.pad":    1.5,

    "axes.prop_cycle":    cycler(color=SERIES),
    "axes.grid":          True,
    "axes.axisbelow":     True,
    "axes.spines.top":    False,
    "axes.spines.right":  False,

    # legend: rounded, tight
    "legend.frameon":     True,
    "legend.fancybox":    True,      # required for a rounded frame
    "legend.edgecolor":   C["ink"],
    "legend.facecolor":   "white",
    "legend.framealpha":  1.0,
    "legend.borderpad":       0.0,   # inset comes from the boxstyle pad instead
    "legend.labelspacing":    0.2,
    "legend.handletextpad":   0.4,
    "legend.handlelength":    1.5,
    "legend.borderaxespad":   1.6,   # must exceed the boxstyle pad, or the frame
                                     # ends up flush against the axis spine

    "figure.facecolor":   "white",
    "savefig.dpi":        300,
    "savefig.bbox":       "tight",
})
```

**Hatched bars.** matplotlib ties hatch color to edge color, so a colored hatch with a black
outline needs two passes: the fill layer carries the hatch in the series color with no
visible edge, and a second transparent bar draws the black outline on top.

```python
def hatched_bar(ax, x, height, bottom, color, hatch, lw=1.0):
    ax.bar(x, height, bottom=bottom, color=tint(color, 0.20),
           edgecolor=color, hatch=hatch, linewidth=0, zorder=3)
    ax.bar(x, height, bottom=bottom, color="none",
           edgecolor=C["ink"], linewidth=lw, zorder=4)


def hatched_handle(color, hatch, label):
    """Legend proxy matching hatched_bar."""
    return Patch(facecolor=tint(color, 0.20), edgecolor=color,
                 hatch=hatch, label=label, linewidth=0)
```

**Rounded legend.**

```python
def round_legend(leg, rounding=0.6, pad=0.30, lw=1.0):
    """Rounded frame matching the badge radius.

    rounding and pad are in font-size units, so they track the legend's
    fontsize automatically. Requires legend.fancybox = True, and
    legend.borderpad = 0 — otherwise this pad and that one both apply.
    """
    frame = leg.get_frame()
    frame.set_boxstyle("round", pad=pad, rounding_size=rounding)
    frame.set_linewidth(lw)
    frame.set_edgecolor(C["ink"])
    frame.set_facecolor("white")
    return leg


leg = ax.legend(handles=handles[::-1], title="NSFW browsing levels",
                fontsize=5.5, loc="upper left")
leg.get_title().set_fontweight("bold")
leg.get_title().set_fontsize(6)
for text, color in zip(leg.get_texts(), ORDINAL[::-1]):
    text.set_color(color)
    text.set_fontweight("bold")
round_legend(leg)
```

**Badges.**

```python
def badge(ax, x, y, text, color, fontsize=6, pad=0.35, transform=None):
    return ax.text(
        x, y, text, color=color, fontsize=fontsize, fontweight="bold",
        ha="center", va="center", zorder=5,
        transform=transform or ax.transAxes,
        bbox=dict(boxstyle=f"round,pad={pad},rounding_size=0.45",
                  facecolor=tint(color, 0.18), edgecolor=color, linewidth=1.0),
    )
```

### LaTeX

```latex
\usepackage{xcolor}
\usepackage[most]{tcolorbox}

\definecolor{coral}{HTML}{FF7F50}
\definecolor{crimson}{HTML}{DC143C}
\definecolor{maroon}{HTML}{800000}
\definecolor{rosybrown}{HTML}{BC8F8F}
\definecolor{blueviolet}{HTML}{8A2BE2}
\definecolor{slategray}{HTML}{708090}
\definecolor{silver}{HTML}{C0C0C0}
\definecolor{darkgrey}{HTML}{A9A9A9}
\definecolor{gainsboro}{HTML}{DCDCDC}

% inline badge matching the figure style
\newtcbox{\badge}[1][coral]{on line, nobeforeafter,
  colframe=#1, colback=#1!20!white, coltext=#1,
  boxrule=0.5pt, arc=3pt, boxsep=0pt,
  left=3pt, right=3pt, top=1.5pt, bottom=1.5pt,
  fontupper=\bfseries\small}

% usage: \badge{SD 1.5}  \badge[blueviolet]{Pony}  \badge[slategray]{LORA}
```

Note `colback=#1!20!white` is the same 0.20 tint as §3, so LaTeX badges and matplotlib
badges land on identical fills.

### CSS

```css
:root {
  --coral:      #FF7F50;
  --crimson:    #DC143C;
  --maroon:     #800000;
  --rosybrown:  #BC8F8F;
  --blueviolet: #8A2BE2;
  --slategray:  #708090;
  --bisque:     #FFE4C4;
  --silver:     #C0C0C0;
  --darkgrey:   #A9A9A9;
  --gainsboro:  #DCDCDC;
  --ink:        #000000;

  --accent:     var(--coral);
  --accent-alt: var(--blueviolet);
  --meta:       var(--slategray);
  --emphasis:   var(--crimson);
  --numeric:    var(--maroon);
  --rule:       var(--gainsboro);
  --grid:       var(--silver);

  --font: "Noto Sans Condensed", "Noto Sans", sans-serif;
}

.badge {
  display: inline-block;
  padding: 0.15em 0.55em;
  border: 1px solid var(--c);
  border-radius: 0.6em;
  background: color-mix(in srgb, var(--c) 20%, white);
  color: var(--c);
  font: bold 0.75rem/1.35 var(--font);
  white-space: nowrap;
}
.badge--base { --c: var(--coral); }
.badge--pony { --c: var(--blueviolet); }
.badge--type { --c: var(--slategray); }
.badge--tag  { --c: var(--silver); color: var(--darkgrey); }
```

---

## 10. Open questions

1. **Two type systems.** Figures are Noto Sans; the document is Latin Modern. Keep the
   contrast, or move figures to Latin Modern Sans so the whole artifact is one family?
   Noto Sans has the practical edge — it covers the CJK model names in Figures 6 and 7 that
   Latin Modern cannot set.
2. **SteelBlue `#4682B4`** is defined in the preamble and never used. Assign it a role or
   delete it.
3. **Bisque** — drop it, or assign it to page tint / table headers?
4. **Maroon as a fill.** It sits at position 3 in the categorical order but is only ever
   used as text. Confirm it may fill, or restrict it to text and cut the categorical list
   to five.
5. **Hatch retrofit.** §6.3 proposes distinct patterns per series where the reference uses
   one. Adopt going forward, or rebuild existing figures?
6. **Coral text** fails AA at small sizes, in badges and in URLs. Accept, or adopt the
   darkened `#E2622F` variant for text while keeping true Coral for borders and fills?
