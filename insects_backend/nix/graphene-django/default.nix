{ pkgs, buildPythonPackage, fetchPypi, django, pytest, graphql-core, aniso8601, graphql-relay, pytest-runner, singledispatch, python-graphene }:

buildPythonPackage rec {
    version = "2.7.1";
    name = "graphene-django-${version}";

    src = fetchPypi {
      pname = "graphene-django";
      inherit version;
      sha256 = "0pg68yzmdbm2z9qx0n0bi8snl0a854x78lbz6nhx9nan5al3fc13";
    };

    buildInputs = [ pytest-runner ];
    propagatedBuildInputs = [ graphql-core graphql-relay aniso8601 singledispatch django python-graphene ];

    # All tests error with
    # InvalidGitRepositoryError: /tmp/nix-build-python2.7-GitPython-1.0.1.drv-0/GitPython-1.0.1
    # Maybe due to being in a chroot?
    doCheck = false;
}
