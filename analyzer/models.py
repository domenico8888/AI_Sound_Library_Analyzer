from dataclasses import dataclass, field
from typing import Optional, List, Dict


@dataclass
class PluginInfo:

    name: Optional[str] = None
    vendor: Optional[str] = None
    version: Optional[str] = None
    format: Optional[str] = None



@dataclass
class SoundClassification:

    category: Optional[str] = None
    style: Optional[str] = None
    mood: List[str] = field(default_factory=list)
    energy: Optional[float] = None



@dataclass
class SoundMetadata:

    filename: str
    extension: str
    path: str
    sound_type: str



@dataclass
class Sound:

    id: str

    metadata: SoundMetadata

    plugin: Optional[PluginInfo] = None

    classification: SoundClassification = field(
        default_factory=SoundClassification
    )

    synthesis: Dict = field(
        default_factory=dict
    )

    audio_features: Dict = field(
        default_factory=dict
    )

    midi_features: Dict = field(
        default_factory=dict
    )

    embedding: Optional[List[float]] = None



    def to_dict(self):

        return {

            "id": self.id,

            "metadata": {

                "filename": self.metadata.filename,
                "extension": self.metadata.extension,
                "path": self.metadata.path,
                "type": self.metadata.sound_type

            },


            "plugin":
                vars(self.plugin)
                if self.plugin
                else None,


            "classification":
                vars(self.classification),


            "synthesis":
                self.synthesis,


            "audio_features":
                self.audio_features,


            "midi_features":
                self.midi_features,


            "embedding":
                self.embedding

        }