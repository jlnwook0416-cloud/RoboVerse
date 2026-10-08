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
- **Programming Language:** Python
- **Physics Engine:** MuJoCo
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

Development rules for AI coding agents are defined in:

```text
AGENTS.md
```

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

The project is currently in the initial development phase.

Current work focuses on preparing the development environment and establishing the basic project foundation.

More detailed implementation status will be updated as development progresses.

---

## Project Structure

The project structure will be expanded gradually as needed.

Current example:

```text
RoboVerse/
├── AGENTS.md
├── README.md
├── .gitignore
└── .venv/
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

Dependencies will be documented here as they are added to the project.

The project is expected to use MuJoCo and Python-related packages required for simulation.

Do not install unnecessary dependencies before they are required by the current Stage.

---

## Running the Simulator

The simulator entry point has not been finalized yet.

The run command will be added after the main application structure is created.

Example placeholder:

```bash
python <main-file>.py
```

---

## Testing

Automated testing will be introduced as the project grows.

Until then, development may include checks such as:

- Python syntax validation
- Import validation
- MuJoCo model loading
- Simulator startup
- Basic robot behavior verification
- Regression checks

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

Detailed development rules for coding agents are maintained separately in `AGENTS.md`.

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