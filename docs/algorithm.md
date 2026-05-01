# Algorithm

The toolkit follows a summary-first pipeline:

1. Collect available social-video metadata.
2. Optionally transcribe audio.
3. Extract a compact set of keyframes.
4. Format text, metadata, transcript, and keyframes for a summary model.
5. Generate a grounded short video summary.
6. Optionally compute lightweight post-summary features.

## Why Not Frame-by-Frame?

Short-form social videos are dense but brief. For many research applications,
analyzing every frame is unnecessary and expensive. A small number of
informative keyframes, combined with transcript and available social metadata, often
captures the semantic content needed for downstream analysis.

## Missing Metadata

The pipeline does not assume that every platform exposes the same fields. TikTok
data may include music, stickers, subtitles, hashtags, and descriptions, while
other platforms may only provide a video file and description. Missing fields
are omitted from the prompt.

## Output Philosophy

The primary output is a summary. Feature extraction is intentionally optional.
This keeps the package focused and lets researchers choose their own downstream
topic, emotion, embedding, or classification models.
