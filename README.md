# AI Infused — Class 1

From your first API call to a live AI app. Covers Groq (Qwen & GPT-OSS), web scraping, and Gradio UIs.

## Prerequisites

- Python 3.9+
- A [Groq API key](https://console.groq.com/keys) (free)

## Setup

### 1. Clone the repo

```bash
git clone https://github.com/vinayakkumar/ai-infused-class-1.git
cd ai-infused-class-1
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

Create a file named `.env` in the project root with your Groq API key:

```text
GROQ_API_KEY=gsk_...
```

---

## Files and what you see when you run them

### `first_class.py` — Your very first API call

```bash
python3 first_class.py
```

Sends a single prompt to Groq using the `qwen/qwen3.8-27b` model.

**What you see:** A witty travel tip for Bangalore printed in the terminal.

---

### `groq_call.py` — Groq API call standalone

```bash
python3 groq_call.py
```

Same as above but as a clean standalone script using `qwen/qwen3.8-27b`.

**What you see:** A travel suggestion for Bangalore printed in the terminal.

---

### `class1.py` — Full class walkthrough (Steps 1 to 5)

```bash
python3 class1.py
```

Runs all 5 steps back to back:

| Step | What happens | What you see |
|------|-------------|--------------|
| Step 1 | API call to Groq (`qwen/qwen3.8-27b`) | Travel tip printed in terminal |
| Step 2 | Same prompt, different Groq model (`openai/gpt-oss-20b`) | Second travel tip printed |
| Step 3 | Scraper defined — fetches and cleans a webpage | (no output, function defined) |
| Step 4 | Summarizer defined — chains scraper + Groq | (no output, function defined) |
| Step 5 | Gradio UI launches with the summarizer | Browser opens at `http://localhost:7860` with a text box to paste any URL |

---

### `app.py` — AI Website Summarizer (Gradio UI)

```bash
python3 app.py
```

A one-page web app: paste any URL, get an AI summary.

**What you see:**
- Terminal prints the local URL: `http://localhost:7860`
- Browser shows a text box labelled **Website URL**
- Enter a URL → Groq reads the page and returns a markdown summary

---

### `arena_app.py` — LLM Arena (compare two models)

```bash
python3 arena_app.py
```

Sends the same prompt to two different Groq models side by side and lets you vote.

**What you see:**
- Terminal prints the local URL: `http://localhost:7860`
- Browser shows a prompt box and two columns — **Model A** (`openai/gpt-oss-20b`) and **Model B** (`qwen/qwen3.8-27b`)
- Click **Battle!** → both models answer simultaneously
- Click 👍 or 👎 under each answer to vote for the better one

---

### `scraper.py` — Website scraper (utility module)

Not run directly. Imported by `app.py`, `class1.py`, and `summarizer.py`.

Fetches a URL, strips scripts/navbars/footers, and returns clean text.

---

### `summarizer.py` — Summarizer (utility module)

Not run directly. Imported by `app.py`.

Chains `scraper.py` → Groq (`openai/gpt-oss-20b`) to produce a markdown summary of any URL.

---

### `arena.py` — Arena battle logic (snippet/reference)

Not run directly. Contains the `battle()` function used as a reference for how `arena_app.py` works under the hood.

---

## Models used

| Model | Provider | Used in |
|-------|----------|---------|
| `qwen/qwen3.8-27b` | Groq (free) | `first_class.py`, `groq_call.py`, `class1.py` (Step 1), `arena_app.py` (Model B) |
| `openai/gpt-oss-20b` | Groq (free) | `class1.py` (Step 2), `summarizer.py`, `app.py`, `arena_app.py` (Model A) |

---

> **Note:** Always activate the virtual environment before running any script:
>
> ```bash
> source venv/bin/activate
> ```
