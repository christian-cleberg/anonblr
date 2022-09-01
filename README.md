# anonblr

anonblr is a anonymous proxy service for viewing Tumblr blogs. This service uses 
a server-side Tumblr account that will fetch any submitted blogs and return 
their content.

## Development

If you need to perform system-wide updates or install `virtualenv` prior to 
creating the virtual environment, do so now:

```bash
python3 -m pip install --user --upgrade pip
python3 -m pip install --user virtualenv
```

Create the `env` environment and activate it. Then you can install 
project-specific packages:

```bash
python3 -m venv env
source env/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

Finally, you can make any changes and run the program:

```bash
flask run
```
