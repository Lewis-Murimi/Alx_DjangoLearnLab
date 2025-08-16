# Django Blog Project – Overview Documentation

## 📌 Project Summary
This project is a simple Django blog application with **user authentication**.  
It demonstrates template inheritance, static file usage, and styled forms using a global CSS file.  

---

## 🎯 Features
- User registration with email and password confirmation
- User login and logout
- Profile page showing user details
- Base template (`base.html`) for consistent layout
- Global stylesheet applied to all pages
- Extendable structure for adding blog posts and comments

---

## 📂 Project Structure (Overview)
- **blog/** → Main app containing templates, views, and forms  
- **templates/blog/** → All HTML templates (base, register, login, profile)  
- **static/css/** → Global stylesheet (`styles.css`)  
- **django_blog/** → Project settings and URL configurations  

---

## 🖼 Templates
- **base.html** → Common layout (header, footer, navigation)  
- **register.html** → User registration form  
- **login.html** → User login form  
- **profile.html** → User profile page  

---

## 🎨 Styling
- A single CSS file (`styles.css`) is used for the entire project.  
- It provides:
  - Page layout reset  
  - Header and footer styling  
  - Navigation bar design  
  - Simple clean look for forms and content  

---

## 🚀 How It Works
1. **Base template inheritance** ensures consistent structure.  
2. **Forms** are automatically styled by the global CSS.  
3. **Static files** (CSS/JS) are loaded through Django’s `{% static %}` system.  
4. **Authentication views** handle user signup, login, and profile access.  

---

## ✅ Deliverable Notes
- No extra CSS was added — all forms use the **existing global styling**.  
- The structure is ready for extension with blog posts, comments, and more.  
- Templates, static files, and authentication are well-organized and reusable.  
