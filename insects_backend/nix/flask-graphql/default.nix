{ pkgs, buildPythonPackage, fetchPypi, graphql-server-core }:
buildPythonPackage rec {
    version = "2.0.1";
    name = "Flask-GraphQL-${version}";

    src = fetchPypi {
      pname = "Flask-GraphQL";
      inherit version;
      sha256 = "0p93qm5rcdjpwkhbdsd5rl5aj6f966yqp8q38pbnqhyz8k07hmc2";
    };

    buildInputs = [];
    propagatedBuildInputs = [graphql-server-core];

    # All tests error with
    # InvalidGitRepositoryError: /tmp/nix-build-python2.7-GitPython-1.0.1.drv-0/GitPython-1.0.1
    # Maybe due to being in a chroot?
    doCheck = false;
}
