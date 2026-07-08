# AI Sound Library Analyzer 🎛️🧠

An intelligent framework for analyzing, organizing and generating audio plugin libraries using Artificial Intelligence.

The goal of this project is to build an AI-powered system capable of understanding existing sound libraries, analyzing presets, samples and MIDI files, extracting meaningful audio features and eventually generating completely new sound libraries.

---

# 🚀 Project Vision

Modern music producers work with thousands of:

* Synth presets (`.fxp`, `.vital`, `.h2p`, etc.)
* Audio samples (`.wav`, `.aiff`)
* MIDI patterns (`.mid`)

Most sound libraries are manually organized and difficult to search or classify.

This project aims to create an AI assistant capable of:

* Automatically scanning sound libraries
* Detecting synthesizers and plugins
* Understanding sound characteristics
* Classifying sounds
* Extracting synthesis parameters
* Building structured datasets
* Training AI models
* Generating new original sound libraries

The final objective is an AI sound designer capable of understanding and creating sounds.

---

# 🎯 Project Pipeline

The complete workflow is divided into multiple stages:

```
Sound Libraries

       |
       v

Library Scanner

       |
       v

Preset / Audio Analyzer

       |
       v

library_analysis.json

       |
       v

Dataset Builder

       |
       v

dataset.json

       |
       v

Machine Learning Models

       |
       v

AI Generated Sounds
```

---

# 📚 Library Organization

Before running the analyzer, sound libraries must be placed inside:

```
libraries/
```

Each library should have its own folder.

Recommended structure:

```
libraries/

├── Serum_Bass_Library/
│
│   ├── Presets/
│   │   ├── Deep_Bass_01.fxp
│   │   ├── Sub_Bass_02.fxp
│   │
│   ├── Samples/
│   │   ├── Texture.wav
│   │   ├── Noise.wav
│   │
│   └── MIDI/
│       └── Bassline.mid
│
│
├── Diva_Cinematic_Pads/
│
│   ├── Presets/
│   │   ├── Dark_Pad_01.fxp
│   │
│   ├── Samples/
│   │   └── Atmosphere.wav
│   │
│   └── MIDI/
│       └── Sequence.mid
```

The analyzer works recursively.

Folder names are not mandatory.

Files are classified automatically by extension.

---

# 🎛️ Supported File Types

## Audio

Supported:

```
.wav
.aiff
.aif
```

---

## MIDI

Supported:

```
.mid
.midi
```

---

## Presets

Supported:

```
.fxp
.h2p
.vital
```

Future support:

* Serum
* Diva
* Massive
* Vital
* Other VST instruments

---

# ⚙️ Installation

Requirements:

* Python 3.12+
* Git

Clone repository:

```bash
git clone https://github.com/YOUR_USERNAME/AI_Sound_Library_Analyzer.git
```

Enter folder:

```bash
cd AI_Sound_Library_Analyzer
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate:

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# ⚙️ Configuration

All parameters are managed through:

```
config.json
```

Example:

```json
{
    "mode": "analyze",

    "dataset": {

        "input_folder": "libraries",

        "analysis_output": "output/library_analysis.json",

        "dataset_output": "output/dataset.json"

    },

    "extensions": {

        "audio": [
            ".wav",
            ".aiff",
            ".aif"
        ],

        "midi": [
            ".mid",
            ".midi"
        ],

        "preset": [
            ".fxp",
            ".h2p",
            ".vital"
        ]

    }
}
```

---

# 🔍 Analyze Mode

Analyze mode is the first stage.

Purpose:

To understand and catalog existing sound libraries.

The analyzer:

* scans folders
* detects files
* classifies extensions
* extracts metadata
* analyzes presets
* detects plugins when possible

Configuration:

```json
{
    "mode": "analyze"
}
```

Run:

```bash
python main.py
```

Output:

```
output/library_analysis.json
```

Example:

```json
{
    "file": "Deep_Bass_01.fxp",
    "type": "preset",
    "plugin": "Serum"
}
```

---

# 🧬 Dataset Mode

Dataset mode is the second stage.

Purpose:

Convert raw analysis information into structured data for Artificial Intelligence.

The dataset builder:

* reads analysis results
* normalizes information
* creates training samples
* prepares ML-ready data

Configuration:

```json
{
    "mode": "dataset"
}
```

Run:

```bash
python main.py
```

Output:

```
output/dataset.json
```

Example:

```json
{
    "preset": "Deep_Bass_01.fxp",
    "plugin": "Serum",
    "category": "Bass",
    "features": {
        "brightness": 0.72,
        "complexity": 0.61
    }
}
```

---

# 🧠 AI Development Roadmap

## Phase 1 — Scanner ✅

Implemented:

* Recursive scanning
* File detection
* Configuration system

## Phase 2 — Preset Analysis 🔄

Goals:

* Parse VST formats
* Extract metadata
* Identify plugins
* Extract synthesis parameters

## Phase 3 — Dataset Creation

Goals:

* Build AI training datasets
* Create sound representations
* Link presets with audio characteristics

## Phase 4 — Sound Classification

AI classification:

* Bass
* Lead
* Pad
* Pluck
* Keys
* FX
* Atmosphere

## Phase 5 — Generative AI

Future objective:

Generate:

* New presets
* New samples
* MIDI patterns
* Complete sound libraries

---

# 🏗️ Project Structure

```
AI_Sound_Library_Analyzer/

├── analyzer/

│   ├── scanner.py
│   ├── fxp_reader.py
│   ├── plugin_detector.py
│   ├── dataset_builder.py
│   └── pipeline.py

├── libraries/
│   User audio libraries
│   (excluded from Git)

├── output/
│   Generated analysis files
│   (excluded from Git)

├── config.json

├── main.py

├── requirements.txt

└── README.md
```

---

# 📌 Current Status

Version:

```
v0.1 - Foundation
```

Implemented:

✅ Project structure
✅ Configuration system
✅ Library scanner
✅ File classification
✅ Analysis pipeline foundation
✅ Dataset pipeline foundation

Next:

⬜ Advanced FXP parser
⬜ Serum parameter extraction
⬜ Diva parameter extraction
⬜ Audio feature extraction
⬜ Machine learning models
⬜ Generative sound engine

---

# 🎛️ Project Philosophy

The goal is not only to store sounds.

The goal is to teach an AI system how sound designers think:

* Why a sound has a specific character
* Which synthesis parameters create it
* How different sounds relate to each other
* How to generate new original sounds

---

# 📜 License

License information will be added in a future stable release.
