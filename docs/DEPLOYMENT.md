# Deployment

## Purpose

This document defines the default deployment workflow for websites created from Personal Blog Starter.

The recommended stack is:

- GitHub
- Cloudflare
- Hugo

## Source Repository

Each website should have its own GitHub repository.

The master starter repository should remain reusable and should not contain production-specific settings for a cloned website.

## Recommended Workflow

1. Create a new repository from Personal Blog Starter.
2. Update site configuration.
3. Update content and branding.
4. Push changes to GitHub.
5. Connect the repository to Cloudflare.
6. Build the Hugo website.
7. Publish the generated static site.
8. Connect the custom domain.
9. Test the production website.

## Build Command

Use:

hugo

## Output Directory

Hugo generates the production website in:

public/

## Local Development

Run:

hugo server

Use the local development server to preview changes before deployment.

## Environment Separation

The project should distinguish between:

- Local development
- Preview deployment
- Production deployment

Do not place secrets directly in the Git repository.

## Domain

Each cloned website should configure its own domain.

The domain must not be hard-coded into reusable layout files.

Update the appropriate site configuration and deployment settings for the cloned website.

## Cloudflare

Cloudflare is the preferred hosting and delivery platform.

The production setup may use Cloudflare Workers or another supported Cloudflare deployment workflow depending on the project requirements.

The starter should remain deployment-friendly and should not depend on website-specific Cloudflare identifiers.

## Git-Based Deployment

Recommended deployment flow:

GitHub repository
→ Cloudflare build
→ Hugo build
→ public/
→ Production website

## CMS Deployment Considerations

Decap CMS production authentication must be configured separately for each cloned website.

The master starter uses a test backend and should not contain production OAuth credentials.

## Pre-Launch Checklist

Before launching a cloned website, confirm:

- Site name is correct
- Domain is correct
- Language is correct
- Navigation is correct
- Branding is updated
- Favicon is updated
- About page is updated
- Contact page is updated
- Privacy Policy is updated
- Terms of Use is updated
- CMS production backend is configured
- Production authentication works
- Sitemap works
- robots.txt works
- RSS works
- 404 page works
- Mobile navigation works
- Desktop navigation works
- Images load correctly
- SEO metadata is correct
- HTTPS works

## Important Rule

Deployment settings that belong to one specific website should stay in that website's repository or deployment platform configuration.

Do not add website-specific deployment credentials or identifiers to Personal Blog Starter.
