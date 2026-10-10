# RoboVerse

RoboVerse is a MuJoCo-based humanoid robot simulator project.

The goal is to build a humanoid robot simulator step by step while learning robotics, simulation, physics, control, and AI-assisted development.

This project is being developed incrementally using AI-assisted coding tools such as ChatGPT, Codex, and Claude.

---

## Project Goals

RoboVerse aims to develop a humanoid robot simulator that can gradually support:

- Humanoid robot body modeling
- Joint-based movement
- Physics simulation
- Robot control
- Sensor simulation
- ROS 2 integration
- AI-based robot control
- Possible future connection to real robot hardware

The project will be developed in small stages rather than building all systems at once.

---

## Development Environment

- **Operating System:** macOS
- **Editor:** Visual Studio Code
- **Programming Language:** Python 3.13.14
- **Physics Engine:** MuJoCo 3.15.0
- **Python Environment:** project-local `.venv`
- **Version Control:** Git / GitHub

### AI Development Tools

- **ChatGPT** — planning, architecture, explanation, review, and learning support
- **Codex** — code implementation, modification, and testing
- **Claude** — optional secondary review and validation

---

## Development Method

RoboVerse follows an incremental development approach.

The basic workflow is:

```text
Plan
↓
Implement a small task
↓
Run and test
↓
Fix errors
↓
Verify existing functionality
↓
Review results
↓
Proceed to the next approved task
```

The project avoids unnecessary large refactors and future-stage implementation.

If an `AGENTS.md` file is provided, read it before making changes. It is not
currently included in this checkout.

---

## Development Roadmap

| Stage | Goal |
|---|---|
| Stage 0 | Make the project ready for development |
| Stage 1 | Create the project structure |
| Stage 2 | Create the virtual world |
| Stage 3 | Create the torso |
| Stage 4 | Create the head |
| Stage 5 | Create the arms |
| Stage 6 | Create the legs and feet |
| Stage 7 | Adjust the robot into a human-like form |
| Stage 8 | Apply and refine physics |
| Stage 9 | Verification, documentation, and GitHub cleanup |

Each Stage may be divided into smaller tasks such as:

```text
0-1
0-2
0-3
```

A later Stage should not begin until the current Stage has been completed and approved.

---

## Project Status

The project is at **Stage 2: the virtual world and basic physics environment**.

- `main.py` loads the virtual world and opens the managed MuJoCo Viewer.
- The world contains a ground plane, gravity, lighting, a fixed camera, and a sky background.
- A separate sphere-drop model and automated regression test verify free fall,
  ground contact, and stable rest.
- Automated physics checks and manual Viewer checks have passed in the
  development environment listed above.

The next planned stage is torso modeling. Later stages require explicit approval.

---

## Project Structure

```text
RoboVerse/
├── .gitignore
├── .venv/                     # Local environment; ignored by Git
├── README.md
├── main.py                    # Virtual-world entry point
├── test_mujoco.py             # Original manual Viewer check
├── docs/
│   └── .gitkeep
├── models/
│   ├── .gitkeep
│   ├── world.xml              # Base environment
│   └── physics_test.xml       # Includes world.xml and adds one test sphere
├── src/
│   └── __init__.py
└── tests/
    ├── __init__.py
    └── test_physics.py         # Automated physics regression test
```

Additional source code, robot models, tests, configuration files, and simulation assets will be added only when required by the current development Stage.

---

## Setup

### 1. Clone the repository

```bash
git clone <repository-url>
```

Move into the project directory:

```bash
cd RoboVerse
```

---

### 2. Create a Python virtual environment

```bash
python3 -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

---

### 3. Install Dependencies

Stage 2 uses MuJoCo 3.15.0 in the existing Python 3.13.14 virtual environment.
Confirm that environment before running the simulator:

```bash
.venv/bin/python -c 'import sys, mujoco; print(sys.version); print(mujoco.__version__)'
```

The commands below use `.venv` directly, so activating it is optional. Existing
installations do not need dependency updates for this stage.

---

## Running the Simulator

From the project root, run:

```bash
.venv/bin/python main.py
```

`main.py` resolves `models/world.xml` relative to its own file location, so it
also works when called by absolute path from another working directory. It
creates `MjModel` and `MjData` and calls `mujoco.viewer.launch(model, data)`
using ordinary Python on macOS. Viewer controls provide simulation timing,
pause, resume, and window closure. The named `overview` camera is available in
the Viewer camera controls.

Missing files, model-loading errors, and Viewer-launch errors are reported to
the terminal with exit code 1. Closing the Viewer normally returns exit code 0.

### Virtual world

`models/world.xml` contains:

- A ground plane at `z = 0`, with collision masks `contype=1` and `conaffinity=1`.
- Gravity `(0, 0, -9.81)` in meters and seconds.
- A directional light and a fixed `overview` camera.
- A blue-gray gradient skybox and a contrasting pale ground color.

The base world has no robot or obstacles. `models/physics_test.xml` includes the
base world and adds one freely moving sphere: mass 1 kg, radius 0.1 m, initial
center height 1 m. Its higher-priority contact setting uses `solref="0.004 1"`
to limit temporary soft-contact overlap at the default 0.002 s timestep. This
setting belongs to the test sphere; future robot contact settings need their
own validation.

---

## Testing

Run the physics regression test from the project root:

```bash
.venv/bin/python -B -m unittest tests.test_physics -v
```

Run all automated tests in `tests/`:

```bash
.venv/bin/python -B -m unittest discover -s tests -v
```

The test simulates 5 seconds, records height and vertical velocity, checks
free-fall predictions before impact, detects sphere-ground contact, and checks
stability throughout the final second. Passing runs print `OK`.

| Check | Tolerance |
|---|---|
| Free-fall height | 5 mm |
| Free-fall vertical velocity | 0.01 m/s |
| First contact time | 0.004 s |
| Temporary overlap during impact | 5 mm |
| Resting height relative to radius | 1 mm |
| Resting linear speed | 0.001 m/s |
| Resting angular speed | 0.001 rad/s |
| Height variation during final second | 1 mm |

MuJoCo uses soft contacts, so small temporary overlap is expected. These limits
apply to this test setup and do not guarantee results for future robot models.

### Manual Viewer checks

Open the sphere-drop model to observe falling, contact, and settling:

```bash
.venv/bin/python -m mujoco.viewer --mjcf=models/physics_test.xml
```

Use the Viewer reset control to replay the drop. Check pause and resume, close
the window, then confirm a normal exit:

```bash
echo $?
```

The expected exit code is `0`. Repeat the display and closure checks with
`main.py`. The original `test_mujoco.py` is an interactive smoke-check script,
not an automated unittest; run it separately:

```bash
.venv/bin/python test_mujoco.py
```

A feature should not be considered complete unless it has been verified appropriately.

---

## Development Principles

RoboVerse follows several core principles:

- Make small and safe changes.
- Protect existing working functionality.
- Avoid unnecessary complexity.
- Do not guess unknown project structures or values.
- Use realistic physical values when possible.
- Clearly identify temporary assumptions.
- Test changes before reporting them as successful.
- Do not move to future Stages without approval.
- Keep the code understandable for learning purposes.

---

## Git Guidelines

Files that should generally not be committed include:

```text
.venv/
__pycache__/
.DS_Store
cache files
temporary editor files
generated build artifacts
```

Sensitive information must never be committed.

Examples:

```text
API keys
access tokens
passwords
private credentials
```

Commit titles follow `[RoboVerse][Stage N] English Commit Description`.
The Stage 2 commit title is:

```text
[RoboVerse][Stage 2] Build MuJoCo Simulation Environment
```

---

## Documentation

Documentation will be updated when changes affect:

- Installation
- Dependencies
- Project structure
- Run commands
- Robot controls
- Simulation behavior
- User-visible features

Read any supplied `AGENTS.md` for additional development rules.

---

## Future Direction

After the basic humanoid simulator is completed, RoboVerse may be expanded with:

- More realistic robot dynamics
- Advanced joint control
- Sensor simulation
- Cameras
- IMU
- Force and torque sensors
- ROS 2
- AI-based control
- Reinforcement learning
- Physical AI
- Real robot hardware integration

These features are long-term possibilities and are not implemented in advance unless required by the current roadmap.

---

## License

A license has not been selected yet.
