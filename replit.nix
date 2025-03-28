{ pkgs }: {
  deps = [
    pkgs.python311
    pkgs.python311Packages.pip
    pkgs.python311Packages.flask
    pkgs.python311Packages.python-dotenv
    pkgs.python311Packages.setuptools
    pkgs.python311Packages.wget
  ];

  pip = [
    "openai==0.27.10"
  ];
}
