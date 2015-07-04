__author__ = 'Kevork Kazanjian'

import argparse
import sys

import sample_tools
from oauth2client import client

# Declare command-line flags.
argparser = argparse.ArgumentParser(add_help=False)
argparser.add_argument(
    'report_id', type=int,
    help='The ID of the report to get a file for')
argparser.add_argument(
    'file_id', type=int,
    help='The ID of the file to get')


def main(report_id, file_id):
  # Authenticate and construct service.
  service, flags = sample_tools.init(
      '', 'dfareporting', 'v2.1', __doc__, __file__, parents=[argparser],
      scope=['https://www.googleapis.com/auth/dfareporting',
             'https://www.googleapis.com/auth/dfatrafficking'])

  report_id = report_id
  file_id = file_id

  try:
    # Construct the request.
    request = service.files().get_media(reportId=report_id, fileId=file_id)

    # Execute request and print the file contents
    f = open('Conversions_Metadata.csv', 'w' )
    f.write(request.execute())
    f.close()
    #print request.execute()

  except client.AccessTokenRefreshError:
    print ('The credentials have been revoked or expired, please re-run the '
           'application to re-authorize')


if __name__ == '__main__':
  main(sys.argv)