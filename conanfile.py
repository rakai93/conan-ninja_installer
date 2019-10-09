import os
from conans import ConanFile
from conans.client import tools


class NinjaConan(ConanFile):
    name = "ninja"
    version = "1.8.2"
    license = "TDB"
    url = "TBD"
    settings = "os_build", "arch_build"
    build_policy = "missing"
    description = "Ninja installer. Useful as a build_requires."

    @property
    def ninja_download_url(self):
        if self.settings.os_build == "Windows":
            suffix = "win"
        else:
            suffix = "linux"
        return f"https://github.com/ninja-build/ninja/releases/download/v{self.version}/ninja-{suffix}.zip"

    @property
    def ninja_folder(self):
        return "ninja"

    def build(self):
        self.output.info(f"Downloading Ninja from {self.ninja_download_url}")
        tools.get(self.ninja_download_url, destination="bin")
        if self.settings.os_build != "Windows":
            os.chmod('bin/ninja', 0o775)

    def package(self):
        self.copy("bin/*", dst="bin", keep_path=False)

    def package_info(self):
        self.env_info.path.append(os.path.join(self.package_folder, "bin"))
