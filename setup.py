#from setuptools import setup, find_packages
import pkg_resources
# import find_packages,setuptools
from setuptools import find_packages, setup

setup(
    name='proshop',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
    entry_points={
                    'console_scripts':
                    [
                        'run-api=proshop.run:run',
                        'run-cli=proshop.run:cli',
                        'run-manage=proshop.run:manage'

                    ],
                }
)
