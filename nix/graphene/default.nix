{ pkgs, buildPythonPackage, fetchPypi, six, graphql-core, graphql-relay, aniso8601 }:
buildPythonPackage rec {
    version = "2.1.8";
    name = "graphene-${version}";

    src = fetchPypi {
      pname = "graphene";
      inherit version;
      sha256 = "1y8jgi4wzln0zl6rj3qvrrhp2x40bc70lxp00mw7pz2wy576vgic";
    };

    buildInputs = [six ];
    propagatedBuildInputs = [graphql-core graphql-relay aniso8601];

    # All tests error with
    # InvalidGitRepositoryError: /tmp/nix-build-python2.7-GitPython-1.0.1.drv-0/GitPython-1.0.1
    # Maybe due to being in a chroot?
    doCheck = false;
}
