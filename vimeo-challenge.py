import pandas as pd


def get_500s_by_domain(file):
    print(f'the file {file}')
    df = pd.read_csv('log_sample.txt',
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

    # create a series of 500's grouped by host
    http_500 = df[df.status.eq(500)].groupby('host').size()

    # create a series of all requests grouped by host
    host_total = df.groupby('host').size()

    # divide 2 series grouped by the same axis
    pct = 100 * (http_500 / host_total)

    print(f'''
    Between time XXXXXXXXXX and time YYYYYYYYYY:
    vimeo.com returned 2.15% 5xx errors
    player.vimeo.com returned 3.01% 5xx errors
    api.vimeo.com returned 0.01% 5xx errors
    ''')

get_500s_by_domain('log_sample.txt')
