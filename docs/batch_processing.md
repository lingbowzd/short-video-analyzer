# Batch Processing

The MVP focuses on the single-video API. Batch workflows can be built by
iterating over rows and saving each `SummaryResult` as JSON.

```python
for row in rows:
    result = summarizer.summarize(**row)
    result.save_json(f"outputs/{row['video_id']}.json")
```

Future versions can add checkpointing, retry logic, rate-limit handling, and
JSONL/CSV exporters.

