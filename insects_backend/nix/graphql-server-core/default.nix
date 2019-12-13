{ pkgs, buildPythonPackage, gitdb2, fetchPypi, promise, graphql-core, six, rx, flask }:
buildPythonPackage rec {
    version = "1.1.3";
    name = "graphql-server-core-${version}";

    src = fetchPypi {
      pname = "graphql-server-core";
      inherit version;
      sha256 = "10rr2dcr6d8n9fc4y5j1y5mjnbx1qdi9b0a9mhwdj7fr3j0hz0gs";
    };

    buildInputs = [];
    propagatedBuildInputs = [flask promise graphql-core six rx];

    # All tests error with
    # InvalidGitRepositoryError: /tmp/nix-build-python2.7-GitPython-1.0.1.drv-0/GitPython-1.0.1
    # Maybe due to being in a chroot?
    doCheck = false;
}
