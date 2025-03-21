from transformers import pipeline

# Load the pre-trained summarization model
model_summarization_pipeline = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text):
    """
    Summarizes the given text into 3-5 sentences, ensuring clarity.
    """
    if not text or len(text) < 50:
        return text  # Return as is if too short

    # Generate summary with controlled length
    summary = model_summarization_pipeline(text, max_length=80, min_length=40, do_sample=False)
    summary_sentences = summary[0]['summary_text'].split(". ")

    # Limit to 3-5 meaningful sentences
    return ". ".join(summary_sentences[:5])