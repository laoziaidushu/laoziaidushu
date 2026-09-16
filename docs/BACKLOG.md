# Backlog

## Purpose

This document tracks planned improvements, optional features, future ideas, and unresolved tasks for Personal Blog Starter.

Items listed here are not automatically approved for implementation.

Before implementing a backlog item, confirm that it is still needed and fits the current project scope.

## Current Priority

### Template Foundation

- Verify all starter documentation
- Verify Hugo build
- Verify responsive navigation
- Verify Blog list and single pages
- Verify standard pages
- Verify SEO metadata
- Verify RSS
- Verify sitemap
- Verify robots.txt
- Verify 404 page
- Verify Decap CMS test backend
- Verify media uploads structure

### Template Reuse

- Test the starter with a real cloned website
- Confirm site identity can be changed through configuration
- Confirm navigation can be changed without editing components
- Confirm design tokens can be changed without rewriting CSS
- Confirm Blog can be adapted into another content type
- Confirm CMS collections can be adapted for cloned websites

## Planned Improvements

Potential future improvements:

- Active navigation state
- Improved mobile More menu behavior
- Keyboard accessibility improvements
- Better focus states
- Improved typography scale
- Optional dark mode
- Optional logo support
- Social sharing image fallback
- Default Open Graph image
- Structured data
- Breadcrumb component
- Pagination
- Tag pages
- Search
- Reading time
- Previous and next content navigation
- Table of contents
- Related content
- Image captions
- Additional reusable content components

## CMS

Potential CMS improvements:

- Better editorial workflow
- More reusable field definitions
- Optional author fields
- Optional featured content
- Optional SEO override fields
- Optional social image fields
- Better media organization
- Production GitHub backend setup guide
- Cloudflare authentication guide

## Deployment

Potential deployment improvements:

- Cloudflare Workers deployment example
- Preview deployment workflow
- Production deployment checklist automation
- Environment variable documentation
- Domain migration notes
- Redirect configuration

## Documentation

Potential documentation improvements:

- Clone checklist
- New website setup checklist
- Troubleshooting guide
- Content author guide
- CMS editor guide
- Release checklist

## Real-World Clone Test

The first real-world clone should validate the template architecture.

Initial planned test:

Personal Blog Starter
→ Lao Zi Ai Du Shu

Expected adaptation:

- Blog becomes Book
- Site language becomes Chinese
- URL slugs remain English
- Brand name becomes 老子爱读书
- English brand name becomes Lao Zi Ai Du Shu
- Website-specific design and content are added
- Core reusable system remains unchanged

Any problems discovered during this clone should be evaluated for improvement in the master starter.

## Backlog Rules

- Do not implement backlog items automatically.
- Keep the starter simple.
- Avoid adding features that most cloned websites will not need.
- Prefer optional components over permanent complexity.
- Move completed items out of the active backlog when appropriate.
- Document important architectural decisions elsewhere when they become permanent.

## Guiding Principle

The starter should remain small, reusable, understandable, and easy to clone.

Features should be added only when they provide clear reusable value.
