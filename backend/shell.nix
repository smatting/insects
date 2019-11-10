{ pkgs ? (import <nixpkgs> {}) }:
with pkgs;
(python37.withPackages(ps: with ps; [
  flask
  flask-socketio
  ipython
  ipdb
])).env
