# Django Blog Project – Overview Documentation

## 📌 Project Summary
This project is a simple Django blog application with **user authentication** and **blog post management**.  
It demonstrates template inheritance, static file usage, styled forms using a global CSS file, and full CRUD operations for blog posts.  

---

## 🎯 Features
- User registration with email and password confirmation  
- User login and logout  
- Profile page showing user details  
- Blog post CRUD operations:
  - List all posts  
  - View individual post details  
  - Create new posts (authenticated users only)  
  - Edit and delete posts (author-only access)  
- Permissions with `LoginRequiredMixin` and `UserPassesTestMixin`  
- Base template (`base.html`) for consistent layout  
- Global stylesheet applied to all pages  
- Extendable structure for adding comments and extra features  

---

## 📂 Project Structure (Overview)
- **blog/** → Main app containing models, views, forms, templates, and urls  
- **templates/blog/** → All HTML templates (base, register, login, profile, CRUD templates)  
  - `post_list.html` – List all posts  
  - `post_detail.html` – View full post  
  - `post_form.html` – Create & edit posts  
  - `post_confirm_delete.html` – Delete confirmation  
- **static/css/** → Global stylesheet (`styles.css`)  
- **django_blog/** → Project settings and URL configurations  

---

## 🖼 Templates
- **base.html** → Common layout (header, footer, navigation)  
- **register.html** → User registration form  
- **login.html** → User login form  
- **profile.html** → User profile page  
- **post_list.html** → Displays all blog posts  
- **post_detail.html** → Displays a single post in detail  
- **post_form.html** → Used for creating and updating posts  
- **post_confirm_delete.html** → Confirms deletion of a post  

---

## 🎨 Styling
- A single CSS file (`styles.css`) is used for the entire project.  
- It provides:
  - Page layout reset  
  - Header and footer styling  
  - Navigation bar design  
  - Simple clean look for forms, lists, and blog post views  

---

## 🚀 How It Works
1. **Base template inheritance** ensures consistent structure across all pages.  
2. **Authentication system** handles user registration, login, and profile access.  
3. **CRUD views** (`ListView`, `DetailView`, `CreateView`, `UpdateView`, `DeleteView`) power blog post management.  
4. **ModelForm** for the `Post` model manages creation and editing of posts.  
5. **Permissions** restrict creation, editing, and deletion of posts to logged-in users and post authors.  
6. **Static files** (CSS/JS) are loaded through Django’s `{% static %}` system.  

---

## ✅ Deliverable Notes
- No extra CSS was added — all templates use the **existing global styling**.  
- Blog post CRUD features are fully integrated with authentication and permissions.  
- Navigation links connect list, detail, create, edit, and delete views.  
- The project is now a functional blog with both **user management** and **post management**.  
- Templates, static files, and authentication are well-organized and reusable.  

---
