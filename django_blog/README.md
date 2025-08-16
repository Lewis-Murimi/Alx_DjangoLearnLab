# Django Blog Project – Overview Documentation

## 📌 Project Summary
This project is a simple Django blog application with **user authentication, blog post management, and comment functionality**.  
It demonstrates template inheritance, static file usage, styled forms, and permission-based access for both posts and comments.  

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
- **Comment System**
  - View all comments under a blog post
  - Add comments (authenticated users only)
  - Edit or delete comments (author only)
- **Template & Styling**
  - Base template (`base.html`) for consistent layout
  - Global stylesheet applied to all pages
  - Clean and simple UI for forms and content

---

## 📂 Project Structure (Overview)
- **blog/** → Main app containing models, views, forms, templates, and URLs  
- **templates/blog/** → HTML templates for authentication, posts, and comments  
- **static/css/** → Global stylesheet (`styles.css`)  
- **django_blog/** → Project settings and URL configurations  

---

## 🖼 Templates
- **base.html** → Common layout (header, footer, navigation)  
- **register.html** → User registration form  
- **login.html** → User login form  
- **profile.html** → User profile page  
- **post_list.html** → List of all posts  
- **post_detail.html** → Full post view with comments section  
- **post_form.html** → Create/edit post form  
- **post_confirm_delete.html** → Delete post confirmation  
- **comment_form.html** → Add/edit comment form  
- **comment_confirm_delete.html** → Delete comment confirmation  

---

## 🎨 Styling
- A single CSS file (`styles.css`) is used for the entire project.  
- It provides:
  - Page layout reset  
  - Header and footer styling  
  - Navigation bar design  
  - Simple clean look for forms, posts, and comments  

---

## 🚀 How It Works
1. **Authentication**  
   Users can register, log in, and access their profile.  
2. **Blog Post CRUD**  
   - All users can view posts.  
   - Authenticated users can create posts.  
   - Only post authors can edit or delete their own posts.  
3. **Comment System**  
   - Comments are displayed under each post.  
   - Logged-in users can add comments.  
   - Authors of comments can edit or delete them.  
   - Permissions prevent unauthorized editing/deletion.  
4. **Template Inheritance**  
   All pages extend from `base.html` for a consistent layout.  
5. **Static Files**  
   CSS styling is applied globally via Django’s `{% static %}` system.  

---

## ✅ Deliverable Notes
- No new CSS was added; all templates use the **existing global styling**.  
- Blog post and comment systems are fully integrated with authentication and permissions.  
- Templates and URLs are logically structured for easy navigation.  
- Tested for security: only authors can modify their content.  

---
