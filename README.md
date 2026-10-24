# Automated Podcast Chapter Segmentation and Topic Modeling

An NLP-powered audio intelligence pipeline that ingests long-form podcast transcripts, performs semantic shift detection, segments audio tracks into logical chapters with descriptive titles, and extracts core topic keywords.

## Features
- **Semantic Boundary Detection:** Identifies topic shifts across long transcripts.
- **Automated Chapter Titling:** Generates meaningful chapter names and timestamps.
- **FastAPI REST Endpoint:** Ready for integration with podcast streaming and hosting platforms.

## Project Structure
```text
podcast_chapter_segmenter/
├── data/
│   └── podcast_transcript.txt
├── src/
│   ├── podcast_analyzer.py
│   └── app.py
├── requirements.txt
└── README.md
```

## Quick Start
1. Install dependencies: `pip install -r requirements.txt`
2. Run segmentation script: `python src/podcast_analyzer.py`
3. Start API server: `uvicorn src.app:app --reload`
