#!/usr/bin/env python3

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "public"

errors = []
warnings = []


def read(path):
    path = ROOT / path
    if not path.exists():
        errors.append(f"Missing file: {path.relative_to(ROOT)}")
        return ""
    return path.read_text(encoding="utf-8")


def check(label, condition):
    if condition:
        print(f"✅ {label}")
    else:
        print(f"❌ {label}")
        errors.append(label)


print("\n=== Lao Zi Ai Du Shu Site Check ===\n")

# Core generated pages
pages = {
    "Homepage": "public/index.html",
    "Book archive": "public/book/index.html",
    "About": "public/about/index.html",
    "Contact": "public/contact/index.html",
    "Privacy": "public/privacy/index.html",
    "Terms": "public/terms/index.html",
}

for label, filename in pages.items():
    check(label, (ROOT / filename).exists())

print("\n=== Global files ===")

for label, filename in {
    "robots.txt": "public/robots.txt",
    "sitemap.xml": "public/sitemap.xml",
    "RSS": "public/index.xml",
    "Default OG image": "public/images/og-default.png",
    "Favicon": "public/images/favicon.svg",
}.items():
    check(label, (ROOT / filename).exists())

print("\n=== Homepage metadata ===")

home = read("public/index.html")

check("Title", bool(re.search(r"<title>.+?</title>", home, re.S)))
check("Meta description", 'name="description"' in home)
check("Canonical", 'rel="canonical"' in home)
check("Robots", 'name="robots"' in home)
check("OG title", 'property="og:title"' in home)
check("OG description", 'property="og:description"' in home)
check("OG image", 'property="og:image"' in home)
check("OG image alt", 'property="og:image:alt"' in home)
check("Twitter card", 'name="twitter:card"' in home)
check("Twitter image", 'name="twitter:image"' in home)
check("Twitter image alt", 'name="twitter:image:alt"' in home)

check(
    "Single favicon declaration",
    len(re.findall(r'rel="icon"', home)) == 1
)

print("\n=== Homepage schema ===")

compact_home = re.sub(r"\s+", "", home)

check('"WebSite" schema', '"@type":"WebSite"' in compact_home)
check('"Organization" schema', '"@type":"Organization"' in compact_home)
check(
    "Site alternate name",
    '"alternateName":"LaoZiAiDuShu"' in compact_home
)

print("\n=== Book schema ===")

book_files = list((PUBLIC / "book").glob("*/index.html")) if (PUBLIC / "book").exists() else []

if book_files:
    book = book_files[0].read_text(encoding="utf-8")
    compact_book = re.sub(r"\s+", "", book)

    check("BlogPosting schema", '"@type":"BlogPosting"' in compact_book)
    check("Book schema", '"@type":"Book"' in compact_book)
    check("Publisher organization", '"publisher":{' in compact_book)
else:
    warnings.append("No generated book detail pages found.")
    print("⚠️ No generated book detail pages found")

print("\n=== Taxonomy indexing ===")

business = read("public/categories/business/index.html")
psychology = read("public/categories/psychology/index.html")
categories_root = read("public/categories/index.html")
tags_root = read("public/tags/index.html")

check(
    "Non-empty category is indexable",
    'content="index, follow, max-image-preview:large"' in business
)

check(
    "Empty category is noindex",
    'content="noindex, follow"' in psychology
)

check(
    "Categories root is noindex",
    'content="noindex, follow"' in categories_root
)

check(
    "Tags root is noindex",
    'content="noindex, follow"' in tags_root
)

print("\n=== Configuration ===")

config = read("data/site.yaml")
hugo = read("hugo.toml")

check('Chinese site name configured', 'name: "老子爱读书"' in config)
check(
    "English alternate name configured",
    'alternateName: "Lao Zi Ai Du Shu"' in config
)

check(
    "Configured favicon",
    'favicon: "/images/favicon.svg"' in config
)

if 'baseURL = "/"' in hugo:
    print("ℹ️ baseURL is still temporary (/). This is expected before the production domain is connected.")
else:
    print("✅ Production-style baseURL configured")

print("\n=== Result ===")

if warnings:
    for warning in warnings:
        print(f"⚠️ {warning}")

if errors:
    print(f"\n❌ {len(errors)} check(s) failed.")
    sys.exit(1)

print("\n✅ All automated checks passed.")
