# Realistic cycling speeds for the Helsinki metropolitan region

This is a Python package to ‘bake in’ cycling speeds into the edges of an
OpenStreetMap dump. This package does not contain input data, but relies on a
CSV file with columns `osm_id` and `speed` (m/s), produced, for instance, from
Strava Metro data or the Helsinki bike-share system data set.

This package is used, for instance, for [calculating travel time matrices of the
metropolitan
area](https://github.com/masked-for-review/helsinki-ttm-sdata-2024).


## Installation

```
pip install git+https://github.com/masked-for-review/cycling-speed-annotator.git
```


## Use

Instantiate a `CyclingSpeedAnnotator()`, passing a `pandas.DataFrame` with
columns for the `osm_id` and the measured speed of OpenStreetMap network edges.
Optionally, also specify `cycling_speeds_column_names` as a `tuple`, a
`base_speed` to normalise using the average of the measured speeds to, or a
`tag_name` to adjust the name of the OSM tag to which this value will be
written.

```
>>> from cycling_speed_annotator import CyclingSpeedAnnotator
>>> cycling_speed_annotator = CyclingSpeedAnnotator(
...     pandas.DataFrame({
...         "osm_id" [123,],
...         "speed": [6.5,]
...     })
... )
>>> cycling_speed_annotator.annotate("input.osm.pbf", "output.osm.pbf")
```


## Dependencies

This package calls [`osmium`](https://docs.osmcode.org/pyosmium/latest/ref_osmium.html), which is available as a package for most Linux distributions (e.g., `osmium-tool` on Ubuntu and Arch).
