###### \# Planetary\_Atlas

###### 

###### Version: 1.0.0 (Experimental)

###### 

###### This project is an experimental scientific toolkit for analyzing protoplanetary disk data, identifying planet‑forming regions, and generating hydro simulation plans. It is not actively supported, maintained, or guaranteed to be stable. You are free to use it, fork it, modify it, or extend it, but it is provided as‑is.

###### 

###### If you use this project in academic work, please cite it. A DOI will be added once the first release is archived on Zenodo.

###### 

###### \## Features

###### 

###### \- Load and analyze disk physics data

###### \- Identify planet candidate radii

###### \- Generate hydro simulation target lists

###### \- Simple, modular tool architecture

###### \- Minimal dependencies

###### \- Clear documentation and examples

###### 

###### \## Installation

###### 

###### Clone the repository:

###### 

###### git clone https://github.com/RadioJupiter/Planetary\_Atlas.git

###### cd Planetary\_Atlas

###### 

###### Install dependencies:

###### 

###### pip install -r requirements.txt

###### 

###### \## Quickstart

###### 

###### from atlas.disk\_atlas import DiskAtlas

###### from tools.planet\_finder import find\_planet\_candidates

###### from tools.hydro\_planner import make\_hydro\_plan

###### 

###### atlas = DiskAtlas("atlas/atlas\_data.npz")

###### 

###### candidates = find\_planet\_candidates(atlas)

###### plan = make\_hydro\_plan(atlas)

###### 

###### print("Candidates:", candidates)

###### print("Hydro Plan:", plan)

###### 

###### \## Documentation

###### 

###### All documentation is located in the `docs/` directory:

###### 

###### \- overview.md — project overview

###### \- installation.md — how to install and run

###### \- api.md — module and function reference

###### \- architecture.md — system design and data flow

###### \- examples.md — usage examples

###### \- Quickstart.ipynb — interactive notebook

###### 

###### \## Project Structure

###### 

###### atlas/  

###### &#x20;   disk\_atlas.py  

###### tools/  

###### &#x20;   planet\_finder.py  

###### &#x20;   hydro\_planner.py  

###### docs/  

###### &#x20;   \*.md  

###### &#x20;   Quickstart.ipynb  

###### 

###### \## License

###### 

###### This project is released under an open license. You may use, modify, and redistribute it freely.

###### 

###### \## Support

###### 

###### This project is experimental and not actively supported. Issues and pull requests may not be reviewed.

###### 

###### \## Citation

###### 

###### A DOI will be added once the first tagged release is archived on Zenodo. Until then, please cite the GitHub repository:

###### 

###### RadioJupiter (2026). Planetary\_Atlas. GitHub repository: https://github.com/RadioJupiter/Planetary\_Atlas

###### 

