import boto3

from rootkey import keyid, secretkey

sandbox = "https://mturk-requester-sandbox.us-east-1.amazonaws.com"
production = "https://mturk-requester.us-east-1.amazonaws.com"
client = boto3.client('mturk', endpoint_url=production, region_name='us-east-1', aws_access_key_id=keyid,
                      aws_secret_access_key=secretkey)


def create_quali():
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
                                                # RetryDelayInSeconds=0,
                                                AutoGranted=False)


if __name__ == '__main__':
    create_quali()
