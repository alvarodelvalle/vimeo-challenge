Background
You have 10GB of text logs. Each log line corresponds to a single HTTP response from web frontend. You goal is to write a simple, reusable tool that returns the percentage of responses that were HTTP 5xx errors, broken down by domain, for a given timeframe.
Output should look something like this:
Between time XXXXXXXXXX and time YYYYYYYYYY:
vimeo.com returned 2.15% 5xx errors
player.vimeo.com returned 3.01% 5xx errors
api.vimeo.com returned 0.01% errors


The input to your tool will be a start time, an end time, and a list of files. You should consider lines at or after the start time, and strictly before the end time. You may choose to take input in whatever format you like.
Each log line looks like this (this is a single line, which may be wrapped on your screen):
1493969101.644 | https | vimeo.com | GET | 404 | 1493969101583195,1493969101635320, | IAD |  | 10.10.3.59 | 0.009


The fields are:
Time of response (seconds since epoch, as a float)
Response scheme ("http" or "https")
HTTP Host (domain)
HTTP request method
HTTP status
CDN information
CDN ingress point
Remote address metadata
Remote address
Time taken by request in seconds
Each field is separated by " | " (a pipe enclosed by spaces). The fields you care about are (1), (3), and (5).
log_sample.txt contains a small sample of log entries.
We wrote a sample solution in about 1 hour, and we're expecting something of a similar level of complexity -- we don't need something complex, and it doesn't need to solve use cases other than the one we're describing.
Our Questions
Please write a program to solve the problem above, in Python, Ruby, or Go. (If you don't know any of these languages, talk to us and we'll figure something out.)
Please write a README file including the following information:
A sample invocation of your program and its output.
A list of any external dependencies of your program, and any applicable installation instructions.
A list of any assumptions you made in your solution.
Thanks for taking the time to complete this exercise!
<3, Vimeo

# vimeo-challenge
## Usage
```shell
❯ /Users/alvaro/.conda/envs/vimeo-challenge/bin/python
Python 3.8.5 (default, Sep  4 2020, 02:22:02) 
[Clang 10.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from vimeo_challenge import get_500s_by_domain
>>> get_500s_by_domain('5-5-2017 7:25:01.638', '5-5-2017 7:25:01.655',
...                    ['log_sample.txt', 'log_sample_2.txt', 'does_not_exist.txt'])
[Errno 2] No such file or directory: 'does_not_exist.txt'
Between time 5-5-2017 7:25:01.638 and time 5-5-2017 7:25:01.655:
 player.vimeo.com  returned 35.0% 5xx errors
 vimeo.com  returned 16.67% 5xx errors
```
