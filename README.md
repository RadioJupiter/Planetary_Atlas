# Planetary_Atlas
A physics-driven tool for mapping protoplanetary disks, predicting ring formation, and identifying hidden planet candidates.

Core features:
-DiskAtlas model for laoding and analyzing disk physics
    - Planet-candidate finder (planet_finder.py)
        - Hydro-time reduction planner (hydro_planner.py)
            - Modular structure for scientific workflows
                - Clean Python package layout

Installation: 

git clone https://github.com/RadioJupiter/Planetary_Atlas.git
cd Planetary_Atlas


Install dependencies: 

pip install numpy pandas matplotlib


USAGE

Load the atlas: 

from atlas.disk_atlas import DiskAtlas
atlas = DiskAtlas("atlas/atlas_data.npz")

Find planet candidates:

from tools.planet_finder import find_planet_candidates
find_planet_candidates(atlas)

Generate  hydro simulation targets:

from tools.hydro_planner import make_hydro_plan
make_hydro_plan(atlas)

Run example script: 

python run_atlas.py


Project Structure: 

Planetary_Atlas/
  atlas/
    disk_atlas.py
    atlas_data.npz
  tools/
    planet_finder.py
    hydro_planner.py
  run_atlas.py
  README.md
  LICENSE
  .gitignore

LICENSE

MIT License