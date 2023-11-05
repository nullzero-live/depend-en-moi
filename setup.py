from setuptools import setup, find_packages

setup(
    name='Depend En Moi',
    version='0.0.1',
    author='Nullzero',
    author_email='p4rlx-news@pm.me',
    packages=find_packages(),
    license='LICENSE.txt',
    description='An example Python package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        # Add your package dependencies here
        # 'numpy',
        # 'pandas',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',  # Change as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # Change as appropriate
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)