# Todo List Project

## Project Description
The **Todo List** project is a web application built with Django for managing tasks and tags. Users can create, edit, delete tasks, and assign tags to them. Tasks are conveniently grouped by their status (completed/not completed) and creation time.

---

## Features
### Tasks
- Create new tasks with the following fields:
  - Task description (`content`);
  - Creation date;
  - Optional deadline (`datetime`);
  - Completion status (completed/not completed).
- View the task list:
  - Tasks are sorted from incomplete to complete;
  - Sorted from newest to oldest.
- Edit tasks.
- Delete tasks.
- Toggle task status (completed ↔ not completed).

### Tags
- Create, edit, and delete tags.
- Assign tags to tasks.
- View all tags in a list.

### Navigation
- Sidebar for quick navigation between pages:
  - Home page (task list);
  - Tag list page.

---

# Technologies Used
- Backend: Django
- Frontend: Bootstrap 5
- Database: SQLite 