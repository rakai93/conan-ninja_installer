import os
from conans import ConanFile
from conans.client import tools


class NinjaConan(ConanFile):
    name = "ninja"
    version = "1.10.0"
    license = "TDB"
    url = "https://ninja-build.org/"
    settings = "os_build", "arch_build"
    build_policy = "missing"
    description = "Ninja build tool. Useful as a build_requires."

    @property
    def binary_available(self):
        return (
            self.settings.arch_build == "x86_64"
            and self.settings.os_build in ("Windows", "Linux", "Macos")
        )

    def build_requirements(self):
        if not self.binary_available:
            self.build_requires("python/3.7.4@bananamonster/misc")

    @property
    def binary_url(self):
        if self.settings.os_build == "Windows":
            suffix = "win"
        else:
            suffix = "linux"
        return f"https://github.com/ninja-build/ninja/releases/download/v{self.version}/ninja-{suffix}.zip"

    @property
    def source_url(self):
        return f"https://github.com/ninja-build/ninja/archive/v{self.version}.zip"

    def source(self):
        if self.binary_available:
            self.output.info(f"Downloading Ninja from {self.binary_url}")
            tools.get(self.binary_url, destination="bin")
            if self.settings.os_build != "Windows":
                os.chmod('bin/ninja', 0o775)
        else:
            self.output.info(f"Downloading Ninja sources from {self.source_url}")
            tools.get(self.source_url)
            os.rename(f"ninja-{self.version}", "ninja")

    def build(self):
        if self.binary_available:
            return

        python_bin = os.path.join(self.deps_cpp_info["python"].bin_paths[0], "python3.7")
        with tools.chdir("ninja"):
            self.run("chmod +x src/*.sh")
            self.run(f"{python_bin} ./configure.py --bootstrap")

        os.mkdir("bin")
        os.rename("ninja/ninja", "bin/ninja")

    def package(self):
        self.copy("bin/*", dst="bin", keep_path=False)

    def package_info(self):
        self.env_info.path.append(os.path.join(self.package_folder, "bin"))
        self.env_info.CONAN_CMAKE_GENERATOR = "Ninja"
