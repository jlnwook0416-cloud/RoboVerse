from pathlib import Path
import sys

import mujoco
import mujoco.viewer


def main() -> int:
    print("RoboVerse Simulator Started")
    world_path = Path(__file__).resolve().parent / "models" / "world.xml"

    if not world_path.is_file():
        print(f"World file not found: {world_path}", file=sys.stderr)
        return 1

    try:
        model = mujoco.MjModel.from_xml_path(str(world_path))
        data = mujoco.MjData(model)
    except Exception as error:
        print(
            f"Failed to load world '{world_path}': "
            f"{type(error).__name__}: {error}",
            file=sys.stderr,
        )
        return 1

    try:
        mujoco.viewer.launch(model, data)
    except Exception as error:
        print(
            f"Failed to launch MuJoCo Viewer: {type(error).__name__}: {error}",
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
