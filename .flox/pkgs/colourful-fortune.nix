{
  catalogs,
  fortune,
  python3Packages,
}:

python3Packages.buildPythonApplication {
  pname = "colourful-fortune";
  src = ../..;
  version = "0.1.0";
  format = "setuptools";
  buildInputs = [ fortune ];
  postPatch = ''
    substituteInPlace colourful_fortune.py \
      --replace-fail '@fortune@' '${fortune}'
  '';
  dependencies = [
    catalogs.lol-cat-py.python3Packages.lol-cat-py
    python3Packages.setuptools
  ];
}
