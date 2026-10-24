from fastapi import FastAPI
from pydantic import BaseModel
from src.podcast_analyzer import PodcastChapterSegmenter

app = FastAPI(title="Podcast Chapter Segmentation & Topic API", version="1.0")
segmenter = PodcastChapterSegmenter()

@app.get("/")
def home():
    return {"message": "Podcast Chapter Segmentation API is online!"}

@app.get("/chapters")
def get_chapters():
    return segmenter.process_podcast()
