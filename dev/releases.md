# Releases

Release Please updates `version.txt` and the changelog through a release PR.
Merging it creates a tag and GitHub Release.

NuGet publishing uses trusted publishing with these settings:

- Account: `menk-dev`; package: `PostWarden`.
- Repository: `menk-dev/post-warden`; workflow: `release.yml`; environment: `nuget`.
- Set repository variable `NUGET_PUBLISH_ENABLED=true` to enable publishing.

The publishing job validates the packages, attaches them to the release, and
pushes packages and symbols to nuget.org.

Retry a failed job or dispatch `release.yml` from `main` with its existing
`vMAJOR.MINOR.PATCH` tag. The tag must belong to main and match `version.txt`.
Publish changed package contents under a new version.
