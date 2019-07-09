### Google Cloud Utility Functions

There are still some things that don't mesh well when leveraging the Adobe Sign API and attempting to integrate it into other platforms.  I'll use this repo as a place to create some alternative ways to process data from transactions using GCP.  I'll try to focus on simple "functions" but may, in the future also create some apps.

*  **[Get Form-Data as JSON](https://github.com/skaboy71/Adobe-Sign-GCP-Functions-/blob/master/Get-FormData-as-JSON.md)** This google Cloud Function leverages the Adobe Sign API to get the CSV of the form data and then converts it to JSON which is consumable by MS Flow and other similar "workflow engine" platforms
