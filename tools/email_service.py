import smtplib
from config.keys import EMAIL_ADDRESS, EMAIL_PASSWORD

def _process_spelled_email(spelled_email):
    """Converts a spelled-out email into a valid email string."""
    return spelled_email.replace(" at ", "@").replace(" dot ", ".").replace(" ", "")

def send_email_flow(speak, takeCommand):
    """Guides the user through the process of sending an email."""
    try:
        speak("To whom should I send the email?")
        recipient_name = takeCommand()
        if not recipient_name: return

        speak(f"Okay, please spell out the email address for {recipient_name}.")
        spelled_email = takeCommand().lower()
        recipient_email = _process_spelled_email(spelled_email)

        if not recipient_email:
            speak("I'm sorry, I didn't catch the email address.")
            return

        speak(f"The email address is {recipient_email}. Is that correct?")
        confirmation = takeCommand().lower()

        if "yes" in confirmation:
            speak("What is the subject of the email?")
            subject = takeCommand()
            speak("And what should the message say?")
            body = takeCommand()

            message = f"Subject: {subject}\n\n{body}"

            # Connect to your email provider's server
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.sendmail(EMAIL_ADDRESS, recipient_email, message)
            speak("The email has been sent successfully, sir.")
        else:
            speak("My apologies. I will cancel the request.")

    except Exception as e:
        print(f"Failed to send email: {e}")
        speak("I'm sorry, sir. I was unable to send the email.")
