{ pkgs, buildPythonPackage, fetchPypi, setuptools_scm }:
buildPythonPackage rec {
    version = "5.2";
    name = "pytest-runner-${version}";

    src = fetchPypi {
      pname = "pytest-runner";
      inherit version;
      sha256 = "0awll1bva5zy8cspsxcpv7pjcrdf5c6pf56nqn4f74vvmlzfgiwn";
    };

    buildInputs = [];
    propagatedBuildInputs = [ setuptools_scm];

    # All tests error with
    # InvalidGitRepositoryError: /tmp/nix-build-python2.7-GitPython-1.0.1.drv-0/GitPython-1.0.1
    # Maybe due to being in a chroot?
    doCheck = false;
}
