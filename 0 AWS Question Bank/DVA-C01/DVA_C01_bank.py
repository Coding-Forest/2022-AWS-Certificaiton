import os
import sqlite3


class AWSQuestionBank:

    db = 'DVA_C01_bank.db'
    columns = ['id', 'question', 'choiceA', 'choiceB', 'choiceC', 'choiceD', 'choiceE', 'answer']

    def __init__(self):
        pass

    def create_db(self):
        # DB
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()

        # Create table
        cursor.execute("""  CREATE TABLE Questionbank (
            id integer,
            question text,
            choiceA text, 
            choiceB text,
            choiceC text,
            choiceD text,
            choiceE text,
            answer text 
        )""")

        conn.commit()
        conn.close()


    def query(self, record_id="*"):
        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()

        if record_id == "*":
            cursor.execute(f'SELECT * FROM Questionbank')
        else:
            cursor.execute(f'SELECT * FROM Questionbank WHERE id={record_id}')

        records = cursor.fetchall()
        for record in records:
            for item in record:
                print(item)

        # for r in records:
        #     for i in range(r):
        #         if i == 7:
        #             print(i + 1, r[i], end="\n")
        #         else:
        #             print(i + 1, r[i])

        conn.commit()
        conn.close()

        return records


    def submit(self, question, a, b, c, d, e, answer):

        conn = sqlite3.connect(self.db)
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM Questionbank')

        records = cursor.fetchall()
        id = len(records) + 1

        cursor.execute(f'INSERT INTO Questionbank VALUES (:{self.columns[0]}, :{self.columns[1]}, :{self.columns[2]}, :{self.columns[3]}, :{self.columns[4]}, :{self.columns[5]}, :{self.columns[6]}, :{self.columns[7]})',
                        {
                            self.columns[0]: id,
                            self.columns[1]: question,
                            self.columns[2]: a,
                            self.columns[3]: b,
                            self.columns[4]: c,
                            self.columns[5]: d,
                            self.columns[6]: e,
                            self.columns[7]: answer,
                        })
        conn.commit()
        conn.close()


if __name__ == "__main__":

    qb = AWSQuestionBank()
    records = qb.query(10)

    print(len(records))
    print(records)


# ======================================================================================

    #qb.submit(question='',
    #          a='',
    #          b='',
    #          c='',
    #          d='',
    #          e='',
    #          answer='')



    # qb.create_db()
    #
    # qb.submit('A company is migrating a legacy application to Amazon EC2. The application uses a user name and password stored in the source code to connect to a MySQL database. The database will be migrated to an Amazon RDS for MySQL DB instance. As part of the migration, the company wants to implement a secure way to store and automatically rotate the database credentials. Which approach meets these requirements?',
    #           'Store the database credentials in environment variables in an Amazon Machine Image (AMI). Rotate the credentials by replacing the AMI.',
    #           'Store the database credentials in AWS Systems Manager Parameter Store. Configure Parameter Store to automatically rotate the credentials.',
    #           'Store the database credentials in environment variables on the EC2 instances. Rotate the credentials by relaunching the EC2 instances.',
    #           'Store the database credentials in AWS Secrets Manager. Configure Secrets Manager to automatically rotate the credentials.',
    #           '',
    #           '')
    #
    # qb.submit(question='A developer is designing a web application that allows the users to post comments and receive near-real-time feedback. Which architectures meet these requirements? (Select TWO.)',
    #          a='Create an AWS AppSync schema and corresponding APIs. Use an Amazon DynamoDB table as the data store.',
    #          b='Create a WebSocket API in Amazon API Gateway. Use an AWS Lambda function as the backend and an Amazon DynamoDB table as the data store.',
    #          c='Create an AWS Elastic Beanstalk application backed by an Amazon RDS database. Configure the application to allow long-lived TCP/IP sockets.',
    #          d='Create a GraphQL endpoint in Amazon API Gateway. Use an Amazon DynamoDB table as the data store.',
    #          e='Enable WebSocket on Amazon CloudFront. Use an AWS Lambda function as the origin and an Amazon Aurora DB cluster as the data store.',
    #          answer='')
    #
    #
    # qb.submit(question='A developer is adding sign-up and sign-in functionality to an application. The application is required to make an API call to a custom analytics solution to log user sign-in events. Which combination of actions should the developer take to satisfy these requirements? (Select TWO.)',
    #          a='Use Amazon Cognito to provide the sign-up and sign-in functionality.',
    #          b='Use AWS IAM to provide the sign-up and sign-in functionality.',
    #          c='Configure an AWS Config rule to make the API call triggered by the post-authentication event.',
    #          d='Invoke an Amazon API Gateway method to make the API call triggered by the post-authentication event.',
    #          e='Execute an AWS Lambda function to make the API call triggered by the post-authentication event.',
    #          answer='')
    #
    # qb.submit(question='A company is using Amazon API Gateway for its REST APIs in an AWS account. The security team wants to allow only IAM users from another AWS account to access the APIs. Which combination of actions should the security team take to satisfy these requirements? (Select TWO.)',
    #          a='Create an IAM permission policy and attach it to each IAM user. Set the APIs method authorization type to AWS_IAM. Use Signature Version 4 to sign the API requests.',
    #          b='Create an Amazon Cognito user pool and add each IAM user to the pool. Set the method authorization type for the APIs to COGNITO_USER_POOLS. Authenticate using the IAM credentials in Amazon Cognito and add the ID token to the request headers.',
    #          c='Create an Amazon Cognito identity pool and add each IAM user to the pool. Set the method authorization type for the APIs to COGNITO_USER_POOLS. Authenticate using the IAM credentials in Amazon Cognito and add the access token to the request headers',
    #          d='Create a resource policy for the APIs that allows access for each IAM user only.',
    #          e='Create an Amazon Cognito authorizer for the APIs that allows access for each IAM user only. Set the method authorization type for the APIs to COGNITO_USER_POOLS.',
    #          answer='')
    #
    # qb.submit(question='A developer is building an application that transforms text files to .pdf files. The text files are written to a source Amazon S3 bucket by a separate application. The developer wants to read the files as they arrive in Amazon S3 and convert them to .pdf files using AWS Lambda. The developer has written an IAM policy to allow access to Amazon S3 and Amazon CloudWatch Logs. Which actions should the developer take to ensure that the Lambda function has the correct permissions?',
    #          a='Create a Lambda execution role using AWS IAM. Attach the IAM policy to the role. Assign the Lambda execution role to the Lambda function.',
    #          b='Create a Lambda execution user using AWS IAM. Attach the IAM policy to the user. Assign the Lambda execution user to the Lambda function.',
    #          c='Create a Lambda execution role using AWS IAM. Attach the IAM policy to the role. Store the IAM role as an environment variable in the Lambda function.',
    #          d='Create a Lambda execution user using AWS IAM. Attach the IAM policy to the user. Store the IAM user credentials as environment variables in the Lambda function.',
    #          e='',
    #          answer='')
    #
    # qb.submit(question='A company has AWS workloads in multiple geographical locations. A developer has created an Amazon Aurora database in the us-west-1 Region. The database is encrypted using a customer-managed AWS KMS key. Now the developer wants to create the same encrypted database in the us-east-1 Region. Which approach should the developer take to accomplish this task?',
    #          a='Create a snapshot of the database in the us-west-1 Region. Copy the snapshot to the us-east-1 Region and specify a KMS key in the us-east-1 Region. Restore the database from the copied snapshot.',
    #          b='Create an unencrypted snapshot of the database in the us-west-1 Region. Copy the snapshot to the us-east-1 Region. Restore the database from the copied snapshot and enable encryption using the KMS key from the us-east-1 Region.',
    #          c='Disable encryption on the database. Create a snapshot of the database in the us-west-1 Region. Copy the snapshot to the us-east-1 Region. Restore the database from the copied snapshot.',
    #          d='In the us-east-1 Region, choose to restore the latest automated backup of the database from the us-west-1 Region. Enable encryption using a KMS key in the us-east-1 Region.',
    #          e='',
    #          answer='')
    #
    # qb.submit(question='A developer is adding Amazon ElastiCache for Memcached to a company\'s existing record storage application to reduce the load on the database and increase performance. The developer has decided to use lazy loading based on an analysis of common record handling patterns. Which pseudocode example would correctly implement lazy loading?',
    #          a='record_value = db.query("UPDATE Records SET Details = {1} WHERE ID == {0}", \nrecord_key, record_value) \ncache.set (record_key, record_value)',
    #          b='record_value = cache.get(record_key)\nif (record_value == NULL)\nrecord_value = db.query("SELECT Details FROM Records WHERE ID == {0}", record_key)\ncache.set (record_key, record_value)',
    #          c='record_value = cache.get (record_key)\ndb.query("UPDATE Records SET Details = {1} WHERE ID == {0}", record_key, record_value)',
    #          d='record_value = db.query("SELECT Details FROM Records WHERE ID == {0}", record_key)\nif (record_value != NULL)\ncache.set (record_key, record_value)',
    #          e='',
    #          answer='')
    #
    # qb.submit(question='A developer wants to track the performance of an application that runs on a fleet of Amazon EC2 instances. The developer wants to view and track statistics across the fleet, such as the average and maximum request latency. The developer would like to be notified immediately if the average response time exceeds a threshold.\nWhich solution meets these requirements?',
    #          a='Configure a cron job on each instance to measure the response time and update a log file stored in an Amazon S3 bucket every minute. Use an Amazon S3 event notification to trigger an AWS Lambda function that reads the log file and writes new entries to an Amazon Elasticsearch Service (Amazon ES) cluster. Visualize the results in a Kibana dashboard. Configure Amazon ES to send an alert to an Amazon SNS topic when the response time exceeds a threshold.',
    #          b='Configure the application to write the response times to the system log. Install and configure the Amazon Inspector agent to continually read the logs and send the response times to Amazon EventBridge. View the metrics graphs in the EventBridge console. Configure an EventBridge custom rule to send an Amazon SNS notification when the average of the response time metric exceeds the threshold.',
    #          c='Configure the application to write the response times to a log file. Install and configure the Amazon CloudWatch agent on the instances to stream the application log to CloudWatch Logs. Create a metric filter of the response time from the log. View the metrics graphs in the CloudWatch console. Create a CloudWatch alarm to send an Amazon SNS notification when the average of the response time metric exceeds the threshold.',
    #          d='Install and configure the AWS Systems Manager Agent on the instances to monitor the response time and send it to Amazon CloudWatch as a custom metric. View the metrics graphs in Amazon QuickSight. Create a CloudWatch alarm to send an Amazon SNS notification when the average of the response time metric exceeds the threshold.',
    #          e='',
    #          answer='')
    #
    # qb.submit(question='A developer is testing an application locally and has deployed it to AWS Lambda. To remain under the package size limit, the dependencies were not included in the deployment file. When testing the application remotely, the function does not execute because of missing dependencies.\nWhich approach would resolve the issue?',
    #          a='Use the Lambda console editor to update the code and include the missing dependencies.',
    #          b='Create an additional .zip file with the missing dependencies and include the file in the original Lambda deployment package.',
    #          c='Add references to the missing dependencies in the Lambda function\'s environment variables.',
    #          d='Attach a layer to the Lambda function that contains the missing dependencies.',
    #          e='',
    #          answer='')
    #
    # qb.submit(question='A developer is building a web application that uses Amazon API Gateway. The developer wants to maintain different environments for development and production (dev and prod) workloads. The API will be backed by an AWS Lambda function with two aliases: one for dev and one for prod.\nHow can this be achieved with the LEAST amount of configuration?',
    #          a='Create a REST API for each environment and integrate the APIs with the corresponding dev and prod aliases of the Lambda function. Then deploy the two APIs to their respective stages and access them using the stage URLs.',
    #          b='Create one REST API and integrate it with the Lambda function using a stage variable in place of an alias. Then deploy the API to two different stages – dev and prod – and create a stage variable in each stage with different aliases as the values. Access the API using the different stage URLs.',
    #          c='Create one REST API and integrate it with the dev alias of the Lambda function, and deploy it to a dev environment. Configure a canary release deployment for prod where the canary will integrate with the Lambda prod alias.',
    #          d='Create one REST API and integrate it with the prod alias of the Lambda function and deploy it to a prod environment. Configure a canary release deployment for dev where the canary will integrate with the Lambda dev alias.',
    #          e='',
    #          answer='')
