# Development

Requires the .NET SDK selected by [global.json](../global.json) and Python 3.
Tests use xUnit v3 with Microsoft Testing Platform.

```sh
dotnet restore PostWarden.slnx --locked-mode
dotnet format PostWarden.slnx --verify-no-changes --no-restore
dotnet build PostWarden.slnx -c Release --no-restore
dotnet test --solution PostWarden.slnx -c Release --no-build --ignore-exit-code 8
dotnet pack PostWarden.slnx -c Release --no-build -o artifacts/packages
python3 tools/validate_packages.py artifacts/packages
```

In Codex, prefix commands with `rtk`. Use `rtk proxy dotnet format` to apply
formatting and `rtk proxy dotnet test` to preserve the test runner behavior.
Remove `--ignore-exit-code 8` from the commands and workflows when adding tests.

Manage dependency versions in `Directory.Packages.props`. After updates, run
`dotnet restore PostWarden.slnx --force-evaluate` and commit the lock files.
CI validates builds and packages on Linux and Windows. Dependabot opens updates
weekly; patch and minor updates auto-merge after required checks pass.

See [releases](releases.md) for versioning and publishing.
