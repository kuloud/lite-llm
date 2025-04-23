import soundfile as sf
from dia.model import Dia

# Load the model
model = Dia.from_pretrained("nari-labs/Dia-1.6B")

class DiaService:
    @staticmethod
    def generate_audio(text: str, output_path: str = "simple.mp3"):
        """
        Generate audio from the given text using the Dia model.

        Args:
            text (str): The input text for audio generation.
            output_path (str): The path to save the generated audio file.

        Returns:
            str: The path of the generated audio file.
        """
        output = model.generate(text)
        sf.write(output_path, output, 44100)
        return output_path
