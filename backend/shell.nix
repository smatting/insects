{ pkgs ? (import <nixpkgs> {}) }:
with pkgs;
(python36.withPackages(ps: with ps; [
  flask
  flask-socketio
  ipython
  ipdb
])).env
