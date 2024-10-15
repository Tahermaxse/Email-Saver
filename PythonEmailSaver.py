import imaplib
import email
import os
from email.header import decode_header
import socket

def clean(text):
    # Clean text for creating a valid filename
    return "".join(c if c.isalnum() else "_" for c in text)

def save_emails(email_address, password, imap_server, save_directory):
    # Create the save directory if it doesn't exist
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    try:
        # Connect to the IMAP server
        print(f"Attempting to connect to {imap_server}...")
        imap = imaplib.IMAP4_SSL(imap_server)
        print("Connected successfully.")

        print("Attempting to log in...")
        imap.login(email_address, password)
        print("Logged in successfully.")

        # Select the mailbox you want to fetch emails from
        imap.select("INBOX")

        # Search for all emails
        _, message_numbers = imap.search(None, "ALL")

        for num in message_numbers[0].split():
            # Fetch the email message by ID
            _, msg = imap.fetch(num, "(RFC822)")
            
            for response in msg:
                if isinstance(response, tuple):
                    # Parse the email content
                    email_msg = email.message_from_bytes(response[1])
                    
                    # Decode the email subject
                    subject, encoding = decode_header(email_msg["Subject"])[0]
                    if isinstance(subject, bytes):
                        subject = subject.decode(encoding or "utf-8")
                    
                    # Clean the subject to create a valid filename
                    clean_subject = clean(subject)
                    
                    # Create a filename for the email
                    filename = f"{clean_subject}.txt"
                    filepath = os.path.join(save_directory, filename)
                    
                    # Write the email content to a file
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(f"Subject: {subject}\n")
                        f.write(f"From: {email_msg['From']}\n")
                        f.write(f"To: {email_msg['To']}\n")
                        f.write(f"Date: {email_msg['Date']}\n\n")
                        
                        # Get email body
                        if email_msg.is_multipart():
                            for part in email_msg.walk():
                                if part.get_content_type() == "text/plain":
                                    body = part.get_payload(decode=True).decode()
                                    f.write(body)
                        else:
                            body = email_msg.get_payload(decode=True).decode()
                            f.write(body)
                    
                    print(f"Saved email: {filename}")

        # Close the connection
        imap.close()
        imap.logout()

    except imaplib.IMAP4.error as e:
        print(f"An IMAP error occurred: {e}")
    except socket.gaierror as e:
        print(f"A network error occurred: {e}")
        print("Please check your internet connection and the IMAP server address.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


email_address = "example@gmail.com"
password = "your_16_character_app_password_here"
imap_server = "imap.gmail.com"
save_directory = "./emails"

save_emails(email_address, password, imap_server, save_directory)