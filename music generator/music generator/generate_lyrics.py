from transformers import pipeline

def generate_lyrics(topic, theme):
    generator = pipeline("text-generation", model="gpt2")
    prompt = f"Write a {theme} song about {topic}:\n"
    result = generator(prompt, max_length=100, do_sample=True, temperature=0.9)
    lyrics = result[0]['generated_text']
    return lyrics.strip()
