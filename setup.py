#from setuptools import setup, find_packages
import pkg_resources
# import find_packages,setuptools
from setuptools import find_packages, setup

setup(
    name='projectname',
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
                        'run-api=projectname.run:run',
                        'run-cli=projectname.run:cli',
                        'run-manage=projectname.run:manage'

                    ],
                }
)
