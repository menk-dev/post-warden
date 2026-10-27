# PostWarden

PostWarden is a public .NET 10 messaging and transport library under development.
It favors constrained configuration, robustness, and fault tolerance over flexibility.
RabbitMQ is the first planned transport. Additional transports may follow when needed.

**Status:** repository infrastructure only. No messaging API or RabbitMQ integration
is implemented, and the package is not ready for application use.

## Development

Install the .NET SDK selected by [global.json](global.json), then run:

```sh
dotnet restore PostWarden.slnx --locked-mode
dotnet format PostWarden.slnx --verify-no-changes --no-restore
dotnet build PostWarden.slnx -c Release --no-restore
dotnet test --solution PostWarden.slnx -c Release --no-build --ignore-exit-code 8
dotnet pack PostWarden.slnx -c Release --no-build -o artifacts/packages
python3 tools/validate_packages.py artifacts/packages
```

The test project is intentionally empty. Exit code 8 (no tests) is temporarily
accepted; remove that exception when the first behavior tests are added.

See the [development guide](dev/README.md), [design guidance](dev/design.md),
and [release setup](dev/releases.md). Contributions use scoped Conventional Commits.

Code conventions follow [Structly.AI](https://github.com/menk-dev/structly-ai).
Licensed under [MIT](LICENSE).
