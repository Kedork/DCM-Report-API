__author__ = "Kevork Kazanjian"

import argparse
import sys

import sample_tools
from oauth2client import client

# Declare command-line flags.
argparser = argparse.ArgumentParser(add_help=False)
argparser.add_argument(
    'profile_id', type=int,
    help='The ID of the profile to list reports for')


def main():
  # Authenticate and construct service.
  service, flags = sample_tools.init(
      '', 'dfareporting', 'v2.1', __doc__, __file__, parents=[argparser],
      scope=['https://www.googleapis.com/auth/dfareporting',
             'https://www.googleapis.com/auth/dfatrafficking'])

  profile_id = 1087970

  try:
    # Construct the request.
    request = service.reports().list(profileId=profile_id)

    while True:
      # Execute request and print response.
      response = request.execute()

      for report in response['items']:
        print ('Found %s report with ID %s and name "%s".'
               % (report['type'], report['id'], report['name']))

      if response['items'] and response['nextPageToken']:
        request = service.reports().list_next(request, response)
      else:
        break
  except client.AccessTokenRefreshError:
    print ('The credentials have been revoked or expired, please re-run the '
           'application to re-authorize')


if __name__ == '__main__':
  main()