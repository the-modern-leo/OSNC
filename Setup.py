from distutils.core import setup
from setuptools import find_packages

setup(
    name='ONSC',
    version='0.1dev0',
    description='A Framework for Handling Network Devices',
    packages=find_packages(include=['DNS',
                                    'Email',
                                    'Monitoring',
                                    'Network',
                                    'Network',
                                    'SNMP',
                                    'SSH',
                                    'Tacacs',
                                    'Tracker',
                                    'Vendor_Applications'
                                    ],
                           exclude=['Tests']),
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
    author='Themodernleo',
    author_email='themodernleo@protonmail.com',
    project_urls={'Source': 'https://github.com/the-modern-leo/OSNC/tree/packaging-deployment'},
    install_requires=[
        "paramiko >= 2",
        "netmiko",
        "netaddr",
    ],
    python_requires='>=3'
)