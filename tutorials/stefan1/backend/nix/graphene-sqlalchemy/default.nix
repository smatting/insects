{ pkgs, buildPythonPackage, gitdb2, fetchPypi, python-graphene, promise, six, singledispatch, sqlalchemy }:
buildPythonPackage rec {
    version = "2.2.2";
    name = "graphene-sqlalchemy-${version}";

    src = fetchPypi {
      pname = "graphene-sqlalchemy";
      inherit version;
      sha256 = "0xqlkilxljy97yd9r4wj5fi0pn7d09hjgn6430mz15ls2hqs38zx";
    };

    buildInputs = [];
    propagatedBuildInputs = [python-graphene promise six singledispatch sqlalchemy];

    # All tests error with
    # InvalidGitRepositoryError: /tmp/nix-build-python2.7-GitPython-1.0.1.drv-0/GitPython-1.0.1
    # Maybe due to being in a chroot?
    doCheck = false;
}
