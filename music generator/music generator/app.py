from flask import Flask, render_template, request, send_from_directory
from generate_lyrics import generate_lyrics
from generate_music import generate_music
import os
import pyttsx3

app = Flask(__name__)
OUTPUT_DIR = "static/generated"
os.makedirs(OUTPUT_DIR, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    lyrics = ""
    if request.method == "POST":
        custom_lyrics = request.form.get("custom_lyrics", "").strip()
        theme = request.form.get("theme", "").strip()

        if custom_lyrics:
            lyrics = custom_lyrics
        elif theme:
            lyrics = generate_lyrics(theme)
        else:
            lyrics = "No lyrics provided."

        # Save lyrics to text file
        lyrics_path = os.path.join(OUTPUT_DIR, "lyrics.txt")
        with open(lyrics_path, "w") as f:
            f.write(lyrics)

        # Generate music
        music_path = os.path.join(OUTPUT_DIR, "music.wav")
        generate_music(lyrics, music_path)

        # Text-to-speech
        engine = pyttsx3.init()
        tts_path = os.path.join(OUTPUT_DIR, "tts.wav")
        engine.save_to_file(lyrics, tts_path)
        engine.runAndWait()

    return render_template("index.html", lyrics=lyrics)

@app.route("/download/<filename>")
def download_file(filename):
    return send_from_directory(OUTPUT_DIR, filename, as_attachment=True)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Required for Railway
    app.run(host="0.0.0.0", port=port)


