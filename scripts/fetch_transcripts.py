"""
YouTube Transcript Fetcher for AI-Powered SEO Research
=======================================================
This script fetches transcripts from YouTube videos by expert practitioners
in AI-powered SEO content production, and saves them as structured markdown files.

Usage:
    python fetch_transcripts.py

Requirements:
    pip install youtube-transcript-api
"""

import os
import re
from datetime import datetime
from youtube_transcript_api import YouTubeTranscriptApi, NoTranscriptFound, TranscriptsDisabled

# ─────────────────────────────────────────────
# TARGET VIDEOS: High-signal, practitioner-led
# Each entry: (expert_name, video_id, video_title, channel_name, why_selected)
# ─────────────────────────────────────────────
TARGET_VIDEOS = [
    {
        "expert": "Koray Tugberk Gubur",
        "video_id": "X_ou1eO28gE",
        "title": "Exploring Holistic SEO (Semantic SEO, Topical Authority, Technical SEO) with Koray Tugberk",
        "channel": "Koray Tugberk Gubur",
        "why": "Core methodology for building topic cluster architecture - foundational for any AI content production system.",
        "filename": "koray-gubur-topical-authority-semantic-seo.md"
    },
    {
        "expert": "Ross Simmonds",
        "video_id": "VXxFJAg7YJw",
        "title": "Content Distribution in the Age of AI -- Ross Simmonds, Foundation Marketing",
        "channel": "Ross Simmonds",
        "why": "Practical GEO (Generative Engine Optimization) walkthrough - directly actionable for making AI content get cited by LLMs.",
        "filename": "ross-simmonds-content-distribution-ai.md"
    },
    {
        "expert": "Lily Ray",
        "video_id": "9dONdby7dDU",
        "title": "You are what you EEAT | Lily Ray, Founder @ Algorythmic & VP SEO & AI Search @ Amsive",
        "channel": "Lily Ray",
        "why": "E-E-A-T deep dive - the quality framework AI content must satisfy to avoid algorithm penalties.",
        "filename": "lily-ray-eeat-ai-search.md"
    },
    {
        "expert": "Kevin Indig",
        "video_id": "p3_P0dDspBI",
        "title": "Chat With Kevin Indig | The Great Decoupling, SEO Attribution & AI-Driven Growth Strategies",
        "channel": "Kevin Indig",
        "why": "SEO attribution and AI-driven growth strategies - essential for measuring AI content production ROI.",
        "filename": "kevin-indig-seo-attribution-ai-growth.md"
    },
    {
        "expert": "Eli Schwartz",
        "video_id": "_wbGrykRzQA",
        "title": "Product-Led SEO Still Works For AI Search, with Eli Schwartz",
        "channel": "Eli Schwartz",
        "why": "Audience-intent framework that ensures AI content targets real buyer queries, not vanity keywords.",
        "filename": "eli-schwartz-product-led-seo-ai.md"
    },
]

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "research", "youtube-transcripts")
os.makedirs(OUTPUT_DIR, exist_ok=True)


def clean_text(text: str) -> str:
    """Remove excessive whitespace and normalize transcript text."""
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def chunk_transcript(transcript_list: list, chunk_size: int = 30) -> list:
    """Group transcript entries into readable chunks (every N entries = ~1 paragraph)."""
    chunks = []
    for i in range(0, len(transcript_list), chunk_size):
        batch = transcript_list[i:i + chunk_size]
        combined_text = " ".join([clean_text(entry["text"]) for entry in batch])
        start_time = batch[0]["start"]
        minutes = int(start_time // 60)
        seconds = int(start_time % 60)
        timestamp = f"{minutes:02d}:{seconds:02d}"
        chunks.append({"timestamp": timestamp, "text": combined_text})
    return chunks


def format_as_markdown(video_info: dict, chunks: list) -> str:
    """Format the transcript chunks as a structured markdown document."""
    expert = video_info["expert"]
    title = video_info["title"]
    channel = video_info["channel"]
    video_id = video_info["video_id"]
    why = video_info["why"]
    url = f"https://www.youtube.com/watch?v={video_id}"
    fetch_date = datetime.now().strftime("%B %d, %Y")

    md = f"""# Transcript: {title}

**Expert:** {expert}  
**Channel:** {channel}  
**Video URL:** {url}  
**Fetched:** {fetch_date}  
**Why This Video Was Selected:** {why}

---

## Full Transcript (Timestamped)

"""
    for chunk in chunks:
        md += f"**[{chunk['timestamp']}]** {chunk['text']}\n\n"

    md += "---\n\n*Transcript fetched automatically via youtube-transcript-api for research purposes.*\n"
    return md


def fetch_transcript(video_info: dict) -> bool:
    """Attempt to fetch and save transcript for a single video."""
    video_id = video_info["video_id"]
    title = video_info["title"]
    expert = video_info["expert"]
    output_path = os.path.join(OUTPUT_DIR, video_info["filename"])

    print(f"\n[VIDEO] Fetching: [{expert}] {title}")
    print(f"   Video ID: {video_id}")

    try:
        api = YouTubeTranscriptApi()
        fetched = api.fetch(video_id)
        # Convert FetchedTranscriptSnippet objects to dicts for our chunk function
        transcript_list = [{"text": s.text, "start": s.start} for s in fetched]
        chunks = chunk_transcript(transcript_list)
        markdown = format_as_markdown(video_info, chunks)

        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown)

        word_count = sum(len(chunk["text"].split()) for chunk in chunks)
        print(f"   [OK] SUCCESS - {len(chunks)} chunks, ~{word_count} words -> {video_info['filename']}")
        return True

    except NoTranscriptFound:
        print(f"   [WARN] No English transcript available for this video.")
        placeholder = f"""# Transcript: {title}

**Expert:** {expert}  
**Video URL:** https://www.youtube.com/watch?v={video_id}  
**Status:** No auto-generated English transcript available for this video.

## Manual Notes

*To be filled in manually after watching the video.*

**Key Points Observed:**
- Point 1
- Point 2
- Point 3
"""
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(placeholder)
        print(f"   [NOTE] Placeholder created -> {video_info['filename']}")
        return False

    except TranscriptsDisabled:
        print(f"   [WARN] Transcripts are disabled for this video.")
        return False

    except Exception as e:
        print(f"   [ERROR]: {type(e).__name__}: {e}")
        return False


def main():
    print("=" * 60)
    print("[AI-SEO Research] YouTube Transcript Fetcher")
    print(f"[OUTPUT] Directory: {OUTPUT_DIR}")
    print(f"[TARGET] Fetching {len(TARGET_VIDEOS)} videos")
    print("=" * 60)

    success_count = 0
    for video in TARGET_VIDEOS:
        if fetch_transcript(video):
            success_count += 1

    print("\n" + "=" * 60)
    print(f"[DONE] {success_count}/{len(TARGET_VIDEOS)} transcripts fetched successfully.")
    print(f"[OUTPUT] Files saved to: {OUTPUT_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    main()
