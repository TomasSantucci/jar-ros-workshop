from glob import glob

from setuptools import find_packages, setup

package_name = 'launch_rviz'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', glob('launch/*.launch.py')),
        ('share/' + package_name + '/rviz', glob('rviz/*.rviz')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='AIR Club UdeSA',
    maintainer_email='rafadiaz71@gmail.com',
    description='Semana 05 del Challenge JAR: launch files y configuraciones de RViz para levantar de una sola vez los workshops anteriores.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # Vacío a propósito: este paquete no expone ejecutables propios,
            # solo archivos de launch y de RViz que lanzan nodos de otros
            # paquetes.
        ],
    },
)
