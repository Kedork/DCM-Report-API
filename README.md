Summary:
     I needed a quick script to download DCM Reports for ingestion into a data warehouse.
	 The email delivery of reports were no longer doing the trick - file sizes started getting large.
	 I used the "sample tools" from Google's API example and modified it to no look for arguments.
	 Created a JSON file to hold the IDs of the reports I needed files for.
	 
	 The script loops through the JSON file for Report IDs, pulls a list of File IDs for that report
	 and downloads the last available file. I have my reports scheduled to run every day. The files will
	 be named after the report IDs from the JSON file, this way your ETL can always look for the same file.
	 Keep in mind this will override previous run's data.
	 
	 I have a separate ETL process that takes the downloaded CSVs and import into the warehouse.
	 
Instructions:
	1 - Follow Google's instructions to create an app on Google's Developer Console https://console.developers.google.com/project
	2 - Enable "DCM/DFA Reporting and Trafficking API"
	3 - Create credentials for a native application and download the JSON file title "client_secret.json". Save to project folder
	4 - Modify "IDs.json"
		a - Profile ID is very important
		b - Report IDs are very important
	5 - When you have step 1-4 completed run "get_report_files.py"
	
Next steps:
	Again, this was done very quick and dirty, didn't have time to document every step in the code. There's also a bunch of files 
	I used when I was testing that need to go on the ignore list. Soon I will clean up the code, add comments and delete old files.
	
Enjoy