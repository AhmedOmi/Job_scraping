from urllib import request

""" get urls from linkedin and indeed """
def getUrl():
    Indeed = request.urlopen('https://www.indeed.com/jobs?q=machine+learning&jt=internship')
    linkedin = request.urlopen('https://www.linkedin.com/jobs/search/?f_JT=I&keywords=machine%20learning%20internship')
    print("result code:" + str(Indeed.getcode()), str(linkedin.getcode()))
    data_linkedin = linkedin.read()
    print(data_linkedin)
    print("\n ---------------------------------------------------------------------------------\n")
    print("\n ---------------------------------------------------------------------------------\n")
    print("\n ---------------------------------------------------------------------------------\n")
    print("\n ---------------------------------------------------------------------------------\n")
    data_Indeed = Indeed.read()
    print(data_Indeed)
