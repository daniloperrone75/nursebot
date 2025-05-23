from setuptools import find_packages, setup

package_name = 'nursebot'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/robot.launch.py']),
        ('share/' + package_name + '/rviz', ['rviz/nursebot.rviz']),
        ('share/' + package_name + '/urdf', ['urdf/nursebot.urdf']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Danilo Perrone',
    maintainer_email='danilo@fei.edu.br',
    description='Robô autônomo para apoio hospitalar com interações multimodais.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)

