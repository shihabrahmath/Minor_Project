# Minor_Project
My first minor project
# WhatsApp Group Chat Analyzer

## Project Overview

The WhatsApp Group Chat Analyzer is a simple Python project developed as part of the DADS Minor Project. It analyzes an exported WhatsApp chat file and generates useful statistics such as the total number of messages, most active users, busiest day, busiest hour, media messages, and the most frequently used words.

This project is built using only basic Python concepts like:
- Variables
- Loops
- Functions
- Lists
- Dictionaries
- Strings
- File Handling

No external libraries such as Pandas, NumPy, or Matplotlib are used.

---

## Features

- Read WhatsApp exported chat (.txt) file
- Count total messages
- Count messages sent by each user
- Find the most active user
- Find the busiest day
- Find the busiest hour
- Calculate average words per message for each user
- Count media messages sent by each user
- Display the top 10 most frequently used words
- Ignore common stop words while counting word frequency

---

## Technologies Used

- Python 3.x
- File Handling
- Lists
- Dictionaries
- String Manipulation
- Functions

---

## Project Structure

```
whatsapp analyzer/
│
├── whatsapp_chat_analyzer.py
├── DADS_Minor_PROJECT_dataset.txt.txt
└── README.md
```

---

## Input File Format

Export your WhatsApp chat without media.

Example:

```
01/04/24, 10:15 - Rahul: Good morning everyone
01/04/24, 10:18 - Priya: Hello
01/04/24, 10:20 - Aman: <Media omitted>
```

---

## How to Export WhatsApp Chat

1. Open WhatsApp.
2. Open the group chat.
3. Tap the three dots.
4. Select **More**.
5. Click **Export Chat**.
6. Choose **Without Media**.
7. Save the text file.

---

## How to Run the Project

### Step 1

Install Python 3.x

Download from:

https://www.python.org/downloads/

### Step 2

Download or clone this project.

### Step 3

Place your exported WhatsApp chat text file inside the project folder.

### Step 4

Open `whatsapp_chat_analyzer.py`

Change the file path:

```python
FILE_PATH = "C:/Users/YourName/Desktop/whatsapp analyzer/chat.txt"
```

Replace it with the location of your own chat file.

### Step 5

Open Command Prompt or PowerShell.

Navigate to the project folder.

Example:

```
cd "C:\Users\YourName\Desktop\whatsapp analyzer"
```

Run the program:

```
python whatsapp_chat_analyzer.py
```

---

## Sample Output

```
=======================================================
      WHATSAPP GROUP CHAT ANALYSIS REPORT
=======================================================

Total Messages : 3174

Messages Per User

Rahul : 953
Priya : 718
Karan : 354
Neha : 635
Aman : 490
Vikas : 24

Most Active User : Rahul - 953

Busiest Day : 04/05/24 - 76

Busiest Hour : 18:00 - 248

Average Words Per Message

Rahul : 2.56
Priya : 4.98
Karan : 55.66
Neha : 5.27
Aman : 4.99
Vikas : 1.83

Media Messages

Rahul : 7
Priya : 4
Karan : 7
Neha : 8
Aman : 4
Vikas : 2

Top 10 Words

1. how - 321
2. about - 274
3. am - 260
4. today - 257
5. which - 202
6. everyone - 187
7. telling - 179
8. from - 174
9. up - 172
10. one - 157

=======================================================
END OF REPORT
=======================================================
```

---

## Functions Used

| Function | Description |
|----------|-------------|
| `parse_chat()` | Reads the chat file and stores messages |
| `messages_per_user()` | Counts messages sent by each user |
| `busiest_day()` | Finds the day with the highest messages |
| `busiest_hour()` | Finds the busiest hour |
| `average_message_length()` | Calculates average words per message |
| `media_count_per_user()` | Counts media messages |
| `top_words()` | Finds the top 10 most frequent words |
| `most_active_user()` | Finds the user with the most messages |
| `print_report()` | Displays the final report |
## Future Improvements

- Emoji Analysis
- User Response Time
- Monthly Chat Statistics
- Weekly Activity Report
- Chat Visualizations using Matplotlib
- Export Report to PDF
- GUI using Tkinter
## Author

**Name:** Shihab Rahmath S

**Course:** Master of Computer Applications (MCA)

**College:** St. Francis De Sales Autonomous College

**University:** Bengaluru City University

**Academic Year:** 2025–2027

## License

This project is created for educational purposes as part of the DADS Minor Project.
