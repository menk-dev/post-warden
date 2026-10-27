# Releases and repository setup

Release Please prepares version and changelog PRs from Conventional Commits.
Merging a release PR creates a version tag and GitHub Release. The same workflow
then rebuilds, tests, validates and publishes NuGet packages with OIDC when enabled.
`version.txt` is the single package-version source; the simple release strategy
updates it automatically. The manifest starts at 0.0.0 for the first 0.1.0 release.
No package is published just by initializing this repository.

## One-time account configuration

After pushing the repository to GitHub:

1. Enable Actions and allow GitHub Actions to create and approve pull requests.
   The release workflow uses `GITHUB_TOKEN` and explicitly dispatches CI for its
   release PR because token-created PRs do not trigger ordinary PR workflows.
2. Protect `main` with required checks `validate (ubuntu-latest)` and
   `validate (windows-latest)`, prohibit force pushes and deletion, and require PRs.
   Preserve scoped Conventional Commit titles when squash merging. Enable squash
   merging, auto-merge, automatic branch deletion, and private vulnerability reporting.
3. Once those required checks are enforced, set `DEPENDABOT_AUTO_MERGE_ENABLED=true`
   as a repository variable to let patch and minor updates merge after checks pass.
   Major dependency updates remain manual.
4. Create the GitHub environment `nuget`. In the NuGet account `menk-dev`, configure
   a trusted publishing policy for owner `menk-dev`, repository `post-warden`,
   workflow `release.yml`, environment `nuget`, and package ID `PostWarden`.
   Confirm package-name availability and ownership before the first publication.
5. When the library is ready for distribution, set repository variable
   `NUGET_PUBLISH_ENABLED=true`. Until then, release preparation works but publishing
   is disabled. No long-lived NuGet API key is required.

These are account settings, not settings applied by the scaffold. NuGet policy
configuration requires an authenticated NuGet account. See
[NuGet trusted publishing](https://learn.microsoft.com/en-us/nuget/nuget-org/trusted-publishing).

## Retry

Rerun a failed publish job, or dispatch `release.yml` from `main` with an existing
`vMAJOR.MINOR.PATCH` tag. The tag must belong to main and match `version.txt` at
that commit. Uploads replace release assets; existing NuGet versions are skipped.
Change package contents only in a new version. Symbol packages are sent alongside
the main package by `dotnet nuget push`.

Publication runs the same checks as CI. It validates the actual package archive,
including metadata, runtime assembly, XML docs, portable symbols and Source Link.
CI uploads package artifacts for inspection without publishing them.
