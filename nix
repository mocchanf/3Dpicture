{ pkgs }: {
  deps = [
    pkgs.python311
    pkgs.python311Packages.pip
    pkgs.python311Packages.flask
    pkgs.python311Packages.python-dotenv
    pkgs.python311Packages.openai
    pkgs.wget
  ];
}
