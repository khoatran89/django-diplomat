
from setuptools import find_packages, setup

setup(
	name='diplomat',
	version=__import__('diplomat').__version__,
	description='Language and country models for Django derived from the pycountry module.',
	author='Justin Locsei',
	author_email='justin.locsei@oberlin.edu',
	url='http://github.com/oberlin/diplomat/',
	download_url='https://github.com/oberlin/diplomat/zipball/master',
	long_description=open('README.md', 'r').read(),
	packages=find_packages(),
	install_requires=[
		'django-autoslug',
		'pycountry'
	],
	include_package_data=True,
	license="BSD",
	platforms='any',
	zip_safe=False,
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Environment :: Web Environment',
		'Intended Audience :: Developers',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Framework :: Django'
	]
)
