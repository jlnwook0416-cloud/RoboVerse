"""Drop one sphere onto the existing world without changing world.xml."""

import math
from pathlib import Path
import unittest

import mujoco


class PhysicsEnvironmentTest(unittest.TestCase):
    def test_sphere_drop(self):
        path = Path(__file__).resolve().parents[1] / "models" / "physics_test.xml"
        model = mujoco.MjModel.from_xml_path(str(path))
        data = mujoco.MjData(model)
        ground = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_GEOM, "ground")
        sphere = mujoco.mj_name2id(model, mujoco.mjtObj.mjOBJ_GEOM, "sphere")
        self.assertGreaterEqual(ground, 0)
        self.assertGreaterEqual(sphere, 0)
        self.assertEqual(model.nq, 7)
        self.assertEqual(model.nv, 6)
        self.assertEqual(model.geom_type[sphere], mujoco.mjtGeom.mjGEOM_SPHERE)
        self.assertAlmostEqual(model.body_mass[model.geom_bodyid[sphere]], 1.0)
        self.assertEqual(tuple(model.opt.gravity), (0.0, 0.0, -9.81))

        duration = 5.0
        radius = float(model.geom_size[sphere, 0])
        initial_height = float(data.qpos[2])
        sample_times = (0.1, 0.2, 0.3, 0.4, 0.5, 1.0, 2.0, 5.0)
        samples = [(0.0, initial_height, 0.0)]
        minimum_height = initial_height
        first_contact = None
        resting_heights = []
        resting_linear_speeds = []
        resting_angular_speeds = []

        for step in range(1, round(duration / model.opt.timestep) + 1):
            mujoco.mj_step(model, data)
            height = float(data.qpos[2])
            linear_speed = math.sqrt(sum(float(v) ** 2 for v in data.qvel[:3]))
            angular_speed = math.sqrt(sum(float(v) ** 2 for v in data.qvel[3:]))
            self.assertTrue(all(math.isfinite(float(v)) for v in (*data.qpos, *data.qvel)))
            minimum_height = min(minimum_height, height)
            for contact in data.contact:
                if {int(contact.geom1), int(contact.geom2)} == {ground, sphere}:
                    if first_contact is None:
                        first_contact = float(data.time)
            if data.time >= 4.0:
                resting_heights.append(height)
                resting_linear_speeds.append(linear_speed)
                resting_angular_speeds.append(angular_speed)
            if any(step == round(t / model.opt.timestep) for t in sample_times):
                samples.append((float(data.time), height, float(data.qvel[2])))

        # Soft contact permits small temporary penetration. The sphere uses a
        # 4 ms contact time constant, twice the 2 ms timestep.
        fall_tolerance = 0.005       # 5 mm: covers Euler integration error.
        penetration_tolerance = 0.005  # 5 mm during impact.
        height_tolerance = 0.001     # 1 mm after settling.
        speed_tolerance = 0.001      # 1 mm/s linear, 0.001 rad/s angular.

        print("\nMuJoCo:", mujoco.__version__, "timestep:", model.opt.timestep)
        print("time_s  center_height_m  vertical_velocity_m_s")
        for time, height, velocity in samples:
            print(f"{time:.3f}  {height:.9f}  {velocity:.9f}")
        print(f"first_contact_s={first_contact}, minimum_height_m={minimum_height:.9f}")
        print(f"final_qvel={data.qvel.tolist()}")
        print(f"last_second_max_linear_speed={max(resting_linear_speeds):.9g}, "
              f"max_angular_speed={max(resting_angular_speeds):.9g}, "
              f"height_range={max(resting_heights) - min(resting_heights):.9g}")

        self.assertAlmostEqual(data.time, duration, places=9)
        self.assertIsNotNone(first_contact, "No sphere-ground contact detected")
        expected_contact = math.sqrt(2 * (initial_height - radius) / 9.81)
        self.assertAlmostEqual(first_contact, expected_contact, delta=2 * model.opt.timestep)
        self.assertLess(samples[1][1], initial_height)
        for time, height, velocity in samples[1:5]:
            expected_height = initial_height - 0.5 * 9.81 * time ** 2
            self.assertAlmostEqual(height, expected_height, delta=fall_tolerance)
            self.assertAlmostEqual(velocity, -9.81 * time, delta=0.01)
        self.assertGreaterEqual(minimum_height, radius - penetration_tolerance)
        self.assertLessEqual(max(abs(h - radius) for h in resting_heights), height_tolerance)
        self.assertLessEqual(max(resting_linear_speeds), speed_tolerance)
        self.assertLessEqual(max(resting_angular_speeds), speed_tolerance)
        self.assertLessEqual(max(resting_heights) - min(resting_heights), height_tolerance)


if __name__ == "__main__":
    unittest.main()
