{ pkgs, buildPythonPackage, fetchPypi, six }:
buildPythonPackage rec {
    version = "2.2.1";
    name = "promise-${version}";

    src = fetchPypi {
      pname = "promise";
      inherit version;
      sha256 = "0p35hm648gkxlmqki9js6xni6c8vmh1ysnnnkiyd8kyx7rn5z3rl";
    };

    buildInputs = [six];
    propagatedBuildInputs = [];

    # All tests error with
    # InvalidGitRepositoryError: /tmp/nix-build-python2.7-GitPython-1.0.1.drv-0/GitPython-1.0.1
    # Maybe due to being in a chroot?
    doCheck = false;
}
