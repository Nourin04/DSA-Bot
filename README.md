

# Coding Tutor Bot

The **Coding Tutor Bot** is a web-based interactive interface designed to help users learn Python programming and Data Structures & Algorithms (DSA). It offers three core features:

1. Code Explanation
2. DSA Question Answering
3. Random Problem Generation

This project provides an engaging UI, smart input detection, responsive design, and accessibility-friendly features to enhance the learning experience.

---

## Features

### 1. Code Explanation

* Paste any Python code snippet into the input box.
* The bot will break down the code step-by-step and explain its functionality.

### 2. DSA Question Answering

* Ask conceptual questions about algorithms, data structures, or complexity analysis.
* Examples:

  * How does quicksort work?
  * Difference between BFS and DFS?
  * Time complexity of merge sort.

### 3. Problem Generator

* Generates random coding problems based on a **topic** and **difficulty**.
* Topics could include: Recursion, Arrays, Trees, Graphs, etc.
* Difficulty levels: Easy, Medium, Hard.

---

## UI/UX Highlights

* **Feature Selector**
  Interactive selection cards that allow users to switch between modes.

* **Smart Input Detection**
  Automatically detects if pasted content is Python code and switches to **Code Explanation** mode.

* **Responsive Design**
  Fully optimized for both desktop and mobile devices.

* **Loading State**
  Disables form submission button with visual feedback while processing.

* **Accessibility**

  * Focus indicators for keyboard navigation.
  * Reduced-motion support for users with motion sensitivity.
  * Semantic HTML structure.

* **Animations and Feedback**

  * Smooth scroll on focus.
  * Interactive hover effects.
  * Intersection observer animations when elements enter the viewport.

---

## Folder Structure

```
├── __pycache__/              # Compiled Python files
├── static/                   # Static assets (CSS, JS, images)
├── templates/                # HTML templates
│   └── index.html
├── .gitignore                # Ignored files for Git
├── README.md                 # Project documentation
├── app.py                    # Main Flask app entry point
├── openrouter_utils.py       # Helper functions for OpenRouter API
├── prompts.py                # Predefined prompt templates
├── requirements.txt          # Python dependencies
       
```


---

##  Setup Instructions

Follow these steps to set up and run the **DSA Bot** locally.

###  Clone the Repository

```bash
git clone https://github.com/Nourin04/DSA-Bot.git
cd DSA-Bot
```

###  Create a Virtual Environment (Recommended)

It’s best to keep dependencies isolated.

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

###  Install Dependencies

```bash
pip install -r requirements.txt
```

###  Set Environment Variables

You’ll need your **OpenRouter API key**. Create a `.env` file in the project root and add:

```env
OPENROUTER_API_KEY=your_api_key_here
```

> Get your API key from [OpenRouter](https://openrouter.ai/).

###  Run the Application

```bash
python app.py
```

The app will start on:

```
http://127.0.0.1:5000/
```

### Deactivate Environment (When Done)

```bash
deactivate
```
.



---

## Future Enhancements

* Backend AI integration for real-time Python explanations and problem generation.
* Syntax highlighting for code in responses.
* User authentication for saving progress.
* Support for multiple programming languages.

---



If you’d like, I can also prepare a **Flask backend** for this HTML so that your Coding Tutor Bot works end-to-end with AI responses. That would make this README complete with full deployment instructions.
