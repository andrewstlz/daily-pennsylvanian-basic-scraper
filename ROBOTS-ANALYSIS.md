# Robots Analysis for the Daily Pennsylvanian

The Daily Pennsylvanian's `robots.txt` file is available at
[https://www.thedp.com/robots.txt](https://www.thedp.com/robots.txt).

## Contents of the `robots.txt` file on [ ... date you accessed the file ... ]

```
User-agent: *
Crawl-delay: 10
Allow: /

User-agent: SemrushBot
Disallow: /
```

## Explanation

User-agent: *
This applies to all web crawlers (the * is a wildcard, meaning "any bot").

Crawl-delay: 10
This instructs all bots to wait 10 seconds between requests to the server. This is often used to reduce server load.

Allow: /
This explicitly allows all bots to crawl the entire website.

User-agent: SemrushBot
This is a specific rule for SemrushBot (a popular SEO analysis bot).

Disallow: /
This tells SemrushBot that it is not allowed to crawl any part of the website.
