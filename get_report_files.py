__author__ = 'Kevork Kazanjian'

import argparse
import sys
from download_file import main as download

import json
import sample_tools
from oauth2client import client

# Declare command-line flags.
argparser = argparse.ArgumentParser(add_help=False)
argparser.add_argument(
    'profile_id', type=int,
    help='The ID of the profile to use')
argparser.add_argument(
    'report_id', type=int,
    help='The ID of the report to list files for')


def main():
    # Authenticate and construct service.
    service, flags = sample_tools.init(
        '', 'dfareporting', 'v2.1', __doc__, __file__, parents=[argparser],
        scope=['https://www.googleapis.com/auth/dfareporting',
             'https://www.googleapis.com/auth/dfatrafficking'])

    with open('IDs.json') as data_file:
        data = json.load(data_file)

    for alldata in data['data']:
        profile_id = data['data'][alldata]['Profile']
        for Reports in data['data'][alldata]['Reports']:
            report_id = data['data'][alldata]['Reports'][Reports]

            try:
                # Construct a get request for the specified report.
                request = service.reports().files().list(profileId=profile_id, reportId=report_id)
                f = open('Reports.txt', 'w')
                while True:
                    # Execute request and print response.
                    response = request.execute()

                    for report_file in response['items']:
                        #f.writelines('Report file with ID %s and file name "%s" has status %s.'
                            #% (report_file['id'], report_file['fileName'],
                                #report_file['status']))
                        f.writelines(report_file['id'])
                        f.writelines('\n')

                    if response['items'] and response['nextPageToken']:
                        request = service.reports().files().list_next(request, response)
                    else:
                        break
                f.close()
            except client.AccessTokenRefreshError:
                print ('The credentials have been revoked or expired, please re-run the '
                    'application to re-authorize')

            f = open('Reports.txt','r')
            file_id = f.readline()
            download(report_id, file_id)
            f.close()

if __name__ == '__main__':
  main()