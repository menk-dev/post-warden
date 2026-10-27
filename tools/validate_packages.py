"""Validate the distribution archives without third-party Python dependencies."""

from pathlib import Path
import sys
import xml.etree.ElementTree as ET
from zipfile import ZipFile


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate(directory):
    version = (Path(__file__).resolve().parents[1] / "version.txt").read_text().strip()
    package = directory / f"PostWarden.{version}.nupkg"
    symbols = directory / f"PostWarden.{version}.snupkg"
    require(set(directory.glob("*.nupkg")) == {package}, "Unexpected or missing packages")
    require(set(directory.glob("*.snupkg")) == {symbols}, "Unexpected or missing symbols")
    with ZipFile(package) as archive:
        names = set(archive.namelist())
        nuspecs = [name for name in names if name.endswith(".nuspec")]
        require(len(nuspecs) == 1, "Expected one package manifest")
        root = ET.fromstring(archive.read(nuspecs[0]))
        namespace = {"n": root.tag.split("}")[0].lstrip("{")}
        metadata = root.find("n:metadata", namespace)

        def value(name):
            return metadata.findtext(f"n:{name}", namespaces=namespace)

        require(value("id") == "PostWarden", "Wrong package ID")
        require(value("version") == version, "Package version mismatch")
        license_node = metadata.find("n:license", namespace)
        require(license_node is not None and license_node.get("type") == "expression"
                and license_node.text == "MIT", "Missing MIT license expression")
        require(value("readme") == "README.md", "Missing package README metadata")
        repository = metadata.find("n:repository", namespace)
        require(repository is not None
                and repository.get("url") == "https://github.com/menk-dev/post-warden"
                and repository.get("commit"), "Missing source repository or commit")
        for name in ("README.md", "LICENSE", "lib/net10.0/PostWarden.dll",
                     "lib/net10.0/PostWarden.xml"):
            require(name in names, f"Missing {name}")
        assemblies = {name for name in names if name.startswith("lib/") and name.endswith(".dll")}
        require(assemblies == {"lib/net10.0/PostWarden.dll"}, "Unexpected target frameworks")
        dependencies = metadata.findall("n:dependencies/n:group/n:dependency", namespace)
        require(not any(node.get("id") in {"StyleCop.Analyzers", "Roslynator.Formatting.Analyzers"}
                        for node in dependencies), "Build analyzers leaked into runtime dependencies")
    with ZipFile(symbols) as archive:
        pdb = archive.read("lib/net10.0/PostWarden.pdb")
        require(pdb.startswith(b"BSJB"), "Symbols must use portable PDB format")
        require(b"raw.githubusercontent.com/menk-dev/post-warden/" in pdb,
                "Missing GitHub Source Link mapping")
    print(f"Validated PostWarden {version}: metadata, contents, symbols, Source Link")


if __name__ == "__main__":
    try:
        validate(Path(sys.argv[1]))
    except (IndexError, OSError, ValueError, KeyError, ET.ParseError) as error:
        sys.exit(f"Package validation failed: {error}")
