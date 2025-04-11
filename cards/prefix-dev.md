
Project ideas `pixi` and `rattler`: 

## rattler-build parallelization

Users have asked us if we can run `rattler-build` package builds in parallel - and we would like to make it a reality. For this, we need a global process control and start - stop build processes when needed to make sure that they are parallelized efficiently.

During this task, you would interact with low-level system primitives to handle raw processes and manage system resources!


## Pixi UI

Work on the first Pixi UI with us. We would like to build a prototype for a UI to manage your pixi projects and environments. The UI will be written with a Rust backend, and a JS/TS frontend that runs with Tauri on the user machines. 

Features should include:

- See what's installed in the pixi environment
- What updates are available
- Run pixi tasks from the UI
- And more ...

## Pixi for Lua, Postgres and Ruby

Help us to make the Lua and Postgres ecosystems play really nice with pixi! 

Currently, most users associate the Conda ecosystem with Python. But – Conda packages are generic binary packages that can work with any language and on all operating systems. We want to drive this point home and extend the Conda packages that exist for a few key ecosystems such as Postgres (Postgres itself, as well as extensions that usually contain C code), Lua (and Lua extension packages), Ruby (and Ruby packages). 

During this project you would learn a lot about package management, the Conda ecosystem, and how we can create a frictionless experience for our users. You would help us grow the Conda ecosystems in new, exciting directions.
