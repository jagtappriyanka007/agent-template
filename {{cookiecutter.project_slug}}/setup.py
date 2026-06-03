from setuptools import Extension, setup
from Cython.Build import cythonize

extensions = [
    Extension("app.cython_modules.scoring", ["src/app/cython_modules/scoring.pyx"]),
]

setup(
    ext_modules=cythonize(
        extensions,
        language_level="3",
        compiler_directives={
            "boundscheck": False,
            "wraparound": False,
            "cdivision": True,
        },
    ),
)
