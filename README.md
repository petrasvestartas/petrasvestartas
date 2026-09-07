<div align="center">

# Petras Vestartas

**Computational design · Timber joinery · Geometry kernels**

PhD in Timber Structures, [IBOIS](https://www.epfl.ch/labs/ibois/) · EPFL &nbsp;&nbsp;|&nbsp;&nbsp; Postdoctoral researcher, [Block Research Group](https://block.arch.ethz.ch) · ETH Zürich

[![Website](https://img.shields.io/badge/vestartas.com-1F6FEB?style=for-the-badge&logo=googlechrome&logoColor=white)](https://vestartas.com)
[![Sponsor](https://img.shields.io/badge/Sponsor-DB61A2?style=for-the-badge&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/petrasvestartas)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-FF5E5B?style=for-the-badge&logo=kofi&logoColor=white)](https://ko-fi.com/petrasvestartas)

</div>

I build open-source geometry tooling for architecture and digital fabrication: **timber joint
generation**, **2D nesting** for sheet material, and **multi-language geometry kernels** that expose
one identical API from Python, C++ and Rust.

---

## Projects

**Own work**

- **[wood_research](https://github.com/petrasvestartas/wood_research)** &nbsp;![C++](https://img.shields.io/badge/-C%2B%2B-00599C?logo=cplusplus&logoColor=white&style=flat-square) ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square)<br>The timber-joinery stack as one superproject. [`wood`](https://github.com/petrasvestartas/wood) detects where two plates touch and carves the joint; [`wood_nano`](https://github.com/petrasvestartas/wood_nano) binds it to Python via `nanobind`; [`compas_wood`](https://github.com/petrasvestartas/compas_wood) wraps that for [COMPAS](https://compas.dev). Pinned as submodules, so one clone builds the whole chain. &nbsp;[📖 Docs](https://petrasvestartas.github.io/compas_wood/latest/)
- **[OpenNest](https://github.com/petrasvestartas/OpenNest)** &nbsp;![C#](https://img.shields.io/badge/-C%23-512BD4?logo=dotnet&logoColor=white&style=flat-square) ![C++](https://img.shields.io/badge/-C%2B%2B-00599C?logo=cplusplus&logoColor=white&style=flat-square)<br>2D polygonal nesting for Rhino / Grasshopper — parts with holes, nesting *inside* holes, non-rectangular sheets. &nbsp;[📖 Docs](https://petrasvestartas.github.io/OpenNest/)
- **[NGon](https://github.com/petrasvestartas/NGon)** &nbsp;![C#](https://img.shields.io/badge/-C%23-512BD4?logo=dotnet&logoColor=white&style=flat-square)<br>Polygonal (n-gon) mesh processing for Grasshopper. &nbsp;[📦 food4rhino](https://www.food4rhino.com/en/app/ngon)
- **[session](https://github.com/petrasvestartas/session)** &nbsp;![Rust](https://img.shields.io/badge/-Rust-CE422B?logo=rust&logoColor=white&style=flat-square) ![C++](https://img.shields.io/badge/-C%2B%2B-00599C?logo=cplusplus&logoColor=white&style=flat-square) ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square)<br>One geometry kernel, implemented three times — Python, C++, Rust — with identical APIs, shared protobuf schemas and one shared test suite.

**[COMPAS](https://compas.dev)** — computational framework for architecture, engineering and fabrication

- **[compas_cgal](https://github.com/compas-dev/compas_cgal)** &nbsp;![C++](https://img.shields.io/badge/-C%2B%2B-00599C?logo=cplusplus&logoColor=white&style=flat-square) ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square)<br>CGAL bindings for COMPAS — booleans, meshing, slicing, remeshing
- **[compas_libigl](https://github.com/compas-dev/compas_libigl)** &nbsp;![C++](https://img.shields.io/badge/-C%2B%2B-00599C?logo=cplusplus&logoColor=white&style=flat-square) ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square)<br>libigl bindings for COMPAS — geodesics, parametrisation, isolines
- **[compas_occt](https://github.com/petrasvestartas/compas_occt)** &nbsp;![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square) ![C++](https://img.shields.io/badge/-C%2B%2B-00599C?logo=cplusplus&logoColor=white&style=flat-square)<br>OpenCASCADE (OCCT 8) geometry for COMPAS: NURBS, Breps, booleans and STEP/IGES/STL I/O. A drop-in [`compas_occ`](https://github.com/compas-dev/compas_occ) replacement that links OCCT through a single `nanobind` module instead of `pythonocc-core`. &nbsp;[📖 Docs](https://petrasvestartas.github.io/compas_occt) &nbsp;[📦 PyPI](https://pypi.org/project/compas-occt/)
- **[compas_shapeop](https://github.com/compas-dev/compas_shapeop)** &nbsp;![C++](https://img.shields.io/badge/-C%2B%2B-00599C?logo=cplusplus&logoColor=white&style=flat-square) ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square)<br>ShapeOp bindings via `nanobind` — constraint-based geometry solving
- **[compas_nanobind_package_template](https://github.com/compas-dev/compas_nanobind_package_template)** &nbsp;![C++](https://img.shields.io/badge/-C%2B%2B-00599C?logo=cplusplus&logoColor=white&style=flat-square) ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square)<br>cookiecutter template for COMPAS C++ extensions
- **[compas](https://github.com/compas-dev/compas)** &nbsp;![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square)<br>the main COMPAS library and its Rhino / Grasshopper / Blender integrations

**[Block Research Group](https://block.arch.ethz.ch), ETH Zürich**

- **[compas_model](https://github.com/BlockResearchGroup/compas_model)** &nbsp;![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square)<br>universal model datastructure for design, analysis, fabrication and construction
- **[compas-RV](https://github.com/BlockResearchGroup/compas-RV)** &nbsp;![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square)<br>Rhino plugin for form finding of compression networks via reciprocal form and force diagrams
- **[compas_cra](https://github.com/BlockResearchGroup/compas_cra)** &nbsp;![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square)<br>Coupled Rigid-Block Analysis — stability-aware design of discrete-element assemblies
- **[compas_lmgc90](https://github.com/BlockResearchGroup/compas_lmgc90)** &nbsp;![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square) ![C++](https://img.shields.io/badge/-C%2B%2B-00599C?logo=cplusplus&logoColor=white&style=flat-square)<br>COMPAS wrapper around the LMGC90 multi-body contact solver
- **[compas_3dec](https://github.com/BlockResearchGroup/compas_3dec)** &nbsp;![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square)<br>discrete element modelling with Itasca 3DEC
- **[compas_grid](https://github.com/BRG-research/compas_grid)** &nbsp;![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square)<br>grid structure models for multi-storey buildings
- **[compas_cnc](https://github.com/BRG-research/compas_cnc)** &nbsp;![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square)<br>subtractive fabrication operations

**[IBOIS](https://www.epfl.ch/labs/ibois/), EPFL** — Laboratory for Timber Constructions

- **[Cockroach](https://github.com/ibois-epfl/Cockroach)** &nbsp;![C++](https://img.shields.io/badge/-C%2B%2B-00599C?logo=cplusplus&logoColor=white&style=flat-square)<br>Rhino plug-in for point cloud post-processing and meshing
- **[Raccoon-ibois](https://github.com/ibois-epfl/Raccoon-ibois)** &nbsp;![C#](https://img.shields.io/badge/-C%23-512BD4?logo=dotnet&logoColor=white&style=flat-square)<br>CNC toolpath generation for timber fabrication
- **[COMPAS_ABB6700_IRBT](https://github.com/ibois-epfl/COMPAS_ABB6700_IRBT)** &nbsp;![ROS](https://img.shields.io/badge/-ROS-22314E?logo=ros&logoColor=white&style=flat-square) ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square)<br>ROS and COMPAS setup for an ABB IRB6700 on a linear track

---

## Toolbox

**Languages**

![C++](https://img.shields.io/badge/C%2B%2B-00599C?style=flat-square&logo=cplusplus&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Rust](https://img.shields.io/badge/Rust-CE422B?style=flat-square&logo=rust&logoColor=white)
![C#](https://img.shields.io/badge/C%23-512BD4?style=flat-square&logo=dotnet&logoColor=white)

**Geometry &amp; fabrication**

![Rhino](https://img.shields.io/badge/Rhino-801010?style=flat-square&logo=rhinoceros&logoColor=white)
![Grasshopper](https://img.shields.io/badge/Grasshopper-2C7A3F?style=flat-square)
![COMPAS](https://img.shields.io/badge/COMPAS-0092D2?style=flat-square)
![OpenCASCADE](https://img.shields.io/badge/OpenCASCADE-4B6A88?style=flat-square)
![CGAL](https://img.shields.io/badge/CGAL-B33A3A?style=flat-square)
![WebGPU](https://img.shields.io/badge/WebGPU-005A9C?style=flat-square&logo=webgpu&logoColor=white)

**Build &amp; tooling**

![CMake](https://img.shields.io/badge/CMake-064F8C?style=flat-square&logo=cmake&logoColor=white)
![nanobind](https://img.shields.io/badge/nanobind-306998?style=flat-square)
![Protobuf](https://img.shields.io/badge/Protobuf-4A9E8F?style=flat-square)
![GitHub Actions](https://img.shields.io/badge/Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![conda-forge](https://img.shields.io/badge/conda--forge-4E844E?style=flat-square&logo=anaconda&logoColor=white)

---

## GitHub

<div align="center">

[![Profile overview](https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=petrasvestartas&theme=default)](https://github.com/petrasvestartas?tab=repositories#gh-light-mode-only)
[![Profile overview](https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=petrasvestartas&theme=github_dark)](https://github.com/petrasvestartas?tab=repositories#gh-dark-mode-only)

[![Top languages by repository](https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=petrasvestartas&theme=default)](https://github.com/petrasvestartas?tab=repositories#gh-light-mode-only)
[![Top languages by repository](https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=petrasvestartas&theme=github_dark)](https://github.com/petrasvestartas?tab=repositories#gh-dark-mode-only)
[![Top languages by commit](https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=petrasvestartas&theme=default)](https://github.com/petrasvestartas?tab=repositories#gh-light-mode-only)
[![Top languages by commit](https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=petrasvestartas&theme=github_dark)](https://github.com/petrasvestartas?tab=repositories#gh-dark-mode-only)

[![Contribution stats](https://github-profile-summary-cards.vercel.app/api/cards/stats?username=petrasvestartas&theme=default)](https://github.com/petrasvestartas?tab=repositories#gh-light-mode-only)
[![Contribution stats](https://github-profile-summary-cards.vercel.app/api/cards/stats?username=petrasvestartas&theme=github_dark)](https://github.com/petrasvestartas?tab=repositories#gh-dark-mode-only)
[![Productive hours](https://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=petrasvestartas&utcOffset=1&theme=default)](https://github.com/petrasvestartas?tab=repositories#gh-light-mode-only)
[![Productive hours](https://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=petrasvestartas&utcOffset=1&theme=github_dark)](https://github.com/petrasvestartas?tab=repositories#gh-dark-mode-only)

</div>

---

<div align="center">

### Support this work

The libraries above are free and maintained in the open.
If they save you time, sponsorship keeps them moving.

[![Sponsor on GitHub](https://img.shields.io/badge/Sponsor%20on%20GitHub-DB61A2?style=for-the-badge&logo=githubsponsors&logoColor=white)](https://github.com/sponsors/petrasvestartas)
[![Support on Ko-fi](https://img.shields.io/badge/Support%20on%20Ko--fi-FF5E5B?style=for-the-badge&logo=kofi&logoColor=white)](https://ko-fi.com/petrasvestartas)

</div>
