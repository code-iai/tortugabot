from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'tortugabot_bringup'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*')),
        (os.path.join('share', package_name, 'maps'), glob('maps/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Arthur Niedzwiecki',
    maintainer_email='aniedz@cs.uni-bremen.de',
    description='Bringup scripts for the tortugabots',
    license='GPLv3+',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
