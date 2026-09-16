# AI Guidelines

## Purpose

This document defines how AI coding assistants should work with Personal Blog Starter and websites created from it.

The goal is to make AI-assisted development predictable, safe, and easy to maintain.

These rules apply to any capable AI coding assistant, including ChatGPT, Gemini, Claude, and future tools.

## Source of Truth

The repository is the source of project context.

Before making structural changes, read:

- README.md
- docs/PROJECT.md
- docs/DESIGN-SYSTEM.md
- docs/CONTENT-MODEL.md
- docs/CMS.md
- docs/DEPLOYMENT.md
- docs/SECURITY.md
- docs/AI-GUIDELINES.md
- docs/BACKLOG.md

Do not assume project rules that conflict with these files.

## Core Architecture

The project is divided into three layers:

### System

Reusable infrastructure.

Examples:

- Base layout
- Header
- Footer
- Navigation system
- Responsive behavior
- SEO
- RSS
- Sitemap
- CMS foundation
- Media handling

### Config

Website-specific settings.

Examples:

- Site name
- Description
- Navigation
- Colors
- Typography
- Branding
- Social links

### Content

Website-specific content.

Examples:

- Blog posts
- Books
- Notes
- About page
- Contact page
- Privacy Policy
- Terms of Use

Prefer changing Config and Content before changing System.

## Scope Control

Only modify files required for the current task.

Do not redesign unrelated pages.

Do not rewrite working components without a clear reason.

Do not change unrelated colors, typography, spacing, navigation, or layout.

Do not perform large refactors unless explicitly requested.

## One Task at a Time

Prefer small, reviewable changes.

For example:

Good:

- Change one navigation item.
- Add one content field.
- Improve one page.
- Fix one mobile layout issue.

Avoid:

- Redesigning the entire website while fixing one button.
- Replacing the navigation system when only one label needs changing.
- Rewriting multiple unrelated templates in one task.

## Reuse Existing Components

Before creating a new component, check whether an existing reusable component can be used.

Avoid duplicate implementations of:

- Header
- Footer
- Navigation
- Cover image
- SEO metadata
- Standard page layouts
- Design tokens

## Configuration First

Do not hard-code website-specific information into templates if it belongs in configuration.

Use:

- data/site.yaml
- data/navigation.yaml
- data/design.yaml

when appropriate.

Examples of information that should normally be configurable:

- Website name
- Navigation labels
- URLs
- Colors
- Fonts
- Social links
- Branding

## Content First

Ordinary content changes should happen in Markdown files.

Do not modify templates just to change article, book, About, Contact, Privacy, or Terms content.

## Responsive Rules

The site is mobile-first.

Always consider:

- Mobile
- Tablet
- Desktop

Mobile uses bottom navigation.

Tablet and desktop use top navigation.

Do not break one viewport while modifying another.

## Navigation Rules

Navigation must remain configurable.

Do not assume the navigation will always contain exactly four items.

Default navigation is:

- Home
- Blog
- About
- More

A cloned website may change these labels and destinations.

## Design Rules

Follow docs/DESIGN-SYSTEM.md.

Prefer centralized design tokens.

Do not scatter brand colors or font definitions across components.

## Content Model Rules

Follow docs/CONTENT-MODEL.md.

The default content type is Blog.

A cloned website may adapt Blog into Book, Notes, Journal, Guides, Reviews, or another content type.

When adapting the content type, avoid changing unrelated system architecture.

## CMS Rules

Follow docs/CMS.md.

Markdown remains the source of truth.

Do not put production credentials in CMS configuration.

Do not bind the master starter to a specific production repository.

## Security Rules

Follow docs/SECURITY.md.

Never expose:

- API keys
- OAuth secrets
- Access tokens
- Private keys
- Platform credentials

## Before Editing

Before making changes:

1. Identify the exact task.
2. Identify the smallest set of files that need modification.
3. Check existing project documentation.
4. Reuse existing architecture where possible.
5. Avoid unnecessary dependencies.

## After Editing

After changes:

1. Run Hugo build.
2. Check for build errors.
3. Test the affected page or feature.
4. Check mobile behavior when relevant.
5. Check desktop behavior when relevant.
6. Review git diff.
7. Confirm unrelated files were not changed.

Recommended commands:

hugo

git status

git diff

## Git Discipline

Keep changes small and understandable.

Use clear commit messages.

Do not commit temporary files, secrets, build artifacts, or unrelated changes.

## Master Starter Rule

Personal Blog Starter is the reusable master template.

Do not customize the master starter for one specific website.

Website-specific changes belong in the cloned website repository.

## Important Principle

Make the smallest correct change.

Preserve working systems.

Prefer reuse over rebuilding.

Prefer configuration over hard-coding.

Prefer clear structure over clever complexity.
