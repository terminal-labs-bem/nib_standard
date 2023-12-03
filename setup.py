# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['standardnib', 'standardnib.content']

package_data = \
{'': ['*'], 'standardnib': ['assets/*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'flask>=3.0.0,<4.0.0',
 'lowkit @ git+https://github.com/terminal-labs/low_kit.git@main']

entry_points = \
{'console_scripts': ['standardnib = standardnib.cli:cli']}

setup_kwargs = {
    'name': 'standardnib',
    'version': '0.0.1',
    'description': '',
    'long_description': '',
    'author': 'Michael Verhulst',
    'author_email': 'michael@terminallabs.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.11,<4.0',
}


setup(**setup_kwargs)
