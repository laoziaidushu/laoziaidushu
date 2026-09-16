# Security

## Purpose

This document defines basic security rules for Personal Blog Starter and websites created from it.

The starter is primarily a static Hugo website, which keeps the attack surface relatively small.

However, connected services such as GitHub, Cloudflare, and Decap CMS still require proper security practices.

## Secrets

Never commit secrets directly into the Git repository.

Examples of secrets include:

- API keys
- OAuth client secrets
- Access tokens
- Private keys
- Service credentials
- Cloudflare tokens
- GitHub tokens

Use environment variables or platform secret management instead.

## GitHub

Use appropriate repository permissions.

Recommended practices:

- Enable two-factor authentication
- Use least-privilege access
- Review collaborators regularly
- Avoid sharing personal access tokens
- Protect important production branches when needed

## Cloudflare

Do not store Cloudflare credentials in source files.

Use Cloudflare environment variables, secrets, or platform configuration for sensitive values.

Production-specific Cloudflare identifiers should remain outside the reusable starter whenever possible.

## Decap CMS

The starter uses a test backend only for development and template testing.

A production website must use its own authenticated backend.

Production CMS access should only be available to authorized editors.

Never place OAuth secrets directly in:

- static/admin/config.yml
- Markdown files
- Hugo templates
- JavaScript delivered to browsers

## Public Files

Everything inside the generated public website should be considered publicly accessible.

Do not place private documents or credentials inside:

- static/
- public/
- content/
- data/

unless the information is intentionally public.

## User Input

The default starter does not include public user accounts, comments, forms, or database-backed user submissions.

If these features are added later, their security requirements must be reviewed separately.

## Dependencies

Keep Hugo and other project dependencies reasonably up to date.

Before major upgrades:

1. Review release notes.
2. Test locally.
3. Build the site.
4. Check important pages.
5. Deploy only after testing.

## Content Safety

Only trusted editors should have permission to publish content through the CMS.

Review embedded HTML, scripts, and third-party content before publishing.

## Backup and Recovery

GitHub provides version history for project files and Markdown content.

Important production configuration stored outside Git should also have an appropriate recovery plan.

## Cloned Websites

Each cloned website is responsible for its own:

- Authentication
- Secrets
- Repository access
- Cloudflare configuration
- CMS permissions
- Domain security

Do not reuse sensitive credentials across unrelated websites.

## Important Rule

Personal Blog Starter should contain reusable structure and safe defaults.

It should never contain credentials or private production information belonging to a specific website.
