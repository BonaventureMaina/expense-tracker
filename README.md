# Expense Tracker

A personal expense tracking web application built with Django. Users can log, categorize, filter, and summarize their daily expenses — all in a clean, responsive interface.

---

## Features

- **User authentication** — register, login, logout with session management
- **Expense management** — full CRUD (create, read, update, delete)
- **User-specific data** — each user sees only their own expenses
- **Category filtering** — filter expenses by category or month
- **Spending summary** — real-time breakdown of totals per category
- **Django messages** — success and error notifications on all actions
- **Responsive UI** — styled with Tailwind CSS via CDN

---

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Django 6.0.3 |
| Language | Python 3.13 |
| Database | SQLite (development) |
| Frontend | Tailwind CSS (CDN) |
| Auth | Django built-in authentication |

---

## Project Structure

```
expense-tracker/
├── core/                  # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── expenses/              # Expenses app
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
├── accounts/              # Authentication app
│   ├── views.py
│   └── urls.py
├── templates/
│   ├── base.html
│   ├── accounts/
│   │   ├── login.html
│   │   └── register.html
│   └── expenses/
│       ├── expense_list.html
│       ├── expense_form.html
│       └── expense_confirm_delete.html
├── manage.py
└── requirements.txt
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- pip

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/BonaventureMaina/expense-tracker.git
cd expense-tracker
```

**2. Create and activate a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Apply migrations**

```bash
python manage.py migrate
```

**5. Create a superuser**

```bash
python manage.py createsuperuser
```

**6. Run the development server**

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## Expense Categories

- Food
- Transport
- Rent
- Utilities
- Entertainment
- Health
- Other

---

## Screenshots

> Register, log in, and start tracking your expenses immediately.

---

## Git Workflow

Each feature was committed incrementally:

```
Initial project setup
Add Expense model, list, create, edit, delete views with auth
Add category and month filtering to expense list
Add category summary with aggregation to expense list
Style form fields with Tailwind across expenses and accounts
Add root URL redirect to expenses list
Add login error message and complete full user flow testing
```

---

## Author

**Bonaventure Maina Wachira**  
BSc Computer Technology — JKUAT, Kenya  
[github.com/BonaventureMaina](https://github.com/BonaventureMaina)

---

## License

This project is open source and available under the [MIT License](LICENSE).
