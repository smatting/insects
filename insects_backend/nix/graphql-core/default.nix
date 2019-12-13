{ pkgs, buildPythonPackage, gitdb2, fetchPypi, rx, six, promise }:
buildPythonPackage rec {
    version = "2.2.1";
    name = "graphql-core${version}";

    src = fetchPypi {
      pname = "graphql-core";
      inherit version;
      sha256 = "1r705zv7fld3bkk9nynl3f2642r1b6l8ppp8l8vlbni0sxrc8r6s";
    };

    buildInputs = [rx six promise];
    propagatedBuildInputs = [];

    # All tests error with
    # InvalidGitRepositoryError: /tmp/nix-build-python2.7-GitPython-1.0.1.drv-0/GitPython-1.0.1
    # Maybe due to being in a chroot?
    doCheck = false;
}
