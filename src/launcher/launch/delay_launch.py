from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            # Node(
            #     package="image_transport",
            #     executable="republish",
            #     arguments=["raw"],
            #     # remappings=[("/in", "/image_raw/compressed"), ("/out", "/camera")],
            # ),
            Node(
                package="proxy",
                executable="main",
            ),            
            Node(
                package="pose",
                executable="delayer",
            ),
            Node(
                package="display",
                executable="main",
                # remappings=[("/camera", "/proxy")],
                remappings=[("/camera", "/delay")],
            ),
            Node(
                package="pose",
                executable="main",
                remappings=[("/camera", "/proxy")],
            ),
        ]
    )