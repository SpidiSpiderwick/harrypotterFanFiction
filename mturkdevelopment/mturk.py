import boto3

from rootkey import keyid, secretkey

sandbox = "https://mturk-requester-sandbox.us-east-1.amazonaws.com"
production = "https://mturk-requester.us-east-1.amazonaws.com"
client = boto3.client('mturk', endpoint_url=production, region_name='us-east-1', aws_access_key_id=keyid,
                      aws_secret_access_key=secretkey)


def create_grammar_quali():
    desc = "Diese Qualification zeigt, dass Sie in der Lage sind, einen grammatikalisch und orthographisch korrekten " \
           "deutschen Satz zu bilden. Außerdem ermöglicht sie Ihnen, unsere Tasks zur Satzsynthese durchzuführen."
    with open("qualification.xml", "r", encoding="utf-8") as quxml:
        test = quxml.read()
    with open("answerkey.xml", "r", encoding="utf-8") as anxml:
        answerKey = anxml.read()
    response = client.create_qualification_type(Name="GrammatikExpertIn",
                                                Keywords="Grammatik,Satz,Proofread,Satz,Satz bilde,Satzsynthese",
                                                Description=desc,
                                                QualificationTypeStatus="Active",
                                                Test=test,
                                                AnswerKey=answerKey,
                                                TestDurationInSeconds=300,
                                                RetryDelayInSeconds=300,
                                                AutoGranted=False)


def create_translate_quali():
    desc = "Hiermit qualifizieren Sie sich, Englisch - Deutsch zu übersetzen."
    with open("translate_quali.xml", "r", encoding="utf-8") as quxml:
        test = quxml.read()
    with open("translate_answ.xml", "r", encoding="utf-8") as anxml:
        answerKey = anxml.read()
    response = client.create_qualification_type(Name="Translater",
                                                Keywords="Satz,Translation",
                                                Description=desc,
                                                QualificationTypeStatus="Active",
                                                Test=test,
                                                AnswerKey=answerKey,
                                                TestDurationInSeconds=300,
                                                # RetryDelayInSeconds=0,
                                                AutoGranted=False)


if __name__ == '__main__':
    create_translate_quali()
