__author__ = 'Kevork Kazanjian'

import argparse
import sys
from download_file import main as download

from apiclient import sample_tools
from oauth2client import client

# Declare command-line flags.
argparser = argparse.ArgumentParser(add_help=False)
argparser.add_argument(
    'profile_id', type=int,
    help='The ID of the profile to use')
argparser.add_argument(
    'report_id', type=int,
    help='The ID of the report to list files for')


def main(argv):
  # Authenticate and construct service.
  service, flags = sample_tools.init(
      argv, 'dfareporting', 'v2.1', __doc__, __file__, parents=[argparser],
      scope=['https://www.googleapis.com/auth/dfareporting',
             'https://www.googleapis.com/auth/dfatrafficking'])

  profile_id = flags.profile_id
  report_id = flags.report_id

  try:
    # Construct a get request for the specified report.
    request = service.reports().files().list(
        profileId=profile_id, reportId=report_id)

    while True:
      # Execute request and print response.
      response = request.execute()

      for report_file in response['items']:
        print ('Report file with ID %s and file name "%s" has status %s.'
               % (report_file['id'], report_file['fileName'],
                  report_file['status']))
        ids = '%s,%s\n' % (report_file['reportId'], report_file['id'])

        download(report_file['reportId'], report_file['id'])

      if response['items'] and response['nextPageToken']:
        break
        #request = service.reports().files().list_next(request, response)
      else:
        break
  except client.AccessTokenRefreshError:
    print ('The credentials have been revoked or expired, please re-run the '
           'application to re-authorize')

if __name__ == '__main__':
  main(sys.argv)