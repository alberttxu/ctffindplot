import setuptools

setuptools.setup(
    name="ctffindplot",
    version="0.0.5",
    description="Sequentially plot ctffind results from aligned micrographs",
    url="https://github.com/alberttxu/ctffindplot",
    author="Albert Xu",
    author_email="albert.t.xu@gmail.com",
    license="MIT",
    packages=setuptools.find_packages(),
    install_requires=["PyGnuplot", "dash", "pandas"],
    entry_points={"console_scripts": ["ctffindplot = ctffindplot.__main__:main"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
