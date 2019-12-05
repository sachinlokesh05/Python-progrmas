
import smtplib# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("sachinsanju04@gmail.com", "@sachinsanju")

# message to be sent
message = "Message_you_need_to_send"

# sending the mail
s.sendmail("sachin.beee.15@acharya.ac.in"),
           "sachin.beee.15@acharya.ac.in", message)

# terminating the session
s.quit()
