<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Route53 Backup to S3</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            padding: 20px;
            max-width: 800px;
            margin: auto;
        }

        h1,
        h2,
        h3 {
            color: #333;
        }

        code {
            background-color: #f4f4f4;
            padding: 5px;
            border-radius: 3px;
            font-family: monospace;
        }

        pre {
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
            overflow-x: auto;
        }

        ul {
            list-style-type: none;
            padding: 0;
        }

        ul li {
            margin-bottom: 10px;
        }

        ul li:before {
            content: "\2022";
            color: #333;
            display: inline-block;
            width: 1em;
            margin-left: -1em;
        }
    </style>
</head>

<body>
    <h1>Route53 Backup to S3</h1>

    <p>This Python script is designed to backup Route53 hosted zones and their resource record sets to an Amazon S3
        bucket. It ensures that older backups are deleted from the S3 bucket to manage storage efficiently. Each backup
        file is named with a timestamp appended to the hosted zone name for identification and versioning purposes.</p>

    <h2>Requirements</h2>
    <ul>
        <li>Python 3.x</li>
        <li><code>boto3</code> library</li>
        <li>AWS credentials configured on the system</li>
    </ul>

    <h2>Installation</h2>
    <ol>
        <li>Clone the repository to your local machine:</li>
        <pre><code>git clone https://github.com/your-username/route53-backup.git</code></pre>

        <li>Install the required dependencies using pip:</li>
        <pre><code>pip install boto3</code></pre>

        <li>Configure AWS credentials on your system. You can do this by setting environment variables or using AWS
            CLI.</li>
    </ol>

    <h2>Usage</h2>
    <ol>
        <li>Navigate to the directory containing the Python script:</li>
        <pre><code>cd route53-backup</code></pre>

        <li>Run the script:</li>
        <pre><code>python route53_backup.py</code></pre>

        <li>The script will automatically backup Route53 hosted zones to the specified S3 bucket. It will delete older
            backups (older than 30 days) from the S3 bucket to manage storage efficiently.</li>
    </ol>

    <h2>Configuration</h2>
    <ul>
        <li>Modify the <code>bucket_name</code> and <code>folder_name</code> variables in the script to specify the S3
            bucket and folder where backups will be stored.</li>
        <li>Adjust the age threshold (<code>age &gt; 30</code>) if you want to retain backups for a different
            duration.</li>
    </ul>

    <h2>License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>

    <h2>Authors</h2>
    <ul>
        <li><a href="https://github.com/your-username">Your Name</a></li>
    </ul>

    <h2>Acknowledgments</h2>
    <ul>
        <li>Thanks to the <a href="https://github.com/boto/boto3">boto3</a> library developers for providing a
            convenient way to interact with AWS services.</li>
        <li>Inspiration for this script came from the need to automate Route53 backups for disaster recovery and
            configuration management purposes.</li>
    </ul>
</body>

</html>
