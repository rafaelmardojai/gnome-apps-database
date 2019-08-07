#!/usr/bin/python3
"""
This file is a WIP for testing.
"""

import os
import shutil

import requests
import json
import yaml
import markdown2

def main():
    print('Starting generation...')

    d = os.getcwd()

    apps_dir = os.path.join(d, 'non-flathub-apps')
    flathub_apps_file = open(d+'/flathub-apps.yml') 
    flathub_apps = yaml.safe_load(flathub_apps_file)

    src_screenshots_dir = d+'/screenshots-src'

    screenshots_dir = d+'/screenshots'
    icons_dir = d+'/icons'

    print('Creating generation dirs...')
    if os.path.exists(screenshots_dir):
        print('Screenshots dir exists, removing it...')
        shutil.rmtree(screenshots_dir)
    if os.path.exists(icons_dir):
        print('Icons dir exists, removing it...')
        shutil.rmtree(icons_dir)
    os.makedirs(icons_dir) # Create icons dir
    os.makedirs(screenshots_dir) # Create screenshots dir
    print('Created screenshots & icons dirs.')

    apps = {}

    print('Reading non flathub apps...')
    for app in os.listdir(apps_dir):
        app_dir = os.path.join(apps_dir, app) # Open app dir

        metadata_file = open(app_dir+'/metadata.yml') # Load app metadata file
        app_metadata = yaml.safe_load(metadata_file) # Parse YAML metadata file to py dict

        description = markdown2.markdown_path(app_dir+'/description.md') # Load md app description & convert it to html
        app_metadata['description'] = description # Add description to metadata dict

        apps[app] = app_metadata # Add app metadata dict to apps dict

        if os.path.isfile(app_dir+'/icon.png'):
           shutil.copy(app_dir+'/icon.png', icons_dir+'/'+app+'.png')

        if os.path.isfile(app_dir+'/screenshot.png'):
           shutil.copy(app_dir+'/screenshot.png', screenshots_dir+'/'+app+'.png')

        print('- Added '+app)

    print('Reading flathub apps...')
    for i in range(len(flathub_apps)): 
        url = 'https://flathub.org/api/v1/apps/'+flathub_apps[i]
        response = requests.get(url)
        data = json.loads(response.text)
        app_metadata = {}
        app_metadata['name'] = data['name']
        app_metadata['summary'] = data['summary']
        app_metadata['website'] = data['homepageUrl']
        app_metadata['categories'] = []

        for ix in range(len(data['categories'])):
            app_metadata['categories'].append(data['categories'][ix]['name'])

        app_metadata['description'] = data['description']
        apps[flathub_apps[i]] = app_metadata

        with open(icons_dir+'/'+flathub_apps[i]+'.png', 'wb') as handle:
            response_img = requests.get('https://flathub.org/'+data['iconDesktopUrl'], stream=True)
            shutil.copyfileobj(response_img.raw, handle)

        if os.path.isfile(src_screenshots_dir+'/'+flathub_apps[i]+'.png'): # Check if exist an alt screenshot
            shutil.copy(src_screenshots_dir+'/'+flathub_apps[i]+'.png', screenshots_dir+'/'+flathub_apps[i]+'.png')
        else: # Else use flathub screenshot
            with open(screenshots_dir+'/'+flathub_apps[i]+'.png', 'wb') as handle:
                response_img = requests.get(data['screenshots'][0]['imgDesktopUrl'], stream=True)
                shutil.copyfileobj(response_img.raw, handle)

        print('- Added '+flathub_apps[i])

    print('Creating JSON file...')
    with open(d+'/apps.json', 'w') as outfile:
        json.dump(apps, outfile, indent=4)

    print('End. Files generated in: '+d)

main()
