{ pkgs, buildPythonPackage, fetchPypi }:
buildPythonPackage rec {
    version = "7.0.0";
    name = "aniso8601-${version}";

    src = fetchPypi {
      pname = "aniso8601";
      inherit version;
      sha256 = "07jgf55yq2j2q76gaj3hakflnxg8yfkarzvrmq33i1dp6xk2ngai";
    };

    buildInputs = [];
    propagatedBuildInputs = [];

    # All tests error with
    # InvalidGitRepositoryError: /tmp/nix-build-python2.7-GitPython-1.0.1.drv-0/GitPython-1.0.1
    # Maybe due to being in a chroot?
    doCheck = false;
}
