# Development

The solution contains `src/PostWarden` and `tests/PostWarden.Tests`. Do not introduce
speculative transport projects or a public API until their behavior is designed.
Tests use xUnit v3 with Microsoft Testing Platform, matching Structly.AI.

Run the commands in the root README before committing. In Codex, prefix shell
commands with `rtk`. Use `rtk proxy dotnet format PostWarden.slnx --no-restore` to
apply formatting. Use `rtk proxy dotnet test` for this Microsoft Testing Platform
solution because RTK's test wrapper does not preserve its runner behavior.
Python 3 is required for package validation.

Dependencies are centrally versioned in `Directory.Packages.props`. After changing
them, run `dotnet restore PostWarden.slnx --force-evaluate` and commit the updated
lock files. CI restores in locked mode, checks formatting, builds with warnings as
errors, runs tests, packs, and validates package metadata on Linux and Windows.
Dependency and action updates are opened weekly by Dependabot.

The initial test project has no tests. The command's `--ignore-exit-code 8` exception
must be removed from documentation and workflows when behavior tests are introduced.
Do not add a meaningless passing test just to make the scaffold appear covered.

`version.txt` is the single package-version source. Release Please updates it and
the changelog through a release PR. See [releases](releases.md) for initial setup.
