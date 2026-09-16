# Content Model

## Purpose

This document defines the reusable content structure for Personal Blog Starter.

The default primary content type is Blog.

A cloned website may adapt Blog into another content type such as Book, Notes, Journal, Guides, or Reviews.

The reusable website system should remain unchanged whenever possible.

## Default Content Structure

The default content structure is:

- content/blog/
- content/blog/_index.md
- content/about.md
- content/contact.md
- content/privacy.md
- content/terms.md

## Blog Section

Default URL:

/blog/

Default content directory:

content/blog/

Default archetype:

archetypes/blog.md

Default layouts:

- layouts/blog/section.html
- layouts/blog/page.html

## Blog Post Fields

Each Blog post supports these fields:

- title
- description
- date
- draft
- slug
- cover
- tags
- body

### Title

Required.

The visible title of the content.

### Description

A short summary used for content lists, SEO descriptions, and social sharing.

### Date

Publication date.

### Draft

Controls whether the content should be published.

### Slug

Optional custom URL slug.

Use lowercase English words separated by hyphens.

Example:

how-i-read-books

### Cover

Optional cover image.

Example:

/uploads/example.webp

### Tags

Optional descriptive metadata.

### Body

The main Markdown content.

## Standard Pages

About:

- File: content/about.md
- URL: /about/

Contact:

- File: content/contact.md
- URL: /contact/

Privacy Policy:

- File: content/privacy.md
- URL: /privacy/

Terms of Use:

- File: content/terms.md
- URL: /terms/

These pages use the shared default page layout.

## URL Rules

Use English URL slugs by default.

Recommended examples:

- /blog/atomic-habits/
- /about/
- /privacy/

Avoid spaces and Chinese characters in URL slugs.

## Content Type Adaptation

When cloning the starter for a website that does not use Blog, adapt only the content-specific layer.

Example:

Blog becomes Book.

Typical changes:

- content/blog/ becomes content/book/
- layouts/blog/ becomes layouts/book/
- archetypes/blog.md becomes archetypes/book.md
- Blog navigation becomes Book
- Blog CMS collection becomes Book

The following systems should normally remain unchanged:

- Base layout
- Header
- Footer
- Navigation system
- Responsive behavior
- SEO system
- Media system
- Design tokens
- Standard pages

## Content vs System

Content files contain website-specific information.

System files control reusable website behavior.

Adding a new article, book, note, or page should not require changing system files.

## Source of Truth

Content lives in Markdown files.

Decap CMS is an editing interface for Markdown content.

The Git repository remains the source of truth.
