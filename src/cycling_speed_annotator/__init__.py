

"""Add custom tags to OSM extracts for travel time matrices"""

__version__ = "0.0.1"

from .cycling_speed_annotator import CyclingSpeedAnnotator

__all__ = [
    "CyclingSpeedAnnotator",
    "__version__",
]
