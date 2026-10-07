import mujoco
import mujoco.viewer

xml = """
<mujoco>
    <worldbody>

        <light pos="0 0 5"/>

        <camera
            name="camera"
            pos="4 -4 3"
            xyaxes="1 1 0 -0.4 0.4 1"
        />

        <geom
            type="plane"
            size="5 5 0.1"
            rgba="0.8 0.8 0.8 1"
        />

        <body pos="0 0 0.5">
            <geom
                type="box"
                size="0.5 0.5 0.5"
                rgba="0.8 0.1 0.1 1"
            />
        </body>

    </worldbody>
</mujoco>
"""

model = mujoco.MjModel.from_xml_string(xml)
data = mujoco.MjData(model)

mujoco.viewer.launch(model, data)