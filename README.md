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
        "ninja_installer/x.y.y@<user>/<channel>"
    )

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
```

Alternatively, you can specify the build requirements in a profile:

```ini
[build_requires]
cmake_installer/a.b.c@conan/stable
ninja_installer/x.y.y@<user>/<channel>
```

