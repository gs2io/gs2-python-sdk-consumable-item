import os

from setuptools import setup

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='gs2-python-sdk-consumable-item',
    version='1.2.0',
    package_dir={'': 'src'},
    packages=[
        "",
        "gs2_consumable_item_client",
        "gs2_consumable_item_client.control",
        "gs2_consumable_item_client.model",
    ],
    install_requires=[
        'gs2-python-sdk-core >= 1.1.10',
    ],
    tests_require=[],
    license='Apache License 2.0',
    description='GS2-ConsumableItem SDK for Python.',
    url='https://gs2.io/',
    author='Game Server Services Co., LTD',
    author_email='admin@gs2.io',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
)