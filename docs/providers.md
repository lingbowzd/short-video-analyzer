# Providers

Providers are optional. You can use any object with a compatible method.

## Summary Provider

A summary provider must expose:

```python
summarize(summary_input=..., keyframes=..., metadata=...)
```

Built-in scaffolds:

- `OpenAISummaryProvider`
- `LocalVLMSummaryProvider`

## Transcription Provider

A transcription provider must expose:

```python
transcribe(media_path)
```

Built-in scaffolds:

- `WhisperTranscriber`
- `AzureSpeechTranscriber`

API keys can be passed directly to providers or supplied through provider-native
environment variables.

