# File transfer(FTP)

Transfer file into FTP server.  
This script is created for myself, so I can't guarantee that this script accurately.  
Only python 2.7 work collectly.


## Usage

### Set up library

You set up library like below.

```sh
pip install -r requirements.txt
```

I recommend you to use virtualenv.

### Create config file

First, create config file.
```sh
cp config.ini-dest config.ini
```

After this, set variables in `config.ini`.  
The writing way has in `config.ini`

### Excecute script 

You can run with two type of sync.  

1. Sync directory

If you want to sync directory, you must set variables of `syncdir` and `header_path` in `config.ini`.  
After setting, you can run script the below command.  

```sh
python2.7 main.py -a True
```

2. Sync specific file

If you want to sync specific file, you must set `header_path` in `config.ini`.  
After setting, you can run script the below command.  
You can change the argument of `walker.py` to your target file name.  

```sh
python2.7 main.py -f walker.py
```

## Testing

You can run test ftp server with next command.

```sh
cd testserver
python ftpserver.py
```

There are connection information in `testserver/ftpserver.py`

## TODO

- Check argument strictly
- Simplify setting
- Change setting into environment variable
- Check for python3

## Licence 

MIT
