# Email Saver

A Python script that connects to an IMAP server and downloads all emails from your inbox, saving them as text files.

## Features

- Connects to an IMAP email server (e.g., Gmail).
- Downloads all emails from the inbox.
- Saves each email as a text file with the subject as the filename.
- Handles multipart emails and saves the body content.

## Prerequisites

- Python 3.x
- Required Python libraries: `imaplib`, `email`, `os`, `socket`

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/yourusername/email-saver.git
   cd email-saver
   ```

2. Ensure you have Python 3.x installed on your machine.
    - Open the `email_saver.py` file.
    - Update the following variables with your email credentials and desired save directory:

    
```Python
email_address = "your_email@example.com"  # Your email address
password = "your_password"                  # Your email password
imap_server = "imap.gmail.com"              # IMAP server address (e.g., Gmail)
save_directory = "./emails"                 # Directory to save emails

```

3. Run the script:

    ```bash
    python email_saver.py

    ```
## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Author
- Taher Hathi


### Instructions for Customization
- Replace `yourusername` in the clone command with your GitHub username.
- Update `your_email@example.com` and `your_password` with your actual email credentials in the usage section.


