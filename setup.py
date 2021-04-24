from setuptools import find_packages, setup

setup(
    name="sample_qr",
    version="1.0.0",
    description="create sample qr codes.",
    license="MIT License",
    author="Yuto Watanabe",
    install_requires=[
        "qrcode",
        "rstr",
        "Pillow"
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'sample-qr = sample_qr.main:main',
        ],
    },
)
