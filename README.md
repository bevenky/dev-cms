# Dev-CMS


## User Facing Features

* HTML Pages  - <done>
* Landing Pages - <done>
* Blogs with comments and sharing on social media
* FAQ with Search
* Contact us forms
  - Sales
  - Support
  - Newsletter signups
  - Beta Features
  - Marketing Material Download
  - Landing Pages
  - Signup as a user



## Admin

* Content for HTML pages using html editor - <done>
* Map URLs to Content Pages - <done>
* Redirect URLs - 301 - <done>
* Blog editing (wordpress benchmark)
* Media Embed
    - Image, Css, JS uploads to S3 and ability to embed them to pages
    - Embedded media from popular sites like YouTube, Digg, and Vimeo
* Sitemap generator - <done>
* SEO checker - use seomoz apis
    (Title, URL, Keyword density, meta description)
* FAQ App with search
* User Management
    - Users can edit own blogs and admin can access all
    - Users can be given access to only some pages
* Themes for all pages/blogs/faq - <done>
* Import export themes/pages via admin
* Categories and Popular posts for blogs
* Draft and Preview for Pages and Blogs
* Scheduled Publishing for Blogs
* Copy checker
    - Copyscape
    - After the Deadline plugin
* Backup all data with one click to S3



## Other Notes

* Cache data
* Django Templates from DB for static pages and blog - <done>
* Revision Control
* Permission Management for Users
* Organize Static Pages into groups and groups have permissions
* Blog posts have permissions


## Entities

* Pages - <done>
  - Meta details
    - Title, Description, Keywords, URL
  - Edit using Django template structure
  - Page group and Author
  - Show in Sitemap option

* Media Manager
  - Upload media to S3 bucket
  - have alias for media uploaded and url shown
  - Allow addition of media in HTML + blog

* Redirects - <done>
  - 301 redirects

* Posts
  - Meta details
    - Title, Description, Keywords, URL
  - Fill Content Blocks using WYSIWYG or HTML (formatted)
  - Author, Tags, Categories, Add Featured Image
  - Allow comments option
  - Show in Sitemap option
  - Publish after x date
  - Draft vs Public mode (Draft mode obfuscates url and doesnt show in main blog listing)
  - Feature Post
  - Main blog listing to show features posts
  - End of posts show related articles from same categories maybe

* FAQ
  - FACK + Django knowledge

