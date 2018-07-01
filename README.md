# File synchronize　with Python(Only FTP)

Transfer files into FTP server with Python.  
This script for myself, and there are some bugs in this code.  


## Eevironment

Python2.7


## Usage

### Install

`git clone https://github.com/pyohei/fsync-py.git`

### Set up

Install dependent libraries(recommend virtualenv).  

```sh
cd fsync-py
pip install -r requirements.txt
```

### Create configuration

You need to prepare configure file.  

```sh
cp config.ini-dest config.ini
```

After this, set variables in `config.ini`.  

### Excecute

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
python main.py -f walker.py
```

## Testing

You can run test ftp server with next command.

```sh
cd testserver
python ftpserver.py
```

There are connection information in `testserver/ftpserver.py`

## Licence 

MIT
