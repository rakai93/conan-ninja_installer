Ninja installer for conan
=========================

This conan recipe provides the [Ninja build tool](https://ninja-build.org/),
which can be used as an alternative to GNU Makefiles to build your C++ project.

Creating a local package
------------------------

Checkout this repository and run `conan create ./conan-ninja_installer/ <user>/<channel>`
to create a conan package locally.

Use as build requirement
------------------------

Inside your `conanfile.py`, you can combine CMake and Ninja as build requirements:

```python
class MyCppConan(ConanFile):

    build_requires = (
        "cmake_installer/a.b.c@conan/stable",
        "ninja_installer/x.y.z@<user>/<channel>"
    )

    def build(self):
        cmake = CMake(self, generator="Ninja")
        cmake.configure()
        cmake.build()
```

Alternatively, you can specify the build requirements in a profile:

```ini
[build_requires]
cmake_installer/a.b.c@conan/stable
ninja_installer/x.y.y@<user>/<channel>
```

Building Ninja from source
--------------------------

On the Ninja github project, some pre-compiled binaries are available
for ``Windows``, ``Linux`` and ``Mac OS`` on ``x86_64`` platform.

If you are using any other operating system or platform, Ninja is built from
source. To do so, an additional build requirement is needed: ``python``.
Since not all distributions come with Python 3 pre-installed and since we
do not want to force users to install anything, the Python interpreter
is also provided by another conan recipe.

Bananamonster conan recipes are hosted on an internal system, thus you
have to manually checkout [the python conan recipe](https://github.com/rakai93/conan-python)
and follow the description on the README page to create a local package.
Then, replace the conan package reference in ``build_requires`` in this
``conanfile.py`` with your local user and channel. Afterwards, the Ninja
conan package can be created as described above.
