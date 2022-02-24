from setuptools import setup

setup(
    name="motivedge",
    version="0.1.0",
    license=open("LICENSE","r").read(),
    maintainer="MotivEdge",
    maintainer_email="tech@motivedge.io",
    description="Python SDK to download map via API, MotivEdge",
    long_description=open("README.rst","r").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Environment :: MacOS X",
        "Operating System :: POSIX",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    keywords="maps, costmap, point cloud, robotics, BIM",
    project_urls={
        "Source": "https://github.com/motivedge/python_sdk",
        "Tracker": "https://github.com/motivedge/python_sdk/issues"
    },
    packages=["motivedge"],
    python_requires=">=3.6",
    install_requires=[
        "requests>=2.25.1",
        "PyYAML>=5.4.1",
    ],
)
