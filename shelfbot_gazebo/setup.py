from setuptools import setup
import os
from glob import glob

package_name = 'shelfbot_gazebo'


def generate_model_data_files():
    data_files = []

    for root, dirs, files in os.walk('models'):
        if files:
            install_dir = os.path.join(
                'share',
                package_name,
                root
            )
            file_list = [os.path.join(root, f) for f in files]
            data_files.append((install_dir, file_list))

    return data_files


setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],

    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),
        (
            'share/' + package_name,
            ['package.xml', 'README.md']
        ),
        (
            os.path.join('share', package_name, 'launch'),
            glob('launch/*.py')
        ),
        (
            os.path.join('share', package_name, 'worlds'),
            glob('worlds/*.world')
        ),
        (
            os.path.join('share', package_name, 'third_party/aws_small_warehouse'),
            glob('third_party/aws_small_warehouse/*')
        ),
    ] + generate_model_data_files(),

    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Kodo Robotics',
    maintainer_email='kodorobotics@gmail.com',
    description='Gazebo simulation environment for Kodo Shelfbot',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [],
    },
)