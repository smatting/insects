{ pkgs, buildPythonPackage, gitdb2, fetchPypi, graphql-core, promise, six, rx }:
buildPythonPackage rec {
    version = "2.0.1";
    name = "graphql-relay-${version}";

    src = fetchPypi {
      pname = "graphql-relay";
      inherit version;
      sha256 = "1fzsi99bi351kz9hrx3b8rdcxb11w2n9x9qmnah3hfhj0i9nn2w7";
    };

    buildInputs = [];
    propagatedBuildInputs = [graphql-core promise six rx];

    # All tests error with
    # InvalidGitRepositoryError: /tmp/nix-build-python2.7-GitPython-1.0.1.drv-0/GitPython-1.0.1
    # Maybe due to being in a chroot?
    doCheck = false;
}
