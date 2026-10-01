from yt_dlp import YoutubeDL


class VideoTextExtractor:
    # espera o retorno de uma string em forma de dicionario
    def extract_info(self, url: str) -> dict:
        options = {
            "skip_download": True,
            "quiet": True,
        }

        with YoutubeDL(options) as ydl:
            return ydl.extract_info(
                url,
                download=False,
            )