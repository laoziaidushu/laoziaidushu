# CMS

## Purpose

This document explains how Decap CMS is used in Personal Blog Starter.

Decap CMS provides a browser-based editing interface for Markdown content stored in the Git repository.

The Git repository remains the source of truth.

## Admin URL

The CMS is available at:

/admin/

The CMS files are stored in:

- static/admin/index.html
- static/admin/config.yml

## Default Backend

The starter uses the Decap CMS test backend by default.

This allows the CMS interface to be tested without connecting the starter repository to a production authentication setup.

The test backend should not be used for a production website.

## Production Backend

Each cloned website must configure its own production backend.

Production configuration normally includes:

- GitHub repository
- Authentication
- OAuth or authentication proxy
- Branch
- CMS permissions

Do not hard-code a specific production repository into Personal Blog Starter.

## Media

CMS uploads are stored in:

static/uploads/

Public image paths use:

/uploads/

Example:

/uploads/example.webp

## Default Blog Collection

The starter includes a Blog collection.

Default content folder:

content/blog/

Typical fields include:

- Title
- Description
- Date
- Draft
- Slug
- Cover
- Tags
- Body

## Standard Pages

The CMS also manages:

- About
- Contact
- Privacy Policy
- Terms of Use

These files are stored directly in the content directory.

## Adapting the CMS

When a cloned website replaces Blog with another content type, update the CMS collection.

Example:

Blog becomes Book.

Change:

- Collection name
- Collection label
- Content folder
- Relevant fields if required

Do not rebuild the entire CMS configuration unless necessary.

## Editing Workflow

Recommended workflow:

1. Open /admin/
2. Create or edit content
3. Save content
4. CMS writes Markdown changes to Git
5. Git triggers deployment
6. The updated website is published

## Important Rules

- Keep content in Markdown.
- Keep uploaded media inside the configured media directory.
- Use English slugs.
- Avoid changing CMS system files for ordinary content editing.
- Production authentication belongs to the cloned website, not the master starter.
