# Project

## Name

Personal Blog Starter

## Purpose

Personal Blog Starter is a reusable website foundation for personal blogs and simple content websites.

The goal is to create new websites quickly without rebuilding common systems.

## Core Principle

The project is divided into three layers:

### System

Reusable website infrastructure.

Examples:

- Base layout
- Header
- Footer
- Responsive navigation
- Mobile bottom navigation
- SEO
- RSS
- Sitemap
- 404
- CMS
- Media handling

System files should rarely need changes in cloned websites.

### Config

Website-specific settings.

Examples:

- Website name
- Description
- Language
- Navigation
- Colors
- Typography
- Social links
- Branding

Main configuration files:

- data/site.yaml
- data/navigation.yaml
- data/design.yaml

### Content

Website-specific content.

Examples:

- Blog posts
- About
- Contact
- Privacy
- Terms

## Default Information Architecture

- Home
- Blog
- About
- More
  - Contact
  - Privacy
  - Terms

## Responsive Strategy

Mobile first.

Mobile uses bottom navigation.

Tablet and desktop use top navigation.

Navigation items must remain configurable.

Do not hard-code the number of navigation items into the website architecture.

## Reuse Strategy

When creating a new website:

1. Create a new repository from this starter.
2. Update site configuration.
3. Update navigation.
4. Update design tokens.
5. Replace default content.
6. Rename or adapt the Blog content type if needed.
7. Configure production CMS authentication.
8. Configure deployment and domain.
9. Test.
10. Launch.

## Source of Truth

The repository is the source of project context.

AI coding assistants and developers should read the repository documentation before making structural changes.
