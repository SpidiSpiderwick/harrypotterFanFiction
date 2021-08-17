import boto3
import urllib.parse as url

from rootkey import keyid, secretkey

if __name__ == '__main__':
    client = boto3.client('mturk', endpoint_url='https://mturk-requester-sandbox.us-east-1.amazonaws.com',
                          region_name='us-east-1', aws_access_key_id=keyid, aws_secret_access_key=secretkey)
    desc = "Diese Qualification zeigt, dass Sie in der Lage sind, einen grammatikalisch und orthographisch korrekten " \
           "deutschen Satz zu bilden. Außerdem ermöglicht sie Ihnen, unsere Tasks zur Satzsynthese durchzuführen."
    with open("qualification.xml", "r") as quxml:
        test = quxml.read()
        # test = url.quote(quxml.read(), safe="")
    with open("answerkey.xml", "r") as anxml:
        answerKey = anxml.read()
        # answerKey = url.quote(anxml.read(), safe="")
        print(answerKey)
    response = client.create_qualification_type(Name="GrammatikExpertIn",
                                                Keywords="Grammatik,Satz,Proofread,Satz,Satz bilde,Satzsynthese",
                                                Description=desc,
                                                QualificationTypeStatus="Active",
                                                Test=test,
                                                AnswerKey=answerKey,
                                                TestDurationInSeconds=1800,
                                                AutoGranted=False)
