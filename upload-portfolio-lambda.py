def lambda_handler(event, context):
    import boto3
    import io
    import zipfile
    import mimetypes
    sns = boto3.resource('sns')
    topic = sns.Topic('arn:aws:sns:us-east-1:209335604342:deployPortfolioTopic')
    try:
        s3 = boto3.resource('s3')

        portfolio_bucket = s3.Bucket('portfolio.nicholashopkins.info')
        build_bucket = s3.Bucket('portfoliobuild.nicholashopkins.info')

        portfolio_zip = io.BytesIO()
        build_bucket.download_fileobj('portfoliobuild.zip', portfolio_zip)

        with zipfile.ZipFile(portfolio_zip) as myzip:
            for nm in myzip.namelist():
                print(nm)
        with zipfile.ZipFile(portfolio_zip) as myzip:
            for nm in myzip.namelist():
                obj = myzip.open(nm)

        print "Job done!"
        topic.publish(Subject="Portfolio deployed", Message="Portfolio deployed successfully!")
    except:
        topic.publish(Subject="Portfolio Deploy Failed", Message="The Portfolio was not deployed successfully!")
        raise

    return 'Hello from Lambda'
