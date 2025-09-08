from setuptools import find_packages, setup

package_name = 'my_chatter'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ee106a-tad',
    maintainer_email='andrewchoy@berkeley.edu',
    description='my_chatter implemetnation',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'talker = my_chatter.publisher:main',
                # src/my_chatter/include/my_chatter/publisher.py
                'listener = my_chatter.subscriber:main',                
        ],
    },
)
