# Personal Blog Starter

A reusable Hugo + Decap CMS starter for simple personal and content websites.

## Purpose

This repository is the master starter template.

Do not customize this repository for a specific website.

Create a new website from this starter, then change configuration, content, branding, and content type as needed.

## Core Stack

- Hugo
- GitHub
- Cloudflare
- Decap CMS
- Markdown
- HTML
- CSS
- JavaScript

## Starter Structure

Default navigation:

- Home
- Blog
- About
- More
  - Contact
  - Privacy
  - Terms

Desktop and tablet use top navigation.

Mobile uses configurable bottom navigation.

## Configuration

Website identity:

data/site.yaml

Navigation:

data/navigation.yaml

Design tokens:

data/design.yaml

## Content

Default content section:

content/blog/

Standard pages:

- content/about.md
- content/contact.md
- content/privacy.md
- content/terms.md

## CMS

Decap CMS is available at:

/admin/

Configuration:

static/admin/config.yml

The starter uses a test backend by default.

A cloned production site must configure its own GitHub repository and authentication.

## Documentation

Read the files in /docs before making structural changes.

## Development

Run:

hugo server

Build:

hugo

## Important Rule

Prefer changing Config and Content.

Avoid changing System files unless the change should apply to every website created from this starter.
