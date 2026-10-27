# PostWarden development guidance

## Scope and design

PostWarden targets .NET 10 and is an opinionated messaging library. RabbitMQ is the
first planned transport. Prefer constrained, validated configuration and explicit
failure behavior over flexibility.

## Coding style and naming

Follow the root EditorConfig.
Use lowercase built-in aliases in declarations (`string`, `int`, `bool`) and framework
type names for static members (`String.IsNullOrEmpty(value)`).
Use readonly-first fields with underscore-prefixed camelCase names (`readonly int _count;`).
Prefer primary constructors where dependencies remain clear. Omit explicit `private`
and `internal` modifiers when C# implies the same accessibility.

Organize source and tests by feature. Give each public top-level type its own file,
including enums and attributes. Use `OfT` for generic filenames and name partial
files after the type and responsibility. Put substantial internal types in separate
files and shared test fixtures in `Support/`. Avoid catch-all helper folders.
Preserve public namespaces when moving files.

Add abstractions for meaningful duplication or multiple existing implementations,
not hypothetical transports. Extract methods when their names explain a rule or
hide details the caller need not follow. Keep simple construction and delegation
at the call site. Records with more than two unrelated properties should declare
properties explicitly, using required, get, set, or init as appropriate.

Write documentation in plain, precise technical language. Explain behavior,
limitations, cancellation, resource ownership, and disposal accurately.

## Verification and commits

Run the checks in [dev/README.md](dev/README.md). Commit completed work using
Conventional Commits with a scope and explanatory body. Publish changes through
feature branches and pull requests; never bypass branch protections or force-push main.
Only push, publish packages, or merge when authorized.

Always prefix shell commands with `rtk`. Use `rtk proxy` only when raw output or
direct behavior is necessary, including applying `dotnet format`. If RTK reports
zero tests unexpectedly, verify with the Microsoft Testing Platform runner directly.
Request escalation when sandbox restrictions block required operations.
