import requests
import json

# new_mail = "https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1"
# get_mails = "https://www.1secmail.com/api/v1/?action=getMessages&login=ivuqsiqyrip4&domain=1secmail.org"
# response = requests.get(new_mail)
# email = response.text
# for i in email:
#     if i == "["or i == "\"" or i == "]":
#         email = email.replace(i, "")
# login = email.split("@")
# print(login[0])
# print(login[1])
# get_mails1 = f"https://www.1secmail.com/api/v1/?action=getMessages&login={login[0]}&domain={login[1]}"
# mails = requests.get(get_mails)
# data = json.loads(mails.text)
# id = data[0]["id"]
# messages = f"https://www.1secmail.com/api/v1/?action=readMessage&login=ivuqsiqyrip4&domain=1secmail.org&id={id}"
# message = requests.get(messages)
# data = json.loads(message.text)
# print("Subject:{}".format(data["subject"]))
# print("textBody:{}" .format(data["textBody"]))

# class TempMail(object):
#     """foo"""
#     def __init__(self):
#         """foo"""
#         self.new_mail = "https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1"
#         self.new_mail_response = requests.get(self.new_mail)
#         self.email = self.new_mail_response.text
#         for i in self.email:
#             if i == "["or i == "\"" or i == "]":
#                 self.email = self.email.replace(i, "")
#         self.login = self.email.split("@")

#     def get_mail(self):
#         """foo"""
#         self.get_mails = f"https://www.1secmail.com/api/v1/?action=getMessages&login={self.login[0]}&domain={self.login[1]}"
#         self.mails = requests.get(self.get_mails)
#         return self.mails.text


#     def get_mail_id(self):
#         """foo"""
#         self.data = json.loads(self.mails.text)
#         self.id = self.data[0]["id"]
#         return self.id

#     def get_mail_messages(self):
#         """foo"""
#         self.messages = f"https://www.1secmail.com/api/v1/?action=readMessage&login={self.login[0]}&domain={self.login[1]}&id={self.id}"
#         self.message = requests.get(self.messages)
#         data = json.loads(self.message.text)
#         return data

#     def get_mail_subject(self):
#         """foo"""
#         self.messages = f"https://www.1secmail.com/api/v1/?action=readMessage&login={self.login[0]}&domain={self.login[1]}&id={self.id}"
#         self.message = requests.get(self.messages)
#         data = json.loads(self.message.text)
#         return data["subject"]

#     def get_mail_text(self):
#         """foo"""
#         self.messages = f"https://www.1secmail.com/api/v1/?action=readMessage&login={self.login[0]}&domain={self.login[1]}&id={self.id}"
#         self.message = requests.get(self.messages)
#         data = json.loads(self.message.text)
#         return data["textBody"]

# if __name__ == '__main__':
#     tm = TempMail()
#     print(tm.get_mail())
#     print(tm.get_mail_id())
#     print(tm.get_mail_messages())
#     print(tm.get_mail_subject())
#     print(tm.get_mail_text())

class TempMail(object):
    """foo"""
    def __init__(self):
        """foo"""
        self.new_mail = "https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1"
        try:
            self.new_mail_response = requests.get(self.new_mail)
        except requests.exceptions.ConnectionError:
            try:
                self.new_mail_response = requests.get(self.new_mail)
            except requests.exceptions.ConnectionError:
                try:
                    self.new_mail_response = requests.get(self.new_mail)
                except requests.exceptions.ConnectionError:
                    self.new_mail_response = requests.get(self.new_mail)
        except requests.exceptions.Timeout:
            try:
                self.new_mail_response = requests.get(self.new_mail)
            except requests.exceptions.Timeout:
                try:
                    self.new_mail_response = requests.get(self.new_mail)
                except requests.exceptions.Timeout:
                    self.new_mail_response = requests.get(self.new_mail)
        except requests.exceptions.TooManyRedirects:
            try:
                self.new_mail_response = requests.get(self.new_mail)
            except requests.exceptions.TooManyRedirects:
                try:
                    self.new_mail_response = requests.get(self.new_mail)
                except requests.exceptions.TooManyRedirects:
                    self.new_mail_response = requests.get(self.new_mail)
        except requests.exceptions.RequestException:
            try:
                self.new_mail_response = requests.get(self.new_mail)
            except requests.exceptions.RequestException:
                try:
                    self.new_mail_response = requests.get(self.new_mail)
                except requests.exceptions.RequestException:
                    self.new_mail_response = requests.get(self.new_mail)
        self.email = self.new_mail_response.text
        for i in self.email:
            if i == "["or i == "\"" or i == "]":
                self.email = self.email.replace(i, "")
        self.login = self.email.split("@")
        self.get_mails = f"https://www.1secmail.com/api/v1/?action=getMessages&login={self.login[0]}&domain={self.login[1]}"
        try:
            self.mails = requests.get(self.get_mails)
        except requests.exceptions.ConnectionError:
            try:
                self.mails = requests.get(self.get_mails)
            except requests.exceptions.ConnectionError:
                try:
                    self.mails = requests.get(self.get_mails)
                except requests.exceptions.ConnectionError:
                    self.mails = requests.get(self.get_mails)
        except requests.exceptions.Timeout:
            try:
                self.mails = requests.get(self.get_mails)
            except requests.exceptions.Timeout:
                try:
                    self.mails = requests.get(self.get_mails)
                except requests.exceptions.Timeout:
                    self.mails = requests.get(self.get_mails)
        except requests.exceptions.TooManyRedirects:
            try:
                self.mails = requests.get(self.get_mails)
            except requests.exceptions.TooManyRedirects:
                try:
                    self.mails = requests.get(self.get_mails)
                except requests.exceptions.TooManyRedirects:
                    self.mails = requests.get(self.get_mails)
        except requests.exceptions.RequestException:
            try:
                self.mails = requests.get(self.get_mails)
            except requests.exceptions.RequestException:
                try:
                    self.mails = requests.get(self.get_mails)
                except requests.exceptions.RequestException:
                    self.mails = requests.get(self.get_mails)
        self.data = json.loads(self.mails.text)
        self.id = self.data[0]["id"]
        self.messages = f"https://www.1secmail.com/api/v1/?action=readMessage&login={self.login[0]}&domain={self.login[1]}&id={self.id}"
        try:
            self.message = requests.get(self.messages)
        except requests.exceptions.ConnectionError:
            try:
                self.message = requests.get(self.messages)
            except requests.exceptions.ConnectionError:
                try:
                    self.message = requests.get(self.messages)
                except requests.exceptions.ConnectionError:
                    self.message = requests.get(self.messages)
        except requests.exceptions.Timeout:
            try:
                self.message = requests.get(self.messages)
            except requests.exceptions.Timeout:
                try:
                    self.message = requests.get(self.messages)
                except requests.exceptions.Timeout:
                    self.message = requests.get(self.messages)
        except requests.exceptions.TooManyRedirects:
            try:
                self.message = requests.get(self.messages)
            except requests.exceptions.TooManyRedirects:
                try:
                    self.message = requests.get(self.messages)
                except requests.exceptions.TooManyRedirects:
                    self.message = requests.get(self.messages)
        self.data = json.loads(self.message.text)

    def get_mail_subject(self):
        """foo"""
        return self.data["subject"]

    def get_mail_text(self):
        """foo"""
        return self.data["textBody"]

    def get_mail_id(self):
        """foo"""
        return self.id
    
    def get_mail(self):
        """foo"""
        return self.mails.text
    
    def get_mail_messages(self):
        """foo"""
        return self.message.text
    
if __name__ == '__main__':
    tm = TempMail()
    print(tm.get_mail())
    print(tm.get_mail_id())
    print(tm.get_mail_messages())
    print(tm.get_mail_subject())
    print(tm.get_mail_text())