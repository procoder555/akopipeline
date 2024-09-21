from setuptools import setup, find_packages

setup(
    name='pipeline',
    version='1.0.0',
    url='https://github.com/mypackage.git',
    author='',
    author_email='author@gmail.com',
    description='data pipeline',
    packages = ['pipeline'],
    entry_points = {
        'console_scripts': [
            'pipeline = pipeline.main'
        ] 
        },
    install_requires=[
        'arrow==1.3.0',
        'py3cli==1.0.1',
        'click==8.1.7',
        'cloudpickle==3.0.0',
        'dask==2024.9.0',
        'dask-expr==1.1.14',
        'fsspec==2024.9.0',
        'iniconfig==2.0.0',
        'Jinja2==3.1.4',
        'jinja2-time==0.2.0',
        'locket==1.0.0',
        'make==0.1.6.post2',
        'MarkupSafe==2.1.5',
        'numpy==2.1.1',
        'packaging==24.1',
        'pandas==2.2.2',
        'partd==1.4.2',
        'pluggy==1.5.0',
        'pyarrow==17.0.0',
        'pytest==8.3.3',
        'python-dateutil==2.9.0.post0',
        'pytz==2024.2',
        'PyYAML==6.0.2',
        'six==1.16.0',
        'style==1.1.0',
        'toolz==0.12.1',
        'types-python-dateutil==2.9.0.20240906',
        'tzdata==2024.1',
        'update==0.0.1',
    ],
)