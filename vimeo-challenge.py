from datetime import datetime
from datetime import timezone

import pandas as pd
import math


def get_500s_by_domain(start: str, end: str, files: list):
    af = aggregate_files(files)

    format_string = "%m-%d-%Y %H:%M:%S.%f"
    # convert times to epoch; Friday, May 5, 2017 7:25:01.638 AM - Friday, May 5, 2017 7:25:01.667 AM
    epoch_start = datetime.strptime(start, format_string).replace(tzinfo=timezone.utc).timestamp()
    # epoch_start = datetime.datetime(2017, 5, 5, 3, 25, 1, 638000).timestamp()
    epoch_end = datetime.strptime(end, format_string).replace(tzinfo=timezone.utc).timestamp()

    df = pd.read_csv(af,
                     sep='|',
                     names=["epoch",
                            "scheme",
                            "host",
                            "method",
                            "status",
                            "cdninfo",
                            "cdningress",
                            "metadata",
                            "remoteaddress",
                            "time"])

    dt_filter = (df['epoch'] >= epoch_start) & (df['epoch'] < epoch_end)
    df = df.loc[dt_filter]

    # convert status dtype to str and create a series of 5xx's grouped by host
    df['status'] = df['status'].astype(str)
    http_5xx = df[df.status.str.match(r'^5\d{2}$')].groupby('host').size()

    # create a series of all requests grouped by host
    host_total = df.groupby('host').size()

    # divide 2 series grouped by the same name
    pct = 100 * (http_5xx / host_total)

    header = f'Between time {start} and time {end}:\n'
    body = ''

    for n, v in pct.items():
        if not math.isnan(v):
            body += str(f'{n} returned {round(v, 2)}% 5xx errors\n')

    print(header + body)


def aggregate_files(files: list):
    with open('logz.txt', 'w') as out:
        try:
            for f in files:
                with open(f) as infile:
                    for line in infile:
                        out.write(line)
        except OSError as e:
            if e.strerror == 'No such file or directory':
                print(e)
            else:
                raise e
    return out.name


get_500s_by_domain('5-5-2017 7:25:01.638', '5-5-2017 7:25:01.655',
                   ['log_sample.txt', 'log_sample_2.txt', 'does_not_exist.txt'])
