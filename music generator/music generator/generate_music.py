import torchaudio
from audiocraft.models import MusicGen
from audiocraft.data.audio import audio_write

def generate_music(lyrics, output_path):
    model = MusicGen.get_pretrained('facebook/musicgen-small')
    model.set_generation_params(duration=10)
    wav = model.generate([lyrics])
    audio_write(output_path.replace(".wav", ""), wav[0].cpu(), model.sample_rate, strategy="loudness")

