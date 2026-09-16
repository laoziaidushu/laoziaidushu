# Design System

## Purpose

This file defines the reusable visual rules for websites created from Personal Blog Starter.

The goal is consistency, simplicity, and easy customization through centralized configuration.

## Design Principles

- Simple
- Content-first
- Responsive
- Mobile-first
- Easy to read
- Minimal visual clutter
- Reusable across different website brands

## Design Configuration

Primary design settings are stored in:

`data/design.yaml`

Avoid hard-coding brand colors, typography, and layout widths directly into components when they can be controlled through design tokens.

## Colors

Default tokens:

- Background
- Surface
- Text
- Muted text
- Border
- Primary

These are exposed as CSS variables through:

`layouts/partials/design-tokens.html`

## Typography

Typography is configured through:

`data/design.yaml`

Default categories:

- Body font
- Heading font

Typography should prioritize readability over decoration.

## Layout

Default maximum site width:

`1120px`

Default reading/content width:

`760px`

Content pages should remain narrower than full site layouts for readability.

## Responsive Strategy

### Mobile

Mobile is the primary design target.

Use:

- Comfortable touch targets
- Simple layouts
- Bottom navigation
- Single-column reading layouts

### Tablet

Tablet adapts from the same information architecture.

Use top navigation where space allows.

### Desktop

Desktop uses:

- Top navigation
- Wider containers
- More horizontal spacing

## Navigation

Default navigation:

- Home
- Blog
- About
- More

More contains:

- Contact
- Privacy
- Terms

Navigation labels and destinations are controlled by:

`data/navigation.yaml`

Navigation items must not be hard-coded into components.

## Mobile Bottom Navigation

Mobile uses a configurable bottom navigation.

Default items:

- Home
- Blog
- About
- More

The system must support changing:

- Labels
- URLs
- Number of items

Do not design the system assuming there will always be exactly four items.

## Images

Default content cover image ratio:

16:9

Recommended size:

1200 × 675 px

Preferred format:

WebP

Acceptable alternatives:

- JPEG
- PNG

File naming:

Use lowercase English words separated by hyphens.

Example:

`my-reading-notes.webp`

## Components

Reusable components should be preferred over repeated markup.

Current reusable components include:

- Header
- Footer
- Desktop navigation
- Mobile navigation
- More menu
- Cover image
- SEO metadata
- Design tokens

## Brand Customization

A cloned website should primarily change:

- Site name
- Logo
- Favicon
- Colors
- Typography
- Navigation labels
- Content

Avoid rewriting the system layout unless the new website genuinely needs a different structure.
