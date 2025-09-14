# Contact Book

A simple **terminal-based Contact Book** written in Python.  
It allows you to **add, search, and delete contacts** and **save/load them using a JSON file**.

---

## Features

- Add new contacts (name and phone number)  
- Search for existing contacts by name  
- Delete contacts  
- Save and load contacts automatically using `contacts.json`  
- Easy-to-use terminal interface  

---

## Usage

Run the program:

```bash
python main.py
```

Follow the menu to **add, search, or delete contacts**.

---

## Project Structure

```
ContactBook/
│
├── main.py           # Main program with menu
├── load_contacts.py  # Functions to manage contacts
├── .gitignore        # Files to ignore in Git
├── LICENSE           # License file
├── README.md         # Project description
```

---

## Notes

* If `contacts.json` does not exist, the program will create it automatically.
* Make sure `contacts.json` has valid JSON format if you manually edit it.

---

## License

This project is open source and free to use.
