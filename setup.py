from setuptools import setup, find_packages

setup(
    name='foobar_second',
    version='0.1.0',
    description='A example Python package',
    author='Mariusz Bielecki',
    author_email='someemail@gmail.com',
    namespace_packages=["foobar"],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "foobar-first @ git+https://github.com/MariuszBielecki288728/foobar-first.git@main#egg=foobar-first"
    ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
