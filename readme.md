## Readme

This repo is used to download the Apple TV screensavers in 4k HDR mov format.

The `entries.json` file and `urls-aria.txt` are updated to current, to update, follow the instructions below.

Or to download in another format or resolution, such as SDR or 1080p, edit and re-run `parse_entries.py` and edit HDR to SDR, and/or 4K to 1080.

## Update `entries.json`:

https://sylvan.apple.com/Aerials/resources.tar

Inside the tar file, extract `entries.json` to current directory.

## Parse entries file

Parse json to txt and csv files: `parse_entries.json`

## aria download command

Download videos using aria:

`aria2c --check-certificate=false -i urls_aria.txt -c -d ./apple_4k_screensaver_videos/`

## Subtitles / points of interest:

In the `resources.tar` file, extract `./TVIdleScreenStrings.bundle/en_GB.lproj/Localizable.nocache.strings`.

Convert this file to xml and download as `strings.xml` and put in current directory: https://localise.biz/free/converter/ios-to-android

Run `parse_sub_strings.py` to convert `strings.xml` to `sub_strings.json`.

Run `make_subs.py` to convert `sub_strings.json` to `.srt` subtitles files in the  directory './subs/'.


-------------

also see: https://gist.github.com/dmn001/471efcecc19bfb9be7a8575a557162b7