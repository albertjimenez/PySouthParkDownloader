from dataclasses import dataclass, field

from yt_dlp.postprocessor import PostProcessor


@dataclass()
class SPPostProcessor(PostProcessor):
    filenames: list[str] = field(default_factory=lambda: [])

    def __init__(self):
        super(SPPostProcessor, self).__init__(None)
        self.filenames = []

    def run(self, information):
        self.filenames = self.filenames + [information['filepath']]
        return [], information
