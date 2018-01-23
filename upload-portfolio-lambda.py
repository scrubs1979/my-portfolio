import zipfile
    import mimetypes
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
    return 'Hello from Lambda'
