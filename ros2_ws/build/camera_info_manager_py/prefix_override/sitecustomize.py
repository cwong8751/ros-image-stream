import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/root/ros-image-stream/ros2_ws/install/camera_info_manager_py'
