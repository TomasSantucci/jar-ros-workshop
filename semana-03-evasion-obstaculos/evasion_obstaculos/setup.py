from setuptools import find_packages, setup

package_name = 'evasion_obstaculos'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='AIR Club UdeSA',
    maintainer_email='rafadiaz71@gmail.com',
    description='Semana 03 del Challenge JAR: maquina de estados para avanzar, detectar un choque inminente con el lidar y girar un angulo fijo.',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'evasor = evasion_obstaculos.evasor:main',
        ],
    },
)