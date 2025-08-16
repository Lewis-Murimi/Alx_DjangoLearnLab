# Django Blog Project – Overview Documentation

## 📌 Project Summary
This project is a simple Django blog application with **user authentication, blog post management, comments, search, and tag filtering**.  
It demonstrates template inheritance, static file usage, styled forms, search functionality, and permission-based access for both posts and comments.  

---

## 🎯 Features
- **User Authentication**
  - Registration with email and password confirmation
  - Login and logout
  - Profile page showing user details
- **Blog Post Management (CRUD)**
  - List all posts
  - View single post details
  - Create new posts (authenticated users only)
  - Edit and delete posts (author only)
- **Comment System (CRUD)**
  - View all comments under a blog post
  - Add comments via class-based view (`CommentCreateView`)
  - Edit comments via class-based view (`CommentUpdateView`)
  - Delete comments via class-based view (`CommentDeleteView`)
  - Edit/delete available **only to comment authors**
- **Search Functionality**
  - Search posts by title or content
  - Accessible from the navigation bar
- **Tag System**
  - Each post can be assigned one or more tags
  - Tags displayed on post detail pages
  - Clicking a tag filters posts by that tag
- **Template & Styling**
  - Base template (`base.html`) for consistent layout
  - Global stylesheet applied to all pages
  - Clean and simple UI for forms, posts, comments, and search results

---

## 📂 Project Structure (Overview)
- **blog/** → Main app containing models, views, forms, templates, and URLs  
- **templates/blog/** → HTML templates for authentication, posts, comments, search, and tags  
- **static/css/** → Global stylesheet (`styles.css`)  
- **django_blog/** → Project settings and URL configurations  

---

## 🖼 Templates
- **base.html** → Common layout (header, footer, navigation, search bar)  
- **register.html** → User registration form  
- **login.html** → User login form  
- **profile.html** → User profile page  
- **post_list.html** → List of all posts (with search results and tag filters)  
- **post_detail.html** → Full post view with comments and tags  
- **post_form.html** → Create/edit post form  
- **post_confirm_delete.html** → Delete post confirmation  
- **comment_form.html** → Add/edit comment form  
- **comment_confirm_delete.html** → Delete comment confirmation  
- **search_results.html** → Display posts matching the search query  
- **tag_posts.html** → Display posts filtered by a selected tag  

---

## 🔗 URL Routes
- **Posts**
  - `/posts/` → List all posts  
  - `/post/<id>/` → View post detail with comments  
  - `/post/new/` → Create new post  
  - `/post/<id>/edit/` → Edit post  
  - `/post/<id>/delete/` → Delete post  
- **Comments**
  - `/post/<id>/comments/new/` → Add a new comment  
  - `/comment/<id>/update/` → Edit comment  
  - `/comment/<id>/delete/` → Delete comment  
- **Search & Tags**
  - `/search/` → Search posts by keyword  
  - `/tag/<slug:tag_slug>/` → Filter posts by tag  

---

## 🎨 Styling
- A single CSS file (`styles.css`) is used for the entire project.  
- It provides:
  - Page layout reset  
  - Header and footer styling  
  - Navigation bar with search field  
  - Simple clean look for forms, posts, comments, and tags  

---

## 🚀 How It Works
1. **Authentication**  
   Users can register, log in, and access their profile.  
2. **Blog Post CRUD**  
   - All users can view posts.  
   - Authenticated users can create posts.  
   - Only post authors can edit or delete their own posts.  
3. **Comment System (Class-Based)**  
   - Comments are displayed under each post.  
   - Authenticated users can add comments with `CommentCreateView`.  
   - Comment authors can edit with `CommentUpdateView`.  
   - Comment authors can delete with `CommentDeleteView`.  
4. **Search**  
   - The search bar is available on all pages.  
   - Users can enter keywords to find posts by title or content.  
   - Results are displayed in `search_results.html`.  
5. **Tags**  
   - Posts can have multiple tags.  
   - Tags are displayed as clickable links under each post.  
   - Clicking a tag filters posts by that tag and displays them in `tag_posts.html`.  
6. **Template Inheritance**  
   All pages extend from `base.html` for a consistent layout.  
7. **Static Files**  
   CSS styling is applied globally via Django’s `{% static %}` system.  

---

## ✅ Deliverable Notes
- No new CSS was added; all templates use the **existing global styling**.  
- Blog post, comment, search, and tag systems are fully integrated with authentication and permissions.  
- Templates (`base.html`, `post_list.html`, and `post_detail.html`) updated for search and tag features.  
- Tested for security: only authors can modify their content.  

---
